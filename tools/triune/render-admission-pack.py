#!/usr/bin/env python3
"""Generate a Triune admission pack (admission-pack.v1) from candidate identity
and dry-run evidence.

Usage:
    python tools/triune/render-admission-pack.py \\
      --candidate synthetic-i4 \\
      --candidate-name synthetic-inception-i4 \\
      --event-ir-ref synthetic://triune/i4/event-ir \\
      --proof-ref synthetic://triune/i4/proofs/policy-dry-run \\
      --sbom-ref synthetic://triune/i4/sbom/spdx \\
      --signature-ref synthetic://triune/i4/signatures/herald-agent \\
      --image-ref synthetic://triune/i4/images/herald-agent \\
      --network-policy-ref synthetic://triune/policies/default-deny \\
      --dry-run-result pass \\
      --dry-run-output examples/triune/policy-dry-run.synthetic.json \\
      --output /tmp/i4.admission-pack.json

Rules enforced (fail-closed):
  - dry_run_output_hash is computed from --dry-run-output; a `pass` claim is
    hash-bound (epsilon_gate.dry_run_output_hash + dry_run_evidence_ref).
  - --dry-run-result=pass requires --dry-run-output and refuses to render if
    the dry-run output contains violations.
  - candidate/admission status 'approved' or 'admitted' requires at least one
    HOST approval (--approved-by/--approved-at with --approval-kind host),
    matching tools/triune/validate-admission-pack.py policy.
  - Output is validated against schemas/triune/admission-pack.v1.json before
    writing; a schema-invalid pack is never emitted.

The epsilon gate block is either loaded from --epsilon-gate (a JSON file that
must itself conform to the embedded epsilon-gate shape) or synthesized as a
synthetic_fixture gate whose measurements sit inside the alpha scale limits and
whose pass claim is hash-bound to the dry-run output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import jsonschema

SCHEMA_PATH = ROOT / "schemas" / "triune" / "admission-pack.v1.json"
APPROVED_STATES = {"approved", "admitted"}


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def compute_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_dry_run(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def synthesize_epsilon_gate(
    candidate_id: str,
    now: str,
    passed: bool,
    dry_run_hash: str,
    dry_run_ref: str,
    alpha: float,
) -> dict:
    """Build a synthetic_fixture epsilon gate consistent with the validator math.

    Measurements are placed inside the alpha scale limits (micro<=1a, meso<=2a,
    macro median<=3a / p95<=4a) so a synthesized `pass` gate is internally
    consistent. A failing gate carries decision fail/reject and makes no
    hash-bound pass claim.
    """
    gate: dict = {
        "schema_version": "1.0.0",
        "certificate_kind": "triune_epsilon_gate",
        "epsilon_gate_id": f"epsilon-gate-{candidate_id}-{now[:10]}",
        "created_at": now,
        "execution_status": "synthetic_fixture",
        "alpha": alpha,
        "scale_limits": {
            "micro_multiplier": 1.0,
            "meso_multiplier": 2.0,
            "macro_median_multiplier": 3.0,
            "macro_p95_multiplier": 4.0,
        },
        "measurements": [
            {"cluster_member_id": candidate_id, "scale": "micro",
             "epsilon": round(alpha * 0.44, 8), "epsilon_hat": round(alpha * 0.48, 8),
             "epsilon_eff": round(alpha * 0.48, 8), "measured_at": now},
            {"cluster_member_id": candidate_id, "scale": "meso",
             "epsilon": round(alpha * 0.82, 8), "epsilon_hat": round(alpha * 0.93, 8),
             "epsilon_eff": round(alpha * 0.93, 8), "measured_at": now},
            {"cluster_member_id": candidate_id, "scale": "macro",
             "epsilon": round(alpha * 1.64, 8), "epsilon_hat": round(alpha * 1.78, 8),
             "epsilon_eff": round(alpha * 1.78, 8), "measured_at": now},
        ],
        "boundary_axes": {
            "budget_share": {"value": 0.1, "threshold": 0.25},
        },
        "decision": {
            "gate_result": "pass" if passed else "fail",
            "action": "allow" if passed else "reject",
            "rationale": (
                "Synthetic fixture gate: measurements inside alpha scale limits; "
                "pass claim hash-bound to dry-run output."
                if passed else
                "Synthetic fixture gate: dry-run did not pass; admission refused."
            ),
        },
        "epsilon_gate_passed": passed,
        "non_claims": [
            "execution_status=synthetic_fixture: this gate is a synthetic example only.",
            "Measurements are synthesized; no live epsilon telemetry was collected.",
        ],
        "ledger_entry": {
            "event_id": f"epsilon-gate-render-{candidate_id}-{now}",
            "event_type": "epsilon_gate_rendered",
            "created_at": now,
        },
    }
    if passed:
        # Hash-bind the pass claim (schema + validator both require this).
        gate["dry_run_output_hash"] = dry_run_hash
        gate["dry_run_evidence_ref"] = dry_run_ref
    return gate


def build_pack(args: argparse.Namespace) -> dict:
    now = _now()
    candidate_status = args.candidate_status
    dry_run_result = args.dry_run_result

    dry_run_path = Path(args.dry_run_output) if args.dry_run_output else None
    dry_run_hash = ""
    dry_run_ref = args.dry_run_evidence_ref or ""
    dry_run_id = args.dry_run_id or ""
    checked_policies: list[str] = []
    violations: list[str] = []

    if dry_run_path:
        if not dry_run_path.exists():
            raise FileNotFoundError(f"dry-run output not found: {dry_run_path}")
        dry_run_hash = compute_hash(dry_run_path)
        dr = load_dry_run(dry_run_path)
        checked_policies = dr.get("checked_policies", [])
        violations = dr.get("violations", [])
        if not dry_run_id:
            dry_run_id = dr.get("dry_run_id", "")
        if not dry_run_ref:
            dry_run_ref = f"local://{dry_run_path.resolve()}"

    if not dry_run_id:
        dry_run_id = f"dry-run-{args.candidate}-{now[:10]}"

    if dry_run_result == "pass":
        if not dry_run_hash:
            raise ValueError("--dry-run-result=pass requires --dry-run-output (for hash computation)")
        if not dry_run_ref:
            raise ValueError("--dry-run-result=pass requires --dry-run-evidence-ref or --dry-run-output")
        if violations:
            raise ValueError(
                f"--dry-run-result=pass refused: dry-run output records {len(violations)} violation(s)"
            )
    if not checked_policies:
        raise ValueError("dry-run output must record at least one checked policy (checked_policies)")

    approvals: list[dict] = []
    if args.approved_by or args.approved_at:
        if not (args.approved_by and args.approved_at):
            raise ValueError("an approval requires both --approved-by and --approved-at")
        approvals.append({
            "approved_by": args.approved_by,
            "approved_at": args.approved_at,
            "approval_kind": args.approval_kind,
        })
    if candidate_status in APPROVED_STATES:
        if not any(a["approval_kind"] == "host" for a in approvals):
            raise ValueError(
                f"candidate_status={candidate_status!r} requires a HOST approval "
                "(--approved-by, --approved-at, --approval-kind host)"
            )

    gate_passed = dry_run_result == "pass" and not violations
    if args.epsilon_gate:
        gate = json.loads(Path(args.epsilon_gate).read_text(encoding="utf-8"))
    else:
        gate = synthesize_epsilon_gate(
            args.candidate, now, gate_passed, dry_run_hash, dry_run_ref, args.alpha
        )

    pack: dict = {
        "schema_version": "1.0.0",
        "certificate_kind": "triune_admission_pack",
        "admission_pack_id": args.pack_id or f"admission-pack-{args.candidate}-{now[:10]}",
        "created_at": now,
        "execution_status": "runtime_partial" if args.live else "synthetic_fixture",
        "candidate": {
            "cluster_member_id": args.candidate,
            "cluster_name": args.candidate_name,
            "member_role": args.member_role,
            "trust_domain": args.trust_domain,
            "status": candidate_status,
        },
        "proof_pack": {
            "event_ir_snapshot_ref": args.event_ir_ref or f"synthetic://{args.candidate}/event-ir",
            "proof_artifact_refs": args.proof_ref or [f"synthetic://{args.candidate}/proofs/policy-dry-run"],
            "sbom_ref": args.sbom_ref or f"synthetic://{args.candidate}/sbom/spdx",
            "signature_refs": args.signature_ref or [f"synthetic://{args.candidate}/signatures/agent"],
            "image_refs": args.image_ref or [f"synthetic://{args.candidate}/images/agent"],
            "network_policy_ref": args.network_policy_ref or "synthetic://triune/policies/default-deny",
        },
        "policy_dry_run": {
            "dry_run_id": dry_run_id,
            "result": dry_run_result,
            "checked_policies": checked_policies,
            "violations": violations,
        },
        "epsilon_gate": gate,
        "admission_decision": {
            "status": candidate_status if candidate_status in
            {"proposed", "approved", "admitted", "rejected", "quarantined", "revoked"} else "proposed",
            "requested_role": args.requested_role,
            "authority_chain_ref": args.authority_chain_ref
            or f"synthetic://triune/authority-chain/{args.candidate}",
            "approvals": approvals,
        },
        "reversal_plan": {
            "rollback_action": args.rollback_action,
            "quarantine_action": args.quarantine_action,
            "maximum_time_to_revoke_seconds": args.max_revoke_seconds,
        },
        "non_claims": [
            "This admission pack was generated by render-admission-pack.py.",
            "Structural validation only — cosign, SBOM, FROST, and live cluster state are not verified.",
            "No production authorization. No customer-system attachment.",
        ],
        "ledger_entry": {
            "event_id": f"admission-pack-render-{args.candidate}-{now}",
            "event_type": "admission_pack_rendered",
            "created_at": now,
        },
    }

    if not args.live:
        pack["non_claims"].append(
            "execution_status=synthetic_fixture: this pack is a synthetic example only."
        )
    return pack


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a Triune admission pack (admission-pack.v1).")
    parser.add_argument("--candidate", required=True, help="cluster_member_id of the candidate.")
    parser.add_argument("--candidate-name", required=True, help="cluster_name of the candidate.")
    parser.add_argument("--candidate-status", default="proposed",
                        choices=["observed", "candidate", "dry_run", "proposed",
                                 "approved", "admitted", "quarantined", "revoked", "rejected"])
    parser.add_argument("--member-role", default="faithful_candidate",
                        choices=["inception", "faithful_candidate", "faithful_member"])
    parser.add_argument("--trust-domain", default="lab_airgapped",
                        choices=["lab_airgapped", "dev", "staging", "production", "unknown"])
    parser.add_argument("--requested-role", default="faithful_member",
                        choices=["triune_core", "faithful_member", "observer"])
    parser.add_argument("--event-ir-ref", default="")
    parser.add_argument("--proof-ref", action="append", default=None,
                        help="Proof artifact ref (repeatable).")
    parser.add_argument("--sbom-ref", default="")
    parser.add_argument("--signature-ref", action="append", default=None,
                        help="Signature ref (repeatable).")
    parser.add_argument("--image-ref", action="append", default=None,
                        help="Image ref (repeatable).")
    parser.add_argument("--network-policy-ref", default="")
    parser.add_argument("--authority-chain-ref", default="")
    parser.add_argument("--dry-run-result", required=True, choices=["pass", "warn", "fail"])
    parser.add_argument("--dry-run-output", default="",
                        help="Path to dry-run output file (JSON). Hash is computed from this file.")
    parser.add_argument("--dry-run-evidence-ref", default="",
                        help="Explicit evidence ref (defaults to local path of --dry-run-output).")
    parser.add_argument("--dry-run-id", default="")
    parser.add_argument("--epsilon-gate", default="",
                        help="Path to an externally rendered epsilon-gate JSON (default: synthesize).")
    parser.add_argument("--alpha", type=float, default=0.0073,
                        help="Alpha for the synthesized epsilon gate.")
    parser.add_argument("--approval-kind", default="host",
                        choices=["host", "delegated_operator", "automation"])
    parser.add_argument("--approved-by", default="")
    parser.add_argument("--approved-at", default="")
    parser.add_argument("--rollback-action",
                        default="Remove ClusterMesh peer or KubeFed member; revoke service credentials; restore deny-all egress.")
    parser.add_argument("--quarantine-action",
                        default="Quarantine or stop workloads; record revocation ledger entry; preserve evidence for replay.")
    parser.add_argument("--max-revoke-seconds", type=int, default=300)
    parser.add_argument("--pack-id", default="")
    parser.add_argument("--operator", default="operator")
    parser.add_argument("--live", action="store_true",
                        help="Mark as runtime_partial (default: synthetic_fixture).")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    try:
        pack = build_pack(args)
    except (ValueError, FileNotFoundError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    schema = load_schema()
    try:
        jsonschema.validate(pack, schema)
    except jsonschema.ValidationError as exc:
        print(f"ERROR: rendered pack fails schema validation: {exc.message}", file=sys.stderr)
        sys.exit(1)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(pack, indent=2), encoding="utf-8")
    print(f"OK: {out}")
    print(f"  candidate.status:   {pack['candidate']['status']}")
    print(f"  policy_dry_run:     {pack['policy_dry_run']['result']}")
    print(f"  epsilon_gate:       {pack['epsilon_gate']['decision']['gate_result']}")
    print(f"  admission_decision: {pack['admission_decision']['status']}")


if __name__ == "__main__":
    main()
