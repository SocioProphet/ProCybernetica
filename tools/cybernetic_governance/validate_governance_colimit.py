#!/usr/bin/env python3
"""Validate G7 governance evidence-cocone and colimit-witness fixtures.

This validator is structural. It validates public-synthetic cocone and colimit
witness artifacts and enforces theorem-audit restraint. It does not prove a
colimit, discharge theorem obligations, assert reindex coherence, or execute
runtime evidence aggregation.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "procybernetica"
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "governance-colimit" / "governance-colimit-fixtures.synthetic.json"
THEOREM_AUDIT = ROOT / "docs" / "standards" / "proof" / "procybernetica-theorem-audit-v0.1.md"

SCHEMA_FILES = [
    "evidence-cocone.v0.1.schema.json",
    "colimit-witness.v0.1.schema.json",
]

EXPECTED_FAILURE_REASONS = {
    "schema_validation_error",
    "proved_elsewhere_requires_proof_ref",
    "evidence_cocone_leg_incompatible",
    "theorem_discharge_claim_forbidden",
}

OPEN_THEOREM_ROWS = ["TBD-GROT", "TBD-CLEV", "TBD-GNF", "TBD-COL"]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schemas() -> dict[str, dict[str, Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    for name in SCHEMA_FILES:
        schema = load_json(SCHEMA_DIR / name)
        Draft202012Validator.check_schema(schema)
        schemas[name] = schema
    return schemas


def schema_errors(schema: dict[str, Any], payload: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    return [error.message for error in sorted(validator.iter_errors(payload), key=str)]


def evidence_cocone_failures(payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    apex = payload.get("apex_evidence_ref")
    source_by_id = {source.get("source_id"): source for source in payload.get("source_objects", [])}

    for leg in payload.get("evidence_legs", []):
        if leg.get("apex_evidence_ref") != apex:
            failures.append("evidence_cocone_leg_incompatible")
        source = source_by_id.get(leg.get("source_ref"))
        if source is None:
            failures.append("evidence_cocone_leg_incompatible")
        elif source.get("evidence_ref") != leg.get("source_evidence_ref"):
            failures.append("evidence_cocone_leg_incompatible")
        if not leg.get("compatibility_witness_ref"):
            failures.append("evidence_cocone_leg_incompatible")

    if payload.get("compatibility_status") == "structurally_compatible" and not payload.get("compatibility_witness_refs"):
        failures.append("evidence_cocone_leg_incompatible")

    return sorted(set(failures))


def colimit_witness_failures(payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    proof_ref = payload.get("proof_ref")

    if payload.get("universal_property_status") == "proved_elsewhere" and not proof_ref:
        failures.append("proved_elsewhere_requires_proof_ref")
    if payload.get("uniqueness_status") == "proved_elsewhere" and not proof_ref:
        failures.append("proved_elsewhere_requires_proof_ref")
    if payload.get("naturality_status") == "proved_elsewhere" and not proof_ref:
        failures.append("proved_elsewhere_requires_proof_ref")

    if payload.get("coherence_status") != "not-asserted":
        failures.append("theorem_discharge_claim_forbidden")

    non_claim_text = "\n".join(payload.get("non_claims", [])).lower()
    required_boundaries = [
        "does not prove a colimit",
        "does not prove mediator uniqueness",
        "tbd-col",
        "tbd-grot",
    ]
    if payload.get("universal_property_status") != "proved_elsewhere":
        missing = [phrase for phrase in required_boundaries if phrase not in non_claim_text]
        if missing:
            failures.append("theorem_discharge_claim_forbidden")

    return sorted(set(failures))


def custom_failures(target_schema: str, payload: dict[str, Any]) -> list[str]:
    if target_schema == "evidence-cocone.v0.1.schema.json":
        return evidence_cocone_failures(payload)
    if target_schema == "colimit-witness.v0.1.schema.json":
        return colimit_witness_failures(payload)
    return []


def theorem_audit_failures() -> list[str]:
    text = THEOREM_AUDIT.read_text(encoding="utf-8")
    failures: list[str] = []
    for row in OPEN_THEOREM_ROWS:
        if f"`{row}`" not in text:
            failures.append(f"missing theorem row {row}")

    required_phrases = [
        "These artifacts satisfy representation and validation obligations only.",
        "They do not close `TBD-GROT`, `TBD-CLEV`, `TBD-GNF`, or `TBD-COL`.",
        "No `TBD-REINDEX` row is opened",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            failures.append(f"missing theorem-audit boundary phrase: {phrase}")
    return failures


def validate_fixture_set(path: Path) -> dict[str, Any]:
    schemas = load_schemas()
    fixture_set = load_json(path)
    results: list[dict[str, Any]] = []
    overall_pass = True

    for fixture in fixture_set.get("fixtures", []):
        fixture_id = fixture.get("fixture_id", "<missing>")
        target_schema = fixture.get("target_schema")
        expected_result = fixture.get("expected_result")
        expected_failure_reason = fixture.get("expected_failure_reason")
        payload = fixture.get("payload", {})
        diagnostics: list[str] = []
        observed_failures: list[str] = []

        if target_schema not in schemas:
            observed_failures.append("schema_validation_error")
            diagnostics.append(f"unknown target schema: {target_schema}")
        else:
            messages = schema_errors(schemas[target_schema], payload)
            if messages:
                observed_failures.append("schema_validation_error")
                diagnostics.extend(messages)
            observed_failures.extend(custom_failures(str(target_schema), payload))

        observed_failures = sorted(set(observed_failures))
        actual_result = "fail" if observed_failures else "pass"
        passed = actual_result == expected_result

        if expected_result == "fail":
            if expected_failure_reason not in EXPECTED_FAILURE_REASONS:
                passed = False
                diagnostics.append(f"unknown or missing expected_failure_reason: {expected_failure_reason}")
            elif expected_failure_reason not in observed_failures:
                passed = False
                diagnostics.append(
                    f"expected failure reason {expected_failure_reason!r} not observed; observed {observed_failures}"
                )

        if expected_result == "pass" and observed_failures:
            diagnostics.append(f"unexpected failures: {observed_failures}")

        overall_pass = overall_pass and passed
        results.append(
            {
                "fixture_id": fixture_id,
                "target_schema": target_schema,
                "expected_result": expected_result,
                "actual_result": actual_result,
                "expected_failure_reason": expected_failure_reason,
                "observed_failures": observed_failures,
                "passed": passed,
                "diagnostics": diagnostics,
            }
        )

    audit_failures = theorem_audit_failures()
    audit_result = {
        "check_id": "theorem-audit-boundary",
        "passed": not audit_failures,
        "diagnostics": audit_failures,
    }
    all_results = results + [audit_result]
    overall_pass = overall_pass and audit_result["passed"]

    return {
        "validator": "governance_colimit_g7.validator.v1",
        "fixture_file": str(path.relative_to(ROOT)),
        "passed": overall_pass,
        "fixture_count": len(fixture_set.get("fixtures", [])),
        "results": all_results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = validate_fixture_set(args.fixture)
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: governance colimit G7 fixtures")
        else:
            print("FAIL: governance colimit G7 fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
