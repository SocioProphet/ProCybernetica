from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "certificates" / "base-certificate.v1.3.json"
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_certificate_v13.py"
TRANSITION_FIXTURES = ROOT / "tests" / "fixtures" / "transition"
F4_FIXTURE = ROOT / "tests" / "fixtures" / "falsification" / "f4-cairnmark-stele.synthetic.json"
F4_ADDENDUM = ROOT / "docs" / "falsification" / "F4_CERTIFICATE_V13_MONITORABILITY.md"
CERT_INDEX = ROOT / "docs" / "certificates" / "CERTIFICATE_FAMILY_INDEX_V1_3.md"
TRANSITION_DOCTRINE = ROOT / "docs" / "certificates" / "CAIRNMARK_TO_STELE_TRANSITION_DOCTRINE.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator() -> dict:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(TRANSITION_FIXTURES), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def test_base_certificate_schema_is_valid_draft_2020_12() -> None:
    Draft202012Validator.check_schema(load_json(SCHEMA))


def test_certificate_v13_validator_passes_transition_fixture_set() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["fixture_count"] >= 5
    assert all(result["passed"] for result in payload["results"])


def test_transition_fixtures_cover_candidate_promoted_rejected_and_superseded() -> None:
    payload = run_validator()
    states = {result["promotion_state"] for result in payload["results"]}
    assert {"candidate", "promoted_stele", "rejected", "superseded"} <= states


def test_certificate_v13_fields_present_in_all_transition_fixtures() -> None:
    payload = run_validator()
    for result in payload["results"]:
        assert result["authority_layer"]
        assert result["promotion_state"]
        assert result["cadence_classification"]
        assert result["has_reasoning_trace_ref"] is True


def test_invalid_composite_fails_for_fragment_promotion_state_rule() -> None:
    payload = run_validator()
    invalid = next(
        result for result in payload["results"]
        if result["fixture_file"].endswith("m1-composite-promoted-with-cairnmark-fragment.invalid.synthetic.json")
    )
    assert invalid["expected_result"] == "fail"
    assert invalid["actual_result"] == "fail"
    assert invalid["expected_failure_reason"] == "composite_fragments_match_promotion_state"
    assert "composite_fragments_match_promotion_state" in invalid["observed_failures"]


def test_certificate_family_index_names_all_requested_families_and_v13_fields() -> None:
    text = CERT_INDEX.read_text(encoding="utf-8")
    for expected in [
        "m0-training-provenance",
        "m1a-source-lock",
        "m1b-witness-card",
        "m1c-causal-triad",
        "m1-5-attribution-graph",
        "m1d-off-target-audit",
        "m1-composite",
        "m2-implementability",
        "m3-cross-layer-robustness",
        "m5-public-note",
        "procybernetica-safety-case",
        "authority_layer",
        "promotion_state",
        "reasoning_trace_ref",
        "cadence_classification",
    ]:
        assert expected in text


def test_transition_doctrine_defines_cairnmark_to_stele_states() -> None:
    text = TRANSITION_DOCTRINE.read_text(encoding="utf-8")
    assert "candidate -> promoted_stele" in text
    assert "candidate -> rejected" in text
    assert "candidate -> superseded" in text
    assert "promoted_stele -> superseded" in text
    assert "A record with `promotion_state: candidate` is a Cairnmark" in text
    assert "A record with `promotion_state: promoted_stele` is a Stele" in text


def test_f4_monitorability_addendum_and_fixture_present() -> None:
    addendum = F4_ADDENDUM.read_text(encoding="utf-8")
    assert "F4.1" in addendum
    assert "F4.2" in addendum
    assert "F4.3" in addendum
    assert "schema-testable and fixture-backed" in addendum

    fixture = load_json(F4_FIXTURE)
    observable_ids = {entry["observable_id"] for entry in fixture["fixtures"]}
    assert {"F4.1", "F4.2", "F4.3"} <= observable_ids
