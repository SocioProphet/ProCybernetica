from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "governance-fabric" / "composition_certificate.v1.json"
TIER1_SAFETY_CASE_SCHEMA = ROOT / "schemas" / "governance-fabric" / "cybernetic_safety_case.v1.json"
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "governance-fabric" / "tier2"

STATUS_RANK = {
    "failed": 0,
    "doctrine_only": 1,
    "synthetic_fixture": 2,
    "runtime_partial": 3,
    "runtime_executed": 4,
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validator(schema_path: Path) -> Draft202012Validator:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def validate_schema_shape(instance: dict) -> None:
    validator(SCHEMA).validate(instance)


def composition_invariant_errors(instance: dict) -> list[str]:
    errors: list[str] = []

    if instance.get("composition_order") != 1:
        errors.append("composition_order must be 1 for v0.1")

    if instance.get("composition_rule", {}).get("recursive_composition_allowed") is not False:
        errors.append("recursive composition must be disabled for v0.1")

    composite_status = instance.get("execution_status")
    constituent_statuses = [item.get("execution_status") for item in instance.get("constituent_artifacts", [])]
    if constituent_statuses and STATUS_RANK[composite_status] > min(STATUS_RANK[item] for item in constituent_statuses):
        errors.append("composition cannot upgrade execution_status beyond weakest constituent")

    declared_authorities = {ref["authority_chain_id"] for ref in instance.get("constituent_authority_chain_refs", [])}
    required_authorities = {item["authority_chain_id"] for item in instance.get("constituent_artifacts", [])}
    if not required_authorities.issubset(declared_authorities):
        errors.append("composition must cover every constituent authority chain")

    allowed = set(instance.get("composition_rule", {}).get("allowed_authority_scope", []))
    composed = set(instance.get("composed_authority_scope", []))
    if not composed.issubset(allowed):
        errors.append("composed authority scope exceeds allowed composition rule scope")

    constituent_non_claims = {
        non_claim
        for item in instance.get("constituent_artifacts", [])
        for non_claim in item.get("non_claims", [])
    }
    propagated_or_resolved = set(instance.get("propagated_non_claims", [])) | set(instance.get("resolved_non_claims", []))
    if not constituent_non_claims.issubset(propagated_or_resolved):
        errors.append("composition must propagate or resolve constituent non-claims")

    artifacts_by_id = {
        item["artifact_id"]: item["artifact_sha256"]
        for item in instance.get("constituent_artifacts", [])
    }
    bindings = instance.get("receipt_integration", {}).get("constituent_receipt_bindings", [])
    bindings_by_id = {binding.get("constituent_artifact_id"): binding for binding in bindings}

    missing_receipt_bindings = set(artifacts_by_id) - set(bindings_by_id)
    if missing_receipt_bindings:
        errors.append("composition must bind receipts for every constituent artifact")

    unknown_receipt_bindings = set(bindings_by_id) - set(artifacts_by_id)
    if unknown_receipt_bindings:
        errors.append("composition receipt bindings must not reference unknown constituent artifacts")

    for artifact_id, artifact_sha256 in artifacts_by_id.items():
        binding = bindings_by_id.get(artifact_id)
        if binding is not None and binding.get("constituent_artifact_sha256") != artifact_sha256:
            errors.append("composition receipt binding hash must match constituent artifact hash")

    declared_receipts = {
        (ref["evidence_receipt_id"], ref["evidence_receipt_sha256"])
        for ref in instance.get("evidence_receipt_refs", [])
    }
    integration = instance.get("receipt_integration", {})
    expected_receipts = set()
    for binding in bindings:
        for receipt_ref in binding.get("receipt_refs", []):
            if receipt_ref.get("receipt_kind") == "evidence_receipt":
                expected_receipts.add((receipt_ref["receipt_id"], receipt_ref["receipt_sha256"]))
    composition_receipt = integration.get("composition_receipt_ref")
    if composition_receipt:
        expected_receipts.add((composition_receipt["evidence_receipt_id"], composition_receipt["evidence_receipt_sha256"]))

    if not expected_receipts.issubset(declared_receipts):
        errors.append("composition evidence_receipt_refs must include all hash-bound receipt bindings")

    return errors


def test_tier2_composition_certificate_valid_fixture() -> None:
    instance = load_json(FIXTURE_ROOT / "composition_certificate.synthetic.json")
    validate_schema_shape(instance)
    assert composition_invariant_errors(instance) == []


def test_negative_composite_claim_without_composition_certificate_fails_schema_or_static_gate() -> None:
    instance = load_json(FIXTURE_ROOT / "negative_composite_claim_without_composition_certificate.synthetic.json")
    # This fixture is intentionally a Tier 1 safety case, not a composition certificate.
    # It shows that composite claims cannot satisfy Tier 2 by merely passing Tier 1 shape.
    validator(TIER1_SAFETY_CASE_SCHEMA).validate(instance)
    assert instance["certificate_kind"] != "composition_certificate"


@pytest.mark.parametrize(
    ("fixture_name", "expected_error"),
    [
        (
            "negative_composition_status_boundary.synthetic.json",
            "composition cannot upgrade execution_status beyond weakest constituent",
        ),
        (
            "negative_composition_missing_authority_coverage.synthetic.json",
            "composition must cover every constituent authority chain",
        ),
        (
            "negative_composition_missing_receipt_binding.synthetic.json",
            "composition must bind receipts for every constituent artifact",
        ),
        (
            "negative_composition_unknown_receipt_binding.synthetic.json",
            "composition receipt bindings must not reference unknown constituent artifacts",
        ),
        (
            "negative_composition_receipt_hash_mismatch.synthetic.json",
            "composition receipt binding hash must match constituent artifact hash",
        ),
    ],
)
def test_tier2_static_negative_fixtures_fail_intended_invariants(
    fixture_name: str,
    expected_error: str,
) -> None:
    instance = load_json(FIXTURE_ROOT / fixture_name)
    validate_schema_shape(instance)
    errors = composition_invariant_errors(instance)
    assert expected_error in errors


def test_tier2_fixture_inventory_is_explicit() -> None:
    known = {
        "composition_certificate.synthetic.json",
        "negative_composite_claim_without_composition_certificate.synthetic.json",
        "negative_composition_status_boundary.synthetic.json",
        "negative_composition_missing_authority_coverage.synthetic.json",
        "negative_composition_missing_receipt_binding.synthetic.json",
        "negative_composition_unknown_receipt_binding.synthetic.json",
        "negative_composition_receipt_hash_mismatch.synthetic.json",
    }
    actual = {path.name for path in FIXTURE_ROOT.glob("*.json")}
    assert actual == known
