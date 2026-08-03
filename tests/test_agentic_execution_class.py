"""Agentic Execution Class conformance — IBM open-stack v5 integrated into the Agent Ontology.

prophet-workspace#108 (item 4). Teeth BOTH ways: the estate registry validates; every *.invalid.json
registry is rejected; and each guard (AEC-T1..AEC-T8) fires individually on a targeted mutation of the
valid registry — so a guard that silently stops biting is caught here, not in production. The published
schema is exercised against the validator's canonical sets, and against the estate contracts it consumes
(AgentCoordinateVector always; ControlNode #124 when present), so the binding and the ontology cannot drift.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.cybernetic_governance import validate_agentic_execution_class as V  # noqa: E402


def _load(name: str) -> dict:
    return json.loads((V.FIXTURE_DIR / name).read_text(encoding="utf-8"))


def _rejects(registry: dict) -> bool:
    schema = V.load_schema()
    try:
        V.validate_registry(registry, schema)
        return False
    except V.ValidationError:
        return True


VALID = "estate-agentic-execution-classes.valid.json"


def test_schema_is_valid_draft_2020_12_and_registered() -> None:
    schema = V.load_schema()
    assert schema["$id"].endswith("agentic_execution_class.schema.json")
    V.validate_schema_drift(schema)  # drift + estate reconciliation must pass on the shipped schema


def test_schema_encodes_exactly_the_seven_v5_execution_classes() -> None:
    schema = V.load_schema()
    enum = set(schema["$defs"]["execution_class_binding"]["properties"]["execution_class"]["enum"])
    assert enum == V.CANONICAL_EXECUTION_CLASSES
    assert len(enum) == 7


def test_control_node_type_reconciled_with_estate_contract() -> None:
    # AEC-T2: when ProCybernetica#124 is present, its node_type enum must equal ours (no undeclared node).
    if not V.CONTROL_NODE_SCHEMA.exists():
        return
    cn = json.loads(V.CONTROL_NODE_SCHEMA.read_text(encoding="utf-8"))
    node_types = set(cn["$defs"]["control_node"]["properties"]["node_type"]["enum"])
    assert node_types == V.CANONICAL_CONTROL_NODE_TYPES


def test_coordinate_axis_reconciled_with_agent_coordinate_vector() -> None:
    # AEC-T5: the eleven axes must equal AgentCoordinateVector's coordinate set.
    acv = json.loads(V.AGENT_COORDINATE_VECTOR.read_text(encoding="utf-8"))
    axes = set(acv["properties"]["coordinates"]["required"])
    assert axes == V.CANONICAL_COORDINATE_AXES


def test_all_fixtures_resolve_both_ways() -> None:
    report = V.run()
    assert report["passed"], report
    assert report["valid_count"] >= 1 and report["invalid_count"] >= 1


def test_valid_registry_passes() -> None:
    assert not _rejects(_load(VALID))


def test_valid_registry_covers_all_seven_execution_classes_and_four_sublayers() -> None:
    reg = _load(VALID)
    classes = {b["execution_class"] for b in reg["bindings"]}
    assert classes == V.CANONICAL_EXECUTION_CLASSES
    sublayers = {b["semantic_sublayer"] for b in reg["bindings"] if "semantic_sublayer" in b}
    assert sublayers == V.CANONICAL_SEMANTIC_SUBLAYERS


def test_one_execution_class_may_run_on_several_nodes() -> None:
    # grounding_safe_read legitimately appears on Memory, Observability and WorldModel (distinct triples).
    reg = _load(VALID)
    nodes = {b["control_node_type"] for b in reg["bindings"] if b["execution_class"] == "grounding_safe_read"}
    assert {"Memory", "Observability", "WorldModel"} <= nodes
    assert not _rejects(reg)


def test_aec_t1_unknown_execution_class_fires() -> None:
    m = _load(VALID)
    m["bindings"][0]["execution_class"] = "autonomous_god_mode"
    assert _rejects(m)


def test_aec_t2_undeclared_ontology_node_fires() -> None:
    m = _load(VALID)
    m["bindings"][0]["control_node_type"] = "Consciousness"
    assert _rejects(m)


def test_aec_t3_unknown_agent_class_fires() -> None:
    m = _load(VALID)
    m["bindings"][0]["agent_class"] = "anySource"
    assert _rejects(m)


def test_aec_t4_unknown_semantic_sublayer_fires() -> None:
    m = _load(VALID)
    b = next(x for x in m["bindings"] if "semantic_sublayer" in x)
    b["semantic_sublayer"] = "vibes_layer"
    assert _rejects(m)


def test_aec_t5_unknown_coordinate_axis_fires() -> None:
    m = _load(VALID)
    b = next(x for x in m["bindings"] if "coordinate_axis" in x)
    b["coordinate_axis"] = "ein_sof"
    assert _rejects(m)


def test_aec_t6_duplicate_identity_fires() -> None:
    m = _load(VALID)
    m["bindings"][1]["binding_id"] = m["bindings"][0]["binding_id"]
    assert _rejects(m)


def test_aec_t7_duplicate_triple_fires() -> None:
    m = _load(VALID)
    dup = copy.deepcopy(m["bindings"][4])  # tool_with_approval / app_helper / Execution
    dup["binding_id"] = m["bindings"][4]["binding_id"] + "-dup"
    dup.pop("semantic_sublayer", None)
    dup.pop("coordinate_axis", None)
    m["bindings"].append(dup)
    assert _rejects(m)


def test_aec_t8_dangling_semantic_binding_fires() -> None:
    m = _load(VALID)
    b = next(x for x in m["bindings"] if "coordinate_axis" in x)
    del b["coordinate_axis"]  # sub-layer without its coordinate
    assert _rejects(m)


def test_guards_do_not_over_bite() -> None:
    assert not _rejects(_load(VALID))
