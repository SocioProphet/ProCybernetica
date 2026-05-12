from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_ROOT = ROOT / "schemas"
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "governance-fabric"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validator(schema_path: Path) -> Draft202012Validator:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


VALID_CASES = [
    (
        SCHEMA_ROOT / "governance-fabric" / "authority_chain.v1.json",
        FIXTURE_ROOT / "authority_chain.synthetic.json",
    ),
    (
        SCHEMA_ROOT / "governance-fabric" / "tool_permission_scope.v1.json",
        FIXTURE_ROOT / "tool_permission_scope.synthetic.json",
    ),
    (
        SCHEMA_ROOT / "governance-fabric" / "evidence_receipt.v1.json",
        FIXTURE_ROOT / "evidence_receipt.synthetic.json",
    ),
    (
        SCHEMA_ROOT / "governance-fabric" / "off_history_evidence.v1.json",
        FIXTURE_ROOT / "off_history_evidence.synthetic.json",
    ),
    (
        SCHEMA_ROOT / "governance-fabric" / "monitor_alert.v1.json",
        FIXTURE_ROOT / "monitor_alert.synthetic.json",
    ),
    (
        SCHEMA_ROOT / "governance-fabric" / "agent_action_trace.v1.json",
        FIXTURE_ROOT / "allowed_action.synthetic.json",
    ),
    (
        SCHEMA_ROOT / "governance-fabric" / "agent_action_trace.v1.json",
        FIXTURE_ROOT / "blocked_action.synthetic.json",
    ),
    (
        SCHEMA_ROOT / "governance-fabric" / "safe_completion_decision.v1.json",
        FIXTURE_ROOT / "transformed_safe_completion.synthetic.json",
    ),
    (
        SCHEMA_ROOT / "governance-fabric" / "promotion_decision.v1.json",
        FIXTURE_ROOT / "release_delta_promotion.synthetic.json",
    ),
    (
        SCHEMA_ROOT / "governance-fabric" / "cybernetic_safety_case.v1.json",
        FIXTURE_ROOT / "safety_case.synthetic.json",
    ),
    (
        SCHEMA_ROOT / "composition" / "program-certificate.v1.json",
        FIXTURE_ROOT / "program-certificate.synthetic.json",
    ),
]


NEGATIVE_CASES = [
    (
        "no promotion by prose: evidence_receipt_refs must be non-empty",
        SCHEMA_ROOT / "governance-fabric" / "promotion_decision.v1.json",
        FIXTURE_ROOT / "invalid_promotion_by_prose.synthetic.json",
    ),
    (
        "no hidden authority lane: action traces require authority_chain_ref",
        SCHEMA_ROOT / "governance-fabric" / "agent_action_trace.v1.json",
        FIXTURE_ROOT / "invalid_action_missing_authority.synthetic.json",
    ),
    (
        "non-claims are load-bearing: safety cases require non_claims",
        SCHEMA_ROOT / "governance-fabric" / "cybernetic_safety_case.v1.json",
        FIXTURE_ROOT / "negative_safety_case_empty_non_claims.synthetic.json",
    ),
]


@pytest.mark.parametrize("schema_path, fixture_path", VALID_CASES)
def test_governance_fabric_tier1_valid_fixtures(schema_path: Path, fixture_path: Path) -> None:
    assert schema_path.exists(), schema_path
    assert fixture_path.exists(), fixture_path
    validator(schema_path).validate(load_json(fixture_path))


@pytest.mark.parametrize("reason, schema_path, fixture_path", NEGATIVE_CASES)
def test_governance_fabric_tier1_negative_fixtures_fail(
    reason: str, schema_path: Path, fixture_path: Path
) -> None:
    assert schema_path.exists(), schema_path
    assert fixture_path.exists(), fixture_path
    errors = list(validator(schema_path).iter_errors(load_json(fixture_path)))
    assert errors, reason


def test_governance_fabric_tier1_fixture_inventory_is_explicit() -> None:
    known = {path.name for _, path in VALID_CASES} | {path.name for _, _, path in NEGATIVE_CASES}
    actual = {path.name for path in FIXTURE_ROOT.glob("*.json")}
    assert actual == known
