from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_ROOT = ROOT / "schemas" / "triune"
FIXTURE = ROOT / "examples" / "triune" / "admission-pack.synthetic.json"
VALIDATOR = ROOT / "tools" / "triune" / "validate-admission-pack.py"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_triune_schemas_are_valid_draft_2020_12() -> None:
    for schema_path in SCHEMA_ROOT.glob("*.v1.json"):
        Draft202012Validator.check_schema(load_json(schema_path))


def test_triune_admission_pack_fixture_matches_schema() -> None:
    schema = load_json(SCHEMA_ROOT / "admission-pack.v1.json")
    Draft202012Validator(schema).validate(load_json(FIXTURE))


def test_triune_admission_pack_validator_accepts_synthetic_fixture() -> None:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "PASS:" in result.stdout
