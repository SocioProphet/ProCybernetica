from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_integration_closeout.py"
STATUS = ROOT / "docs" / "INTEGRATION_STATUS.md"
CHECKLIST = ROOT / "docs" / "PUBLIC_REVIEW_CHECKLIST.md"
CONFORMANCE = ROOT / "docs" / "conformance" / "README.md"
README = ROOT / "README.md"
START_HERE = ROOT / "docs" / "START_HERE.md"

REQUIRED_TARGETS = {
    "v0-schemas-ci",
    "profiles-ci",
    "cybernetic-governance-ci",
    "proof-pack-ci",
    "book-xi-slice-a-ci",
    "civic-stack-ci",
    "estate-alignment-followups-ci",
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


def test_integration_closeout_validator_passes() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert all(result["passed"] for result in payload["results"])


def test_integration_status_records_all_twenty_turns_complete() -> None:
    text = STATUS.read_text(encoding="utf-8")
    for turn in range(1, 21):
        assert f"| {turn} |" in text
    assert "| 20 | Stop point | complete |" in text
    assert "#32 CI Observation Ledger" in text
    assert "G7+ proof-pack / colimit / evidence-cocone" in text


def test_public_review_checklist_preserves_non_claims() -> None:
    text = CHECKLIST.read_text(encoding="utf-8")
    assert "CI observation ledger issue remains open by design" in text
    assert "Passing this checklist does not claim production readiness" in text
    assert "runtime implementation remains in owning upstream repos" in text


def test_conformance_readme_lists_required_targets() -> None:
    text = CONFORMANCE.read_text(encoding="utf-8")
    for target in REQUIRED_TARGETS:
        assert target in text
    assert "There is no single monolithic runtime CLI" in text


def test_readme_and_start_here_are_refreshed_for_public_review_state() -> None:
    readme = README.read_text(encoding="utf-8")
    start_here = START_HERE.read_text(encoding="utf-8")

    assert "stable public-review state" in readme
    assert "Public-review readiness is not production-readiness" in readme
    assert "docs/INTEGRATION_STATUS.md" in readme
    assert "docs/PUBLIC_REVIEW_CHECKLIST.md" in readme

    assert "v0 public-review mode" in start_here
    assert "docs/INTEGRATION_STATUS.md" in start_here
    assert "docs/PUBLIC_REVIEW_CHECKLIST.md" in start_here
    assert "Leave the CI Observation Ledger open by design" in start_here


def test_closeout_non_claims_include_runtime_and_downstream_boundaries() -> None:
    text = STATUS.read_text(encoding="utf-8")
    for phrase in [
        "production runtime readiness",
        "live deployment",
        "runtime enforcement",
        "empirical model performance",
        "civic runtime operation",
        "human-impacting authorization",
        "downstream adapter implementation",
    ]:
        assert phrase in text
