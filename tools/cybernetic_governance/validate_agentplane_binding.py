#!/usr/bin/env python3
"""Validate AgentPlane governance binding fixtures.

Repository-local structural validator for #39. This does not implement
AgentPlane runtime services; it validates contract shape and required governance
references for public-synthetic fixtures.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "cybernetic-governance"
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "agentplane-binding" / "agentplane-binding-fixtures.synthetic.json"

SCHEMA_FILES = [
    "agentplane_run_capsule.v1.json",
    "agentplane_tool_grant.v1.json",
    "agentplane_action_dispatch.v1.json",
    "agentplane_subagent_delegation.v1.json",
    "agentplane_operator_readout.v1.json",
    "agentplane_proof_pack_exhibit.v1.json",
]

REQUIRED_CATEGORIES = {
    "normal-run",
    "review-required-run",
    "transformed-run",
    "subagent-delegation-run",
}

EXPECTED_FAILURE_REASONS = {"schema_validation_error", "missing_governance_reference"}


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


def governance_reference_failures(target_schema: str, payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if target_schema in {
        "agentplane_run_capsule.v1.json",
        "agentplane_tool_grant.v1.json",
        "agentplane_action_dispatch.v1.json",
        "agentplane_subagent_delegation.v1.json",
    } and not payload.get("authority_chain_ref"):
        failures.append("missing_governance_reference")

    if target_schema == "agentplane_run_capsule.v1.json":
        if not payload.get("tool_grant_refs") or not payload.get("action_trace_refs") or not payload.get("evidence_receipt_refs"):
            failures.append("missing_governance_reference")

    if target_schema == "agentplane_action_dispatch.v1.json":
        if not payload.get("tool_grant_ref") or not payload.get("agent_action_trace_ref"):
            failures.append("missing_governance_reference")

    if target_schema == "agentplane_proof_pack_exhibit.v1.json":
        if not payload.get("run_capsule_ref") or not payload.get("operator_readout_ref"):
            failures.append("missing_governance_reference")

    return sorted(set(failures))


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
        observed_failures: list[str] = []

        if target_schema not in schemas:
            diagnostics.append(f"unknown target schema: {target_schema}")
            observed_failures.append("schema_validation_error")
        else:
            messages = schema_errors(schemas[target_schema], payload)
            if messages:
                observed_failures.append("schema_validation_error")
                diagnostics.extend(messages)
            observed_failures.extend(governance_reference_failures(target_schema, payload))

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
                "category": fixture.get("category"),
                "target_schema": target_schema,
                "expected_result": expected_result,
                "actual_result": actual_result,
                "expected_failure_reason": expected_failure_reason,
                "observed_failures": observed_failures,
                "passed": passed,
                "diagnostics": diagnostics,
            }
        )

    return {
        "validator": "agentplane_binding.validator.v1",
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
            print("PASS: AgentPlane binding fixtures")
        else:
            print("FAIL: AgentPlane binding fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
