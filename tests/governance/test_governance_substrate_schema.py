import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schemas" / "procybernetica" / "governance-substrate.v0.1.schema.json"
VALID = ROOT / "tests" / "governance" / "fixtures" / "governance-substrate.valid.json"
INVALID_MISSING_ADMISSIBILITY = (
    ROOT / "tests" / "governance" / "fixtures" /
    "governance-substrate.invalid-missing-admissibility.json"
)


def load(path: Path):
    return json.loads(path.read_text())


def test_valid_governance_substrate_fixture_passes():
    validator = Draft202012Validator(load(SCHEMA))
    errors = sorted(validator.iter_errors(load(VALID)), key=lambda e: e.path)
    assert errors == []


def test_token_without_admissibility_role_fails():
    validator = Draft202012Validator(load(SCHEMA))
    errors = sorted(
        validator.iter_errors(load(INVALID_MISSING_ADMISSIBILITY)),
        key=lambda e: e.path,
    )
    assert errors, "schema must reject tokens missing admissibility_role"
    assert any("admissibility_role" in str(error.message) for error in errors)
