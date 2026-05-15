from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "cybernetic-governance"
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_agentplane_binding.py"
FIXTURE = ROOT / "tests" / "fixtures" / "agentplane-binding" / "agentplane-binding-fixtures.synthetic.json"

SCHEMA_FILES = {
    "agentplane_run_capsule.v1.json",
    "agentplane_tool_grant.v1.json",
    "agentplane_action_dispatch.v1.json",
    "agentplane_subagent_delegation.v1.json",
    "agentplane_operator_readout.v1.json",
    "agentplane_proof_pack_exhibit.v1.json",
}

REQUIRED_CATEGORIES = {
    "normal-run",
    "review-required-run",
    "transformed-run",
    "subagent-delegation-run",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator() -> dict:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def test_agentplane_binding_schemas_are_valid_draft_2020_12() -> None:
    for schema_name in SCHEMA_FILES:
        Draft202012Validator.check_schema(load_json(SCHEMA_DIR / schema_name))


def test_agentplane_binding_validator_passes() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["fixture_count"] == 9
    assert all(result["passed"] for result in payload["results"])


def test_agentplane_binding_fixtures_cover_required_run_cases() -> None:
    payload = run_validator()
    categories = {result["category"] for result in payload["results"] if result.get("category")}
    assert REQUIRED_CATEGORIES <= categories


def test_agentplane_binding_fixtures_cover_all_schema_targets() -> None:
    payload = run_validator()
    targets = {result["target_schema"] for result in payload["results"]}
    assert targets == SCHEMA_FILES


def test_invalid_run_capsule_without_tool_grant_fails_for_schema_validation() -> None:
    payload = run_validator()
    invalid = next(
        result for result in payload["results"]
        if result["fixture_id"] == "ap-run-capsule-invalid-missing-tool-grants"
    )
    assert invalid["expected_result"] == "fail"
    assert invalid["actual_result"] == "fail"
    assert "schema_validation_error" in invalid["observed_failures"]


def test_run_capsules_have_required_governance_references() -> None:
    fixture = load_json(FIXTURE)
    run_capsules = [
        record["payload"]
        for record in fixture["fixtures"]
        if record["target_schema"] == "agentplane_run_capsule.v1.json"
        and record["expected_result"] == "pass"
    ]
    assert run_capsules
    for capsule in run_capsules:
        assert capsule["authority_chain_ref"]
        assert capsule["tool_grant_refs"]
        assert capsule["action_trace_refs"]
        assert capsule["evidence_receipt_refs"]
        assert capsule["operator_readout_ref"]


def test_proof_pack_exhibit_references_run_capsule_and_operator_readout() -> None:
    fixture = load_json(FIXTURE)
    exhibits = [
        record["payload"]
        for record in fixture["fixtures"]
        if record["target_schema"] == "agentplane_proof_pack_exhibit.v1.json"
    ]
    assert exhibits
    for exhibit in exhibits:
        assert exhibit["run_capsule_ref"]
        assert exhibit["operator_readout_ref"]
        assert exhibit["evidence_receipt_refs"]
        assert exhibit["known_excluded_claims"]
