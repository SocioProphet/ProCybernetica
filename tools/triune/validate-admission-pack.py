#!/usr/bin/env python3
"""Validate an admission pack against the ProCybernetica Triune schema and policy rules.

Usage:
    python tools/triune/validate-admission-pack.py <path-to-admission-pack.json>

Exit codes:
    0  PASS
    1  FAIL (structural or policy violation)
    2  usage error
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import jsonschema

SCHEMA_PATH = ROOT / "schemas" / "triune" / "admission-pack.v1.json"

APPROVED_STATES = {"approved", "admitted"}


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def load_pack(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def structural_validate(pack: dict, schema: dict) -> list[str]:
    errors = []
    try:
        jsonschema.validate(pack, schema)
    except jsonschema.ValidationError as exc:
        errors.append(f"schema: {exc.message}")
    return errors


def policy_validate(pack: dict) -> list[str]:
    """Enforce ProCybernetica faithful-admission policy rules."""
    errors = []

    policy = pack.get("policy", {})
    decision = pack.get("decision", {})
    candidate_status = pack.get("candidate_status", "")

    dry_run_result = policy.get("dry_run_result")
    dry_run_hash = policy.get("dry_run_output_hash", "").strip()
    dry_run_ref = policy.get("dry_run_evidence_ref", "").strip()
    gate_result = decision.get("gate_result")
    host_approval = decision.get("host_approval")

    violations = policy.get("violations", [])
    reversal_plan = pack.get("reversal_plan", {})
    reversal_steps = reversal_plan.get("steps", [])
    revocation_ref = reversal_plan.get("revocation_evidence_ref", "").strip()

    if dry_run_result == "pass":
        if not dry_run_hash:
            errors.append("policy: dry_run_result=pass requires dry_run_output_hash")
        if not dry_run_ref:
            errors.append("policy: dry_run_result=pass requires dry_run_evidence_ref")

    if gate_result == "pass":
        if not dry_run_hash:
            errors.append("decision: gate_result=pass requires dry_run_output_hash")
        if not dry_run_ref:
            errors.append("decision: gate_result=pass requires dry_run_evidence_ref")

    if violations:
        errors.append(f"policy: {len(violations)} violation(s) present: {violations}")

    if candidate_status in APPROVED_STATES:
        if not host_approval:
            errors.append(
                f"admission: candidate_status={candidate_status!r} requires decision.host_approval"
            )

    if not reversal_steps:
        errors.append("reversal_plan: steps must not be empty")
    if not revocation_ref:
        errors.append("reversal_plan: revocation_evidence_ref must not be empty")

    non_claims = pack.get("non_claims", [])
    if not non_claims:
        errors.append("non_claims: at least one non-claim is required")

    return errors


def validate(path: Path) -> tuple[bool, list[str]]:
    schema = load_schema()
    pack = load_pack(path)
    errors = structural_validate(pack, schema)
    errors += policy_validate(pack)
    return len(errors) == 0, errors


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: validate-admission-pack.py <path>", file=sys.stderr)
        sys.exit(2)
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        sys.exit(2)
    ok, errors = validate(path)
    if ok:
        print(f"PASS: {path}")
        sys.exit(0)
    else:
        print(f"FAIL: {path}")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
