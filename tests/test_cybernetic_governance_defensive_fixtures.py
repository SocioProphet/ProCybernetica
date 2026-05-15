from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_defensive_fixtures.py"
FIXTURE = ROOT / "tests" / "fixtures" / "cybernetic-governance" / "defensive-fixtures.synthetic.json"


def run_validator(*extra_args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE), *extra_args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_cybernetic_governance_defensive_fixture_validator_passes() -> None:
    result = run_validator("--json")
    assert result.returncode == 0, result.stderr

    payload = json.loads(result.stdout)
    assert payload["passed"] is True
    assert payload["fixture_count"] == 13
    assert {entry["actual_result"] for entry in payload["results"]} == {"pass", "fail"}


def test_defensive_fixtures_cover_required_categories() -> None:
    result = run_validator("--json")
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)

    observed_categories = {entry["category"] for entry in payload["results"]}
    expected_categories = {
        "low-risk-action-approval",
        "action-blocking",
        "safe-completion-transformation",
        "irreversible-action-approval",
        "untrusted-external-content-handling",
        "governance-control-modification-attempts",
        "invalid-prose-only-promotion",
        "hidden-release-compensation",
        "missing-off-history-evidence",
        "publication-boundary-enforcement",
        "high-authority-concentration-snapshots",
        "monitor-configuration-review",
        "safety-case-non-claim-enforcement",
    }

    assert expected_categories <= observed_categories


def test_invalid_fixtures_fail_for_intended_reasons() -> None:
    result = run_validator("--json")
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)

    invalid_results = {
        entry["fixture_id"]: entry
        for entry in payload["results"]
        if entry["expected_result"] == "fail"
    }

    assert invalid_results["cg-invalid-prose-only-promotion"]["expected_failure_reason"] == "schema_validation_error"
    assert invalid_results["cg-invalid-safety-case-non-claim-enforcement"]["expected_failure_reason"] == "schema_validation_error"
    assert invalid_results["cg-invalid-hidden-release-compensation"]["expected_failure_reason"] == "hidden_release_compensation"
    assert invalid_results["cg-invalid-missing-off-history-evidence"]["expected_failure_reason"] == "missing_off_history_evidence"
    assert invalid_results["cg-invalid-publication-boundary-enforcement"]["expected_failure_reason"] == "private_evidence_requires_redaction_ref"
    assert invalid_results["cg-invalid-high-authority-concentration"]["expected_failure_reason"] == "high_authority_concentration_requires_mitigation"

    for entry in invalid_results.values():
        assert entry["passed"] is True
        assert entry["expected_failure_reason"] in entry["observed_failures"]


def test_validator_output_maps_to_constitutional_invariants() -> None:
    result = run_validator("--json")
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)

    all_invariants = {
        invariant
        for entry in payload["results"]
        for invariant in entry["invariant_refs"]
    }

    assert "invariant_0_1_no_hidden_authority_lane" in all_invariants
    assert "invariant_0_2_no_action_without_trace" in all_invariants
    assert "invariant_0_3_no_promotion_by_prose" in all_invariants
    assert "invariant_0_5_separation_of_powers" in all_invariants
    assert "invariant_0_7_irreversibility_requires_approval" in all_invariants
    assert "invariant_0_8_off_history_retained" in all_invariants
    assert "invariant_0_9_privacy_and_evidence_minimization" in all_invariants
    assert "invariant_0_10_claims_require_non_claims" in all_invariants
    assert "invariant_0_11_release_delta_required" in all_invariants
    assert "invariant_0_12_monitors_are_monitored" in all_invariants
    assert "invariant_0_13_safety_case_before_frontier_promotion" in all_invariants
    assert "invariant_0_14_public_first_redaction_disciplined_assurance" in all_invariants
    assert "invariant_0_15_frontier_claims_require_metrics" in all_invariants
