from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_estate_alignment_followups.py"
FIXTURE = ROOT / "tests" / "fixtures" / "estate-alignment" / "estate-alignment-followups.synthetic.json"
CONFORMANCE_DOC = ROOT / "docs" / "integration" / "ESTATE_ALIGNMENT_FOLLOWUP_CONFORMANCE.md"

REQUIRED_ISSUES = {"#15", "#16", "#17"}
REQUIRED_FAMILIES = {"ontogenesis", "foundry_model_governance", "operator_workstation"}


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


def load_fixture() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_estate_alignment_followup_validator_passes() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["fixture_count"] == 3
    assert all(result["passed"] for result in payload["results"])


def test_estate_alignment_followup_covers_all_remaining_issues_and_families() -> None:
    fixture = load_fixture()
    issues = {record["issue_ref"] for record in fixture["fixtures"]}
    families = {record["adapter_family"] for record in fixture["fixtures"]}
    assert issues == REQUIRED_ISSUES
    assert families == REQUIRED_FAMILIES


def test_ontogenesis_fixture_requires_ontology_and_validation_evidence_refs() -> None:
    fixture = load_fixture()
    record = next(entry for entry in fixture["fixtures"] if entry["issue_ref"] == "#15")
    payload = record["payload"]
    assert payload["claim_status"] == "validated"
    assert payload["ontology_ref"].startswith("ontogenesis://")
    assert payload["shacl_report_ref"].startswith("ontogenesis://")
    assert payload["ledger_ref"].startswith("ontogenesis://")
    assert payload["signature_ref"].startswith("ontogenesis://")


def test_foundry_fixture_records_maturity_route_and_score_slice_refs() -> None:
    fixture = load_fixture()
    record = next(entry for entry in fixture["fixtures"] if entry["issue_ref"] == "#16")
    payload = record["payload"]
    assert payload["foundry_maturity_ref"]
    assert payload["model_route_ref"]
    assert payload["model_governance_record_ref"]
    assert payload["evaluation_result_ref"]
    assert payload["promotion_decision_ref"]
    assert payload["public_score_slice_ref"]


def test_operator_fixture_preserves_operator_gateway_invariants() -> None:
    fixture = load_fixture()
    record = next(entry for entry in fixture["fixtures"] if entry["issue_ref"] == "#17")
    payload = record["payload"]
    for key in [
        "operator_surface_ref",
        "command_envelope_ref",
        "capability_descriptor_ref",
        "receipt_ref",
        "replay_ref",
        "policy_ref",
        "approval_ref",
        "dashboard_surface_ref",
        "public_projection_ref",
    ]:
        assert payload[key]


def test_estate_alignment_conformance_doc_records_non_ownership_boundaries() -> None:
    text = CONFORMANCE_DOC.read_text(encoding="utf-8")
    assert "must not claim ownership" in text
    assert "does not implement Ontogenesis validation" in text
    assert "does not implement terminal, browser, workstation, or UI runtime" in text
    assert "validated semantic claims must carry ontology_ref" in text
    assert "model-governance evidence rows must cite external owning surfaces" in text
    assert "operator/gateway surfaces must preserve identity" in text
