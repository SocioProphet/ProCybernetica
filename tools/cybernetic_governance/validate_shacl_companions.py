#!/usr/bin/env python3
"""Validate SHACL companion coverage for certificates and bridges.

This validator checks repository-local coverage structure only. It does not run a
SHACL engine and does not claim runtime SHACL enforcement. Its purpose is to
make #46 coverage machine-checkable without adding a new dependency.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
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

REQUIRED_SOURCE_SCHEMAS = {
    "schemas/certificates/base-certificate.v1.3.json",
    "schemas/bridges/ops-history-to-pneumachinalis.v1.json",
    "schemas/bridges/masonmark-to-certificate.v1.json",
    "schemas/bridges/certificate-to-atlas.v1.json",
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

REQUIRED_INVARIANTS = {"CI-1", "CI-4", "CI-9"}


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"missing required file: {path}") from None


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing required file: {path}") from None


def shape_is_declared(shape_name: str, text: str) -> bool:
    return re.search(rf"(^|\n){re.escape(shape_name)}\s*\n\s*a\s+sh:NodeShape\s*;", text) is not None


def validate() -> dict[str, Any]:
    cert_text = read(CERT_SHAPES)
    bridge_text = read(BRIDGE_SHAPES)
    coverage_text = read(COVERAGE_DOC)
    addendum_text = read(F2_ADDENDUM)
    fixture = load_json(F2_FIXTURE)

    results: list[dict[str, Any]] = []

    for shape in sorted(REQUIRED_CERTIFICATE_SHAPES):
        results.append(
            {
                "check_id": f"certificate-shape:{shape}",
                "passed": shape_is_declared(shape, cert_text),
                "diagnostics": [] if shape_is_declared(shape, cert_text) else [f"missing {shape}"],
            }
        )

    for shape in sorted(REQUIRED_BRIDGE_SHAPES):
        results.append(
            {
                "check_id": f"bridge-shape:{shape}",
                "passed": shape_is_declared(shape, bridge_text),
                "diagnostics": [] if shape_is_declared(shape, bridge_text) else [f"missing {shape}"],
            }
        )

    combined_text = "\n".join([cert_text, bridge_text, coverage_text, addendum_text])

    for schema_ref in sorted(REQUIRED_SOURCE_SCHEMAS):
        results.append(
            {
                "check_id": f"source-schema:{schema_ref}",
                "passed": schema_ref in combined_text,
                "diagnostics": [] if schema_ref in combined_text else [f"missing source schema ref {schema_ref}"],
            }
        )

    for rule in sorted(REQUIRED_NON_SHACL_RULES):
        results.append(
            {
                "check_id": f"fallback-rule:{rule}",
                "passed": rule in combined_text,
                "diagnostics": [] if rule in combined_text else [f"missing fallback rule {rule}"],
            }
        )

    for invariant in sorted(REQUIRED_INVARIANTS):
        results.append(
            {
                "check_id": f"invariant:{invariant}",
                "passed": invariant in combined_text,
                "diagnostics": [] if invariant in combined_text else [f"missing invariant coverage marker {invariant}"],
            }
        )

    f2_fixture_records = fixture.get("fixtures", [])
    f2_covered = any(
        record.get("observable_id") == "F2.2"
        and record.get("expected_result") == "covered_with_shacl_plus_non_shacl_fallback"
        for record in f2_fixture_records
        if isinstance(record, dict)
    )
    results.append(
        {
            "check_id": "f2.2-fixture-marker",
            "passed": f2_covered,
            "diagnostics": [] if f2_covered else ["F2.2 fixture marker missing or wrong status"],
        }
    )

    f2_addendum_covered = "covered-with-SHACL-plus-non-SHACL-fallback" in addendum_text
    results.append(
        {
            "check_id": "f2.2-addendum-status",
            "passed": f2_addendum_covered,
            "diagnostics": [] if f2_addendum_covered else ["F2.2 addendum missing coverage status"],
        }
    )

    passed = all(result["passed"] for result in results)
    return {
        "validator": "shacl_companion_coverage.validator.v1",
        "passed": passed,
        "certificate_shape_count": len(REQUIRED_CERTIFICATE_SHAPES),
        "bridge_shape_count": len(REQUIRED_BRIDGE_SHAPES),
        "results": results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = validate()
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: SHACL companion coverage")
        else:
            print("FAIL: SHACL companion coverage", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
