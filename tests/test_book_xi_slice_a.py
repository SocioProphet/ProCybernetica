from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_book_xi_slice_a.py"
FIXTURE = ROOT / "tests" / "fixtures" / "book-xi" / "slice-a-ingest-to-claims.synthetic.json"
PLAN = ROOT / "docs" / "implementation" / "VERTICAL_SLICE_PLAN.md"


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


def load_fixture() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_book_xi_slice_a_validator_passes() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["artifact_count"] == 1
    assert payload["provenance_count"] == 1
    assert payload["claim_count"] == 2
    assert payload["event_count"] == 1
    assert all(result["passed"] for result in payload["results"])


def test_slice_a_fixture_has_required_object_classes() -> None:
    fixture = load_fixture()
    assert len(fixture["artifact_envelopes"]) == 1
    assert len(fixture["provenance_records"]) == 1
    assert len(fixture["claims"]) == 2
    assert len(fixture["event_envelopes"]) == 1


def test_claims_have_provenance_schema_and_ontology_refs() -> None:
    fixture = load_fixture()
    provenance_ids = {record["provenance_id"] for record in fixture["provenance_records"]}
    for claim in fixture["claims"]:
        assert claim["provenance_refs"]
        assert set(claim["provenance_refs"]) <= provenance_ids
        assert claim["schema_ref"] == "schemas/claim.schema.json"
        assert claim["ontology_ref"]


def test_heuristic_claim_enters_soft_lane_before_validation() -> None:
    fixture = load_fixture()
    candidate = next(claim for claim in fixture["claims"] if claim["status"] == "candidate")
    validated = next(claim for claim in fixture["claims"] if claim["status"] == "validated")
    assert candidate["confidence"] < validated["confidence"]
    assert candidate["claim_id"] in validated["derived_from"]


def test_ingest_event_cites_artifact_provenance_and_claims() -> None:
    fixture = load_fixture()
    artifact_id = fixture["artifact_envelopes"][0]["artifact_id"]
    provenance_id = fixture["provenance_records"][0]["provenance_id"]
    claim_ids = {claim["claim_id"] for claim in fixture["claims"]}
    event = fixture["event_envelopes"][0]

    assert artifact_id in event["artifact_refs"]
    assert provenance_id in event["provenance_refs"]
    payload_claim_refs = set(event["payload"]["candidate_claim_refs"]) | set(event["payload"]["validated_claim_refs"])
    assert payload_claim_refs <= claim_ids
    assert payload_claim_refs == claim_ids


def test_slice_a_remains_public_synthetic_and_runtime_free() -> None:
    fixture = load_fixture()
    assert fixture["publication_state"] == "public-synthetic"
    assert fixture["artifact_envelopes"][0]["public_release_state"] == "public-synthetic"
    assert fixture["event_envelopes"][0]["public_release_state"] == "public-synthetic"
    non_claims = "\n".join(fixture["non_claims"])
    assert "does not ingest private data" in non_claims
    assert "does not implement a database" in non_claims
    assert "does not claim production readiness" in non_claims


def test_vertical_slice_plan_maps_all_five_slices_and_defers_runtime() -> None:
    text = PLAN.read_text(encoding="utf-8")
    for heading in [
        "Slice A — Ingest to canonical claims",
        "Slice B — Query to justified answer",
        "Slice C — Plan to safe side effect",
        "Slice D — Replay, promotion, and attestation",
        "Slice E — Mesh coordination",
    ]:
        assert heading in text
    assert "The first code path is not an agent runtime" in text
    assert "does not implement a generic agent runtime" in text
    assert "tests/fixtures/book-xi/slice-a-ingest-to-claims.synthetic.json" in text
