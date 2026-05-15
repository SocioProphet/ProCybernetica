#!/usr/bin/env python3
"""Validate Human Protection Layer reconciliation artifacts.

This validator checks doctrine/reconciliation coverage only. It does not freeze
final JSON Schemas, implement runtime policy services, authorize human actuation,
or adjudicate consent.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HPL_DRAFT = ROOT / "docs" / "reconciliation" / "HUMAN_PROTECTION_LAYER.md"
HPL_STATUS = ROOT / "docs" / "reconciliation" / "HUMAN_PROTECTION_LAYER_RECONCILIATION_STATUS.md"
HPL_ADR = ROOT / "docs" / "decisions" / "00xx-adopt-hpl-v0-profile.md"

REQUIRED_GATES = [
    "Gate 0 — Claim boundary",
    "Gate 1 — Consent and autonomy",
    "Gate 2 — Privacy and minimization",
    "Gate 3 — Physical safety",
    "Gate 4 — Psychological and cognitive safety",
    "Gate 5 — Cyber, adversarial, and misuse safety",
    "Gate 6 — Redress, revocation, appeal, and auditability",
]

REQUIRED_STATUS_VALUES = [
    "SAFE_TO_SIMULATE",
    "SAFE_TO_PUBLISH_AS_SPEC",
    "SAFE_TO_USE_AS_INTERNAL_PLANNING",
    "SAFE_TO_EXPORT_AS_CLAIM",
    "SAFE_FOR_SYNTHETIC_TEST",
    "SAFE_FOR_PHANTOM_TEST",
    "SAFE_FOR_EX_VIVO_RESEARCH",
    "REQUIRES_ETHICS_REVIEW",
    "REQUIRES_REGULATORY_REVIEW",
    "BLOCKED_HUMAN_ACTUATION",
    "BLOCKED_UNSUPPORTED_CLAIM",
    "BLOCKED_PRIVACY_RISK",
    "BLOCKED_CONSENT_MISSING",
    "BLOCKED_AUTHORITY_MISSING",
    "BLOCKED_UNDERIDENTIFIED",
    "BLOCKED_AFFECTED_POPULATION_RISK",
    "BLOCKED_POLICY",
    "SPECULATIVE_ONLY",
]

REQUIRED_EVIDENCE_TIERS = ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"]

REQUIRED_ENVELOPE_CANDIDATES = [
    "hpl_consent_envelope.v0",
    "hpl_privacy_minimization_envelope.v0",
    "hpl_evidence_tier_envelope.v0",
    "hpl_status_envelope.v0",
    "hpl_redress_envelope.v0",
    "hpl_review_outcome_envelope.v0",
    "hpl_trust_surface_envelope.v0",
]

REQUIRED_DOWNSTREAM_SURFACES = [
    "Human Digital Twin / HolographMe",
    "GAIA World Model",
    "Superconscious",
    "AgentPlane",
    "Policy Fabric",
    "SourceOS / SociOS",
]

REQUIRED_CONFORMANCE_TESTS = [
    "unsupported mechanism labels are blocked",
    "speculative claims cannot export as validated",
    "human actuation is blocked by default",
    "raw private evidence cannot export by default",
    "missing consent blocks human-derived export where consent is required",
    "missing trust-surface authority blocks tool or runtime side effects",
    "high-impact outputs require appeal/redress path",
    "world-action profiles require affected-population risk review",
    "planning traces cannot authorize execution",
    "HDT/HolographMe exports must include evidence tier and minimization basis",
]


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"missing required file: {path}") from None


def check_all(label: str, required: list[str], text: str) -> dict[str, Any]:
    missing = [item for item in required if item not in text]
    return {
        "check_id": label,
        "passed": not missing,
        "missing": missing,
        "diagnostics": [] if not missing else [f"missing {label}: {missing}"],
    }


def validate() -> dict[str, Any]:
    draft = read(HPL_DRAFT)
    status = read(HPL_STATUS)
    adr = read(HPL_ADR)
    combined = "\n".join([draft, status, adr])

    results: list[dict[str, Any]] = []
    results.append(check_all("seven-protection-gates", REQUIRED_GATES, draft))
    results.append(check_all("hpl-status-vocabulary", REQUIRED_STATUS_VALUES, draft))
    results.append(check_all("evidence-tier-vocabulary", REQUIRED_EVIDENCE_TIERS, draft))
    results.append(check_all("envelope-candidates", REQUIRED_ENVELOPE_CANDIDATES, combined))
    results.append(check_all("downstream-adoption-surfaces", REQUIRED_DOWNSTREAM_SURFACES, combined))
    results.append(check_all("conformance-test-plan", REQUIRED_CONFORMANCE_TESTS, status))

    boundary_phrases = [
        "validity is not permission",
        "Evidence tier is not permission",
        "HPL status values must not be collapsed",
        "does not freeze final JSON Schemas",
        "does not implement runtime policy services",
        "does not authorize human actuation",
        "does not publish private human evidence",
    ]
    results.append(check_all("boundary-non-claims", boundary_phrases, combined))

    decision_phrases = [
        "Adopt HPL as a v0 ProCybernetica profile",
        "technical-status versus policy-status separation",
        "public-first publication boundary",
        "candidate envelope names",
    ]
    results.append(check_all("adoption-decision", decision_phrases, adr))

    passed = all(result["passed"] for result in results)
    return {
        "validator": "hpl_reconciliation.validator.v1",
        "passed": passed,
        "results": results,
        "non_claims": [
            "No final JSON Schemas are frozen by this validator.",
            "No runtime policy service is implemented.",
            "No human actuation or private evidence publication is authorized.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = validate()
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: HPL reconciliation validates")
        else:
            print("FAIL: HPL reconciliation validates", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
