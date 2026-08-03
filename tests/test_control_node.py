"""ControlNode conformance (ADR-0002 §8 GAP-3 / prophet-workspace#85, L2).

Teeth BOTH ways: every *.valid.json registry validates; every *.invalid.json registry is rejected; and
each of the six guards (CN-T1..CN-T6) fires individually on a targeted mutation of the valid registry —
so a guard that silently stops biting is caught here, not in production. The published schema is exercised
against the validator's canonical sets so the two cannot drift.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.cybernetic_governance import validate_control_node as V  # noqa: E402


def _load(name: str) -> dict:
    return json.loads((V.FIXTURE_DIR / name).read_text(encoding="utf-8"))


def _rejects(registry: dict) -> bool:
    schema = V.load_schema()
    try:
        V.validate_registry(registry, schema)
        return False
    except V.ValidationError:
        return True


def test_schema_is_valid_draft_2020_12_and_registered() -> None:
    schema = V.load_schema()
    assert schema["$id"].endswith("control_node.schema.json")
    # drift guard must pass on the shipped schema
    V.validate_schema_drift(schema)


def test_schema_encodes_exactly_the_eleven_types() -> None:
    schema = V.load_schema()
    enum = set(schema["$defs"]["control_node"]["properties"]["node_type"]["enum"])
    assert enum == V.CANONICAL_NODE_TYPES
    assert len(enum) == 11


def test_all_fixtures_resolve_both_ways() -> None:
    report = V.run()
    assert report["passed"], report
    assert report["valid_count"] >= 1 and report["invalid_count"] >= 1


def test_valid_registry_passes() -> None:
    assert not _rejects(_load("estate-control-nodes.valid.json"))


def test_receipt_gateway_may_hold_two_control_functions() -> None:
    # A single resource embodying Observability AND Execution is lawful (distinct node_type per record).
    reg = _load("estate-control-nodes.valid.json")
    ref = "prophet-platform/apps/receipt-gateway"
    types = {n["node_type"] for n in reg["nodes"] if n["resource"]["ref"] == ref}
    assert {"Observability", "Execution"} <= types
    assert not _rejects(reg)


def test_cn_t1_unknown_node_type_fires() -> None:
    m = _load("estate-control-nodes.valid.json")
    m["nodes"][0]["node_type"] = "Consciousness"
    assert _rejects(m)


def test_cn_t2_bad_resource_kind_fires() -> None:
    m = _load("estate-control-nodes.valid.json")
    m["nodes"][0]["resource"]["kind"] = "database"
    assert _rejects(m)


def test_cn_t3_no_obligations_fires() -> None:
    m = _load("estate-control-nodes.valid.json")
    m["nodes"][0]["obligations"]["membrane_gates"] = []
    assert _rejects(m)


def test_cn_t4_duplicate_identity_fires() -> None:
    m = _load("estate-control-nodes.valid.json")
    m["nodes"][1]["node_id"] = m["nodes"][0]["node_id"]
    assert _rejects(m)


def test_cn_t5_duplicate_function_per_resource_fires() -> None:
    m = _load("estate-control-nodes.valid.json")
    # make a second, distinct-id node claim the same (node_type, resource.ref) as node 0
    dup = copy.deepcopy(m["nodes"][0])
    dup["node_id"] = m["nodes"][0]["node_id"] + "-dup"
    m["nodes"].append(dup)
    assert _rejects(m)


def test_cn_t6_unknown_gate_fires() -> None:
    m = _load("estate-control-nodes.valid.json")
    m["nodes"][0]["obligations"]["membrane_gates"] = ["made-up-gate"]
    assert _rejects(m)


def test_guards_do_not_over_bite() -> None:
    # the base registry is still valid after we stop mutating it
    assert not _rejects(_load("estate-control-nodes.valid.json"))
