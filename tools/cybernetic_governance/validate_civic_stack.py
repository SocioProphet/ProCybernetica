#!/usr/bin/env python3
"""Validate civic-stack assurance fixtures.

Repository-local structural validator for #40. This does not implement civic
ontology, downstream runtime execution, SocioSphere ingestion, Delivery
Excellence scoring, Policy Fabric guardrails, or AgentPlane runtime evidence.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "assurance"
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "civic-stack" / "civic-stack-assurance.synthetic.json"

SCHEMA_FILES = [
    "civic_risk_control_binding.v1.json",
    "civic_evidence_pack.v1.json",
    "civic_incident_control_event.v1.json",
    "civic_audit_signal.v1.json",
    "civic_risk_contribution.v1.json",
    "civic_assurance_trace.v1.json",
]

EXPECTED_FAILURE_REASONS = {
    "schema_validation_error",
    "worked_trace_requires_all_steps",
}

REQUIRED_WORKED_TRACE_STEPS = [
    "artifact_deployed",
    "policy_checked",
    "runtime_attested",
    "control_verified",
    "evidence_pack_emitted",
    "score_updated",
]

REQUIRED_CIVIC_LAYERS = {"CGRM", "SRM", "DRM", "TRM", "OAC"}
REQUIRED_DECISION_TARGETS = {"service_decision", "dataset_decision", "runtime_decision", "policy_decision", "artifact_decision"}
REQUIRED_CONTRIBUTION_KINDS = {"negative_contribution", "blocker", "defeater", "conflict"}


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


def worked_trace_failures(payload: dict[str, Any]) -> list[str]:
    steps = payload.get("steps", [])
    step_kinds = [step.get("step_kind") for step in sorted(steps, key=lambda item: item.get("step_index", -1))]
    if step_kinds != REQUIRED_WORKED_TRACE_STEPS:
        return ["worked_trace_requires_all_steps"]
    return []


def custom_failures(target_schema: str, payload: dict[str, Any]) -> list[str]:
    if target_schema == "civic_assurance_trace.v1.json":
        return worked_trace_failures(payload)
    return []


def validate_fixture_set(path: Path) -> dict[str, Any]:
    schemas = load_schemas()
    fixture_set = load_json(path)
    results: list[dict[str, Any]] = []
    observed_layers: set[str] = set()
    observed_decision_targets: set[str] = set()
    observed_contribution_kinds: set[str] = set()
    overall_pass = True

    for fixture in fixture_set.get("fixtures", []):
        fixture_id = fixture.get("fixture_id", "<missing>")
        target_schema = fixture.get("target_schema")
        expected_result = fixture.get("expected_result")
        expected_failure_reason = fixture.get("expected_failure_reason")
        payload = fixture.get("payload", {})
        diagnostics: list[str] = []
        observed_failures: list[str] = []

        if payload.get("civic_layer"):
            observed_layers.add(payload["civic_layer"])
        if payload.get("decision_target"):
            observed_decision_targets.add(payload["decision_target"])
        if payload.get("contribution_kind"):
            observed_contribution_kinds.add(payload["contribution_kind"])

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

    coverage_checks = [
        {
            "check_id": "schema-target-coverage",
            "passed": {result["target_schema"] for result in results} == set(SCHEMA_FILES),
            "diagnostics": [] if {result["target_schema"] for result in results} == set(SCHEMA_FILES) else ["not all schema targets are covered"],
        },
        {
            "check_id": "civic-layer-runtime-coverage",
            "passed": "TRM" in observed_layers,
            "diagnostics": [] if "TRM" in observed_layers else ["TRM runtime layer must be covered by worked trace"],
        },
        {
            "check_id": "runtime-decision-target-covered",
            "passed": "runtime_decision" in observed_decision_targets,
            "diagnostics": [] if "runtime_decision" in observed_decision_targets else ["runtime_decision evidence pack target missing"],
        },
        {
            "check_id": "rational-grl-defeater-covered",
            "passed": "defeater" in observed_contribution_kinds,
            "diagnostics": [] if "defeater" in observed_contribution_kinds else ["RationalGRL defeater contribution missing"],
        },
    ]

    all_results = results + coverage_checks
    overall_pass = overall_pass and all(check["passed"] for check in coverage_checks)
    return {
        "validator": "civic_stack_assurance.validator.v1",
        "fixture_file": str(path.relative_to(ROOT)),
        "passed": overall_pass,
        "fixture_count": len(fixture_set.get("fixtures", [])),
        "observed_civic_layers": sorted(observed_layers),
        "observed_decision_targets": sorted(observed_decision_targets),
        "observed_contribution_kinds": sorted(observed_contribution_kinds),
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
            print("PASS: civic-stack assurance fixtures")
        else:
            print("FAIL: civic-stack assurance fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
