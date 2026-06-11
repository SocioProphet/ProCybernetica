#!/usr/bin/env python3
"""Validate Enrichment Twin genesis seed and claim hologram fixtures.

Validates:
  - GenesisSeed schema + photo-v1 fixture
  - EnrichmentClaimHologram schema + scene fixture
  - Invalid fixtures are correctly rejected

This validator does not implement the enrichment runtime. It validates the
architecture-phase artefacts from docs/architecture/enrichment-twin-mission-spec.md.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[2]

SEED_SCHEMA_FILE = ROOT / "schemas" / "genesis_seed.schema.json"
CLAIM_SCHEMA_FILE = ROOT / "schemas" / "enrichment_claim_hologram.schema.json"

FIXTURES_DIR = ROOT / "tests" / "fixtures" / "enrichment"

VALID_SEED_FILES = [
    FIXTURES_DIR / "genesis-seed.photo-v1.json",
]

VALID_CLAIM_FILES = [
    FIXTURES_DIR / "enrichment-claim.scene.valid.json",
]

INVALID_SEED_FILES = [
    FIXTURES_DIR / "genesis-seed.missing-approval.invalid.json",
]

INVALID_CLAIM_FILES = [
    FIXTURES_DIR / "enrichment-claim.missing-provenance.invalid.json",
]

# Enrichment twin invariants beyond schema validation
REQUIRED_APPROVAL_GATES = {"burst_cloud_placement", "host_index_writeback"}
REQUIRED_POLICY_PREFIXES = {"policy:enrichment/", "policy:placement/"}
SENSITIVE_MODALITIES = {"face_cluster", "text_ocr", "location"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schema(path: Path) -> dict[str, Any]:
    schema = load_json(path)
    Draft202012Validator.check_schema(schema)
    return schema


def schema_errors(schema: dict[str, Any], instance: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    return [e.message for e in sorted(validator.iter_errors(instance), key=str)]


def validate_seed_invariants(seed: dict[str, Any]) -> list[str]:
    """Enrichment twin invariants beyond JSON Schema for genesis seeds."""
    errors: list[str] = []

    approval = seed.get("approval_profile", {})
    missing_gates = REQUIRED_APPROVAL_GATES - set(approval.keys())
    if missing_gates:
        errors.append(f"approval_profile missing required gates: {sorted(missing_gates)}")

    policy_refs: list[str] = seed.get("policy_profile", [])
    for prefix in REQUIRED_POLICY_PREFIXES:
        if not any(p.startswith(prefix) for p in policy_refs):
            errors.append(f"policy_profile missing a policy with prefix '{prefix}'")

    provider_refs: list[str] = seed.get("provider_profile", [])
    if not any(p.startswith("provider:") for p in provider_refs):
        errors.append("provider_profile must contain at least one provider: ref")

    return errors


def validate_claim_invariants(claim: dict[str, Any]) -> list[str]:
    """Enrichment twin invariants beyond JSON Schema for claim holograms."""
    errors: list[str] = []

    relation_types = {r.get("type") for r in claim.get("relations", [])}
    for required_rel in ("derived_from", "produced_by", "governed_by"):
        if required_rel not in relation_types:
            errors.append(f"relations missing required type: {required_rel}")

    traits = claim.get("traits", {})
    modality = traits.get("modality")
    sensitivity = traits.get("sensitivity_class")
    if modality in SENSITIVE_MODALITIES and sensitivity not in ("sensitive", None):
        errors.append(
            f"modality '{modality}' must have sensitivity_class 'sensitive' "
            f"(got '{sensitivity}')"
        )

    provenance_root = claim.get("provenance_root", "")
    if not provenance_root.startswith("prov:enrich:"):
        errors.append(
            f"provenance_root must start with 'prov:enrich:' (got '{provenance_root}')"
        )

    return errors


def check_valid_fixture(
    schema: dict[str, Any],
    path: Path,
    invariant_fn: Any,
) -> bool:
    instance = load_json(path)
    schema_errs = schema_errors(schema, instance)
    if schema_errs:
        print(f"  FAIL {path.name}: schema errors: {schema_errs}")
        return False
    inv_errs = invariant_fn(instance)
    if inv_errs:
        print(f"  FAIL {path.name}: invariant errors: {inv_errs}")
        return False
    print(f"  ok   {path.name}")
    return True


def check_invalid_fixture(
    schema: dict[str, Any],
    path: Path,
    invariant_fn: Any,
) -> bool:
    instance = load_json(path)
    # Strip meta-field before validation
    clean = {k: v for k, v in instance.items() if not k.startswith("_")}
    schema_errs = schema_errors(schema, clean)
    inv_errs = invariant_fn(clean)
    if not schema_errs and not inv_errs:
        print(f"  FAIL {path.name}: expected rejection but fixture passed all checks")
        return False
    reason = instance.get("_invalid_reason", "(no reason specified)")
    print(f"  ok   {path.name}: correctly rejected — {reason}")
    return True


def main() -> int:
    print("Loading schemas...")
    try:
        seed_schema = load_schema(SEED_SCHEMA_FILE)
        claim_schema = load_schema(CLAIM_SCHEMA_FILE)
    except Exception as exc:
        print(f"FAIL: schema load error: {exc}")
        return 1
    print(f"  ok   {SEED_SCHEMA_FILE.name}")
    print(f"  ok   {CLAIM_SCHEMA_FILE.name}")

    passed = True

    print("\nValid seed fixtures:")
    for p in VALID_SEED_FILES:
        passed &= check_valid_fixture(seed_schema, p, validate_seed_invariants)

    print("\nValid claim fixtures:")
    for p in VALID_CLAIM_FILES:
        passed &= check_valid_fixture(claim_schema, p, validate_claim_invariants)

    print("\nInvalid seed fixtures (must be rejected):")
    for p in INVALID_SEED_FILES:
        passed &= check_invalid_fixture(seed_schema, p, validate_seed_invariants)

    print("\nInvalid claim fixtures (must be rejected):")
    for p in INVALID_CLAIM_FILES:
        passed &= check_invalid_fixture(claim_schema, p, validate_claim_invariants)

    if passed:
        print("\nenrichment twin fixtures validated")
        return 0
    print("\nenrichment twin validation FAILED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
