#!/usr/bin/env python3
"""Validate IOES conformance synthetic fixtures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_FILE = ROOT / "schemas" / "ioes" / "ioes_conformance_record.v0_1.json"
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "ioes" / "ioes-conformance.synthetic.json"

EXPECTED_FAILURE_REASONS = {"schema_validation_error", "ioes_semantic_error"}
REQUIRED_HUMAN_PROTECTION_FLAGS = {
    "person_not_score",
    "stewardship_not_ownership",
    "mentorship_not_control",
    "nba_not_command",
    "delivery_metrics_not_human_worth",
    "projection_not_person",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schema() -> dict[str, Any]:
    schema = load_json(SCHEMA_FILE)
    Draft202012Validator.check_schema(schema)
    return schema


def schema_errors(schema: dict[str, Any], payload: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    return [error.message for error in sorted(validator.iter_errors(payload), key=str)]


def semantic_errors(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    impacts = set(payload.get("ioes_impact_classes", []))
    boundaries = payload.get("declared_boundaries", {})
    protection = payload.get("human_protection", {})
    status = payload.get("status")

    missing_flags = sorted(REQUIRED_HUMAN_PROTECTION_FLAGS - set(protection))
    if missing_flags:
        errors.append(f"missing human protection flags: {missing_flags}")

    false_flags = sorted(flag for flag in REQUIRED_HUMAN_PROTECTION_FLAGS if protection.get(flag) is not True)
    if status == "conformant" and false_flags:
        errors.append(f"conformant IOES record has false human protection flags: {false_flags}")

    if boundaries.get("mutates") is True and not payload.get("consent_refs"):
        errors.append("mutating IOES control requires consent_refs")

    if boundaries.get("exports") is True and not payload.get("consent_refs"):
        errors.append("exporting IOES control requires consent_refs")

    if boundaries.get("mutates") is True and payload.get("repair_posture") == "missing":
        errors.append("mutating IOES control requires repair posture")

    if boundaries.get("exports") is True and payload.get("contest_posture") == "missing":
        errors.append("exporting IOES control requires contest posture")

    if "stewardship_assignment" in impacts and not payload.get("stewardship_refs"):
        errors.append("stewardship impact requires stewardship_refs")

    if "stewardship_transfer" in impacts and not payload.get("succession_refs"):
        errors.append("stewardship transfer requires succession_refs")

    if "succession" in impacts and not payload.get("succession_refs"):
        errors.append("succession impact requires succession_refs")

    if "ecological_dependency" in impacts and not payload.get("gaia_refs"):
        errors.append("ecological dependency impact requires gaia_refs")

    if "learning_canon" in impacts and not payload.get("learning_refs"):
        errors.append("learning canon impact requires learning_refs")

    if "delivery_outcome" in impacts:
        if not payload.get("delivery_refs"):
            errors.append("delivery outcome impact requires delivery_refs")
        if protection.get("delivery_metrics_not_human_worth") is not True:
            errors.append("delivery outcome impact requires delivery_metrics_not_human_worth=true")

    if "policy_state" in impacts and not payload.get("policy_refs"):
        errors.append("policy state impact requires policy_refs")

    non_claims = " ".join(payload.get("non_claims", [])).lower()
    if status == "conformant":
        if "human worth" not in non_claims:
            errors.append("conformant record must state that metrics do not measure human worth")
        if "ownership" not in non_claims:
            errors.append("conformant record must state stewardship is not ownership")

    return errors


def validate_fixture_set(path: Path) -> dict[str, Any]:
    schema = load_schema()
    fixture_set = load_json(path)
    results: list[dict[str, Any]] = []
    observed_failures_by_fixture: dict[str, list[str]] = {}
    overall_pass = True

    for fixture in fixture_set.get("fixtures", []):
        fixture_id = fixture.get("fixture_id", "<missing>")
        expected_result = fixture.get("expected_result")
        expected_failure_reason = fixture.get("expected_failure_reason")
        payload = fixture.get("payload", {})
        diagnostics: list[str] = []
        observed_failures: list[str] = []

        messages = schema_errors(schema, payload)
        if messages:
            observed_failures.append("schema_validation_error")
            diagnostics.extend(messages)

        semantic = semantic_errors(payload)
        if semantic:
            observed_failures.append("ioes_semantic_error")
            diagnostics.extend(semantic)

        observed_failures = sorted(set(observed_failures))
        observed_failures_by_fixture[str(fixture_id)] = observed_failures
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
                "expected_result": expected_result,
                "actual_result": actual_result,
                "expected_failure_reason": expected_failure_reason,
                "observed_failures": observed_failures,
                "passed": passed,
                "diagnostics": diagnostics,
            }
        )

    coverage_checks = [
        {
            "check_id": "negative-fixture-coverage",
            "passed": any(result["expected_result"] == "fail" for result in results),
            "diagnostics": [] if any(result["expected_result"] == "fail" for result in results) else [
                "at least one negative fixture is required"
            ],
        },
        {
            "check_id": "positive-fixture-coverage",
            "passed": any(result["expected_result"] == "pass" for result in results),
            "diagnostics": [] if any(result["expected_result"] == "pass" for result in results) else [
                "at least one positive fixture is required"
            ],
        },
    ]

    overall_pass = overall_pass and all(check["passed"] for check in coverage_checks)
    return {
        "validator": "ioes_conformance.validator.v0_1",
        "schema_file": str(SCHEMA_FILE.relative_to(ROOT)),
        "fixture_file": str(path.relative_to(ROOT)),
        "passed": overall_pass,
        "fixture_count": len(fixture_set.get("fixtures", [])),
        "results": results + coverage_checks,
        "observed_failures_by_fixture": observed_failures_by_fixture,
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
            print("PASS: IOES conformance fixtures")
        else:
            print("FAIL: IOES conformance fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
