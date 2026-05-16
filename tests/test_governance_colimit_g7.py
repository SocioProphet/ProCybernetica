from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "procybernetica"
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_governance_colimit.py"
FIXTURE = ROOT / "tests" / "fixtures" / "governance-colimit" / "governance-colimit-fixtures.synthetic.json"
THEOREM_AUDIT = ROOT / "docs" / "standards" / "proof" / "procybernetica-theorem-audit-v0.1.md"
EVIDENCE_COCONE_DOC = ROOT / "docs" / "standards" / "governance" / "procybernetica-evidence-cocone-v0.1.md"
COLIMIT_WITNESS_DOC = ROOT / "docs" / "standards" / "governance" / "procybernetica-colimit-witness-v0.1.md"

SCHEMA_FILES = {
    "evidence-cocone.v0.1.schema.json",
    "colimit-witness.v0.1.schema.json",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator() -> dict:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def test_governance_colimit_schemas_are_valid_draft_2020_12() -> None:
    for schema_name in SCHEMA_FILES:
        Draft202012Validator.check_schema(load_json(SCHEMA_DIR / schema_name))


def test_governance_colimit_validator_passes_fixture_set() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["fixture_count"] == 3
    assert all(result["passed"] for result in payload["results"])


def test_fixture_covers_cocone_and_colimit_witness_targets() -> None:
    payload = run_validator()
    targets = {result["target_schema"] for result in payload["results"] if "target_schema" in result}
    assert targets == SCHEMA_FILES


def test_evidence_cocone_fixture_is_structurally_compatible_without_coherence_claim() -> None:
    fixture = load_json(FIXTURE)
    cocone = next(record["payload"] for record in fixture["fixtures"] if record["fixture_id"] == "valid-evidence-cocone-two-fibers")
    assert cocone["compatibility_status"] == "structurally_compatible"
    assert cocone["coherence_status"] == "not-asserted"
    assert {"TBD-GROT", "TBD-COL"} <= set(cocone["theorem_audit_refs"])
    assert len(cocone["source_objects"]) == 2
    assert len(cocone["evidence_legs"]) == 2
    assert all(leg["apex_evidence_ref"] == cocone["apex_evidence_ref"] for leg in cocone["evidence_legs"])


def test_colimit_witness_fixture_remains_structural_candidate() -> None:
    fixture = load_json(FIXTURE)
    witness = next(record["payload"] for record in fixture["fixtures"] if record["fixture_id"] == "valid-colimit-structural-candidate")
    assert witness["universal_property_status"] == "structural_candidate"
    assert witness["uniqueness_status"] == "review_required"
    assert witness["naturality_status"] == "not_asserted"
    assert witness["coherence_status"] == "not-asserted"
    non_claims = "\n".join(witness["non_claims"])
    assert "does not prove a colimit" in non_claims
    assert "does not prove mediator uniqueness" in non_claims
    assert "TBD-COL" in non_claims
    assert "TBD-GROT" in non_claims


def test_proved_elsewhere_without_proof_ref_is_rejected() -> None:
    payload = run_validator()
    invalid = next(result for result in payload["results"] if result["fixture_id"] == "invalid-colimit-proved-elsewhere-without-proof-ref")
    assert invalid["actual_result"] == "fail"
    assert invalid["expected_failure_reason"] == "schema_validation_error"
    assert "schema_validation_error" in invalid["observed_failures"]


def test_theorem_audit_rows_remain_open_and_structural_only() -> None:
    text = THEOREM_AUDIT.read_text(encoding="utf-8")
    for row in ["TBD-GROT", "TBD-CLEV", "TBD-GNF", "TBD-COL"]:
        assert f"`{row}`" in text
    assert "These artifacts satisfy representation and validation obligations only." in text
    assert "They do not close `TBD-GROT`, `TBD-CLEV`, `TBD-GNF`, or `TBD-COL`." in text
    assert "No `TBD-REINDEX` row is opened" in text


def test_g7_standards_preserve_theorem_boundaries() -> None:
    cocone = EVIDENCE_COCONE_DOC.read_text(encoding="utf-8")
    colimit = COLIMIT_WITNESS_DOC.read_text(encoding="utf-8")
    assert "This standard does not assert universal property" in cocone
    assert "This standard does not implement runtime evidence aggregation" in cocone
    assert "This standard does not prove a colimit" in colimit
    assert "does not discharge `TBD-COL`" in colimit
    assert "does not discharge `TBD-GROT`" in colimit
