"""Tests for the retention probe — and specifically for the rollback path.

The rollback is the whole point, so most of this file exercises it. A rollback that
has never been observed to fire is not a rollback; the note in the architecture
record was explicit that until it runs in CI the guard is decorative. This is that
CI exercise.
"""

from __future__ import annotations

import pytest

from procyber.semantic.retention_probe import (
    DEFAULT_TOLERANCE,
    IncorporationOutcome,
    ProbeError,
    Regression,
    find_regressions,
    incorporate,
)


def _apply_marker(state):
    """A trivial 'incorporation': tag the state so we can tell the two apart."""
    return {**state, "incorporated": True}


# --------------------------------------------------------------------------- #
# The rollback path — exercised, not assumed
# --------------------------------------------------------------------------- #


def test_a_regressing_incorporation_is_rolled_back():
    original = {"weights": "old"}
    scores = iter([{"retained": 1.0}, {"retained": 0.5}])

    result, outcome = incorporate(
        original, apply=_apply_marker, probe=lambda s: next(scores)
    )

    assert outcome.rolled_back is True
    assert outcome.incorporated is False
    assert result is original, "rollback must return the original object, not a rebuild"
    assert "incorporated" not in result


def test_rollback_names_the_task_that_regressed():
    scores = iter([{"a": 1.0, "b": 1.0}, {"a": 1.0, "b": 0.2}])
    _, outcome = incorporate({}, apply=_apply_marker, probe=lambda s: next(scores))
    assert [r.task for r in outcome.regressions] == ["b"]
    assert "b:" in outcome.reason


def test_the_worst_regression_is_reported_first():
    scores = iter([{"a": 1.0, "b": 1.0}, {"a": 0.9, "b": 0.1}])
    _, outcome = incorporate({}, apply=_apply_marker, probe=lambda s: next(scores))
    assert outcome.regressions[0].task == "b"


# --------------------------------------------------------------------------- #
# The pass path
# --------------------------------------------------------------------------- #


def test_a_clean_incorporation_is_kept():
    scores = iter([{"retained": 1.0}, {"retained": 1.0}])
    result, outcome = incorporate({}, apply=_apply_marker, probe=lambda s: next(scores))
    assert outcome.incorporated is True
    assert outcome.rolled_back is False
    assert result["incorporated"] is True


def test_improvement_on_a_retained_task_is_not_a_regression():
    scores = iter([{"retained": 0.5}, {"retained": 0.9}])
    _, outcome = incorporate({}, apply=_apply_marker, probe=lambda s: next(scores))
    assert outcome.incorporated is True


def test_loss_within_tolerance_is_kept():
    scores = iter([{"retained": 1.0}, {"retained": 1.0 - DEFAULT_TOLERANCE / 2}])
    _, outcome = incorporate({}, apply=_apply_marker, probe=lambda s: next(scores))
    assert outcome.incorporated is True


def test_the_tolerance_is_the_actual_boundary():
    """Pin the threshold, not merely that something somewhere reverts."""
    inside = iter([{"t": 1.0}, {"t": 1.0 - DEFAULT_TOLERANCE}])
    _, kept = incorporate({}, apply=_apply_marker, probe=lambda s: next(inside))
    assert kept.incorporated is True

    outside = iter([{"t": 1.0}, {"t": 1.0 - DEFAULT_TOLERANCE * 2}])
    _, reverted = incorporate({}, apply=_apply_marker, probe=lambda s: next(outside))
    assert reverted.rolled_back is True


def test_a_stricter_tolerance_reverts_what_the_default_keeps():
    def run(tol):
        scores = iter([{"t": 1.0}, {"t": 0.99}])
        return incorporate({}, apply=_apply_marker, probe=lambda s: next(scores), tolerance=tol)[1]

    assert run(DEFAULT_TOLERANCE).incorporated is True
    assert run(0.001).rolled_back is True


# --------------------------------------------------------------------------- #
# Refusals — the ways a probe fails to support a decision
# --------------------------------------------------------------------------- #


def test_an_empty_probe_refuses_rather_than_clearing():
    """An empty probe would clear everything — worse than no gate, since it looks like one."""
    original = {"weights": "old"}
    result, outcome = incorporate(original, apply=_apply_marker, probe=lambda s: {})
    assert outcome.incorporated is False
    assert outcome.rolled_back is False
    assert result is original
    assert "no retained tasks probed" in outcome.reason


def test_probes_disagreeing_on_the_task_set_raise():
    """A task that vanished between probes is a broken probe, not a clean pass."""
    scores = iter([{"a": 1.0}, {"b": 1.0}])
    with pytest.raises(ProbeError):
        incorporate({}, apply=_apply_marker, probe=lambda s: next(scores))


def test_a_task_appearing_only_after_also_raises():
    scores = iter([{"a": 1.0}, {"a": 1.0, "b": 1.0}])
    with pytest.raises(ProbeError):
        incorporate({}, apply=_apply_marker, probe=lambda s: next(scores))


# --------------------------------------------------------------------------- #
# Regression arithmetic
# --------------------------------------------------------------------------- #


def test_fraction_is_relative_to_the_prior_score():
    r = Regression(task="t", before=2.0, after=1.0)
    assert r.lost == 1.0
    assert r.fraction == 0.5


def test_a_regression_from_zero_is_infinite_not_a_crash():
    r = Regression(task="t", before=0.0, after=-1.0)
    assert r.fraction == float("inf")


def test_find_regressions_ignores_ties():
    assert find_regressions({"a": 1.0}, {"a": 1.0}) == ()


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #


def test_the_outcome_reports_what_was_probed_not_just_a_verdict():
    """The probe cannot speak for tasks it never measured, so it names the ones it did."""
    scores = iter([{"a": 1.0, "b": 1.0}, {"a": 1.0, "b": 1.0}])
    _, outcome = incorporate({}, apply=_apply_marker, probe=lambda s: next(scores))
    assert outcome.probed == ("a", "b")


def test_serialisation_carries_the_rollback_and_its_reason():
    scores = iter([{"t": 1.0}, {"t": 0.1}])
    _, outcome = incorporate({}, apply=_apply_marker, probe=lambda s: next(scores))
    payload = outcome.to_json()
    assert payload["rolledBack"] is True
    assert payload["regressions"]
    assert "rolled back" in payload["reason"]


def test_apply_is_not_called_when_there_is_nothing_to_probe():
    """No probe, no incorporation — and no side effect from a speculative apply."""
    called = []

    def apply(state):
        called.append(True)
        return state

    incorporate({}, apply=apply, probe=lambda s: {})
    assert called == []
