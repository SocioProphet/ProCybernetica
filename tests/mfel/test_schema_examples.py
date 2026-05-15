from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "mfel"
EXAMPLE_DIR = ROOT / "examples" / "mfel"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


OBSERVATION_SCHEMA = SCHEMA_DIR / "observation.schema.json"
HYPOTHESIS_SCHEMA = SCHEMA_DIR / "hypothesis.schema.json"
EVIDENCE_GRAPH_SCHEMA = SCHEMA_DIR / "evidence-graph.schema.json"

EXAMPLES = [
    EXAMPLE_DIR / "notes-spotlight-indexing.sanitized.yaml",
    EXAMPLE_DIR / "corespotlight-plist.sanitized.yaml",
    EXAMPLE_DIR / "qanon-rhetorical-construction.sanitized.yaml",
]


def validator(path: Path) -> Draft202012Validator:
    schema = load_json(path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def test_mfel_json_schemas_are_valid_draft_2020_12() -> None:
    for schema_path in [OBSERVATION_SCHEMA, HYPOTHESIS_SCHEMA, EVIDENCE_GRAPH_SCHEMA]:
        Draft202012Validator.check_schema(load_json(schema_path))


@pytest.mark.parametrize("example_path", EXAMPLES)
def test_mfel_sanitized_examples_validate(example_path: Path) -> None:
    validator(OBSERVATION_SCHEMA).validate(load_yaml(example_path))


@pytest.mark.parametrize("example_path", EXAMPLES)
def test_mfel_examples_preserve_five_layer_separation(example_path: Path) -> None:
    payload = load_yaml(example_path)

    assert {entry["layer"] for entry in payload["observed_facts"]} == {"observed_fact"}
    assert {entry["layer"] for entry in payload["derived_facts"]} == {"derived_fact"}
    assert {entry["layer"] for entry in payload["interpretations"]} == {"interpretation"}
    assert {entry["layer"] for entry in payload["hypotheses"]} == {"hypothesis"}
    assert {entry["layer"] for entry in payload["prohibited_conclusions"]} == {"prohibited_conclusion"}


def test_layer_collapse_is_schema_invalid() -> None:
    payload = load_yaml(EXAMPLES[0])
    invalid = copy.deepcopy(payload)
    invalid["derived_facts"][0]["layer"] = "observed_fact"

    with pytest.raises(ValidationError):
        validator(OBSERVATION_SCHEMA).validate(invalid)


def test_suspicious_hypothesis_requires_negative_and_missing_evidence() -> None:
    schema_validator = validator(HYPOTHESIS_SCHEMA)
    invalid = {
        "schema_version": "mfel.hypothesis.v1",
        "hypothesis_id": "hyp-invalid-suspicious",
        "layer": "hypothesis",
        "statement": "A suspicious hypothesis without negative and missing evidence should fail.",
        "risk_level": "suspicious",
        "subject_scope": "synthetic test",
        "status": "live",
        "supporting_evidence": [],
        "redaction_boundary": {
            "classification": "public-synthetic",
            "private_evidence_policy": "No private evidence.",
            "public_substitute": "synthetic_fixture",
        },
        "prohibited_conclusions": ["Do not promote unsupported suspicion."],
        "non_claims": ["Synthetic invalid fixture."],
    }

    with pytest.raises(ValidationError):
        schema_validator.validate(invalid)


def test_high_risk_hypothesis_with_negative_and_missing_evidence_validates() -> None:
    valid = {
        "schema_version": "mfel.hypothesis.v1",
        "hypothesis_id": "hyp-valid-high-risk",
        "layer": "hypothesis",
        "statement": "A high-risk hypothesis can remain live only when negative and missing evidence are explicit.",
        "risk_level": "high",
        "subject_scope": "synthetic test",
        "status": "live",
        "supporting_evidence": [
            {
                "ref_id": "obs-test-001",
                "layer": "observed_fact",
                "relation": "supports",
            }
        ],
        "negative_evidence": ["No independent corroboration is present."],
        "missing_evidence": ["Endpoint evidence is absent."],
        "alternative_explanations": ["Benign local indexing artifact."],
        "redaction_boundary": {
            "classification": "public-synthetic",
            "private_evidence_policy": "No private evidence.",
            "public_substitute": "synthetic_fixture",
        },
        "prohibited_conclusions": ["Do not infer actor attribution."],
        "non_claims": ["Synthetic valid fixture."],
    }

    validator(HYPOTHESIS_SCHEMA).validate(valid)


def test_unsupported_actor_attribution_is_schema_invalid() -> None:
    invalid = {
        "schema_version": "mfel.hypothesis.v1",
        "hypothesis_id": "hyp-invalid-actor-attribution",
        "layer": "hypothesis",
        "statement": "Unsupported actor attribution should fail.",
        "risk_level": "high",
        "subject_scope": "synthetic test",
        "status": "live",
        "supporting_evidence": [],
        "negative_evidence": ["No actor evidence is present."],
        "missing_evidence": ["Attribution basis is absent."],
        "actor_attribution": {
            "actor_label": "unknown actor"
        },
        "redaction_boundary": {
            "classification": "public-synthetic",
            "private_evidence_policy": "No private evidence.",
            "public_substitute": "synthetic_fixture",
        },
        "prohibited_conclusions": ["Do not infer actor attribution."],
        "non_claims": ["Synthetic invalid fixture."],
    }

    with pytest.raises(ValidationError):
        validator(HYPOTHESIS_SCHEMA).validate(invalid)


def test_evidence_graph_schema_validates_layer_prefixes() -> None:
    graph = {
        "schema_version": "mfel.evidence_graph.v1",
        "graph_id": "graph-mfel-synthetic-001",
        "case_id": "mfel-synthetic-001",
        "publication_state": "public-synthetic",
        "redaction_boundary": {
            "classification": "public-synthetic",
            "private_evidence_policy": "No private evidence.",
            "public_substitute": "synthetic_fixture",
        },
        "nodes": [
            {"id": "obs-001", "layer": "observed_fact", "label": "observed", "summary": "Observed fact."},
            {"id": "hyp-001", "layer": "hypothesis", "label": "hypothesis", "summary": "Hypothesis."},
            {"id": "pc-001", "layer": "prohibited_conclusion", "label": "prohibited", "summary": "Prohibited conclusion."},
        ],
        "edges": [
            {"from": "obs-001", "to": "hyp-001", "relation": "supports"},
            {"from": "pc-001", "to": "hyp-001", "relation": "prohibits"},
        ],
        "graph_invariants": {
            "layer_separation_enforced": True,
            "unsupported_actor_attribution_rejected": True,
            "redaction_boundary_present": True,
            "prohibited_conclusions_present": True,
        },
    }

    validator(EVIDENCE_GRAPH_SCHEMA).validate(graph)

    invalid = copy.deepcopy(graph)
    invalid["nodes"][0]["layer"] = "hypothesis"
    with pytest.raises(ValidationError):
        validator(EVIDENCE_GRAPH_SCHEMA).validate(invalid)
