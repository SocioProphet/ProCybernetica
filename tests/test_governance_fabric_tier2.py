from __future__ import annotations

import copy
import hashlib
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


def sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


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


def interpretability_scope_lattice() -> list[dict]:
    return [
        {"narrower_scope": "record_model_artifact", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "record_sae_artifact", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "record_feature_artifact", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "record_feature_explanation", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "record_feature_activation_set", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "record_steering_intervention", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "record_causal_triad", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "record_attribution_graph", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "record_off_target_audit", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "record_manifold_baseline", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "record_implementability_curve", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "record_robustness_certificate", "broader_scope": "govern_interpretability_release_candidate"},
        {"narrower_scope": "govern_interpretability_release_candidate", "broader_scope": "publish_public_interpretability_note"},
    ]


def build_interpretability_composition(manifest: dict) -> dict:
    artifacts = []
    authority_refs = []
    scope_bindings = []
    receipt_bindings = []
    evidence_refs = []
    allowed_scopes = set(manifest["composition_scope"])

    for fragment in manifest["fragment_set"]:
        artifact_id = fragment["artifact_id"]
        artifact_sha = sha256(f"artifact:{artifact_id}")
        declared_scope = fragment["declared_scope"]
        allowed_scopes.add(declared_scope)
        artifacts.append(
            {
                "artifact_kind": fragment["artifact_kind"],
                "artifact_id": artifact_id,
                "artifact_sha256": artifact_sha,
                "schema_version": "0.1.0",
                "execution_status": manifest["execution_status"],
                "authority_chain_id": fragment["authority_chain_id"],
                "non_claims": [fragment["non_claim"]],
            }
        )
        authority_refs.append(
            {
                "authority_chain_id": fragment["authority_chain_id"],
                "authority_chain_sha256": sha256(f"authority:{fragment['authority_chain_id']}"),
            }
        )
        scope_bindings.append(
            {
                "constituent_artifact_id": artifact_id,
                "declared_scopes": [declared_scope],
            }
        )
        receipt_id = f"evidence-{artifact_id}"
        receipt_sha = sha256(f"receipt:{receipt_id}")
        receipt_bindings.append(
            {
                "constituent_artifact_id": artifact_id,
                "constituent_artifact_sha256": artifact_sha,
                "receipt_refs": [
                    {
                        "receipt_kind": "evidence_receipt",
                        "receipt_id": receipt_id,
                        "receipt_sha256": receipt_sha,
                        "schema_version": "1.0.0",
                    }
                ],
            }
        )
        evidence_refs.append(
            {
                "evidence_receipt_id": receipt_id,
                "evidence_receipt_sha256": receipt_sha,
            }
        )

    composition_receipt = {
        "evidence_receipt_id": "evidence-interpretability-release-composition",
        "evidence_receipt_sha256": sha256("receipt:interpretability-release-composition"),
    }
    evidence_refs.append(composition_receipt)

    return {
        "schema_version": "1.0.0",
        "certificate_kind": "composition_certificate",
        "composition_certificate_id": manifest["composition_certificate_id"],
        "created_at": manifest["created_at"],
        "execution_status": manifest["execution_status"],
        "composition_order": 1,
        "composition_kind": "flat_agent_composition",
        "constituent_artifacts": artifacts,
        "constituent_authority_chain_refs": authority_refs,
        "composition_authority_chain_ref": {
            "authority_chain_id": "auth-tier2-interpretability-composition",
            "authority_chain_sha256": sha256("authority:auth-tier2-interpretability-composition"),
        },
        "composition_rule": {
            "rule_id": "flat-interpretability-release-composition-rule",
            "rule_version": "tier2-composition-rule.v1",
            "allowed_authority_scope": sorted(allowed_scopes),
            "status_monotonicity": "no_synthetic_or_doctrine_to_runtime_upgrade",
            "recursive_composition_allowed": False,
        },
        "composed_authority_scope": manifest["composition_scope"],
        "authority_scope_analysis": {
            "comparison_mode": "declared_scope_lattice_v1",
            "constituent_scope_bindings": scope_bindings,
            "scope_lattice": interpretability_scope_lattice(),
            "semantic_comparison_claim": {"composed_scope_must_be_supported_by_constituents": True},
        },
        "receipt_integration": {
            "integration_mode": "hash_bound_reference",
            "constituent_receipt_bindings": receipt_bindings,
            "composition_receipt_ref": composition_receipt,
        },
        "propagated_non_claims": [
            fragment["non_claim"] for fragment in manifest["fragment_set"]
        ]
        + [
            "Composition is synthetic fixture only.",
            "Does not claim runtime steering executed.",
            "Does not claim public interpretability publication has occurred.",
        ],
        "resolved_non_claims": [],
        "off_history_refs": [
            {
                "off_history_id": "off-history-interpretability-negative-controls",
                "off_history_sha256": sha256("offhistory:interpretability-negative-controls"),
            }
        ],
        "evidence_receipt_refs": evidence_refs,
        "composition_domain_annotations": manifest["domain_annotations"],
        "ledger_entry": {
            "event_id": "composition-cert-interpretability-release-gemma-feature-789-event",
            "event_type": "composition_certificate_recorded",
            "created_at": manifest["created_at"],
        },
    }


def apply_interpretability_mutation(instance: dict, mutation: str) -> dict:
    mutated = copy.deepcopy(instance)

    if mutation == "remove_public_note_receipt_binding":
        mutated["receipt_integration"]["constituent_receipt_bindings"] = [
            binding
            for binding in mutated["receipt_integration"]["constituent_receipt_bindings"]
            if binding["constituent_artifact_id"] != "public-interpretability-note-gemma-feature-789"
        ]
    elif mutation == "add_unsupported_runtime_steering_scope_allowed_by_rule":
        mutated["composed_authority_scope"].append("runtime_steering_authority")
        mutated["composition_rule"]["allowed_authority_scope"].append("runtime_steering_authority")
    elif mutation == "add_runtime_steering_scope_without_rule_permission":
        mutated["composed_authority_scope"].append("runtime_steering_authority")
    else:
        raise AssertionError(f"unknown interpretability mutation: {mutation}")

    return mutated


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

    annotations = instance.get("composition_domain_annotations", {})
    for dependency in annotations.get("authority_dependencies", []):
        if dependency["from_artifact_id"] not in artifact_ids or dependency["to_artifact_id"] not in artifact_ids:
            errors.append("domain authority dependency must reference known constituent artifacts")
    for effect in annotations.get("control_effects", []):
        if effect["source_artifact_id"] not in artifact_ids:
            errors.append("domain control effect must reference known source artifact")
        if set(effect.get("bounded_by", [])) - artifact_ids:
            errors.append("domain control effect bounds must reference known constituent artifacts")
    for binding in annotations.get("cancellation_bindings", []):
        if binding["trigger_artifact_id"] not in artifact_ids:
            errors.append("domain cancellation binding must reference known trigger artifact")

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


def test_interpretability_14_fragment_composition_manifest_builds_valid_certificate() -> None:
    manifest = load_json(FIXTURE_ROOT / "interpretability_composition_manifest.synthetic.json")
    instance = build_interpretability_composition(manifest)
    validate_schema_shape(instance)
    assert len(instance["constituent_artifacts"]) == 14
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


@pytest.mark.parametrize(
    "case",
    load_json(FIXTURE_ROOT / "interpretability_composition_negative_cases.synthetic.json")["cases"],
)
def test_interpretability_composition_negative_cases_fail_intended_invariants(case: dict) -> None:
    manifest = load_json(FIXTURE_ROOT / "interpretability_composition_manifest.synthetic.json")
    instance = build_interpretability_composition(manifest)
    mutated = apply_interpretability_mutation(instance, case["mutation"])
    validate_schema_shape(mutated)
    errors = composition_invariant_errors(mutated)
    assert case["expected_error"] in errors


def test_tier2_fixture_inventory_is_explicit() -> None:
    known = {
        "composition_certificate.synthetic.json",
        "interpretability_composition_manifest.synthetic.json",
        "interpretability_composition_negative_cases.synthetic.json",
        "negative_composite_claim_without_composition_certificate.synthetic.json",
        "negative_composition_status_boundary.synthetic.json",
        "negative_composition_missing_authority_coverage.synthetic.json",
        "negative_composition_missing_receipt_binding.synthetic.json",
        "negative_composition_unknown_receipt_binding.synthetic.json",
        "negative_composition_receipt_hash_mismatch.synthetic.json",
        "negative_composition_unsupported_authority_scope.synthetic.json",
    }
    actual = {path.name for path in FIXTURE_ROOT.glob("*.json")}
    assert actual == known
