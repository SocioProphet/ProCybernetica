#!/usr/bin/env python3
"""Validate Sovereign Validation Fabric schema fixtures.

This validator is repository-local. It validates public-synthetic SVF
schema records and checks cross-record semantic constraints for the
policy primitive. It does not execute validation actions or implement a
workspace runner.
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
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "svf" / "svf-schema-records.synthetic.json"
SEMANTIC_FIXTURE_PATH = ROOT / "tests" / "fixtures" / "svf" / "svf-semantic-records.synthetic.json"

SCHEMA_FILES = [
    "svf_validation_action.v1.json",
    "svf_validation_capability_policy.v1.json",
    "svf_validation_plan.v1.json",
    "svf_validation_run.v1.json",
    "svf_validation_receipt.v1.json",
]

PLAN_LEVEL_CLAIMS = {"receipt_integrity_verified"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schemas() -> dict[str, dict[str, Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    for name in SCHEMA_FILES:
        schema = load_json(SCHEMA_DIR / name)
        Draft202012Validator.check_schema(schema)
        schemas[name] = schema
    return schemas


def schema_record_results(schemas: dict[str, dict[str, Any]], fixture: dict[str, Any]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for record in fixture["records"]:
        target_schema = record["target_schema"]
        schema = schemas[target_schema]
        errors = sorted(
            Draft202012Validator(schema).iter_errors(record["payload"]),
            key=lambda error: list(error.absolute_path),
        )
        diagnostics = [f"/{'/'.join(str(part) for part in error.absolute_path)}: {error.message}" for error in errors]
        expected_result = record["expected_result"]
        actual_result = "fail" if errors else "pass"
        results.append(
            {
                "fixture_id": record["fixture_id"],
                "target_schema": target_schema,
                "expected_result": expected_result,
                "actual_result": actual_result,
                "passed": expected_result == actual_result,
                "diagnostics": diagnostics,
            }
        )
    return results


def passing_payloads_by_schema(fixture: dict[str, Any], schema_name: str) -> list[dict[str, Any]]:
    return [
        record["payload"]
        for record in fixture["records"]
        if record["target_schema"] == schema_name and record["expected_result"] == "pass"
    ]


def collect_semantic_checks(actions: dict[str, Any], policies: dict[str, Any], plans: dict[str, Any], runs: dict[str, Any], receipts: list[dict[str, Any]], prefix: str = "") -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    for plan_id, plan in plans.items():
        missing_actions = [step["action_ref"] for step in plan["actions"] if step["action_ref"] not in actions]
        policy_missing = plan["policy_ref"] not in policies
        checks.append(
            {
                "check_id": f"{prefix}plan-refs-resolve:{plan_id}",
                "passed": not missing_actions and not policy_missing,
                "diagnostics": [
                    *(f"missing action ref {action_ref}" for action_ref in missing_actions),
                    *([f"missing policy ref {plan['policy_ref']}"] if policy_missing else []),
                ],
            }
        )

        action_claim_sets = [set(actions[step["action_ref"]]["claim_scopes"]) for step in plan["actions"] if step["action_ref"] in actions]
        supported_by_actions = set().union(*action_claim_sets) if action_claim_sets else set()
        allowed_plan_claims = supported_by_actions | PLAN_LEVEL_CLAIMS
        unsupported_plan_claims = sorted(set(plan["claim_scopes"]) - allowed_plan_claims)
        checks.append(
            {
                "check_id": f"{prefix}plan-claims-supported:{plan_id}",
                "passed": not unsupported_plan_claims,
                "diagnostics": [f"plan claim not supported by any action or plan-level verifier: {claim}" for claim in unsupported_plan_claims],
            }
        )

    for run_id, run in runs.items():
        plan = plans.get(run["plan_ref"])
        policy_missing = run["policy_ref"] not in policies
        plan_missing = plan is None
        step_refs = {step["action_ref"] for step in plan["actions"]} if plan else set()
        unexpected_action_results = [
            result["action_ref"] for result in run["action_results"] if result["action_ref"] not in step_refs
        ]
        checks.append(
            {
                "check_id": f"{prefix}run-refs-resolve:{run_id}",
                "passed": not plan_missing and not policy_missing and not unexpected_action_results,
                "diagnostics": [
                    *([f"missing plan ref {run['plan_ref']}"] if plan_missing else []),
                    *([f"missing policy ref {run['policy_ref']}"] if policy_missing else []),
                    *(f"action result not declared by plan: {action_ref}" for action_ref in unexpected_action_results),
                ],
            }
        )

    for receipt in receipts:
        receipt_id = receipt["receipt_id"]
        plan = plans.get(receipt["plan_ref"])
        run = runs.get(receipt["run_ref"])
        policy_missing = receipt["policy_ref"] not in policies
        plan_missing = plan is None
        run_missing = run is None
        unsupported_claims = sorted(set(receipt["certified_claims"]) - set(plan["claim_scopes"])) if plan else []
        checks.append(
            {
                "check_id": f"{prefix}receipt-refs-and-claims:{receipt_id}",
                "passed": not plan_missing and not run_missing and not policy_missing and not unsupported_claims,
                "diagnostics": [
                    *([f"missing plan ref {receipt['plan_ref']}"] if plan_missing else []),
                    *([f"missing run ref {receipt['run_ref']}"] if run_missing else []),
                    *([f"missing policy ref {receipt['policy_ref']}"] if policy_missing else []),
                    *(f"receipt claim not declared by plan: {claim}" for claim in unsupported_claims),
                ],
            }
        )

    return checks


def semantic_results(fixture: dict[str, Any]) -> list[dict[str, Any]]:
    actions = {
        payload["action_id"]: payload
        for payload in passing_payloads_by_schema(fixture, "svf_validation_action.v1.json")
    }
    policies = {
        payload["policy_id"]: payload
        for payload in passing_payloads_by_schema(fixture, "svf_validation_capability_policy.v1.json")
    }
    plans = {
        payload["plan_id"]: payload
        for payload in passing_payloads_by_schema(fixture, "svf_validation_plan.v1.json")
    }
    runs = {
        payload["run_id"]: payload
        for payload in passing_payloads_by_schema(fixture, "svf_validation_run.v1.json")
    }
    receipts = passing_payloads_by_schema(fixture, "svf_validation_receipt.v1.json")
    return collect_semantic_checks(actions, policies, plans, runs, receipts)


def validate_payload(schema: dict[str, Any], payload: dict[str, Any]) -> list[str]:
    errors = sorted(Draft202012Validator(schema).iter_errors(payload), key=lambda error: list(error.absolute_path))
    return [f"/{'/'.join(str(part) for part in error.absolute_path)}: {error.message}" for error in errors]


def semantic_fixture_results(schemas: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    if not SEMANTIC_FIXTURE_PATH.exists():
        return [{"check_id": "semantic-fixture-file-present", "passed": False, "diagnostics": [str(SEMANTIC_FIXTURE_PATH)]}]

    fixture = load_json(SEMANTIC_FIXTURE_PATH)
    results: list[dict[str, Any]] = []
    for record in fixture["semantic_records"]:
        fixture_id = record["fixture_id"]
        schema_errors: list[str] = []
        for payload in record.get("actions", []):
            schema_errors.extend(validate_payload(schemas["svf_validation_action.v1.json"], payload))
        for payload in record.get("policies", []):
            schema_errors.extend(validate_payload(schemas["svf_validation_capability_policy.v1.json"], payload))
        for payload in record.get("plans", []):
            schema_errors.extend(validate_payload(schemas["svf_validation_plan.v1.json"], payload))
        for payload in record.get("runs", []):
            schema_errors.extend(validate_payload(schemas["svf_validation_run.v1.json"], payload))
        for payload in record.get("receipts", []):
            schema_errors.extend(validate_payload(schemas["svf_validation_receipt.v1.json"], payload))

        if schema_errors:
            results.append(
                {
                    "check_id": f"semantic-fixture-schema-valid:{fixture_id}",
                    "expected_result": record["expected_result"],
                    "actual_result": "schema_fail",
                    "passed": False,
                    "diagnostics": schema_errors,
                }
            )
            continue

        actions = {payload["action_id"]: payload for payload in record.get("actions", [])}
        policies = {payload["policy_id"]: payload for payload in record.get("policies", [])}
        plans = {payload["plan_id"]: payload for payload in record.get("plans", [])}
        runs = {payload["run_id"]: payload for payload in record.get("runs", [])}
        checks = collect_semantic_checks(actions, policies, plans, runs, record.get("receipts", []), prefix=f"{fixture_id}:")
        actual_result = "pass" if all(check["passed"] for check in checks) else "fail"
        results.append(
            {
                "check_id": f"semantic-fixture-expected-result:{fixture_id}",
                "expected_result": record["expected_result"],
                "actual_result": actual_result,
                "passed": actual_result == record["expected_result"],
                "diagnostics": [diagnostic for check in checks if not check["passed"] for diagnostic in check["diagnostics"]],
            }
        )
    return results


def validate() -> dict[str, Any]:
    schemas = load_schemas()
    fixture = load_json(FIXTURE_PATH)
    schema_results = schema_record_results(schemas, fixture)
    semantic = semantic_results(fixture)
    semantic_fixtures = semantic_fixture_results(schemas)
    expected_schema_coverage = {record["target_schema"] for record in fixture["records"]}
    all_results = schema_results + semantic + semantic_fixtures
    passed = (
        expected_schema_coverage == set(SCHEMA_FILES)
        and all(result.get("passed") for result in all_results)
    )
    return {
        "validator": "svf_schema_fixtures.validator.v1",
        "passed": passed,
        "schema_record_count": len(schema_results),
        "semantic_check_count": len(semantic),
        "semantic_fixture_count": len(semantic_fixtures),
        "schema_coverage": sorted(expected_schema_coverage),
        "results": all_results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = validate()
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: svf schema fixtures")
        else:
            print("FAIL: svf schema fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
