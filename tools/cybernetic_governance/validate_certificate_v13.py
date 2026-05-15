#!/usr/bin/env python3
"""Validate certificate-family v1.3 transition fixtures.

This validator is repository-local and public-synthetic. It validates the shared
v1.3 base certificate schema and additional transition rules for the
Cairnmark-to-Stele doctrine. It does not adjudicate live certificates, execute
Atlas admission, or implement capability-tier schemas.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas" / "certificates" / "base-certificate.v1.3.json"
DEFAULT_FIXTURE_DIR = ROOT / "tests" / "fixtures" / "transition"

EXPECTED_FAILURE_REASONS = {
    "composite_fragments_match_promotion_state",
    "schema_validation_error",
    "candidate_cannot_be_promoted_stele",
    "promoted_stele_requires_reasoning_and_authority",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def fixture_files(path: Path) -> list[Path]:
    if path.is_dir():
        return sorted(path.glob("*.json"))
    return [path]


def schema_errors(schema: dict[str, Any], payload: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    return [error.message for error in sorted(validator.iter_errors(payload), key=str)]


def transition_failures(payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    promotion_state = payload.get("promotion_state")
    verdict_status = payload.get("verdict_status")

    if promotion_state == "candidate" and verdict_status not in {"undecided", "review_required"}:
        failures.append("candidate_cannot_be_promoted_stele")

    if promotion_state == "promoted_stele" and (
        not payload.get("reasoning_trace_ref") or not payload.get("signing_authority_chain")
    ):
        failures.append("promoted_stele_requires_reasoning_and_authority")

    if payload.get("certificate_kind") == "m1-composite" and promotion_state == "promoted_stele":
        for fragment in payload.get("fragment_refs", []):
            if fragment.get("promotion_state") != "promoted_stele":
                failures.append("composite_fragments_match_promotion_state")
                break

    return failures


def validate_one(path: Path, schema: dict[str, Any]) -> dict[str, Any]:
    payload = load_json(path)
    expected_failure = payload.get("expected_validation_failure", {}).get("rule")
    expected_result = "fail" if expected_failure else "pass"

    schema_failure_messages = schema_errors(schema, payload)
    observed_failures = []
    if schema_failure_messages:
        observed_failures.append("schema_validation_error")
    observed_failures.extend(transition_failures(payload))

    actual_result = "fail" if observed_failures else "pass"
    passed = actual_result == expected_result
    diagnostics = list(schema_failure_messages)

    if expected_result == "fail":
        if expected_failure not in EXPECTED_FAILURE_REASONS:
            passed = False
            diagnostics.append(f"unknown expected failure reason: {expected_failure}")
        elif expected_failure not in observed_failures:
            passed = False
            diagnostics.append(
                f"expected failure reason {expected_failure!r} not observed; observed {observed_failures}"
            )

    if expected_result == "pass" and observed_failures:
        diagnostics.append(f"unexpected failures: {observed_failures}")

    return {
        "fixture_file": str(path.relative_to(ROOT)),
        "certificate_id": payload.get("certificate_id"),
        "certificate_kind": payload.get("certificate_kind"),
        "promotion_state": payload.get("promotion_state"),
        "authority_layer": payload.get("authority_layer"),
        "cadence_classification": payload.get("cadence_classification"),
        "expected_result": expected_result,
        "actual_result": actual_result,
        "expected_failure_reason": expected_failure,
        "observed_failures": observed_failures,
        "has_reasoning_trace_ref": "reasoning_trace_ref" in payload,
        "passed": passed,
        "diagnostics": diagnostics,
    }


def validate_path(path: Path) -> dict[str, Any]:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    files = fixture_files(path)
    results = [validate_one(file, schema) for file in files]
    passed = all(result["passed"] for result in results)
    return {
        "validator": "certificate_v13_transition.validator.v1",
        "schema": str(SCHEMA_PATH.relative_to(ROOT)),
        "fixture_path": str(path.relative_to(ROOT)),
        "passed": passed,
        "fixture_count": len(results),
        "results": results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE_DIR)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = validate_path(args.fixture)
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: certificate v1.3 transition fixtures")
        else:
            print("FAIL: certificate v1.3 transition fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
