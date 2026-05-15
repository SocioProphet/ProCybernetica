from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "assurance"
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_proof_pack.py"
FIXTURE = ROOT / "tests" / "fixtures" / "proof-pack" / "proof-pack-fixtures.synthetic.json"

SCHEMA_FILES = {
    "proof_pack_manifest.v1.json",
    "proof_pack_artifact_entry.v1.json",
    "proof_pack_evidence_lane.v1.json",
    "proof_pack_disposition.v1.json",
    "proof_pack_scorecard.v1.json",
    "proof_pack_redaction_status.v1.json",
    "proof_pack_claim_discipline.v1.json",
}

EXPECTED_FAILURE_REASONS = {
    "schema_validation_error",
    "claim_level_requires_evidence_backing",
    "artifact_entry_requires_governed_evidence_ref",
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


def test_proof_pack_schemas_are_valid_draft_2020_12() -> None:
    for schema_name in SCHEMA_FILES:
        Draft202012Validator.check_schema(load_json(SCHEMA_DIR / schema_name))


def test_proof_pack_validator_passes_fixture_set() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["fixture_count"] == 11
    assert all(result["passed"] for result in payload["results"])


def test_proof_pack_fixtures_cover_all_schema_targets() -> None:
    payload = run_validator()
    targets = {result["target_schema"] for result in payload["results"]}
    assert targets == SCHEMA_FILES


def test_valid_manifest_cites_lower_level_evidence_objects() -> None:
    fixture = load_json(FIXTURE)
    manifest = next(
        record["payload"] for record in fixture["fixtures"]
        if record["fixture_id"] == "proof-pack-manifest-valid"
    )
    assert manifest["agentplane_proof_pack_exhibit_refs"]
    assert manifest["evidence_receipt_refs"]
    assert manifest["release_delta_report_refs"]
    assert manifest["cybernetic_safety_case_refs"]
    assert manifest["artifact_provenance_refs"]


def test_valid_artifact_entry_references_governed_evidence() -> None:
    fixture = load_json(FIXTURE)
    artifact = next(
        record["payload"] for record in fixture["fixtures"]
        if record["fixture_id"] == "proof-pack-artifact-entry-agentplane-exhibit"
    )
    evidence_kinds = {entry["evidence_kind"] for entry in artifact["evidence_refs"]}
    assert "agentplane_proof_pack_exhibit" in evidence_kinds
    assert "evidence_receipt" in evidence_kinds
    assert "cybernetic_safety_case" in evidence_kinds


def test_missing_redaction_status_fails_validation() -> None:
    payload = run_validator()
    invalid = next(
        result for result in payload["results"]
        if result["fixture_id"] == "proof-pack-manifest-invalid-missing-redaction"
    )
    assert invalid["actual_result"] == "fail"
    assert "schema_validation_error" in invalid["observed_failures"]


def test_regulated_readiness_without_backing_fails_validation() -> None:
    payload = run_validator()
    invalid = next(
        result for result in payload["results"]
        if result["fixture_id"] == "proof-pack-claim-invalid-regulated-without-backing"
    )
    assert invalid["actual_result"] == "fail"
    assert invalid["expected_failure_reason"] == "claim_level_requires_evidence_backing"
    assert "claim_level_requires_evidence_backing" in invalid["observed_failures"]


def test_unbacked_artifact_entry_fails_validation() -> None:
    payload = run_validator()
    invalid = next(
        result for result in payload["results"]
        if result["fixture_id"] == "proof-pack-artifact-invalid-no-governed-evidence"
    )
    assert invalid["actual_result"] == "fail"
    assert invalid["expected_failure_reason"] == "artifact_entry_requires_governed_evidence_ref"
    assert "artifact_entry_requires_governed_evidence_ref" in invalid["observed_failures"]


def test_negative_failure_reasons_are_expected() -> None:
    payload = run_validator()
    observed = {
        result["expected_failure_reason"]
        for result in payload["results"]
        if result["expected_result"] == "fail"
    }
    assert observed == EXPECTED_FAILURE_REASONS
