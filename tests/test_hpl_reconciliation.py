from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_hpl_reconciliation.py"
HPL_STATUS = ROOT / "docs" / "reconciliation" / "HUMAN_PROTECTION_LAYER_RECONCILIATION_STATUS.md"
HPL_ADR = ROOT / "docs" / "decisions" / "00xx-adopt-hpl-v0-profile.md"

REQUIRED_ENVELOPES = {
    "hpl_consent_envelope.v0",
    "hpl_privacy_minimization_envelope.v0",
    "hpl_evidence_tier_envelope.v0",
    "hpl_status_envelope.v0",
    "hpl_redress_envelope.v0",
    "hpl_review_outcome_envelope.v0",
    "hpl_trust_surface_envelope.v0",
}

REQUIRED_DOWNSTREAM = {
    "Human Digital Twin / HolographMe",
    "GAIA World Model",
    "Superconscious",
    "AgentPlane",
    "Policy Fabric",
    "SourceOS / SociOS",
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


def test_hpl_reconciliation_validator_passes() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert all(result["passed"] for result in payload["results"])


def test_hpl_envelope_candidates_are_recorded() -> None:
    text = HPL_STATUS.read_text(encoding="utf-8") + "\n" + HPL_ADR.read_text(encoding="utf-8")
    for envelope in REQUIRED_ENVELOPES:
        assert envelope in text


def test_hpl_downstream_adoption_contract_is_recorded() -> None:
    text = HPL_STATUS.read_text(encoding="utf-8") + "\n" + HPL_ADR.read_text(encoding="utf-8")
    for downstream in REQUIRED_DOWNSTREAM:
        assert downstream in text


def test_hpl_status_and_evidence_tiers_are_accepted_but_not_permission() -> None:
    text = HPL_STATUS.read_text(encoding="utf-8") + "\n" + HPL_ADR.read_text(encoding="utf-8")
    assert "HPL status values must not be collapsed" in text
    assert "Evidence tier is not permission" in text
    assert "validity is not permission" in text


def test_hpl_non_claims_hold_schema_and_runtime_boundary() -> None:
    text = HPL_STATUS.read_text(encoding="utf-8") + "\n" + HPL_ADR.read_text(encoding="utf-8")
    assert "does not freeze final JSON Schemas" in text
    assert "does not implement runtime policy services" in text
    assert "does not authorize human actuation" in text
    assert "does not publish private human evidence" in text
