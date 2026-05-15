from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "cybernetic-governance"
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_dependency_control.py"
FIXTURE = ROOT / "tests" / "fixtures" / "dependency-control" / "dependency-control-fixtures.synthetic.json"

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

REQUIRED_CATEGORIES = {
    "local-control-affects-one-downstream-observable",
    "local-control-blocked-by-authority-boundary",
    "dependency-propagates-through-subagent-delegation",
    "dependency-propagates-through-transport-channel",
    "duplicated-policy-paths-cancel-or-normalize",
    "release-compensation-hides-behavioral-delta",
    "blocked-dependency-branch-preserved-off-history",
    "monitor-evidence-closes-loop-by-changing-future-control-scope",
}

REQUIRED_ANSWER_FIELDS = {
    "what_can_affect_what",
    "what_was_observed",
    "partition_hidden",
    "shared_control_ancestry",
    "cancellation_or_normalization",
    "feedback_closure",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator() -> dict:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def test_dependency_control_schemas_are_valid_draft_2020_12() -> None:
    for schema_name in SCHEMA_FILES:
        schema = load_json(SCHEMA_DIR / schema_name)
        Draft202012Validator.check_schema(schema)


def test_dependency_control_fixture_validator_passes() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["fixture_count"] == 8
    assert all(result["passed"] for result in payload["results"])


def test_dependency_control_fixture_categories_are_complete() -> None:
    payload = run_validator()
    observed = {result["category"] for result in payload["results"]}
    assert REQUIRED_CATEGORIES <= observed


def test_dependency_control_fixture_answers_all_calculus_questions() -> None:
    payload = run_validator()
    for result in payload["results"]:
        assert REQUIRED_ANSWER_FIELDS <= set(result["answers"])
        assert result["answers"]["what_can_affect_what"]
        assert result["answers"]["what_was_observed"]
        assert "evidence_receipt_refs" in result
        assert result["evidence_receipt_refs"]


def test_dependency_control_output_maps_to_safety_cases_when_required() -> None:
    payload = run_validator()
    for result in payload["results"]:
        if result["target_schema"] not in {
            "transport_dependency_channel.v1.json",
            "ontology_dependency_delta.v1.json",
        }:
            assert result["safety_case_ref"], result


def test_dependency_control_schema_targets_include_core_governance_references() -> None:
    graph_schema_text = (SCHEMA_DIR / "dependency_control_graph.v1.json").read_text(encoding="utf-8")
    for expected_ref in [
        "authority_chain_refs",
        "agent_action_trace_refs",
        "tool_permission_scope_refs",
        "off_history_evidence_refs",
        "monitor_alert_refs",
        "release_delta_report_refs",
        "evidence_receipt_refs",
        "cybernetic_safety_case_ref",
        "agentplane_run_capsule_refs",
        "proof_pack_exhibit_refs",
    ]:
        assert expected_ref in graph_schema_text
