from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_SCHEMA = ROOT / "schemas" / "governance-fabric" / "interpretability_composition_manifest.v1.json"
COMPOSITION_SCHEMA = ROOT / "schemas" / "governance-fabric" / "composition_certificate.v1.json"
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "governance-fabric" / "interpretability"
MANIFEST = FIXTURE_ROOT / "interpretability_composition_manifest.synthetic.json"
NEGATIVE_CASES = FIXTURE_ROOT / "interpretability_composition_negative_cases.synthetic.json"

EXPECTED_FRAGMENT_KINDS = {
    "model_artifact",
    "sae_artifact",
    "feature_artifact",
    "feature_explanation",
    "feature_activation_set",
    "steering_intervention",
    "causal_triad",
    "attribution_graph",
    "off_target_audit",
    "manifold_baseline",
    "implementability_curve",
    "robustness_certificate",
    "benchmark_result",
    "public_interpretability_note",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def validator(schema_path: Path) -> Draft202012Validator:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def compile_manifest_to_composition_certificate(manifest: dict) -> dict:
    fragments = manifest["fragment_set"]
    constituent_artifacts = []
    authority_refs = []
    scope_bindings = []
    receipt_bindings = []
    evidence_refs = []
    propagated_non_claims = list(manifest["non_claims"])

    for fragment in fragments:
        artifact_id = fragment["artifact_id"]
        artifact_sha = sha256(f"artifact:{artifact_id}")
        receipt_id = f"evidence-receipt-{artifact_id}"
        receipt_sha = sha256(f"receipt:{artifact_id}")
        authority_chain_id = fragment["authority_chain_id"]

        constituent_artifacts.append(
            {
                "artifact_kind": "program_certificate",
                "artifact_id": artifact_id,
                "artifact_sha256": artifact_sha,
                "schema_version": "1.0.0",
                "execution_status": manifest["execution_status"],
                "authority_chain_id": authority_chain_id,
                "non_claims": [
                    fragment["non_claim"],
                    f"interpretability fragment kind: {fragment['artifact_kind']}",
                ],
            }
        )
        authority_refs.append(
            {
                "authority_chain_id": authority_chain_id,
                "authority_chain_sha256": sha256(f"authority:{authority_chain_id}"),
            }
        )
        scope_bindings.append(
            {
                "constituent_artifact_id": artifact_id,
                "declared_scopes": [fragment["declared_scope"]],
            }
        )
        receipt_ref = {
            "evidence_receipt_id": receipt_id,
            "evidence_receipt_sha256": receipt_sha,
        }
        evidence_refs.append(receipt_ref)
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
        propagated_non_claims.extend(
            [
                fragment["non_claim"],
                f"interpretability fragment kind: {fragment['artifact_kind']}",
            ]
        )

    composition_receipt = {
        "evidence_receipt_id": f"evidence-receipt-{manifest['composition_certificate_id']}",
        "evidence_receipt_sha256": sha256(f"composition-receipt:{manifest['composition_certificate_id']}"),
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
        "constituent_artifacts": constituent_artifacts,
        "constituent_authority_chain_refs": authority_refs,
        "composition_authority_chain_ref": {
            "authority_chain_id": "auth-interpretability-composition",
            "authority_chain_sha256": sha256("authority:interpretability-composition"),
        },
        "composition_rule": {
            "rule_id": "interpretability-release-composition-rule.v1",
            "rule_version": "tier2-composition-rule.v1",
            "allowed_authority_scope": sorted({fragment["declared_scope"] for fragment in fragments}),
            "status_monotonicity": "no_synthetic_or_doctrine_to_runtime_upgrade",
            "recursive_composition_allowed": False,
        },
        "composed_authority_scope": manifest["composition_scope"],
        "authority_scope_analysis": {
            "comparison_mode": "declared_scope_lattice_v1",
            "constituent_scope_bindings": scope_bindings,
            "scope_lattice": [],
            "semantic_comparison_claim": {
                "composed_scope_must_be_supported_by_constituents": True
            },
        },
        "receipt_integration": {
            "integration_mode": "hash_bound_reference",
            "constituent_receipt_bindings": receipt_bindings,
            "composition_receipt_ref": composition_receipt,
        },
        "propagated_non_claims": propagated_non_claims,
        "resolved_non_claims": [],
        "off_history_refs": [],
        "evidence_receipt_refs": evidence_refs,
        "ledger_entry": {
            "event_id": f"ledger-{manifest['composition_certificate_id']}",
            "event_type": "interpretability.composition.synthetic",
            "created_at": manifest["created_at"],
        },
    }


def composition_static_errors(instance: dict) -> list[str]:
    errors: list[str] = []
    artifact_ids = {item["artifact_id"] for item in instance["constituent_artifacts"]}
    receipt_binding_ids = {
        binding["constituent_artifact_id"]
        for binding in instance["receipt_integration"]["constituent_receipt_bindings"]
    }

    if artifact_ids - receipt_binding_ids:
        errors.append("composition must bind receipts for every constituent artifact")

    allowed = set(instance["composition_rule"]["allowed_authority_scope"])
    composed = set(instance["composed_authority_scope"])
    if not composed.issubset(allowed):
        errors.append("composed authority scope exceeds allowed composition rule scope")

    supported = {
        scope
        for binding in instance["authority_scope_analysis"]["constituent_scope_bindings"]
        for scope in binding["declared_scopes"]
    }
    if not composed.issubset(supported):
        errors.append("composed authority scope must be supported by constituent authority scopes")

    return errors


def apply_mutation(instance: dict, mutation: str) -> dict:
    mutated = copy.deepcopy(instance)
    if mutation == "remove_public_note_receipt_binding":
        mutated["receipt_integration"]["constituent_receipt_bindings"] = [
            binding
            for binding in mutated["receipt_integration"]["constituent_receipt_bindings"]
            if binding["constituent_artifact_id"] != "public-interpretability-note-gemma-feature-789"
        ]
    elif mutation == "add_unsupported_runtime_steering_scope_allowed_by_rule":
        mutated["composition_rule"]["allowed_authority_scope"].append("runtime_steering_execution")
        mutated["composed_authority_scope"].append("runtime_steering_execution")
    elif mutation == "add_runtime_steering_scope_without_rule_permission":
        mutated["composed_authority_scope"].append("runtime_steering_execution")
    else:
        raise AssertionError(f"unknown mutation: {mutation}")
    return mutated


def test_interpretability_manifest_schema_and_fragment_set() -> None:
    manifest = load_json(MANIFEST)
    validator(MANIFEST_SCHEMA).validate(manifest)
    kinds = {fragment["artifact_kind"] for fragment in manifest["fragment_set"]}
    assert kinds == EXPECTED_FRAGMENT_KINDS
    assert len(manifest["fragment_set"]) == 14
    assert manifest["execution_status"] == "synthetic_fixture"


def test_interpretability_manifest_compiles_to_current_tier2_certificate() -> None:
    manifest = load_json(MANIFEST)
    certificate = compile_manifest_to_composition_certificate(manifest)
    validator(COMPOSITION_SCHEMA).validate(certificate)
    assert composition_static_errors(certificate) == []


def test_interpretability_domain_annotations_reference_known_fragments() -> None:
    manifest = load_json(MANIFEST)
    artifact_ids = {fragment["artifact_id"] for fragment in manifest["fragment_set"]}
    annotations = manifest["domain_annotations"]

    for dependency in annotations["authority_dependencies"]:
        assert dependency["from_artifact_id"] in artifact_ids
        assert dependency["to_artifact_id"] in artifact_ids

    for effect in annotations["control_effects"]:
        assert effect["source_artifact_id"] in artifact_ids
        assert set(effect["bounded_by"]).issubset(artifact_ids)

    for binding in annotations["cancellation_bindings"]:
        assert binding["trigger_artifact_id"] in artifact_ids


def test_interpretability_negative_cases_fail_expected_static_invariants() -> None:
    manifest = load_json(MANIFEST)
    certificate = compile_manifest_to_composition_certificate(manifest)
    cases = load_json(NEGATIVE_CASES)["cases"]

    for case in cases:
        mutated = apply_mutation(certificate, case["mutation"])
        validator(COMPOSITION_SCHEMA).validate(mutated)
        errors = composition_static_errors(mutated)
        assert case["expected_error"] in errors
