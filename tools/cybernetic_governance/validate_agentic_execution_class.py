#!/usr/bin/env python3
"""Validate Agentic Execution Class registries — integrates IBM open-stack v5 into the Agent Ontology.

prophet-workspace#108 (item 4) asks that the IBM open-stack v5 "agentic execution" model
(ibm_open_stack_inventory_v5_agentic_execution_remounted.xlsx) be integrated into the estate Agent
Ontology, consume-not-fork. `schemas/agentic_execution_class.schema.json` makes the seven v5 execution
classes (Execution_Class_Legend) a CLOSED enum and binds each to already-owned estate types instead of
restating them:

  - control_node_type  -> the Agent-Ontology / Fractal-Control-Fabric node the class acts as
                          (schemas/control_node.schema.json, ADR-0002 L2, ProCybernetica#124).
  - agent_class        -> the AgentPassport host-level typed agent authorized to run it
                          (sourceos-spec schemas/AgentPassport.json, T0-1; ontogenesis T1 / #140).
  - semantic_sublayer  -> one of the four v5 semantic sub-layers (Semantic_SubLayer_Map), OPTIONAL,
    + coordinate_axis     bound both-or-neither to an estate semantic coordinate
                          (contracts/AgentCoordinateVector.v0.1.json).

This validator carries the teeth a pure schema cannot express (cross-record uniqueness, both-or-neither
semantic binding) and drift-guards the schema against the estate contracts it consumes, so the published
contract and the estate ontology cannot silently diverge.

The teeth (enforced BOTH ways — well-formed bindings pass, malformed ones are rejected):

- **AEC-T1  execution_class is one of the seven v5 classes** — schema enum; the validator asserts the
  schema enum equals the canonical seven (drift guard), so a dropped or invented class is caught here.
- **AEC-T2  control_node_type is a declared ontology node** — schema enum equals the canonical 11
  ProCybernetica control-node types; AND, when schemas/control_node.schema.json is present (i.e. once
  ProCybernetica#124 lands on main), the two enums are asserted equal so this contract can never
  reference an ontology node the ControlNode contract does not declare. Binding onto an undeclared node
  is rejected.
- **AEC-T3  agent_class is a real AgentPassport class** — schema enum equals the canonical five-class
  AgentPassport model. An unknown agent_class (e.g. 'anySource', which the estate never admits) is
  rejected.
- **AEC-T4  semantic_sublayer is in the v5 map** — when present, it is one of the four Semantic_SubLayer_Map
  sub-layers. A sub-layer not in the map is rejected.
- **AEC-T5  coordinate_axis is a real semantic coordinate** — schema enum equals the eleven
  AgentCoordinateVector sefirotic axes; AND, since contracts/AgentCoordinateVector.v0.1.json is on main,
  the two are asserted equal (reconciliation with the estate semantic coordinate).
- **AEC-T6  binding identity is unique** — binding_id is unique across the registry.
- **AEC-T7  one execution class per (execution_class, agent_class, control_node_type) triple** — a resource
  MAY hold several execution classes, but the SAME triple claimed twice is a duplicate and is rejected.
- **AEC-T8  semantic binding is both-or-neither** — semantic_sublayer and coordinate_axis appear together
  or not at all (also enforced in-schema via dependentRequired; re-asserted here as a guard).

Run: `python3 tools/cybernetic_governance/validate_agentic_execution_class.py`
     (or `make agentic-execution-class-ci`).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_FILE = ROOT / "schemas" / "agentic_execution_class.schema.json"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "agentic-execution-class"

# Estate contracts this one consumes (consume-not-fork). Reconciled against, never restated.
CONTROL_NODE_SCHEMA = ROOT / "schemas" / "control_node.schema.json"
AGENT_COORDINATE_VECTOR = ROOT / "contracts" / "AgentCoordinateVector.v0.1.json"

# Canonical closed sets the validator KNOWS. The schema is asserted to match these (drift guard),
# so schema and code cannot diverge silently.

# AEC-T1: the seven v5 execution classes (Execution_Class_Legend).
CANONICAL_EXECUTION_CLASSES = {
    "grounding_safe_read",
    "tool_with_approval",
    "tool_autonomous_safe_write",
    "inter_agent_coordination",
    "policy_audit_oversight",
    "human_workflow_system",
    "acp_client_ide",
}
# AEC-T2: the 11 ProCybernetica control-node types (schemas/control_node.schema.json / #124).
CANONICAL_CONTROL_NODE_TYPES = {
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
# AEC-T3: the five AgentPassport agent classes (sourceos-spec schemas/AgentPassport.json).
CANONICAL_AGENT_CLASSES = {
    "system_core",
    "intelligence_automation",
    "app_helper",
    "legacy_bridge",
    "third_party",
}
# AEC-T4: the four v5 semantic sub-layers (Semantic_SubLayer_Map).
CANONICAL_SEMANTIC_SUBLAYERS = {
    "glossary_ontology",
    "metrics_semantics",
    "retrieval_semantics",
    "graph_krr",
}
# AEC-T5: the 11 AgentCoordinateVector sefirotic axes (contracts/AgentCoordinateVector.v0.1.json).
CANONICAL_COORDINATE_AXES = {
    "keter", "chochmah", "binah", "daat", "chesed", "gevurah",
    "tiferet", "netzach", "hod", "yesod", "malchut",
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


def _binding_props(schema: dict[str, Any]) -> dict[str, Any]:
    return schema.get("$defs", {}).get("execution_class_binding", {}).get("properties", {})


def validate_schema_drift(schema: dict[str, Any]) -> None:
    """Assert the published schema still encodes exactly the teeth this validator enforces, and that the
    consumed estate enums are reconciled (not forked)."""
    if schema.get("additionalProperties") is not False:
        raise ValidationError("schema root must be strict (additionalProperties:false)")
    props = schema.get("properties", {})
    if props.get("kind", {}).get("const") != "AgenticExecutionClassRegistry":
        raise ValidationError("schema kind const must be AgenticExecutionClassRegistry")
    binding = schema.get("$defs", {}).get("execution_class_binding", {})
    if binding.get("additionalProperties") is not False:
        raise ValidationError("schema execution_class_binding must be strict (additionalProperties:false)")
    if set(binding.get("required", [])) != {"binding_id", "execution_class", "agent_class", "control_node_type"}:
        raise ValidationError("schema execution_class_binding.required drifted from validator")
    bprops = _binding_props(schema)

    # AEC-T1
    if set(bprops.get("execution_class", {}).get("enum", [])) != CANONICAL_EXECUTION_CLASSES:
        raise ValidationError("AEC-T1: schema execution_class enum drifted from the canonical seven v5 classes")
    # AEC-T2
    if set(bprops.get("control_node_type", {}).get("enum", [])) != CANONICAL_CONTROL_NODE_TYPES:
        raise ValidationError("AEC-T2: schema control_node_type enum drifted from the canonical 11 control-node types")
    # AEC-T3
    if set(bprops.get("agent_class", {}).get("enum", [])) != CANONICAL_AGENT_CLASSES:
        raise ValidationError("AEC-T3: schema agent_class enum drifted from the canonical five AgentPassport classes")
    # AEC-T4
    if set(bprops.get("semantic_sublayer", {}).get("enum", [])) != CANONICAL_SEMANTIC_SUBLAYERS:
        raise ValidationError("AEC-T4: schema semantic_sublayer enum drifted from the four v5 semantic sub-layers")
    # AEC-T5
    if set(bprops.get("coordinate_axis", {}).get("enum", [])) != CANONICAL_COORDINATE_AXES:
        raise ValidationError("AEC-T5: schema coordinate_axis enum drifted from the eleven AgentCoordinateVector axes")
    # AEC-T8: both-or-neither declared in-schema.
    dep = binding.get("dependentRequired", {})
    if dep.get("semantic_sublayer") != ["coordinate_axis"] or dep.get("coordinate_axis") != ["semantic_sublayer"]:
        raise ValidationError("AEC-T8: schema must bind semantic_sublayer<->coordinate_axis both-or-neither")

    _reconcile_estate_contracts()


def _reconcile_estate_contracts() -> None:
    """Consume-not-fork: assert the enums we vendor equal the estate source-of-truth contracts.

    AEC-T5 (AgentCoordinateVector) is on main and is enforced unconditionally. AEC-T2 (ControlNode) is
    enforced whenever schemas/control_node.schema.json is present (i.e. once ProCybernetica#124 lands),
    so the reconciliation tightens automatically without this contract ever crashing before it does."""
    # AEC-T5: reconcile against the estate semantic coordinate.
    acv = load_json(AGENT_COORDINATE_VECTOR)
    axes = set(
        acv.get("properties", {}).get("coordinates", {}).get("required", [])
    )
    if axes != CANONICAL_COORDINATE_AXES:
        raise ValidationError(
            "AEC-T5: coordinate_axis set is not reconciled with contracts/AgentCoordinateVector.v0.1.json"
        )
    # AEC-T2: reconcile against the ControlNode contract when it is present.
    if CONTROL_NODE_SCHEMA.exists():
        cn = load_json(CONTROL_NODE_SCHEMA)
        node_types = set(
            cn.get("$defs", {}).get("control_node", {}).get("properties", {})
              .get("node_type", {}).get("enum", [])
        )
        if node_types != CANONICAL_CONTROL_NODE_TYPES:
            raise ValidationError(
                "AEC-T2: control_node_type set is not reconciled with schemas/control_node.schema.json "
                "(ProCybernetica#124) — the two ontology-node enums have drifted"
            )


def _teeth(registry: dict[str, Any]) -> None:
    """Cross-record teeth a JSON Schema cannot express: identity + execution-class-per-triple uniqueness,
    and the both-or-neither semantic binding (re-asserted beyond dependentRequired)."""
    seen_ids: set[str] = set()
    seen_triples: set[tuple[str, str, str]] = set()
    for b in registry.get("bindings", []):
        binding_id = b["binding_id"]
        if binding_id in seen_ids:
            raise ValidationError(f"AEC-T6: duplicate binding identity {binding_id!r}")
        seen_ids.add(binding_id)

        triple = (b["execution_class"], b["agent_class"], b["control_node_type"])
        if triple in seen_triples:
            raise ValidationError(
                f"AEC-T7: execution class {triple[0]!r} claimed twice for "
                f"(agent_class={triple[1]!r}, control_node_type={triple[2]!r})"
            )
        seen_triples.add(triple)

        has_sub = "semantic_sublayer" in b
        has_axis = "coordinate_axis" in b
        if has_sub != has_axis:
            raise ValidationError(
                f"AEC-T8: binding {binding_id!r} has a dangling semantic binding "
                "(semantic_sublayer and coordinate_axis are both-or-neither)"
            )


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
        "validator": "agentic_execution_class.validator.v0_1",
        "schema_file": str(SCHEMA_FILE.relative_to(ROOT)),
        "fixture_dir": str(fixture_dir.relative_to(ROOT)),
        "control_node_reconciled": CONTROL_NODE_SCHEMA.exists(),
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
        cn = "reconciled with ControlNode #124" if report["control_node_reconciled"] else \
             "ControlNode #124 not yet on main (AEC-T2 falls back to the vendored canonical set)"
        print(f"OK: Agentic Execution Class validation passed "
              f"({report['valid_count']} valid, {report['invalid_count']} invalid rejected; {cn})")
        return 0
    for r in report["results"]:
        if not r["passed"]:
            print(f"FAIL: {r['fixture']} ({r['expected']}) :: {r.get('error')}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
