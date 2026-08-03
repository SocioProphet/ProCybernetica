"""Tests for the Domain-22 three-clock observability instrument.

Teeth both ways: a clean, well-aligned window must PASS, and each distinct defect (disorder,
staleness, rate divergence, phase misalignment) plus the sub-floor and degenerate cases must FAIL
with the matching reason. A gate that only ever passes is not measuring anything.
"""

from __future__ import annotations

from procyber.observability import (
    ClockSample,
    ThreeClockLimits,
    observe_three_clock,
)

PERIOD = 1.0
DT = 0.1  # 0.1 s between samples => 10 Hz


def clean(n: int = 40):
    """A perfectly aligned window: wall 0.1 s apart, causal 1:1, epoch every 1.0 s."""
    return [
        ClockSample(wall_ts=i * DT, causal_seq=i, epoch=int((i * DT) // PERIOD))
        for i in range(n)
    ]


LIMITS = ThreeClockLimits(epoch_period_s=PERIOD)


def test_clean_window_passes_with_zero_residuals():
    obs = observe_three_clock(clean(), LIMITS)
    assert obs.ok, obs.reasons
    assert obs.n == 40
    assert obs.epsilon_order == 0.0
    assert obs.epsilon_rate == 0.0
    assert obs.epsilon_phase == 0.0
    assert obs.staleness_s <= LIMITS.max_staleness_s


def test_below_floor_abstains():
    obs = observe_three_clock(clean(10), LIMITS)
    assert not obs.ok
    assert obs.epsilon_order is None  # nothing computed below the floor
    assert any("insufficient samples" in r for r in obs.reasons)


def test_non_positive_wall_span_abstains():
    samples = [ClockSample(wall_ts=5.0, causal_seq=i, epoch=0) for i in range(40)]
    obs = observe_three_clock(samples, LIMITS)
    assert not obs.ok
    assert any("non-positive wall span" in r for r in obs.reasons)


def test_ordering_disagreement_fails():
    # reverse the causal counter so wall order and causal order maximally disagree.
    samples = [
        ClockSample(wall_ts=i * DT, causal_seq=(40 - i), epoch=int((i * DT) // PERIOD))
        for i in range(40)
    ]
    obs = observe_three_clock(samples, LIMITS)
    assert not obs.ok
    assert obs.epsilon_order == 1.0  # every comparable pair discordant
    assert any("epsilon_order" in r for r in obs.reasons)


def test_staleness_fails_on_a_large_gap():
    samples = clean(40)
    # push a 10 s hole between the last two readings.
    samples[-1] = ClockSample(wall_ts=samples[-2].wall_ts + 10.0, causal_seq=39, epoch=13)
    obs = observe_three_clock(samples, ThreeClockLimits(epoch_period_s=PERIOD, max_staleness_s=5.0))
    assert not obs.ok
    assert obs.staleness_s >= 10.0
    assert any("staleness_s" in r for r in obs.reasons)


def test_rate_divergence_fails_causal_vs_count():
    # causal counter jumps by 2 each event => causal span ~= 2*(n-1), a 100% rate error.
    samples = [
        ClockSample(wall_ts=i * DT, causal_seq=2 * i, epoch=int((i * DT) // PERIOD))
        for i in range(40)
    ]
    obs = observe_three_clock(samples, LIMITS)
    assert not obs.ok
    assert obs.epsilon_rate > 0.5
    assert any("epsilon_rate" in r for r in obs.reasons)


def test_rate_error_against_nominal_hz():
    # samples are 10 Hz; asserting a 4 Hz nominal is a large wall-rate error.
    obs = observe_three_clock(clean(40), ThreeClockLimits(epoch_period_s=PERIOD, nominal_rate_hz=4.0))
    assert not obs.ok
    assert obs.epsilon_rate > 1.0
    assert any("epsilon_rate" in r for r in obs.reasons)


def test_phase_misalignment_fails():
    # hold epoch at 0 forever while wall crosses many epoch boundaries.
    samples = [ClockSample(wall_ts=i * DT, causal_seq=i, epoch=0) for i in range(40)]
    obs = observe_three_clock(samples, LIMITS)
    assert not obs.ok
    assert obs.epsilon_phase is not None and obs.epsilon_phase > 0.05
    assert any("epsilon_phase" in r for r in obs.reasons)


def test_phase_not_gated_when_no_period_supplied():
    # same held-epoch data, but with no epoch_period_s the phase residual is not computed/gated.
    samples = [ClockSample(wall_ts=i * DT, causal_seq=i, epoch=0) for i in range(40)]
    obs = observe_three_clock(samples, ThreeClockLimits())  # no epoch_period_s
    assert obs.epsilon_phase is None
    assert obs.ok, obs.reasons  # order/staleness/rate are all clean here


def test_fully_tied_causal_yields_zero_order_not_divide_by_zero():
    # every causal_seq identical => no comparable pairs on the causal axis.
    samples = [ClockSample(wall_ts=i * DT, causal_seq=7, epoch=int((i * DT) // PERIOD)) for i in range(40)]
    obs = observe_three_clock(samples, LIMITS)
    assert obs.epsilon_order == 0.0  # not a ZeroDivisionError
