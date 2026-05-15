from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "bridges"
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_bridges.py"
FIXTURE = ROOT / "tests" / "fixtures" / "bridges" / "bridge-fixtures.synthetic.json"

SCHEMA_FILES = {
    "ops-history-to-pneumachinalis.v1.json",
    "masonmark-to-certificate.v1.json",
    "certificate-to-atlas.v1.json",
}

EXPECTED_FAILURE_REASONS = {
    "human_actor_requires_consent_for_reputation_microbeat",
    "promotion_state_strict_inheritance",
    "verifier_scores_consistent_with_verdict",
    "undecided_fails_closed_to_deny",
    "pattern_c_always_denies",
}

POSITIVE_CATEGORIES = {
    "opshistory-machine-actor-to-pneumachinalis-microbeat",
    "masonmark-proofpack-to-m2-pattern-a-certificate",
    "m2-pattern-a-certificate-to-atlas-admit",
    "undecided-certificate-to-atlas-deny-fail-closed",
}

NEGATIVE_CATEGORIES = {
    "human-actor-reputation-microbeat-without-consent",
    "candidate-proofpack-mapped-to-promoted-stele",
    "verifier-scores-inconsistent-with-verdict",
    "undecided-certificate-admits",
    "pattern-c-admits",
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


def test_bridge_json_schemas_are_valid_draft_2020_12() -> None:
    for schema_name in SCHEMA_FILES:
        Draft202012Validator.check_schema(load_json(SCHEMA_DIR / schema_name))


def test_bridge_validator_passes_fixture_set() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["fixture_count"] == 9
    assert all(result["passed"] for result in payload["results"])


def test_bridge_fixtures_cover_required_positive_and_negative_cases() -> None:
    payload = run_validator()
    categories = {result["category"] for result in payload["results"]}
    assert POSITIVE_CATEGORIES <= categories
    assert NEGATIVE_CATEGORIES <= categories


def test_bridge_fixtures_cover_all_three_schemas() -> None:
    payload = run_validator()
    targets = {result["target_schema"] for result in payload["results"]}
    assert targets == SCHEMA_FILES


def test_negative_bridge_fixtures_fail_for_intended_reasons() -> None:
    payload = run_validator()
    negative_results = [result for result in payload["results"] if result["expected_result"] == "fail"]
    assert len(negative_results) == 5

    observed = {result["expected_failure_reason"] for result in negative_results}
    assert observed == EXPECTED_FAILURE_REASONS

    for result in negative_results:
        assert result["expected_failure_reason"] in result["observed_failures"]
        assert result["actual_result"] == "fail"
        assert result["passed"] is True


def test_positive_bridge_fixtures_pass() -> None:
    payload = run_validator()
    positives = [result for result in payload["results"] if result["expected_result"] == "pass"]
    assert len(positives) == 4
    for result in positives:
        assert result["actual_result"] == "pass"
        assert result["observed_failures"] == []
        assert result["passed"] is True


def test_capability_tier_invocation_is_optional_and_additive() -> None:
    payload = run_validator()
    with_invocation = [
        result for result in payload["results"]
        if result["capability_tier_invocation_present"] is True
    ]
    without_invocation = [
        result for result in payload["results"]
        if result["capability_tier_invocation_present"] is False
    ]

    assert with_invocation
    assert without_invocation
    assert all(result["passed"] for result in with_invocation + without_invocation)


def test_bridge_execution_plan_is_present() -> None:
    plan = ROOT / "docs" / "bridges" / "BRIDGE_SCHEMAS_V1_EXECUTION_PLAN.md"
    text = plan.read_text(encoding="utf-8")
    assert "ops-history-to-pneumachinalis.v1.json" in text
    assert "masonmark-to-certificate.v1.json" in text
    assert "certificate-to-atlas.v1.json" in text
    assert "#47" in text
