from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_lawful_learning.py"
SCHEMA_DIR = ROOT / "schemas" / "lawful-learning"
EXAMPLE_DIR = ROOT / "examples" / "lawful-learning"
CONFORMANCE_DOC = ROOT / "docs" / "doctrine" / "lawful-learning" / "CONFORMANCE.md"

SCHEMA_FILES = {
    "model.schema.json",
    "constraint.schema.json",
    "ledger.schema.json",
}

EXAMPLE_FILES = {
    "model.yaml",
    "tuning.yaml",
    "ledger.yaml",
}


def run_validator() -> dict:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def test_lawful_learning_conformance_validator_passes() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["schema_count"] == 3
    assert payload["example_count"] == 3
    assert all(result["passed"] for result in payload["results"])


def test_lawful_learning_schemas_parse_as_draft_2020_12() -> None:
    for schema_name in SCHEMA_FILES:
        schema = json.loads((SCHEMA_DIR / schema_name).read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["type"] == "object"
        assert schema["required"]
        assert schema["properties"]


def test_lawful_learning_examples_are_present() -> None:
    for example_name in EXAMPLE_FILES:
        assert (EXAMPLE_DIR / example_name).exists()


def test_lawful_learning_non_claims_are_recorded() -> None:
    payload = run_validator()
    non_claims = "\n".join(payload["non_claims"])
    assert "No live data" in non_claims
    assert "deterministic formal configuration" in non_claims
    assert "not empirical results" in non_claims


def test_lawful_learning_conformance_doc_records_commands() -> None:
    text = CONFORMANCE_DOC.read_text(encoding="utf-8")
    assert "make lawful-learning-fixtures" in text
    assert "make lawful-learning-ci" in text
    assert "PYTHONPATH=. python -m pytest -q tests/test_lawful_learning_toy.py" in text
    assert "No live data" in text
