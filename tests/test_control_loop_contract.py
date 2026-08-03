"""Teeth for the Governed Closed-Loop Control Contract.

Each test is a constitutional tooth on the ControlLoop record (contract:
contracts/control-loop.schema.json). The loop seats under ControlNodes #124 and the
RCS/4D ADR-0003 (prophet-workspace#113): sense -> model -> judge -> act -> receipt.
The contract is measurement/design only; nothing here executes a remediation.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.cybernetic_governance.validate_control_loop import (
    R_JUDGE_DENIED_BUT_FIRED,
    R_NO_AUDIT_RECEIPT_ON_FIRED,
    R_NO_VALUE_JUDGMENT_GATE,
    R_SPURIOUS_ACTION,
    R_UNCONSTITUTIONAL_OBJECTIVE,
    _schema_validator,
    evaluate_control_loop,
    run,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "control-loop"


def _load(name: str) -> dict:
    return json.loads((FIXTURE_DIR / name).read_text(encoding="utf-8"))


def test_fixture_suite_all_teeth_hold() -> None:
    """The whole declared expectation suite must pass (self-validating checker)."""
    report = run()
    assert report["ok"], report["failed"]
    # Guard against a suite that silently shrinks to nothing.
    assert report["total"] >= 7


def test_closed_loop_verifies() -> None:
    verdict = evaluate_control_loop(_load("accept_closed_loop.json"))
    assert verdict["admissible"] is True, verdict["reasons"]


def test_loop_with_no_value_judgment_gate_is_rejected() -> None:
    verdict = evaluate_control_loop(_load("reject_no_value_judgment.json"))
    assert verdict["admissible"] is False
    assert R_NO_VALUE_JUDGMENT_GATE in verdict["reasons"]


def test_fired_remediation_without_audit_receipt_is_rejected() -> None:
    verdict = evaluate_control_loop(_load("reject_fired_no_receipt.json"))
    assert verdict["admissible"] is False
    assert R_NO_AUDIT_RECEIPT_ON_FIRED in verdict["reasons"]


def test_control_max_objective_is_rejected_crown_k1() -> None:
    verdict = evaluate_control_loop(_load("reject_control_max_objective.json"))
    assert verdict["admissible"] is False
    assert R_UNCONSTITUTIONAL_OBJECTIVE in verdict["reasons"]


def test_remediation_fired_without_threshold_cross_is_rejected() -> None:
    verdict = evaluate_control_loop(_load("reject_spurious_action.json"))
    assert verdict["admissible"] is False
    assert R_SPURIOUS_ACTION in verdict["reasons"]


def test_remediation_fired_after_judge_denied_is_rejected() -> None:
    verdict = evaluate_control_loop(_load("reject_judge_denied_but_fired.json"))
    assert verdict["admissible"] is False
    assert R_JUDGE_DENIED_BUT_FIRED in verdict["reasons"]


def test_monitor_only_below_threshold_is_admissible() -> None:
    """A passive monitor loop that does not act must not be over-rejected."""
    verdict = evaluate_control_loop(_load("accept_monitor_only_not_fired.json"))
    assert verdict["admissible"] is True, verdict["reasons"]


def test_evaluation_is_deterministic() -> None:
    """Same record -> identical verdict (no ordering nondeterminism)."""
    validator = _schema_validator()
    record = _load("accept_closed_loop.json")
    first = evaluate_control_loop(record, validator)
    second = evaluate_control_loop(record, validator)
    assert first == second


@pytest.mark.parametrize(
    "unconstitutional_kind", ["control-max", "domination", "unbounded-optimization"]
)
def test_all_domination_objective_kinds_are_rejected(unconstitutional_kind: str) -> None:
    record = _load("accept_closed_loop.json")
    record["objective"]["objective_kind"] = unconstitutional_kind
    verdict = evaluate_control_loop(record)
    assert verdict["admissible"] is False
    assert R_UNCONSTITUTIONAL_OBJECTIVE in verdict["reasons"]
