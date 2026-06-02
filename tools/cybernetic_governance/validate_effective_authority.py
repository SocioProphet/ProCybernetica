#!/usr/bin/env python3
"""Validate Effective Authority Architecture synthetic fixtures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_FILE = ROOT / "schemas" / "effective-authority" / "effective_authority_bundle.v0_1.json"
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "effective-authority" / "effective-authority.synthetic.json"

REQUIRED_DEFS = {
    "EffectiveAuthorityNode",
    "AuthorityEdge",
    "ObservationChannel",
    "ControlChannel",
    "EgressEvent",
    "PolicyLedgerEntry",
    "ToolGrant",
    "ConnectorGrant",
    "TokenInjectionEvent",
    "RuntimeBoundaryContract",
    "BackgroundWorkerRecord",
    "SharedPlaneMembershipEvent",
    "ConversationIntegrityEvent",
    "StopProof",
    "RepoHardeningManifest",
}

REQUIRED_ZONES = {"A", "B", "C", "D", "E", "F", "G"}
EXPECTED_FAILURE_REASONS = {"schema_validation_error"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schema() -> dict[str, Any]:
    schema = load_json(SCHEMA_FILE)
    Draft202012Validator.check_schema(schema)
    defs = set(schema.get("$defs", {}).keys())
    missing_defs = REQUIRED_DEFS - defs
    if missing_defs:
        raise ValueError(f"schema missing required definitions: {sorted(missing_defs)}")
    return schema


def validate_against_def(schema: dict[str, Any], def_name: str, payload: dict[str, Any]) -> list[str]:
    defs = schema.get("$defs", {})
    if def_name not in defs:
        return [f"unknown target definition: {def_name}"]
    validator = Draft202012Validator(defs[def_name])
    return [error.message for error in sorted(validator.iter_errors(payload), key=str)]


def validate_fixture_set(path: Path) -> dict[str, Any]:
    schema = load_schema()
    fixture_set = load_json(path)
    results: list[dict[str, Any]] = []
    observed_defs: set[str] = set()
    observed_zones: set[str] = set()
    observed_record_types: set[str] = set()
    overall_pass = True

    for fixture in fixture_set.get("fixtures", []):
        fixture_id = fixture.get("fixture_id", "<missing>")
        target_def = fixture.get("target_def")
        expected_result = fixture.get("expected_result")
        expected_failure_reason = fixture.get("expected_failure_reason")
        payload = fixture.get("payload", {})
        diagnostics: list[str] = []
        observed_failures: list[str] = []

        if target_def:
            observed_defs.add(str(target_def))
        if payload.get("zone"):
            observed_zones.add(str(payload["zone"]))
        if payload.get("record_type"):
            observed_record_types.add(str(payload["record_type"]))

        messages = validate_against_def(schema, str(target_def), payload)
        if messages:
            observed_failures.append("schema_validation_error")
            diagnostics.extend(messages)

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
                "target_def": target_def,
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
            "check_id": "target-definition-coverage",
            "passed": REQUIRED_DEFS.issubset(observed_defs),
            "diagnostics": [] if REQUIRED_DEFS.issubset(observed_defs) else [
                f"missing fixture targets: {sorted(REQUIRED_DEFS - observed_defs)}"
            ],
        },
        {
            "check_id": "estate-zone-coverage",
            "passed": REQUIRED_ZONES.issubset(observed_zones),
            "diagnostics": [] if REQUIRED_ZONES.issubset(observed_zones) else [
                f"missing estate zones: {sorted(REQUIRED_ZONES - observed_zones)}"
            ],
        },
        {
            "check_id": "negative-fixture-coverage",
            "passed": any(result["expected_result"] == "fail" for result in results),
            "diagnostics": [] if any(result["expected_result"] == "fail" for result in results) else [
                "at least one negative fixture is required"
            ],
        },
    ]

    overall_pass = overall_pass and all(check["passed"] for check in coverage_checks)
    return {
        "validator": "effective_authority.validator.v0_1",
        "schema_file": str(SCHEMA_FILE.relative_to(ROOT)),
        "fixture_file": str(path.relative_to(ROOT)),
        "passed": overall_pass,
        "fixture_count": len(fixture_set.get("fixtures", [])),
        "observed_defs": sorted(observed_defs),
        "observed_zones": sorted(observed_zones),
        "observed_record_types": sorted(observed_record_types),
        "results": results + coverage_checks,
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
            print("PASS: effective authority fixtures")
        else:
            print("FAIL: effective authority fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
