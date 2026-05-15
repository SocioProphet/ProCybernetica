from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_shacl_companions.py"
CERT_SHAPES = ROOT / "shacl" / "certificates" / "certificate-family-v1.3.shacl.ttl"
BRIDGE_SHAPES = ROOT / "shacl" / "bridges" / "bridge-schemas-v1.shacl.ttl"
COVERAGE_DOC = ROOT / "docs" / "shacl" / "CERTIFICATE_AND_BRIDGE_SHACL_COVERAGE.md"
F2_ADDENDUM = ROOT / "docs" / "falsification" / "F2_2_SHACL_COMPANION_COVERAGE.md"
F2_FIXTURE = ROOT / "tests" / "fixtures" / "falsification" / "f2-2-shacl-companion-coverage.synthetic.json"

REQUIRED_CERTIFICATE_SHAPES = {
    "pc:M0TrainingProvenanceCertificateShape",
    "pc:M1ASourceLockCertificateShape",
    "pc:M1BWitnessCardCertificateShape",
    "pc:M1CCausalTriadCertificateShape",
    "pc:M15AttributionGraphCertificateShape",
    "pc:M1DOffTargetAuditCertificateShape",
    "pc:M1CompositeCertificateShape",
    "pc:M2ImplementabilityCertificateShape",
    "pc:M3CrossLayerRobustnessCertificateShape",
    "pc:M5PublicNoteCertificateShape",
    "pc:ProCyberneticaSafetyCaseCertificateShape",
}

REQUIRED_BRIDGE_SHAPES = {
    "pc:OpsHistoryToPneumachinalisBridgeShape",
    "pc:MasonmarkToCertificateBridgeShape",
    "pc:CertificateToAtlasBridgeShape",
}

REQUIRED_NON_SHACL_RULES = {
    "composite_fragments_match_promotion_state",
    "human_actor_requires_consent_for_reputation_microbeat",
    "promotion_state_strict_inheritance",
    "verifier_scores_consistent_with_verdict",
    "undecided_fails_closed_to_deny",
    "pattern_c_always_denies",
    "CI-9 authority-concentration threshold enforcement",
}


def run_validator() -> dict:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def test_shacl_companion_validator_passes() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["certificate_shape_count"] == 11
    assert payload["bridge_shape_count"] == 3
    assert all(result["passed"] for result in payload["results"])


def test_certificate_shape_file_declares_all_certificate_family_shapes() -> None:
    text = CERT_SHAPES.read_text(encoding="utf-8")
    for shape in REQUIRED_CERTIFICATE_SHAPES:
        assert shape in text
    assert "pc:BaseCertificateV13Shape" in text
    assert "schemas/certificates/base-certificate.v1.3.json" in text
    assert "CI-1" in text
    assert "CI-4" in text
    assert "CI-9" in text


def test_bridge_shape_file_declares_all_bridge_shapes() -> None:
    text = BRIDGE_SHAPES.read_text(encoding="utf-8")
    for shape in REQUIRED_BRIDGE_SHAPES:
        assert shape in text
    assert "schemas/bridges/ops-history-to-pneumachinalis.v1.json" in text
    assert "schemas/bridges/masonmark-to-certificate.v1.json" in text
    assert "schemas/bridges/certificate-to-atlas.v1.json" in text


def test_non_shacl_fallback_rules_are_documented() -> None:
    combined = "\n".join(
        [
            CERT_SHAPES.read_text(encoding="utf-8"),
            BRIDGE_SHAPES.read_text(encoding="utf-8"),
            COVERAGE_DOC.read_text(encoding="utf-8"),
            F2_ADDENDUM.read_text(encoding="utf-8"),
        ]
    )
    for rule in REQUIRED_NON_SHACL_RULES:
        assert rule in combined


def test_f2_2_fixture_marker_records_coverage_status() -> None:
    payload = json.loads(F2_FIXTURE.read_text(encoding="utf-8"))
    records = payload["fixtures"]
    assert len(records) == 1
    record = records[0]
    assert record["observable_id"] == "F2.2"
    assert record["expected_result"] == "pass"
    assert record["coverage_status"] == "covered_with_shacl_plus_non_shacl_fallback"
    assert "shacl/certificates/certificate-family-v1.3.shacl.ttl" in record["shacl_shape_refs"]
    assert "shacl/bridges/bridge-schemas-v1.shacl.ttl" in record["shacl_shape_refs"]


def test_f2_2_addendum_records_no_runtime_claim_boundary() -> None:
    text = F2_ADDENDUM.read_text(encoding="utf-8")
    assert "covered-with-SHACL-plus-non-SHACL-fallback" in text
    assert "does not claim runtime SHACL enforcement" in text
    assert "does not claim Rego implementation" in text
