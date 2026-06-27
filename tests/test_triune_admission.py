"""Tests for the existing synthetic admission fixture and the admission pack validator."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "triune" / "admission-pack.v1.json"
SYNTHETIC_PACK = ROOT / "examples" / "triune" / "admission-pack.synthetic.json"

_validator_path = ROOT / "tools" / "triune" / "validate-admission-pack.py"
_spec = importlib.util.spec_from_file_location("validate_admission_pack", _validator_path)
assert _spec and _spec.loader
_validator_mod = importlib.util.module_from_spec(_spec)
sys.modules["validate_admission_pack"] = _validator_mod
_spec.loader.exec_module(_validator_mod)

validate = _validator_mod.validate
policy_validate = _validator_mod.policy_validate


def load_schema():
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def load_pack(path=SYNTHETIC_PACK):
    return json.loads(path.read_text(encoding="utf-8"))


def test_synthetic_admission_pack_validates():
    ok, errors = validate(SYNTHETIC_PACK)
    assert ok, f"synthetic admission pack failed validation: {errors}"


def test_synthetic_admission_pack_schema_valid():
    schema = load_schema()
    pack = load_pack()
    jsonschema.validate(pack, schema)


def test_synthetic_pack_status_is_proposed_not_admitted():
    pack = load_pack()
    assert pack["candidate_status"] == "proposed", (
        "synthetic fixture must not claim admitted state"
    )


def test_synthetic_pack_execution_status_is_fixture():
    pack = load_pack()
    assert pack["execution_status"] == "synthetic_fixture"


def test_missing_dry_run_hash_fails():
    pack = load_pack()
    pack["policy"]["dry_run_output_hash"] = ""
    errors = policy_validate(pack)
    assert any("dry_run_output_hash" in e for e in errors)


def test_missing_dry_run_evidence_ref_fails():
    pack = load_pack()
    pack["policy"]["dry_run_evidence_ref"] = ""
    errors = policy_validate(pack)
    assert any("dry_run_evidence_ref" in e for e in errors)


def test_approved_without_host_approval_fails():
    pack = load_pack()
    pack["candidate_status"] = "approved"
    pack["decision"].pop("host_approval", None)
    errors = policy_validate(pack)
    assert any("host_approval" in e for e in errors)


def test_admitted_without_host_approval_fails():
    pack = load_pack()
    pack["candidate_status"] = "admitted"
    pack["decision"].pop("host_approval", None)
    errors = policy_validate(pack)
    assert any("host_approval" in e for e in errors)


def test_policy_violations_fail():
    pack = load_pack()
    pack["policy"]["violations"] = ["no-privileged-pods violation detected"]
    errors = policy_validate(pack)
    assert any("violation" in e for e in errors)


def test_missing_reversal_plan_steps_fails():
    pack = load_pack()
    pack["reversal_plan"]["steps"] = []
    errors = policy_validate(pack)
    assert any("steps" in e for e in errors)


def test_missing_revocation_evidence_ref_fails():
    pack = load_pack()
    pack["reversal_plan"]["revocation_evidence_ref"] = ""
    errors = policy_validate(pack)
    assert any("revocation_evidence_ref" in e for e in errors)
