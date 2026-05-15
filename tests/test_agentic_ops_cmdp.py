from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "cybernetic-governance"
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_agentic_ops.py"

SCHEMA_FILES = {
    "agentic_uco_step_cost.v1.json",
    "agentic_task_budget.v1.json",
    "agentic_cmdp_trace.v1.json",
    "agentic_degradation_event.v1.json",
    "loop_detector_signal.v1.json",
    "prefix_cache_prompt_plan.v1.json",
    "agentic_post_hoc_eval.v1.json",
}

REQUIRED_PERSONAS = {
    "regulated-enterprise-assistant",
    "interactive-product-assistant",
    "batch-throughput-worker",
    "research-throughput",
    "sre-operator",
    "forensics-analyst",
}

REQUIRED_CHECKS = {
    "regulated-persona-plan-stable-audit-heavy-verification-heavy",
    "research-persona-rejects-regulated-data",
    "budget-overflow-produces-deterministic-rejection",
    "prefix-cache-selected-for-long-trajectories",
    "loop-detector-threshold-derived-from-autonomy-depth",
    "same-persona-workload-output-is-deterministic",
    "interactive-persona-valid-public-single-shot",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator() -> dict:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def test_agentic_ops_schemas_are_valid_draft_2020_12() -> None:
    for schema_name in SCHEMA_FILES:
        Draft202012Validator.check_schema(load_json(SCHEMA_DIR / schema_name))


def test_agentic_ops_validator_passes() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["schema_record_count"] == 7
    assert payload["persona_count"] == 6
    assert payload["workload_count"] == 6
    assert payload["required_personas_present"] is True
    assert payload["required_workloads_present"] is True


def test_agentic_ops_schema_record_coverage_is_complete() -> None:
    payload = run_validator()
    observed_targets = {
        result["target_schema"]
        for result in payload["results"]
        if "target_schema" in result
    }
    assert observed_targets == SCHEMA_FILES


def test_required_persona_and_chooser_checks_pass() -> None:
    payload = run_validator()
    result_ids = {result.get("fixture_id") or result.get("check_id") for result in payload["results"]}
    assert REQUIRED_PERSONAS <= result_ids
    assert REQUIRED_CHECKS <= result_ids

    by_id = {result.get("fixture_id") or result.get("check_id"): result for result in payload["results"]}
    for check_id in REQUIRED_CHECKS:
        assert by_id[check_id]["passed"] is True


def test_regulated_persona_resolves_to_plan_stable_audit_heavy_verification_heavy() -> None:
    payload = run_validator()
    check = next(
        result for result in payload["results"]
        if result.get("check_id") == "regulated-persona-plan-stable-audit-heavy-verification-heavy"
    )
    strategies = set(check["substrategies"])
    assert "plan_commit_before_execute" in strategies
    assert "llm_judge_every_output" in strategies
    assert "self_consistency_k_3_majority" in strategies
    assert "immutable_append_only_trajectory_log" in strategies
    assert "trajectory_hash_chain" in strategies
    assert "per_step_uco_attribution_emit" in strategies


def test_rejections_and_determinism_are_recorded() -> None:
    payload = run_validator()
    by_id = {result.get("fixture_id") or result.get("check_id"): result for result in payload["results"]}
    assert "objective weights must sum to 1.0" in by_id["invalid-objective-sum"]["diagnostics"][0]
    assert "regulated" in by_id["research-persona-rejects-regulated-data"]["diagnostics"][0]
    assert "expected tool calls" in by_id["budget-overflow-produces-deterministic-rejection"]["diagnostics"][0]
    assert by_id["same-persona-workload-output-is-deterministic"]["passed"] is True


def test_prefix_cache_and_loop_detector_rationale_are_recorded() -> None:
    payload = run_validator()
    by_id = {result.get("fixture_id") or result.get("check_id"): result for result in payload["results"]}
    prefix = by_id["prefix-cache-selected-for-long-trajectories"]
    assert "prefix_cache_with_section_breakpoints" in prefix["substrategies"]

    loop = by_id["loop-detector-threshold-derived-from-autonomy-depth"]
    assert "loop_detector_repeated_args_threshold_3" in loop["substrategies"]
    assert "autonomy depth" in loop["rationale"]["loop_detector"]
