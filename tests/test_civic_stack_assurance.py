from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "assurance"
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_civic_stack.py"
FIXTURE = ROOT / "tests" / "fixtures" / "civic-stack" / "civic-stack-assurance.synthetic.json"
SPEC = ROOT / "docs" / "assurance" / "CIVIC_STACK_ASSURANCE_BINDING.md"

SCHEMA_FILES = {
    "civic_risk_control_binding.v1.json",
    "civic_evidence_pack.v1.json",
    "civic_incident_control_event.v1.json",
    "civic_audit_signal.v1.json",
    "civic_risk_contribution.v1.json",
    "civic_assurance_trace.v1.json",
}

REQUIRED_TRACE_STEPS = [
    "artifact_deployed",
    "policy_checked",
    "runtime_attested",
    "control_verified",
    "evidence_pack_emitted",
    "score_updated",
]


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


def test_civic_stack_schemas_are_valid_draft_2020_12() -> None:
    for schema_name in SCHEMA_FILES:
        Draft202012Validator.check_schema(load_json(SCHEMA_DIR / schema_name))


def test_civic_stack_validator_passes_fixture_set() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["fixture_count"] == 8
    assert all(result["passed"] for result in payload["results"])


def test_civic_stack_fixtures_cover_all_schema_targets() -> None:
    payload = run_validator()
    targets = {result["target_schema"] for result in payload["results"] if "target_schema" in result}
    assert targets == SCHEMA_FILES


def test_civic_stack_worked_trace_has_required_sequence() -> None:
    fixture = load_json(FIXTURE)
    trace = next(
        record["payload"] for record in fixture["fixtures"]
        if record["fixture_id"] == "civic-assurance-worked-trace"
    )
    observed = [step["step_kind"] for step in sorted(trace["steps"], key=lambda item: item["step_index"])]
    assert observed == REQUIRED_TRACE_STEPS
    assert trace["evidence_pack_ref"]
    assert trace["audit_signal_ref"]
    assert trace["risk_control_binding_refs"]
    assert trace["rational_grl_contribution_refs"]


def test_civic_stack_audit_signal_is_scoreable_by_delivery_excellence() -> None:
    fixture = load_json(FIXTURE)
    audit_signal = next(
        record["payload"] for record in fixture["fixtures"]
        if record["target_schema"] == "civic_audit_signal.v1.json"
    )
    assert audit_signal["scoreability_status"] == "scoreable"
    assert audit_signal["delivery_excellence_score_ref"]
    assert audit_signal["dimensions"]["policy_decision_coverage"] >= 0
    assert audit_signal["dimensions"]["runtime_attestation_coverage"] >= 0


def test_civic_stack_incident_ready_for_sociosphere() -> None:
    fixture = load_json(FIXTURE)
    incident = next(
        record["payload"] for record in fixture["fixtures"]
        if record["target_schema"] == "civic_incident_control_event.v1.json"
    )
    assert incident["sociosphere_consumption_status"] == "ready_for_ingest"
    assert incident["control_refs"]
    assert incident["evidence_pack_ref"]
    assert incident["evidence_receipt_refs"]


def test_civic_stack_rational_grl_defeater_is_present() -> None:
    fixture = load_json(FIXTURE)
    contribution = next(
        record["payload"] for record in fixture["fixtures"]
        if record["target_schema"] == "civic_risk_contribution.v1.json"
    )
    assert contribution["contribution_kind"] == "defeater"
    assert "rationalgrl" in contribution["semantic_anchor_ref"].lower()
    assert contribution["risk_control_binding_ref"]


def test_invalid_civic_stack_fixtures_fail_for_intended_reasons() -> None:
    payload = run_validator()
    invalid = {
        result["fixture_id"]: result for result in payload["results"]
        if result.get("expected_result") == "fail"
    }
    assert invalid["civic-evidence-pack-invalid-no-binding"]["expected_failure_reason"] == "schema_validation_error"
    assert "schema_validation_error" in invalid["civic-evidence-pack-invalid-no-binding"]["observed_failures"]
    assert invalid["civic-assurance-trace-invalid-missing-step"]["expected_failure_reason"] == "worked_trace_requires_all_steps"
    assert "worked_trace_requires_all_steps" in invalid["civic-assurance-trace-invalid-missing-step"]["observed_failures"]


def test_civic_stack_binding_spec_records_ownership_boundaries() -> None:
    text = SPEC.read_text(encoding="utf-8")
    assert "Ontogenesis owns civic ontology" in text
    assert "Delivery Excellence" in text
    assert "SocioSphere" in text
    assert "Policy Fabric" in text
    assert "AgentPlane" in text
    assert "does not own the civic ontology" in text
    assert "does not own runtime execution" in text
    assert "does not own public-value scoring" in text
