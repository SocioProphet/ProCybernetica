from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_v0_schemas.py"
SCHEMA_README = SCHEMA_DIR / "README.md"
STATUS_DOC = ROOT / "docs" / "schemas" / "V0_SCHEMA_NORMALIZATION_STATUS.md"

CANONICAL_V0_SCHEMAS = [
    "node_descriptor.schema.json",
    "artifact_envelope.schema.json",
    "policy_envelope.schema.json",
    "command_envelope.schema.json",
    "delegation_envelope.schema.json",
    "observation_envelope.schema.json",
    "status_envelope.schema.json",
    "event_envelope.schema.json",
    "trace_event.schema.json",
    "transition_record.schema.json",
    "replay_envelope.schema.json",
    "evaluation_result.schema.json",
    "promotion_decision.schema.json",
    "incident_report.schema.json",
    "claim.schema.json",
    "provenance_record.schema.json",
    "capability_descriptor.schema.json",
]


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


def test_v0_schema_validator_passes() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["schema_count"] == len(CANONICAL_V0_SCHEMAS)
    assert payload["fixture_backed_count"] == 16
    assert all(result["passed"] for result in payload["results"])


def test_all_canonical_v0_schemas_exist_and_validate_as_json_schema() -> None:
    for schema_name in CANONICAL_V0_SCHEMAS:
        path = SCHEMA_DIR / schema_name
        assert path.exists()
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["$id"].startswith("https://schemas.socioprophet.org/procybernetica/")
        assert schema["type"] == "object"
        assert isinstance(schema["additionalProperties"], bool)
        assert "schema_version" in schema["properties"]


def test_schema_readme_lists_canonical_v0_surface() -> None:
    text = SCHEMA_README.read_text(encoding="utf-8")
    assert "Canonical v0 schema set" in text
    assert "schemas.socioprophet.org/procybernetica" in text
    for schema_name in CANONICAL_V0_SCHEMAS:
        assert schema_name in text


def test_v0_schema_status_doc_records_namespace_and_deferred_fixture_posture() -> None:
    text = STATUS_DOC.read_text(encoding="utf-8")
    assert "https://schemas.socioprophet.org/procybernetica/" in text
    assert "incident_report.schema.json" in text
    assert "deferred fixture" in text
    assert "runtime" in text
