import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "procybernetica"
FIXTURE_DIR = ROOT / "tests" / "governance" / "fixtures"

FIBRATION_SCHEMA = SCHEMA_DIR / "governance-fibration.v0.1.schema.json"
CLEAVAGE_SCHEMA = SCHEMA_DIR / "cleavage-operation.v0.1.schema.json"
REINDEX_SCHEMA = SCHEMA_DIR / "reindex-operation.v0.1.schema.json"

FIBRATION_VALID = FIXTURE_DIR / "governance-fibration.valid.json"
CLEAVAGE_VALID = FIXTURE_DIR / "cleavage-operation.valid.json"
CLEAVAGE_INVALID_MISSING_LIFT = FIXTURE_DIR / "cleavage-operation.invalid-missing-lift.json"


def load(path: Path):
    return json.loads(path.read_text())


def validator(schema_path: Path) -> Draft202012Validator:
    schema = load(schema_path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def errors(schema_path: Path, payload_path: Path):
    return sorted(validator(schema_path).iter_errors(load(payload_path)), key=lambda e: list(e.path))


def test_governance_fibration_fixture_validates():
    assert errors(FIBRATION_SCHEMA, FIBRATION_VALID) == []


def test_cleavage_operation_fixture_validates():
    assert errors(CLEAVAGE_SCHEMA, CLEAVAGE_VALID) == []


def test_cleavage_operation_missing_lift_witness_fails():
    validation_errors = errors(CLEAVAGE_SCHEMA, CLEAVAGE_INVALID_MISSING_LIFT)
    assert validation_errors, "cleavage operation missing lift_witness must fail"
    assert any("lift_witness" in str(error.message) for error in validation_errors)


def test_fiber_objects_are_base_context_anchored():
    payload = load(FIBRATION_VALID)
    for fiber in payload["fiber_objects"]:
        assert fiber["base_context_ref"]


def test_canonical_tokens_have_projection_admissibility_and_cleavage_version():
    fibration = load(FIBRATION_VALID)
    cleavage = load(CLEAVAGE_VALID)

    tokens = []
    for fiber in fibration["fiber_objects"]:
        tokens.extend(fiber["fiber_token_set"])
    tokens.extend(cleavage["canonical_tokens"])

    assert tokens
    for token in tokens:
        assert token["projection_role"]
        assert token["admissibility_role"]
        assert token["cleavage_version"] == "cleavage-v0.1"


def test_reindex_schema_is_structural_and_does_not_assert_coherence():
    payload = {
        "schema_version": "0.1.0",
        "reindex_operation_id": "reindex:repo-to-workspace:1",
        "source_base_context_ref": "base:repo-review",
        "target_base_context_ref": "base:workspace-review",
        "source_fiber_ref": "fiber:repo-review",
        "target_fiber_ref": "fiber:workspace-review",
        "base_morphism_ref": "base-morphism:repo-to-workspace-review",
        "operation_kind": "transfer",
        "coherence_status": "not-asserted",
        "coherence_non_claim": "This structural reindex record does not assert functoriality.",
        "related_cleavage_operation_ref": "cleavage:repo-to-workspace:1",
        "theorem_audit_refs": ["TBD-GROT", "TBD-CLEV", "TBD-GNF"],
        "non_claims": ["No reindex functoriality is asserted."]
    }
    validator(REINDEX_SCHEMA).validate(payload)

    invalid = dict(payload)
    invalid["coherence_status"] = "asserted"
    validation_errors = sorted(validator(REINDEX_SCHEMA).iter_errors(invalid), key=lambda e: list(e.path))
    assert validation_errors
    assert any("not-asserted" in str(error.message) for error in validation_errors)
