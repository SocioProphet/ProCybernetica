#!/usr/bin/env python3
"""Generate a cluster-member.v1.json record from a synthetic lab inventory.

Usage:
    python tools/triune/render-cluster-member.py \\
      --input examples/triune/lab/triune-lab.synthetic.yaml \\
      --member inception-i1 \\
      --output /tmp/inception-i1.cluster-member.json

The output defaults to execution_status=synthetic_fixture unless --live is supplied.
Kubeconfig contents are never embedded.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import yaml
import jsonschema

SCHEMA_PATH = ROOT / "schemas" / "triune" / "cluster-member.v1.json"

ROLE_MAP = {
    "genesys": "operator_workstation",
    "k3-a": "bastion",
    "k3-b": "bastion",
}


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def load_inventory(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def resolve_member(inventory: dict, member_name: str) -> dict:
    """Return the raw inventory entry for the named member, or raise."""
    ws = inventory.get("operator_workstation", {})
    if ws.get("name") == member_name:
        return {"_kind": "operator_workstation", **ws}

    for host in inventory.get("twin_bastion", {}).get("hosts", []):
        if host.get("name") == member_name:
            return {"_kind": "bastion", **host}

    for cluster in inventory.get("inception_clusters", []):
        if cluster.get("name") == member_name:
            return {"_kind": "inception_control_plane", **cluster}

    known = (
        [ws.get("name")]
        + [h.get("name") for h in inventory.get("twin_bastion", {}).get("hosts", [])]
        + [c.get("name") for c in inventory.get("inception_clusters", [])]
    )
    raise ValueError(f"member {member_name!r} not found in inventory; known: {known}")


def render(entry: dict, inventory: dict, live: bool, operator: str) -> dict:
    kind = entry["_kind"]
    name = entry.get("name", "unknown")
    member_id = entry.get("cluster_member_id", f"synthetic-{name}")
    trust_domain = entry.get("trust_domain", inventory.get("network", {}).get("isolation", "lab"))
    execution_status = "live" if live else "synthetic_fixture"
    status = "observed" if live else "synthetic_fixture"

    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    record: dict = {
        "schema_version": "1.0.0",
        "cluster_member_id": member_id,
        "cluster_name": inventory.get("lab_id", "synthetic-triune-lab"),
        "member_role": kind,
        "trust_domain": trust_domain,
        "status": status,
        "execution_status": execution_status,
        "hostname": name,
        "control_plane": _control_plane(kind, entry, live),
        "networking": _networking(inventory, live),
        "policy_baseline": _policy_baseline(),
        "governance_refs": _governance_refs(inventory),
        "safety_status": {
            "production_attachment_allowed": inventory.get("policy", {}).get(
                "production_attachment_allowed", False
            ),
            "customer_network_allowed": False,
            "public_ingress_allowed": False,
        },
        "non_claims": _non_claims(execution_status, name),
        "ledger_entry": {
            "event": "cluster_member_record_created",
            "recorded_at": now,
            "recorded_by": operator,
            "evidence_refs": [],
            "notes": f"Rendered by render-cluster-member.py for {name}.",
        },
    }
    return record


def _control_plane(kind: str, entry: dict, live: bool) -> dict:
    if kind == "operator_workstation":
        return {
            "engine": "none",
            "version_ref": "n/a",
            "kubeconfig_ref": "n/a",
        }
    if kind == "bastion":
        return {
            "engine": "none",
            "version_ref": "n/a",
            "kubeconfig_ref": "n/a",
            "notes": "Bastion host — no k3s control plane.",
        }
    return {
        "engine": "k3s",
        "version_ref": "pending-evidence" if not live else "local://evidence/k3s-version.txt",
        "installer_digest_ref": "pending-evidence" if not live else "local://evidence/installer.sha256",
        "kubeconfig_ref": "local://kubeconfigs/" + entry.get("cluster_member_id", "synthetic"),
        "notes": "Kubeconfig stored outside repository. Path template only.",
    }


def _networking(inventory: dict, live: bool) -> dict:
    net = inventory.get("network", {})
    fed = inventory.get("federation", {})
    return {
        "cni": "cilium",
        "default_deny_applied": False if not live else False,
        "isolation": net.get("isolation", "lab_airgapped"),
        "clustermesh_id_ref": "pending-evidence",
        "policy_refs": [
            "examples/triune/networkpolicy/default-deny.yaml"
        ],
        "notes": "default_deny_applied reflects live state; false until evidence recorded.",
    }


def _policy_baseline() -> dict:
    return {
        "deny_all_ingress": True,
        "deny_all_egress": True,
        "no_privileged_pods": True,
        "no_host_pid": True,
        "signed_images_required": False,
        "signed_images_status": "pending — not yet enforced; see non_claims",
        "resource_limits_required": True,
        "notes": "Baseline targets. Actual enforcement state requires live evidence.",
    }


def _governance_refs(inventory: dict) -> dict:
    return {
        "runbook_ref": "docs/runbooks/TRIUNE_EXECUTION_PACK.md",
        "ledger_ref": "local://ledger/",
        "reversal_plan_ref": "local://evidence/revocation-plan.json",
    }


def _non_claims(execution_status: str, name: str) -> list[str]:
    claims = [
        f"This record was generated for {name}.",
        "This record does not prove a live k3s cluster is running.",
        "kubeconfig_ref is a path template; it does not contain kubeconfig contents.",
        "default_deny_applied reflects intended posture; it is not verified by this tool.",
        "No production authorization. No customer-system attachment.",
    ]
    if execution_status == "synthetic_fixture":
        claims.append("execution_status=synthetic_fixture: this record is a synthetic example only.")
    return claims


def validate_output(record: dict, schema: dict) -> None:
    jsonschema.validate(record, schema)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a cluster-member record.")
    parser.add_argument("--input", required=True, help="Path to lab inventory YAML.")
    parser.add_argument("--member", required=True, help="Member name to render.")
    parser.add_argument("--output", required=True, help="Output JSON path.")
    parser.add_argument("--live", action="store_true", help="Mark as live (default: synthetic_fixture).")
    parser.add_argument("--operator", default="operator", help="Operator identity for ledger entry.")
    args = parser.parse_args()

    inventory = load_inventory(Path(args.input))
    try:
        entry = resolve_member(inventory, args.member)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    record = render(entry, inventory, live=args.live, operator=args.operator)

    schema = load_schema()
    try:
        validate_output(record, schema)
    except jsonschema.ValidationError as exc:
        print(f"ERROR: rendered record fails schema validation: {exc.message}", file=sys.stderr)
        sys.exit(1)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"OK: {out}")


if __name__ == "__main__":
    main()
