#!/usr/bin/env python3
"""Validate dependency-control calculus fixtures.

This validator is structural and repository-local. It answers the dependency-control
questions from QUANTUM_CYBERNETIC_DEPENDENCE_CALCULUS.md without claiming quantum
hardware, live runtime behavior, or production governance enforcement.
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
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "dependency-control" / "dependency-control-fixtures.synthetic.json"

SCHEMA_FILES = [
    "dependency_control_graph.v1.json",
    "control_reachability_record.v1.json",
    "observability_partition.v1.json",
    "shared_dependency_ancestry.v1.json",
    "dependency_cancellation_record.v1.json",
    "adaptive_feedback_loop.v1.json",
    "transport_dependency_channel.v1.json",
    "ontology_dependency_delta.v1.json",
]

REQUIRED_ANSWER_FIELDS = {
    "what_can_affect_what",
    "what_was_observed",
    "partition_hidden",
    "shared_control_ancestry",
    "cancellation_or_normalization",
    "feedback_closure",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schemas() -> dict[str, dict[str, Any]]:
    schemas = {}
    for name in SCHEMA_FILES:
        schema = load_json(SCHEMA_DIR / name)
        Draft202012Validator.check_schema(schema)
        schemas[name] = schema
    return schemas


def schema_errors(schema: dict[str, Any], payload: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    return [error.message for error in sorted(validator.iter_errors(payload), key=str)]


def validate_fixture_set(path: Path) -> dict[str, Any]:
    schemas = load_schemas()
    fixture_set = load_json(path)
    results = []
    overall_pass = True

    for fixture in fixture_set.get("fixtures", []):
        fixture_id = fixture.get("fixture_id", "<missing>")
        target_schema = fixture.get("target_schema")
        expected_result = fixture.get("expected_result")
        answers = fixture.get("answers", {})
        payload = fixture.get("payload", {})
        diagnostics = []

        missing_answer_fields = REQUIRED_ANSWER_FIELDS - set(answers)
        if missing_answer_fields:
            diagnostics.append(f"missing answer fields: {sorted(missing_answer_fields)}")

        if target_schema not in schemas:
            diagnostics.append(f"unknown target schema: {target_schema}")
            schema_failure = True
        else:
            schema_messages = schema_errors(schemas[target_schema], payload)
            schema_failure = bool(schema_messages)
            diagnostics.extend(schema_messages)

        if not payload.get("evidence_receipt_refs"):
            diagnostics.append("payload must map to evidence_receipt_refs")

        if not payload.get("safety_case_ref") and target_schema not in {"transport_dependency_channel.v1.json", "ontology_dependency_delta.v1.json"}:
            diagnostics.append("payload must map to safety_case_ref")

        actual_result = "fail" if diagnostics else "pass"
        passed = actual_result == expected_result
        overall_pass = overall_pass and passed

        results.append(
            {
                "fixture_id": fixture_id,
                "category": fixture.get("category"),
                "target_schema": target_schema,
                "expected_result": expected_result,
                "actual_result": actual_result,
                "passed": passed,
                "answers": answers,
                "evidence_receipt_refs": payload.get("evidence_receipt_refs", []),
                "safety_case_ref": payload.get("safety_case_ref"),
                "diagnostics": diagnostics,
            }
        )

    return {
        "validator": "dependency_control_calculus.validator.v1",
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
            print("PASS: dependency-control fixtures")
        else:
            print("FAIL: dependency-control fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
