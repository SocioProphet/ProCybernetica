#!/usr/bin/env python3
"""Validate Agentic Ops CMDP/UCO/persona-policy fixtures.

This validator is repository-local. It exercises the deterministic persona ->
substrategy chooser and validates public-synthetic Agentic Ops schema records.
It does not train an RL policy, execute runtime agents, or emit production telemetry.
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
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "agentic-ops"

sys.path.insert(0, str(ROOT / "tools" / "cybernetic_governance"))
from agentic_persona_substrategy_chooser import (  # noqa: E402
    AgenticAxes,
    Budget,
    DataClass,
    Objectives,
    PersonaPolicy,
    ReversibilityClass,
    Scenario,
    WorkloadSignature,
    resolve_substrategies,
)

SCHEMA_FILES = [
    "agentic_uco_step_cost.v1.json",
    "agentic_task_budget.v1.json",
    "agentic_cmdp_trace.v1.json",
    "agentic_degradation_event.v1.json",
    "loop_detector_signal.v1.json",
    "prefix_cache_prompt_plan.v1.json",
    "agentic_post_hoc_eval.v1.json",
]

REQUIRED_PERSONAS = {
    "regulated-enterprise-assistant",
    "interactive-product-assistant",
    "batch-throughput-worker",
    "research-throughput",
    "sre-operator",
    "forensics-analyst",
}

REQUIRED_WORKLOADS = {
    "workload:single-shot-public",
    "workload:regulated-plan-then-execute",
    "workload:react-exploration-public",
    "workload:multi-agent-internal",
    "workload:long-horizon-internal",
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


def persona_from_fixture(record: dict[str, Any]) -> PersonaPolicy:
    objectives = Objectives(**record["objectives"])
    budget = Budget(**record["budget"])
    axes_record = record["axes"]
    axes = AgenticAxes(
        autonomy_depth=axes_record["autonomy_depth"],
        reversibility=ReversibilityClass(axes_record["reversibility"]),
        plan_mode=axes_record["plan_mode"],
        max_replans=axes_record["max_replans"],
        verification_judge_rate=axes_record["verification_judge_rate"],
        self_consistency_k=axes_record["self_consistency_k"],
        cascade_enabled=axes_record["cascade_enabled"],
    )
    return PersonaPolicy(
        persona_id=record["persona_id"],
        objectives=objectives,
        budget=budget,
        axes=axes,
        data_class_allowlist={DataClass(value) for value in record["data_class_allowlist"]},
        max_staleness_seconds=record["max_staleness_seconds"],
    )


def workload_from_fixture(record: dict[str, Any]) -> WorkloadSignature:
    return WorkloadSignature(
        scenario=Scenario(record["scenario"]),
        data_class=DataClass(record["data_class"]),
        expected_trajectory_length=record["expected_trajectory_length"],
        expected_tool_calls=record["expected_tool_calls"],
        read_write_ratio=record["read_write_ratio"],
        hotness_skew=record["hotness_skew"],
        sensitivity_class=DataClass(record["sensitivity_class"]),
    )


def schema_record_results(schemas: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    fixture = load_json(FIXTURE_DIR / "agentic-ops-schema-records.synthetic.json")
    results = []
    for record in fixture["records"]:
        schema = schemas[record["target_schema"]]
        errors = [error.message for error in Draft202012Validator(schema).iter_errors(record["payload"])]
        expected_result = record["expected_result"]
        actual_result = "fail" if errors else "pass"
        results.append(
            {
                "fixture_id": record["fixture_id"],
                "target_schema": record["target_schema"],
                "expected_result": expected_result,
                "actual_result": actual_result,
                "passed": expected_result == actual_result,
                "diagnostics": errors,
            }
        )
    return results


def validate_personas() -> tuple[dict[str, PersonaPolicy], list[dict[str, Any]]]:
    fixture = load_json(FIXTURE_DIR / "persona-policies.synthetic.json")
    results = []
    personas: dict[str, PersonaPolicy] = {}

    for record in fixture["personas"]:
        persona = persona_from_fixture(record)
        personas[persona.persona_id] = persona
        results.append({"fixture_id": record["persona_id"], "passed": True, "diagnostics": []})

    for record in fixture.get("invalid_personas", []):
        try:
            persona_from_fixture(record)
        except ValueError as exc:
            expected = record.get("expected_error", "")
            results.append(
                {
                    "fixture_id": record["persona_id"],
                    "passed": expected in str(exc),
                    "diagnostics": [str(exc)],
                }
            )
        else:
            results.append(
                {
                    "fixture_id": record["persona_id"],
                    "passed": False,
                    "diagnostics": ["invalid persona unexpectedly accepted"],
                }
            )

    return personas, results


def validate_workloads() -> tuple[dict[str, WorkloadSignature], list[dict[str, Any]]]:
    fixture = load_json(FIXTURE_DIR / "workload-signatures.synthetic.json")
    workloads = {record["workload_id"]: workload_from_fixture(record) for record in fixture["workloads"]}
    results = [{"fixture_id": workload_id, "passed": True, "diagnostics": []} for workload_id in workloads]
    return workloads, results


def chooser_results(personas: dict[str, PersonaPolicy], workloads: dict[str, WorkloadSignature]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    regulated_result = resolve_substrategies(
        personas["regulated-enterprise-assistant"],
        workloads["workload:regulated-plan-then-execute"],
    )
    required_regulated = {
        "plan_commit_before_execute",
        "llm_judge_every_output",
        "self_consistency_k_3_majority",
        "two_phase_commit_with_compensating_actions",
        "immutable_append_only_trajectory_log",
        "trajectory_hash_chain",
        "per_data_class_memory_isolation",
        "per_step_uco_attribution_emit",
    }
    checks.append(
        {
            "check_id": "regulated-persona-plan-stable-audit-heavy-verification-heavy",
            "passed": regulated_result.rejection_reason is None and required_regulated <= set(regulated_result.substrategies),
            "diagnostics": [regulated_result.rejection_reason] if regulated_result.rejection_reason else [],
            "substrategies": regulated_result.substrategies,
            "rationale": regulated_result.rationale,
        }
    )

    research_reject = resolve_substrategies(
        personas["research-throughput"],
        workloads["workload:regulated-plan-then-execute"],
    )
    checks.append(
        {
            "check_id": "research-persona-rejects-regulated-data",
            "passed": research_reject.rejection_reason is not None and "regulated" in research_reject.rejection_reason,
            "diagnostics": [research_reject.rejection_reason],
        }
    )

    overflow = resolve_substrategies(
        personas["regulated-enterprise-assistant"],
        workloads["workload:budget-overflow-tool-calls"],
    )
    checks.append(
        {
            "check_id": "budget-overflow-produces-deterministic-rejection",
            "passed": overflow.rejection_reason is not None and "expected tool calls" in overflow.rejection_reason,
            "diagnostics": [overflow.rejection_reason],
        }
    )

    long_horizon = resolve_substrategies(
        personas["research-throughput"],
        workloads["workload:long-horizon-internal"],
    )
    checks.append(
        {
            "check_id": "prefix-cache-selected-for-long-trajectories",
            "passed": long_horizon.rejection_reason is None and "prefix_cache_with_section_breakpoints" in long_horizon.substrategies,
            "diagnostics": [long_horizon.rejection_reason] if long_horizon.rejection_reason else [],
            "substrategies": long_horizon.substrategies,
            "rationale": long_horizon.rationale,
        }
    )

    loop_strategy = "loop_detector_repeated_args_threshold_3"
    checks.append(
        {
            "check_id": "loop-detector-threshold-derived-from-autonomy-depth",
            "passed": loop_strategy in regulated_result.substrategies and "autonomy depth" in regulated_result.rationale.get("loop_detector", ""),
            "diagnostics": [],
            "substrategies": regulated_result.substrategies,
            "rationale": regulated_result.rationale,
        }
    )

    repeat_result = resolve_substrategies(
        personas["regulated-enterprise-assistant"],
        workloads["workload:regulated-plan-then-execute"],
    )
    checks.append(
        {
            "check_id": "same-persona-workload-output-is-deterministic",
            "passed": repeat_result.substrategies == regulated_result.substrategies and repeat_result.rationale == regulated_result.rationale,
            "diagnostics": [],
        }
    )

    interactive_result = resolve_substrategies(
        personas["interactive-product-assistant"],
        workloads["workload:single-shot-public"],
    )
    checks.append(
        {
            "check_id": "interactive-persona-valid-public-single-shot",
            "passed": interactive_result.rejection_reason is None,
            "diagnostics": [interactive_result.rejection_reason] if interactive_result.rejection_reason else [],
            "substrategies": interactive_result.substrategies,
        }
    )

    return checks


def validate() -> dict[str, Any]:
    schemas = load_schemas()
    schema_results = schema_record_results(schemas)
    personas, persona_results = validate_personas()
    workloads, workload_results = validate_workloads()
    chooser = chooser_results(personas, workloads)

    required_personas_present = REQUIRED_PERSONAS <= set(personas)
    required_workloads_present = REQUIRED_WORKLOADS <= set(workloads)

    all_results = schema_results + persona_results + workload_results + chooser
    passed = (
        required_personas_present
        and required_workloads_present
        and all(result.get("passed") for result in all_results)
        and {result["target_schema"] for result in schema_results} == set(SCHEMA_FILES)
    )
    return {
        "validator": "agentic_ops_cmdp.validator.v1",
        "passed": passed,
        "schema_record_count": len(schema_results),
        "persona_count": len(personas),
        "workload_count": len(workloads),
        "required_personas_present": required_personas_present,
        "required_workloads_present": required_workloads_present,
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
            print("PASS: agentic ops fixtures")
        else:
            print("FAIL: agentic ops fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
