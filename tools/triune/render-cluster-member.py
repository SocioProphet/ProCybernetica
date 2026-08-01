#!/usr/bin/env python3
"""Generate a cluster-member.v1.json record from a synthetic lab inventory.

Usage:
    python tools/triune/render-cluster-member.py \\
      --input examples/triune/lab/triune-lab.synthetic.yaml \\
      --member inception-i1 \\
      --output /tmp/inception-i1.cluster-member.json

Inventory kinds map onto the canonical member_role vocabulary:
    operator_workstation -> genesys
    bastion              -> twin_bastion
    inception cluster    -> inception

The output defaults to execution_status=synthetic_fixture unless --live is
supplied (--live records runtime_partial: an inventory walk, not full runtime
evidence). Kubeconfig contents are never embedded — only path-template refs.
The record is validated against schemas/triune/cluster-member.v1.json before
writing; a schema-invalid record is never emitted.
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

# inventory kind -> canonical member_role
ROLE_MAP = {
    "operator_workstation": "genesys",
    "bastion": "twin_bastion",
    "inception_control_plane": "inception",
}

TRUST_DOMAINS = {"lab_airgapped", "dev", "staging", "production", "unknown"}

FEDERATION_MODES = {"none", "cilium_clustermesh", "kubefed", "herald_multi_kubeconfig", "other"}


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def load_inventory(path: Path) -> dict:
    # Fail closed: an empty file parses as None and a list/scalar root parses as a
    # non-mapping; resolve_member() would then crash on inventory.get(...). Malformed
    # YAML raises yaml.YAMLError. Convert both into a clear error, never a traceback.
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ValueError(f"inventory {str(path)!r} is not valid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(
            f"inventory {str(path)!r} must be a YAML mapping at its root; got "
            f"{type(data).__name__} (an empty file parses as null). Refusing to render."
        )
    return data


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


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _trust_domain(entry: dict) -> str:
    td = entry.get("trust_domain", "lab_airgapped")
    return td if td in TRUST_DOMAINS else "lab_airgapped"


def _control_plane(kind: str) -> dict:
    if kind == "inception_control_plane":
        return {
            "kubernetes_distribution": "k3s",
            "version": "pending-evidence",
            "node_count": 1,
            "shared_fate_boundary": "per_vm_control_plane",
        }
    if kind == "bastion":
        return {
            "kubernetes_distribution": "other",
            "version": "n/a",
            "node_count": 1,
            "shared_fate_boundary": "bastion_host",
        }
    # operator workstation (genesys): no control plane of its own
    return {
        "kubernetes_distribution": "other",
        "version": "n/a",
        "node_count": 1,
        "shared_fate_boundary": "unknown",
    }


def _federation_mode(inventory: dict) -> str:
    mode = inventory.get("federation", {}).get("default_mode", "none")
    return mode if mode in FEDERATION_MODES else "other"


def _networking(inventory: dict) -> dict:
    # default_deny reflects VERIFIED live state — false until evidence is
    # recorded, regardless of the inventory's default_deny_required intent.
    return {
        "cni": "cilium",
        "default_deny": False,
        "hubble_enabled": False,
        "federation_mode": _federation_mode(inventory),
    }


def _policy_baseline() -> dict:
    # Baseline TARGETS; enforcement state requires live evidence (see non_claims).
    return {
        "admission_controller": "unknown",
        "privileged_pods_allowed": False,
        "host_pid_allowed": False,
        "signed_images_required": False,
        "resource_limits_required": True,
    }


def _safety_status() -> dict:
    # No epsilon gate has run for a freshly rendered record: gate_result is
    # honestly unknown and the numeric fields carry zero readings.
    return {
        "gate_result": "unknown",
        "epsilon_eff": 0.0,
        "boundary_axes": {"budget_share": 0.0},
        "lambda_b": 0.0,
    }


def _non_claims(execution_status: str, name: str) -> list[str]:
    claims = [
        f"This record was generated for {name}.",
        "This record does not prove a live k3s cluster is running.",
        "kubeconfig refs are path templates; kubeconfig contents are never embedded.",
        "networking.default_deny reflects verified state; false until evidence is recorded.",
        "policy_baseline records target posture; enforcement state requires live evidence.",
        "safety_status.gate_result=unknown: no epsilon gate has been run for this member.",
        "No production authorization. No customer-system attachment.",
    ]
    if execution_status == "synthetic_fixture":
        claims.append("execution_status=synthetic_fixture: this record is a synthetic example only.")
    return claims


def render(entry: dict, inventory: dict, live: bool, operator: str, status: str = "observed") -> dict:
    kind = entry["_kind"]
    name = entry.get("name", "unknown")
    member_id = entry.get("cluster_member_id", f"synthetic-{name}")
    execution_status = "runtime_partial" if live else "synthetic_fixture"
    now = _now()

    record: dict = {
        "schema_version": "1.0.0",
        "certificate_kind": "triune_cluster_member",
        "cluster_member_id": member_id,
        "created_at": now,
        "execution_status": execution_status,
        "cluster_name": inventory.get("lab_id", "synthetic-triune-lab"),
        "member_role": ROLE_MAP[kind],
        "trust_domain": _trust_domain(entry),
        "status": status,
        "control_plane": _control_plane(kind),
        "networking": _networking(inventory),
        "policy_baseline": _policy_baseline(),
        "safety_status": _safety_status(),
        "non_claims": _non_claims(execution_status, name),
        "ledger_entry": {
            "event_id": f"cluster-member-render-{member_id}-{now}",
            "event_type": "cluster_member_record_created",
            "created_at": now,
        },
    }

    if kind == "inception_control_plane":
        # Path-template refs only — never kubeconfig contents.
        record["endpoints"] = {
            "api_server_ref": f"local://endpoints/{member_id}/api-server",
            "kubeconfig_secret_ref": f"local://kubeconfigs/{member_id}",
        }

    return record


def validate_output(record: dict, schema: dict) -> None:
    jsonschema.validate(record, schema)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a cluster-member record (cluster-member.v1).")
    parser.add_argument("--input", required=True, help="Path to lab inventory YAML.")
    parser.add_argument("--member", required=True, help="Member name to render.")
    parser.add_argument("--output", required=True, help="Output JSON path.")
    parser.add_argument("--status", default="observed",
                        choices=["observed", "candidate", "dry_run", "proposed",
                                 "approved", "admitted", "quarantined", "revoked", "rejected"])
    parser.add_argument("--live", action="store_true",
                        help="Mark as runtime_partial (default: synthetic_fixture).")
    parser.add_argument("--operator", default="operator", help="Operator identity (reserved).")
    args = parser.parse_args()

    try:
        inventory = load_inventory(Path(args.input))
        entry = resolve_member(inventory, args.member)
    except (ValueError, FileNotFoundError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    record = render(entry, inventory, live=args.live, operator=args.operator, status=args.status)

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
    print(f"  member_role: {record['member_role']}")
    print(f"  status:      {record['status']} / {record['execution_status']}")


if __name__ == "__main__":
    main()
