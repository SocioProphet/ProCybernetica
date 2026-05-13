from __future__ import annotations

import copy
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


def test_epsilon_gate_bypass_rejected_by_schema() -> None:
    """A pass claim without hash-bound dry-run evidence must be structurally invalid."""
    schema = load_json(SCHEMA_ROOT / "admission-pack.v1.json")
    invalid_pack = copy.deepcopy(load_json(FIXTURE))
    invalid_pack["epsilon_gate"]["epsilon_gate_passed"] = True
    invalid_pack["epsilon_gate"].pop("dry_run_output_hash", None)
    invalid_pack["epsilon_gate"].pop("dry_run_evidence_ref", None)

    errors = list(Draft202012Validator(schema).iter_errors(invalid_pack))
    rendered = "\n".join(error.message for error in errors).lower()

    assert errors, "schema must reject epsilon_gate_passed=true without hash-bound dry-run evidence"
    assert "dry_run_output_hash" in rendered or "dry_run_evidence_ref" in rendered


def test_epsilon_gate_bypass_rejected_by_validator(tmp_path: Path) -> None:
    """
    Admission pack that claims epsilon gate pass but carries no hash-bound
    dry-run output evidence must be rejected by the validator.
    """
    invalid_pack = copy.deepcopy(load_json(FIXTURE))
    invalid_pack["epsilon_gate"]["epsilon_gate_passed"] = True
    invalid_pack["epsilon_gate"].pop("dry_run_output_hash", None)
    invalid_pack["epsilon_gate"].pop("dry_run_evidence_ref", None)

    invalid_path = tmp_path / "epsilon-gate-bypass.invalid.json"
    invalid_path.write_text(json.dumps(invalid_pack, indent=2), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(invalid_path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    rendered = result.stderr.lower()

    assert result.returncode != 0
    assert "dry_run_output_hash" in rendered or "dry_run_evidence_ref" in rendered
