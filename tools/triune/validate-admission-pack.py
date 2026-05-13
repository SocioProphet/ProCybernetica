#!/usr/bin/env python3
"""Validate a ProCybernetica Triune admission pack.

This validator is intentionally structural and invariant-focused. It does not
verify cosign signatures, SBOM integrity, FROST signatures, or cluster runtime
state. Those checks belong to runtime evidence adapters. This script checks
that the admission pack is shaped correctly and that the alpha/boundary gates
encoded in the pack are internally consistent.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing file: {path}") from None
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from None


def percentile(values: list[float], pct: float) -> float:
    if not values:
        raise ValueError("empty percentile input")
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    rank = (len(ordered) - 1) * pct
    lower = int(rank)
    upper = min(lower + 1, len(ordered) - 1)
    weight = rank - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_epsilon_gate(gate: dict[str, Any], errors: list[str]) -> None:
    alpha = gate.get("alpha")
    limits = gate.get("scale_limits", {})
    measurements = gate.get("measurements", [])

    require(isinstance(alpha, (int, float)) and alpha > 0, "epsilon_gate.alpha must be positive", errors)
    require(isinstance(measurements, list) and len(measurements) > 0, "epsilon_gate.measurements must be non-empty", errors)

    if not isinstance(alpha, (int, float)) or alpha <= 0 or not isinstance(measurements, list):
        return

    by_scale: dict[str, list[float]] = {"micro": [], "meso": [], "macro": []}
    for idx, measurement in enumerate(measurements):
        scale = measurement.get("scale") if isinstance(measurement, dict) else None
        eff = measurement.get("epsilon_eff") if isinstance(measurement, dict) else None
        require(scale in by_scale, f"measurement[{idx}].scale must be micro, meso, or macro", errors)
        require(isinstance(eff, (int, float)) and eff >= 0, f"measurement[{idx}].epsilon_eff must be non-negative", errors)
        if scale in by_scale and isinstance(eff, (int, float)):
            by_scale[scale].append(float(eff))

    micro_limit = float(alpha) * float(limits.get("micro_multiplier", 1.0))
    meso_limit = float(alpha) * float(limits.get("meso_multiplier", 2.0))
    macro_median_limit = float(alpha) * float(limits.get("macro_median_multiplier", 3.0))
    macro_p95_limit = float(alpha) * float(limits.get("macro_p95_multiplier", 4.0))

    if by_scale["micro"]:
        require(max(by_scale["micro"]) <= micro_limit, f"micro epsilon_eff exceeds {micro_limit:.8f}", errors)
    if by_scale["meso"]:
        require(max(by_scale["meso"]) <= meso_limit, f"meso epsilon_eff exceeds {meso_limit:.8f}", errors)
    if by_scale["macro"]:
        macro_median = statistics.median(by_scale["macro"])
        macro_p95 = percentile(by_scale["macro"], 0.95)
        require(macro_median <= macro_median_limit, f"macro median epsilon_eff exceeds {macro_median_limit:.8f}", errors)
        require(macro_p95 <= macro_p95_limit, f"macro p95 epsilon_eff exceeds {macro_p95_limit:.8f}", errors)

    axes = gate.get("boundary_axes", {})
    require(isinstance(axes, dict) and len(axes) > 0, "epsilon_gate.boundary_axes must be non-empty", errors)
    if isinstance(axes, dict):
        for name, axis in axes.items():
            value = axis.get("value") if isinstance(axis, dict) else None
            threshold = axis.get("threshold") if isinstance(axis, dict) else None
            require(isinstance(value, (int, float)), f"boundary axis {name!r} must include numeric value", errors)
            require(isinstance(threshold, (int, float)) and threshold > 0, f"boundary axis {name!r} must include positive threshold", errors)
            if isinstance(value, (int, float)) and isinstance(threshold, (int, float)) and threshold > 0:
                require(abs(float(value)) < float(threshold), f"boundary axis {name!r} exceeds threshold", errors)


def validate_admission_pack(pack: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    require(pack.get("schema_version") == "1.0.0", "schema_version must be 1.0.0", errors)
    require(pack.get("certificate_kind") == "triune_admission_pack", "certificate_kind must be triune_admission_pack", errors)

    candidate = pack.get("candidate", {})
    require(candidate.get("cluster_member_id") if isinstance(candidate, dict) else False, "candidate.cluster_member_id is required", errors)
    require(candidate.get("status") in {"observed", "candidate", "dry_run", "proposed", "approved", "admitted", "quarantined", "revoked", "rejected"} if isinstance(candidate, dict) else False, "candidate.status is invalid", errors)

    proof_pack = pack.get("proof_pack", {})
    if not isinstance(proof_pack, dict):
        errors.append("proof_pack must be an object")
        proof_pack = {}
    require(bool(proof_pack.get("event_ir_snapshot_ref")), "proof_pack.event_ir_snapshot_ref is required", errors)
    require(bool(proof_pack.get("sbom_ref")), "proof_pack.sbom_ref is required", errors)
    require(len(proof_pack.get("proof_artifact_refs", [])) > 0, "proof_pack.proof_artifact_refs must be non-empty", errors)
    require(len(proof_pack.get("signature_refs", [])) > 0, "proof_pack.signature_refs must be non-empty", errors)
    require(len(proof_pack.get("image_refs", [])) > 0, "proof_pack.image_refs must be non-empty", errors)

    dry_run = pack.get("policy_dry_run", {})
    if not isinstance(dry_run, dict):
        errors.append("policy_dry_run must be an object")
        dry_run = {}
    require(dry_run.get("result") == "pass", "policy_dry_run.result must be pass for admission proposal", errors)
    require(len(dry_run.get("checked_policies", [])) > 0, "policy_dry_run.checked_policies must be non-empty", errors)
    require(len(dry_run.get("violations", [])) == 0, "policy_dry_run.violations must be empty for admission proposal", errors)

    gate = pack.get("epsilon_gate", {})
    require(isinstance(gate, dict), "epsilon_gate must be an object", errors)
    if isinstance(gate, dict):
        validate_epsilon_gate(gate, errors)
        decision = gate.get("decision", {})
        require(isinstance(decision, dict), "epsilon_gate.decision must be an object", errors)
        if isinstance(decision, dict):
            require(decision.get("gate_result") == "pass", "epsilon_gate.decision.gate_result must be pass for admission proposal", errors)
            require(decision.get("action") in {"allow", "align"}, "epsilon_gate.decision.action must be allow or align for admission proposal", errors)

    decision = pack.get("admission_decision", {})
    if not isinstance(decision, dict):
        errors.append("admission_decision must be an object")
        decision = {}
    status = decision.get("status")
    require(status in {"proposed", "approved", "admitted", "rejected", "quarantined", "revoked"}, "admission_decision.status is invalid", errors)
    approvals = decision.get("approvals", [])
    if status in {"approved", "admitted"}:
        require(len(approvals) > 0, "approved/admitted decisions require at least one approval", errors)
        require(
            any(approval.get("approval_kind") == "host" for approval in approvals if isinstance(approval, dict)),
            "approved/admitted decisions require host approval under current policy",
            errors,
        )

    reversal = pack.get("reversal_plan", {})
    if not isinstance(reversal, dict):
        errors.append("reversal_plan must be an object")
        reversal = {}
    require(bool(reversal.get("rollback_action")), "reversal_plan.rollback_action is required", errors)
    require(bool(reversal.get("quarantine_action")), "reversal_plan.quarantine_action is required", errors)
    require(isinstance(reversal.get("maximum_time_to_revoke_seconds"), int), "reversal_plan.maximum_time_to_revoke_seconds must be an integer", errors)

    require(len(pack.get("non_claims", [])) > 0, "non_claims must be non-empty", errors)
    require(isinstance(pack.get("ledger_entry"), dict), "ledger_entry is required", errors)

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("admission_pack", type=Path, help="Path to a triune admission-pack JSON file")
    args = parser.parse_args(argv)

    pack = load_json(args.admission_pack)
    errors = validate_admission_pack(pack)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"PASS: {args.admission_pack}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
