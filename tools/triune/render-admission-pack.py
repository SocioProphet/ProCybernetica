#!/usr/bin/env python3
"""Generate a Triune admission pack from candidate identity and dry-run evidence.

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
      --dry-run-output /tmp/policy-dry-run.synthetic.json \\
      --output /tmp/i4.admission-pack.json

Rules enforced:
  - dry_run_output_hash is computed from --dry-run-output file.
  - dry_run_evidence_ref is required when --dry-run-result=pass.
  - Default candidate_status is 'proposed'.
  - 'approved' or 'admitted' requires --host-approval-kind, --approved-by, --approved-at.
  - Policy violations in the dry-run output cause failure.
  - Output is validated against schemas/triune/admission-pack.v1.json before writing.
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


def build_pack(args: argparse.Namespace) -> dict:
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    candidate_status = args.candidate_status
    dry_run_result = args.dry_run_result

    dry_run_path = Path(args.dry_run_output) if args.dry_run_output else None
    dry_run_hash = ""
    dry_run_ref = args.dry_run_evidence_ref or ""
    checked_policies: list[str] = []
    violations: list[str] = []

    if dry_run_path:
        if not dry_run_path.exists():
            raise FileNotFoundError(f"dry-run output not found: {dry_run_path}")
        dry_run_hash = compute_hash(dry_run_path)
        dr = load_dry_run(dry_run_path)
        checked_policies = dr.get("checked_policies", [])
        violations = dr.get("violations", [])
        if not dry_run_ref:
            dry_run_ref = f"local://{dry_run_path.resolve()}"

    if dry_run_result == "pass":
        if not dry_run_hash:
            raise ValueError("--dry-run-result=pass requires --dry-run-output (for hash computation)")
        if not dry_run_ref:
            raise ValueError("--dry-run-result=pass requires --dry-run-evidence-ref or --dry-run-output")

    if candidate_status in APPROVED_STATES:
        if not (args.host_approval_kind and args.approved_by and args.approved_at):
            raise ValueError(
                f"candidate_status={candidate_status!r} requires "
                "--host-approval-kind, --approved-by, and --approved-at"
            )

    policy: dict = {
        "dry_run_result": dry_run_result,
        "checked_policies": checked_policies,
        "violations": violations,
    }
    if dry_run_hash:
        policy["dry_run_output_hash"] = dry_run_hash
    if dry_run_ref:
        policy["dry_run_evidence_ref"] = dry_run_ref

    decision: dict = {
        "gate_result": "pass" if dry_run_result == "pass" and not violations else "fail"
        if violations else "pending",
    }
    if candidate_status in APPROVED_STATES:
        decision["host_approval"] = {
            "approval_kind": args.host_approval_kind,
            "approved_by": args.approved_by,
            "approved_at": args.approved_at,
        }

    pack = {
        "schema_version": "1.0.0",
        "pack_id": args.pack_id or f"pack-{args.candidate}-{now[:10]}",
        "candidate_id": args.candidate,
        "candidate_name": args.candidate_name,
        "candidate_status": candidate_status,
        "execution_status": "live" if args.live else "synthetic_fixture",
        "proof_refs": {
            "event_ir_ref": args.event_ir_ref or f"synthetic://{args.candidate}/event-ir",
        },
        "policy": policy,
        "decision": decision,
        "reversal_plan": {
            "steps": [
                "Remove ClusterMesh peer or KubeFed member.",
                "Revoke service credentials.",
                "Restore deny-all egress.",
                "Quarantine or stop workloads.",
                "Record revocation ledger entry.",
                "Preserve evidence for replay.",
            ],
            "revocation_evidence_ref": args.revocation_ref or f"local://evidence/{args.candidate}/revocation-plan.json",
            "tested": False,
            "notes": "Reversal plan created at render time. Must be tested before admission.",
        },
        "non_claims": [
            "This admission pack was generated by render-admission-pack.py.",
            "structural validation only — cosign, SBOM, FROST, and live cluster state are not verified.",
            "No production authorization. No customer-system attachment.",
        ],
        "ledger_entry": {
            "event": "admission_pack_rendered",
            "recorded_at": now,
            "recorded_by": args.operator or "operator",
            "evidence_refs": [dry_run_ref] if dry_run_ref else [],
            "notes": f"Rendered for candidate {args.candidate}.",
        },
    }

    if args.proof_ref:
        pack["proof_refs"]["policy_dry_run_ref"] = args.proof_ref
    if args.sbom_ref:
        pack["proof_refs"]["sbom_ref"] = args.sbom_ref
    if args.signature_ref:
        pack["proof_refs"]["signature_ref"] = args.signature_ref
    if args.image_ref:
        pack["proof_refs"]["image_ref"] = args.image_ref
    if args.network_policy_ref:
        pack["proof_refs"]["network_policy_ref"] = args.network_policy_ref

    if not args.live:
        pack["non_claims"].append("execution_status=synthetic_fixture: this pack is a synthetic example only.")

    return pack


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a Triune admission pack.")
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--candidate-name", required=True)
    parser.add_argument("--candidate-status", default="proposed",
                        choices=["observed", "candidate", "dry_run", "proposed",
                                 "approved", "admitted", "synthetic_fixture"])
    parser.add_argument("--event-ir-ref", default="")
    parser.add_argument("--proof-ref", default="")
    parser.add_argument("--sbom-ref", default="")
    parser.add_argument("--signature-ref", default="")
    parser.add_argument("--image-ref", default="")
    parser.add_argument("--network-policy-ref", default="")
    parser.add_argument("--dry-run-result", required=True,
                        choices=["pass", "fail", "pending", "non_claim"])
    parser.add_argument("--dry-run-output", default="",
                        help="Path to dry-run output file (JSON). Hash is computed from this file.")
    parser.add_argument("--dry-run-evidence-ref", default="",
                        help="Explicit evidence ref (defaults to local path of --dry-run-output).")
    parser.add_argument("--revocation-ref", default="")
    parser.add_argument("--host-approval-kind", default="")
    parser.add_argument("--approved-by", default="")
    parser.add_argument("--approved-at", default="")
    parser.add_argument("--pack-id", default="")
    parser.add_argument("--operator", default="operator")
    parser.add_argument("--live", action="store_true",
                        help="Mark as live execution (default: synthetic_fixture).")
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
    print(f"  candidate_status: {pack['candidate_status']}")
    print(f"  dry_run_result:   {pack['policy']['dry_run_result']}")
    print(f"  gate_result:      {pack['decision']['gate_result']}")


if __name__ == "__main__":
    main()
