#!/usr/bin/env python3
"""Validate ControlNode registries — closes ADR-0002 §8 GAP-3 / prophet-workspace#85 (L2).

ADR-0002's Layer 2 (Fractal Control Fabric / ProCybernetica) names 11 control-node types and says
"repos/agents/services/gateways/hosts are treated as lawful control nodes." Before this contract they
were prose. `schemas/control_node.schema.json` makes the 11 a CLOSED, typed enum and binds each lawful
control node to a concrete resource + its lawful-promotion obligations. This validator carries the teeth
that a pure schema cannot express (cross-record uniqueness) and drift-guards the schema against itself,
so the published contract and these Python teeth cannot silently diverge.

The teeth (enforced BOTH ways — valid registries pass, malformed ones are rejected):

- **CN-T1  node_type is one of the 11** — schema enum; the validator asserts the schema enum equals the
  canonical 11 (drift guard), so a 12th type or a dropped type is caught here, not in production.
- **CN-T2  resource is a real kind + ref** — resource.kind in {repo,agent,service,gateway,host} and a
  non-empty ref. A node governs a *concrete* resource, never nothing.
- **CN-T3  no ungated authority** — obligations.membrane_gates is non-empty. A control node governing a
  resource with NO declared obligation cannot exist; every lawful node crosses at least one gate.
- **CN-T4  identity is unique** — node_id is unique across the registry. A duplicate identity is rejected.
- **CN-T5  one control function per resource** — the pair (node_type, resource.ref) is unique. A resource
  MAY embody several control functions (a receipt-gateway is both Observability and Execution) as separate
  records, but the SAME function claimed twice for one resource is a duplicate and is rejected.
- **CN-T6  obligations name real gates** — every membrane gate is from the closed estate set (ADR-0002 L3).
  An obligation that names a gate that does not exist is rejected.

Consume-not-fork: this does not duplicate the rich NodeDescriptor (node_descriptor.schema.json); a
ControlNode may point at one via descriptor_ref, and node_class is kept in lockstep with that enum.

Run: `python3 tools/cybernetic_governance/validate_control_node.py`  (or `make control-node-ci`).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_FILE = ROOT / "schemas" / "control_node.schema.json"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "control-node"

# Canonical closed sets the validator KNOWS. The schema is asserted to match these (drift guard),
# so schema and code cannot diverge silently.
CANONICAL_NODE_TYPES = {
    "Identity",
    "Lifecycle",
    "Interfaces",
    "Memory",
    "WorldModel",
    "ValueJudgment",
    "BehaviorGeneration",
    "Execution",
    "Learning",
    "Coordination",
    "Observability",
}
CANONICAL_RESOURCE_KINDS = {"repo", "agent", "service", "gateway", "host"}
CANONICAL_MEMBRANE_GATES = {
    "capability-membrane",
    "pr-merge-gate",
    "purpose-admissibility",
    "region-residency",
    "policy-fabric-pre-dispatch",
    "autonomy-admission",
    "image-promotion-gate",
    "promotion-decision",
    "proof-artifact-publish",
    "inference-receipt",
}


class ValidationError(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in {path}: {exc}") from exc


def load_schema() -> dict[str, Any]:
    schema = load_json(SCHEMA_FILE)
    Draft202012Validator.check_schema(schema)
    return schema


def validate_schema_drift(schema: dict[str, Any]) -> None:
    """Assert the published schema still encodes exactly the teeth this validator enforces."""
    if schema.get("additionalProperties") is not False:
        raise ValidationError("schema root must be strict (additionalProperties:false)")
    props = schema.get("properties", {})
    if props.get("kind", {}).get("const") != "ControlNodeRegistry":
        raise ValidationError("schema kind const must be ControlNodeRegistry")
    node = schema.get("$defs", {}).get("control_node", {})
    if node.get("additionalProperties") is not False:
        raise ValidationError("schema control_node must be strict (additionalProperties:false)")
    if set(node.get("required", [])) != {"node_id", "node_type", "resource", "obligations"}:
        raise ValidationError("schema control_node.required drifted from validator")
    nprops = node.get("properties", {})
    # CN-T1: the 11 control-node types, closed and complete.
    if set(nprops.get("node_type", {}).get("enum", [])) != CANONICAL_NODE_TYPES:
        raise ValidationError("CN-T1: schema node_type enum drifted from the canonical 11 control-node types")
    # CN-T2: resource kinds closed.
    res = nprops.get("resource", {}).get("properties", {})
    if set(res.get("kind", {}).get("enum", [])) != CANONICAL_RESOURCE_KINDS:
        raise ValidationError("CN-T2: schema resource.kind enum drifted from validator")
    # CN-T3 + CN-T6: obligations required, non-empty, closed gate set.
    obl = nprops.get("obligations", {})
    if set(obl.get("required", [])) != {"membrane_gates"}:
        raise ValidationError("CN-T3: schema obligations must require membrane_gates")
    gates = obl.get("properties", {}).get("membrane_gates", {})
    if gates.get("minItems") != 1:
        raise ValidationError("CN-T3: schema membrane_gates must be non-empty (minItems:1)")
    if set(gates.get("items", {}).get("enum", [])) != CANONICAL_MEMBRANE_GATES:
        raise ValidationError("CN-T6: schema membrane_gates enum drifted from the canonical estate gate set")


def _teeth(registry: dict[str, Any]) -> None:
    """Cross-record teeth a JSON Schema cannot express: identity + control-function uniqueness."""
    seen_ids: set[str] = set()
    seen_pairs: set[tuple[str, str]] = set()
    for node in registry.get("nodes", []):
        node_id = node["node_id"]
        if node_id in seen_ids:
            raise ValidationError(f"CN-T4: duplicate control-node identity {node_id!r}")
        seen_ids.add(node_id)
        pair = (node["node_type"], node["resource"]["ref"])
        if pair in seen_pairs:
            raise ValidationError(
                f"CN-T5: control function {pair[0]!r} claimed twice for resource {pair[1]!r}"
            )
        seen_pairs.add(pair)


def validate_registry(registry: Any, schema: dict[str, Any]) -> None:
    """Schema-validate the registry, then apply the cross-record teeth. Raises ValidationError."""
    errors = sorted(Draft202012Validator(schema).iter_errors(registry), key=str)
    if errors:
        raise ValidationError("; ".join(e.message for e in errors))
    _teeth(registry)


def run(fixture_dir: Path = FIXTURE_DIR) -> dict[str, Any]:
    schema = load_schema()
    validate_schema_drift(schema)

    files = sorted(fixture_dir.glob("*.json"))
    valids = [f for f in files if f.name.endswith(".valid.json")]
    invalids = [f for f in files if f.name.endswith(".invalid.json")]
    if not valids or not invalids:
        raise ValidationError(
            f"{fixture_dir} must contain both *.valid.json and *.invalid.json registries"
        )

    results: list[dict[str, Any]] = []
    ok = True
    for path in valids:
        try:
            validate_registry(load_json(path), schema)
            results.append({"fixture": path.name, "expected": "pass", "passed": True})
        except ValidationError as exc:
            ok = False
            results.append({"fixture": path.name, "expected": "pass", "passed": False, "error": str(exc)})
    for path in invalids:
        try:
            validate_registry(load_json(path), schema)
            ok = False
            results.append({"fixture": path.name, "expected": "reject", "passed": False,
                            "error": "expected rejection but the registry validated"})
        except ValidationError as exc:
            results.append({"fixture": path.name, "expected": "reject", "passed": True, "rejected_by": str(exc)})

    return {
        "validator": "control_node.validator.v0_1",
        "schema_file": str(SCHEMA_FILE.relative_to(ROOT)),
        "fixture_dir": str(fixture_dir.relative_to(ROOT)),
        "passed": ok,
        "valid_count": len(valids),
        "invalid_count": len(invalids),
        "results": results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit the full JSON report")
    args = parser.parse_args(argv)
    try:
        report = run()
    except ValidationError as exc:
        print(f"ERR: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    if report["passed"]:
        print(f"OK: ControlNode validation passed "
              f"({report['valid_count']} valid, {report['invalid_count']} invalid rejected)")
        return 0
    for r in report["results"]:
        if not r["passed"]:
            print(f"FAIL: {r['fixture']} ({r['expected']}) :: {r.get('error')}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
