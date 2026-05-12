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


def transitive_scope_closure(scopes: set[str], lattice_edges: list[dict]) -> set[str]:
    """Return all scopes supported by a set of declared scopes.

    A constituent that supports a broader scope also supports any narrower scope
    declared by the lattice edge narrower_scope -> broader_scope. It does not
    automatically support broader scopes.
    """
    closure = set(scopes)
    changed = True
    while changed:
        changed = False
        for edge in lattice_edges:
            narrower = edge["narrower_scope"]
            broader = edge["broader_scope"]
            if broader in closure and narrower not in closure:
                closure.add(narrower)
                changed = True
    return closure


def supported_authority_scopes(instance: dict) -> set[str]:
    analysis = instance.get("authority_scope_analysis", {})
    declared = {
        scope
        for binding in analysis.get("constituent_scope_bindings", [])
        for scope in binding.get("declared_scopes", [])
    }
    return transitive_scope_closure(declared, analysis.get("scope_lattice", []))


def non_claim_pairs(records: list[dict]) -> set[tuple[str, str]]:
    return {
        (record["constituent_artifact_id"], record["non_claim"])
        for record in records
    }


def declared_evidence_pairs(instance: dict) -> set[tuple[str, str]]:
    return {
        (ref["evidence_receipt_id"], ref["evidence_receipt_sha256"])
        for ref in instance.get("evidence_receipt_refs", [])
    }


def has_cycle(edges: dict[str, set[str]]) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for next_node in edges.get(node, set()):
            if visit(next_node):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in edges)


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

    analysis = instance.get("authority_scope_analysis", {})
    artifact_ids = {item["artifact_id"] for item in instance.get("constituent_artifacts", [])}
    scope_binding_ids = {binding.get("constituent_artifact_id") for binding in analysis.get("constituent_scope_bindings", [])}
    if artifact_ids - scope_binding_ids:
        errors.append("authority scope analysis must bind every constituent artifact")
    if scope_binding_ids - artifact_ids:
        errors.append("authority scope analysis must not reference unknown constituent artifacts")

    supported_scopes = supported_authority_scopes(instance)
    if not composed.issubset(supported_scopes):
        errors.append("composed authority scope must be supported by constituent authority scopes")

    constituent_non_claims = {
        non_claim
        for item in instance.get("constituent_artifacts", [])
        for non_claim in item.get("non_claims", [])
    }
    propagated_or_resolved = set(instance.get("propagated_non_claims", [])) | set(instance.get("resolved_non_claims", []))
    if not constituent_non_claims.issubset(propagated_or_resolved):
        errors.append("composition must propagate or resolve constituent non-claims")

    non_claim_analysis = instance.get("non_claim_analysis")
    if non_claim_analysis is not None:
        source_pairs = non_claim_pairs(non_claim_analysis.get("source_non_claims", []))
        expected_source_pairs = {
            (item["artifact_id"], non_claim)
            for item in instance.get("constituent_artifacts", [])
            for non_claim in item.get("non_claims", [])
        }
        if source_pairs != expected_source_pairs:
            errors.append("non_claim_analysis source_non_claims must match constituent non-claims")

        propagated_pairs = non_claim_pairs(non_claim_analysis.get("propagation_records", []))
        resolved_pairs = non_claim_pairs(non_claim_analysis.get("resolution_records", []))
        handled_pairs = propagated_pairs | resolved_pairs
        if not source_pairs.issubset(handled_pairs):
            errors.append("non_claim_analysis must propagate or resolve every source non-claim")

        propagated_as_values = {
            record["propagated_as"]
            for record in non_claim_analysis.get("propagation_records", [])
        }
        if not propagated_as_values.issubset(set(instance.get("propagated_non_claims", []))):
            errors.append("non_claim_analysis propagation records must appear in propagated_non_claims")

        resolution_values = {
            record["non_claim"]
            for record in non_claim_analysis.get("resolution_records", [])
        }
        if not resolution_values.issubset(set(instance.get("resolved_non_claims", []))):
            errors.append("non_claim_analysis resolution records must appear in resolved_non_claims")

        declared_receipts_for_resolution = declared_evidence_pairs(instance)
        for record in non_claim_analysis.get("resolution_records", []):
            receipt = record["evidence_receipt_ref"]
            pair = (receipt["evidence_receipt_id"], receipt["evidence_receipt_sha256"])
            if pair not in declared_receipts_for_resolution:
                errors.append("non_claim_analysis resolutions must cite declared evidence receipts")
                break

    monitor_analysis = instance.get("monitor_independence_analysis")
    if monitor_analysis is not None:
        relationships = monitor_analysis.get("monitor_relationships", [])
        claim = monitor_analysis.get("independence_claim", {})
        target_ids = {item["artifact_id"] for item in instance.get("constituent_artifacts", [])}
        observed_targets = {relationship["target_artifact_id"] for relationship in relationships}
        if target_ids - observed_targets:
            errors.append("monitor_independence_analysis must cover every constituent artifact")
        if observed_targets - target_ids:
            errors.append("monitor_independence_analysis must not target unknown constituent artifacts")

        declared_receipts_for_monitoring = declared_evidence_pairs(instance)
        for relationship in relationships:
            receipt = relationship["evidence_receipt_ref"]
            pair = (receipt["evidence_receipt_id"], receipt["evidence_receipt_sha256"])
            if pair not in declared_receipts_for_monitoring:
                errors.append("monitor_independence_analysis monitor attestations must cite declared evidence receipts")
                break

        if claim.get("requires_distinct_monitors"):
            monitors = [relationship["monitor_id"] for relationship in relationships]
            if len(monitors) != len(set(monitors)):
                errors.append("monitor_independence_analysis requires distinct monitors for constituent artifacts")

        if claim.get("forbids_self_monitoring"):
            if any(relationship["monitor_id"] == relationship["target_artifact_id"] for relationship in relationships):
                errors.append("monitor_independence_analysis forbids self-monitoring relationships")

        if claim.get("requires_acyclic_monitor_graph"):
            edges: dict[str, set[str]] = {}
            for relationship in relationships:
                edges.setdefault(relationship["monitor_id"], set()).add(relationship["target_artifact_id"])
            if has_cycle(edges):
                errors.append("monitor_independence_analysis requires an acyclic monitor graph")

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

    declared_receipts = declared_evidence_pairs(instance)
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
        (
            "negative_composition_unsupported_authority_scope.synthetic.json",
            "composed authority scope must be supported by constituent authority scopes",
        ),
        (
            "negative_composition_unhandled_non_claim.synthetic.json",
            "non_claim_analysis must propagate or resolve every source non-claim",
        ),
        (
            "negative_composition_resolution_missing_evidence.synthetic.json",
            "non_claim_analysis resolutions must cite declared evidence receipts",
        ),
        (
            "negative_composition_shared_monitor.synthetic.json",
            "monitor_independence_analysis requires distinct monitors for constituent artifacts",
        ),
        (
            "negative_composition_self_monitoring.synthetic.json",
            "monitor_independence_analysis forbids self-monitoring relationships",
        ),
        (
            "negative_composition_monitor_cycle.synthetic.json",
            "monitor_independence_analysis requires an acyclic monitor graph",
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
        "negative_composition_unsupported_authority_scope.synthetic.json",
        "negative_composition_unhandled_non_claim.synthetic.json",
        "negative_composition_resolution_missing_evidence.synthetic.json",
        "negative_composition_shared_monitor.synthetic.json",
        "negative_composition_self_monitoring.synthetic.json",
        "negative_composition_monitor_cycle.synthetic.json",
    }
    actual = {path.name for path in FIXTURE_ROOT.glob("*.json")}
    assert actual == known
