#!/usr/bin/env python3
"""Validate cybernetic-governance defensive fixtures.

This validator is repository-local and public-safe. It validates synthetic fixture
shape and cross-field governance invariants. It does not implement runtime gates,
live policy enforcement, production telemetry, SHACL, or Rego.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, RefResolver

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "cybernetic-governance"
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "cybernetic-governance" / "defensive-fixtures.synthetic.json"

REQUIRED_FIXTURE_FIELDS = {
    "fixture_id",
    "category",
    "target_schema",
    "expected_result",
    "invariant_refs",
    "payload",
}

EXPECTED_FAILURE_REASONS = {
    "schema_validation_error",
    "hidden_release_compensation",
    "missing_off_history_evidence",
    "private_evidence_requires_redaction_ref",
    "high_authority_concentration_requires_mitigation",
}

SCHEMA_FILES = [
    "agent_action_trace.v1.json",
    "authority_chain.v1.json",
    "authority_graph_snapshot.v1.json",
    "cybernetic_safety_case.v1.json",
    "environment_delta.v1.json",
    "evidence_receipt.v1.json",
    "incident_record.v1.json",
    "instruction_conflict_case.v1.json",
    "meta_monitor_report.v1.json",
    "monitor_alert.v1.json",
    "off_history_evidence.v1.json",
    "privacy_evidence_classification.v1.json",
    "promotion_decision.v1.json",
    "release_delta_report.v1.json",
    "side_effect_assessment.v1.json",
    "tool_permission_scope.v1.json",
]


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing file: {path}") from None
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from None


def load_schemas() -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    store: dict[str, Any] = {}

    enums = load_json(SCHEMA_DIR / "enums.v1.json")
    Draft202012Validator.check_schema(enums)
    store["enums.v1.json"] = enums
    store[enums["$id"]] = enums

    for name in SCHEMA_FILES:
        schema = load_json(SCHEMA_DIR / name)
        Draft202012Validator.check_schema(schema)
        schemas[name] = schema
        store[name] = schema
        store[schema["$id"]] = schema

    return schemas, store


def schema_errors(schema: dict[str, Any], store: dict[str, Any], payload: dict[str, Any]) -> list[str]:
    resolver = RefResolver.from_schema(schema, store=store)
    validator = Draft202012Validator(schema, resolver=resolver)
    return [error.message for error in sorted(validator.iter_errors(payload), key=str)]


def custom_failures(fixture: dict[str, Any]) -> list[str]:
    payload = fixture["payload"]
    category = fixture["category"]
    failures: list[str] = []

    if category == "hidden-release-compensation":
        if (
            payload.get("gate_color") == "green"
            and payload.get("non_renormalizable_change") is True
            and not payload.get("counter_term_refs")
        ):
            failures.append("hidden_release_compensation")

    if category == "missing-off-history-evidence":
        material_classes = {
            "externally_visible",
            "irreversible",
            "legally_material",
            "financially_material",
            "privacy_material",
            "security_material",
            "physical_world_material",
        }
        if payload.get("side_effect_class") in material_classes and not payload.get("off_history_evidence_ref"):
            failures.append("missing_off_history_evidence")

    if category == "publication-boundary-enforcement":
        if payload.get("disclosure_class") in {"private", "sealed", "privileged", "sensitive_ops"} and not payload.get("redaction_ref"):
            failures.append("private_evidence_requires_redaction_ref")

    if category == "high-authority-concentration-snapshots":
        if (
            float(payload.get("authority_concentration_index", 0)) >= 0.8
            and payload.get("separation_of_powers_status") == "violated"
            and not payload.get("mitigation_refs")
        ):
            failures.append("high_authority_concentration_requires_mitigation")

    return failures


def validate_fixture_set(path: Path) -> dict[str, Any]:
    schemas, store = load_schemas()
    fixture_set = load_json(path)

    results: list[dict[str, Any]] = []
    overall_pass = True

    for fixture in fixture_set.get("fixtures", []):
        fixture_id = fixture.get("fixture_id", "<missing>")
        missing = REQUIRED_FIXTURE_FIELDS - set(fixture)
        if missing:
            overall_pass = False
            results.append(
                {
                    "fixture_id": fixture_id,
                    "expected_result": fixture.get("expected_result"),
                    "actual_result": "fail",
                    "passed": False,
                    "diagnostics": [f"missing fixture fields: {sorted(missing)}"],
                }
            )
            continue

        target_schema = fixture["target_schema"]
        expected_result = fixture["expected_result"]
        if expected_result not in {"pass", "fail"}:
            overall_pass = False
            results.append(
                {
                    "fixture_id": fixture_id,
                    "expected_result": expected_result,
                    "actual_result": "fail",
                    "passed": False,
                    "diagnostics": ["expected_result must be pass or fail"],
                }
            )
            continue

        if target_schema not in schemas:
            overall_pass = False
            results.append(
                {
                    "fixture_id": fixture_id,
                    "expected_result": expected_result,
                    "actual_result": "fail",
                    "passed": False,
                    "diagnostics": [f"unknown target_schema: {target_schema}"],
                }
            )
            continue

        if not isinstance(fixture.get("invariant_refs"), list) or not fixture["invariant_refs"]:
            overall_pass = False
            results.append(
                {
                    "fixture_id": fixture_id,
                    "expected_result": expected_result,
                    "actual_result": "fail",
                    "passed": False,
                    "diagnostics": ["invariant_refs must be non-empty"],
                }
            )
            continue

        payload = fixture["payload"]
        schema_failure_messages = schema_errors(schemas[target_schema], store, payload)
        custom_failure_reasons = custom_failures(fixture)
        all_failures = []
        if schema_failure_messages:
            all_failures.append("schema_validation_error")
        all_failures.extend(custom_failure_reasons)

        actual_result = "fail" if all_failures else "pass"
        expected_failure_reason = fixture.get("expected_failure_reason")
        passed = actual_result == expected_result
        diagnostics: list[str] = []

        if expected_result == "fail":
            if expected_failure_reason not in EXPECTED_FAILURE_REASONS:
                passed = False
                diagnostics.append(f"unknown or missing expected_failure_reason: {expected_failure_reason}")
            elif expected_failure_reason not in all_failures:
                passed = False
                diagnostics.append(
                    f"expected failure reason {expected_failure_reason!r} not observed; observed {all_failures}"
                )

        if expected_result == "pass" and all_failures:
            diagnostics.append(f"unexpected failures: {all_failures}")

        diagnostics.extend(schema_failure_messages)
        overall_pass = overall_pass and passed
        results.append(
            {
                "fixture_id": fixture_id,
                "category": fixture["category"],
                "target_schema": target_schema,
                "expected_result": expected_result,
                "actual_result": actual_result,
                "expected_failure_reason": expected_failure_reason,
                "observed_failures": all_failures,
                "invariant_refs": fixture["invariant_refs"],
                "passed": passed,
                "diagnostics": diagnostics,
            }
        )

    return {
        "validator": "cybernetic_governance.defensive_fixture_validator.v1",
        "fixture_file": str(path.relative_to(ROOT)),
        "passed": overall_pass,
        "fixture_count": len(fixture_set.get("fixtures", [])),
        "results": results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON only")
    args = parser.parse_args(argv)

    result = validate_fixture_set(args.fixture)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(json.dumps(result, indent=2, sort_keys=True))
        if result["passed"]:
            print("PASS: cybernetic governance defensive fixtures")
        else:
            print("FAIL: cybernetic governance defensive fixtures", file=sys.stderr)

    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
