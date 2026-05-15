#!/usr/bin/env python3
"""Validate bridge schema fixtures for OpsHistory, Masonmark, and Atlas.

This validator is repository-local and public-synthetic. It validates JSON Schema
shape and cross-field bridge invariants. It does not implement runtime bridge
execution, Atlas admission runtime, Masonmark adjudication, OpsHistory ingestion,
Pneumachinalis scoring, SHACL, Rego, or capability-tier schemas.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "bridges"
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "bridges" / "bridge-fixtures.synthetic.json"

SCHEMA_FILES = [
    "ops-history-to-pneumachinalis.v1.json",
    "masonmark-to-certificate.v1.json",
    "certificate-to-atlas.v1.json",
]

EXPECTED_FAILURE_REASONS = {
    "human_actor_requires_consent_for_reputation_microbeat",
    "promotion_state_strict_inheritance",
    "verifier_scores_consistent_with_verdict",
    "undecided_fails_closed_to_deny",
    "pattern_c_always_denies",
}


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


def cross_field_failures(target_schema: str, payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []

    if target_schema == "ops-history-to-pneumachinalis.v1.json":
        microbeat = payload.get("pneumachinalis_microbeat", {})
        is_reputation = (
            microbeat.get("microbeat_kind") == "reputation"
            or microbeat.get("reputation_effect") in {"positive", "negative", "review_required"}
        )
        if payload.get("actor_kind") == "human" and is_reputation and not payload.get("consent_evidence_ref"):
            failures.append("human_actor_requires_consent_for_reputation_microbeat")

    if target_schema == "masonmark-to-certificate.v1.json":
        projection = payload.get("certificate_projection", {})
        proofpack_state = payload.get("proofpack_state")
        promotion_state = projection.get("promotion_state")
        verdict = projection.get("verdict")
        scores = payload.get("verifier_scores", {})

        if proofpack_state != "verified" and promotion_state == "promoted_stele":
            failures.append("promotion_state_strict_inheritance")

        if verdict == "allow" or promotion_state == "promoted_stele":
            low_scores = [
                name for name in ["soundness", "traceability", "non_claim_integrity"]
                if float(scores.get(name, 0)) < 0.8
            ]
            if low_scores:
                failures.append("verifier_scores_consistent_with_verdict")

    if target_schema == "certificate-to-atlas.v1.json":
        promotion_state = payload.get("promotion_state")
        pattern_class = payload.get("pattern_class")
        disposition = payload.get("atlas_disposition")
        fail_closed = payload.get("fail_closed")

        if promotion_state == "undecided" and not (disposition == "deny" and fail_closed is True):
            failures.append("undecided_fails_closed_to_deny")

        if pattern_class == "pattern_c" and disposition != "deny":
            failures.append("pattern_c_always_denies")

    return failures


def validate_fixture_set(path: Path) -> dict[str, Any]:
    schemas = load_schemas()
    fixture_set = load_json(path)
    results = []
    overall_pass = True

    for fixture in fixture_set.get("fixtures", []):
        fixture_id = fixture.get("fixture_id", "<missing>")
        target_schema = fixture.get("target_schema")
        expected_result = fixture.get("expected_result")
        expected_failure_reason = fixture.get("expected_failure_reason")
        payload = fixture.get("payload", {})
        diagnostics: list[str] = []

        if target_schema not in schemas:
            diagnostics.append(f"unknown target schema: {target_schema}")
            schema_failure_messages: list[str] = []
        else:
            schema_failure_messages = schema_errors(schemas[target_schema], payload)
            diagnostics.extend(schema_failure_messages)

        observed_failures = []
        if schema_failure_messages:
            observed_failures.append("schema_validation_error")
        observed_failures.extend(cross_field_failures(str(target_schema), payload))

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
                "category": fixture.get("category"),
                "target_schema": target_schema,
                "expected_result": expected_result,
                "actual_result": actual_result,
                "expected_failure_reason": expected_failure_reason,
                "observed_failures": observed_failures,
                "passed": passed,
                "diagnostics": diagnostics,
                "capability_tier_invocation_present": "capability_tier_invocation" in payload,
            }
        )

    return {
        "validator": "bridge_schema_validator.v1",
        "fixture_file": str(path.relative_to(ROOT)),
        "passed": overall_pass,
        "fixture_count": len(fixture_set.get("fixtures", [])),
        "results": results,
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
            print("PASS: bridge fixtures")
        else:
            print("FAIL: bridge fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
