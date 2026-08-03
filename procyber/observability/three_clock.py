"""Domain-22 embedded three-clock observability.

The doc3 "time-as-ordering-field" program is, on the whole, research physics that this kit does
NOT attempt to derive. Its ONE platform-buildable slice — identified in the spec-intake gap
analysis — is an *embedded observability instrument*: given a window of observations, each stamped
with three notions of time, measure how much those clocks disagree, and refuse to report a verdict
below a statistical floor.

The three clocks
----------------
* **wall**   — physical wall-clock timestamp (seconds, monotone real).
* **causal** — a logical/causal counter that increments once per intended event (Lamport-style).
* **epoch**  — a coarse generation counter expected to advance once per ``epoch_period_s`` of wall.

The four residuals (each a normalized, unit-free error)
------------------------------------------------------
* ``epsilon_order`` — fraction of ordered pairs whose wall order disagrees with causal order
  (a normalized Kendall discordance in ``[0, 1]``; ties excluded from the denominator).
* ``staleness_s``   — worst-case gap between consecutive wall timestamps (seconds); how stale the
  freshest reading can be.
* ``epsilon_rate``  — divergence between the number of events actually observed and the causal
  span that should accompany them (or, when a nominal rate is supplied, the wall-rate error).
* ``epsilon_phase`` — fraction of samples whose observed epoch differs from the epoch predicted by
  wall time and ``epoch_period_s`` (``None`` when no period is supplied, so it does not gate).

Fail-closed
-----------
Below ``min_samples`` (default 30) — or with a non-positive wall span — the instrument does not
pretend to measure: ``ok`` is ``False`` and the verdict abstains with a reason. This mirrors the
estate's ``n>=30`` measurement floor: a control that reports on 3 samples is not measuring anything.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Sequence


@dataclass(frozen=True)
class ClockSample:
    """One observation stamped on all three clocks."""

    wall_ts: float
    causal_seq: int
    epoch: int


@dataclass(frozen=True)
class ThreeClockLimits:
    """Thresholds + the sample floor. Every bound is inclusive."""

    min_samples: int = 30
    max_epsilon_order: float = 0.05
    max_staleness_s: float = 5.0
    max_epsilon_rate: float = 0.10
    max_epsilon_phase: float = 0.05
    #: expected wall seconds per epoch tick; when None, phase is not computed and does not gate.
    epoch_period_s: Optional[float] = None
    #: expected events/sec; when set (>0), epsilon_rate is the wall-rate error against it,
    #: otherwise epsilon_rate is the causal-span-vs-count divergence.
    nominal_rate_hz: Optional[float] = None


@dataclass(frozen=True)
class ThreeClockObservation:
    """The measured residuals plus the fail-closed verdict."""

    n: int
    epsilon_order: Optional[float]
    staleness_s: Optional[float]
    epsilon_rate: Optional[float]
    epsilon_phase: Optional[float]
    ok: bool
    reasons: List[str] = field(default_factory=list)


def _sign(x: float) -> int:
    return (x > 0) - (x < 0)


def _epsilon_order(samples: Sequence[ClockSample]) -> float:
    """Normalized Kendall discordance between wall order and causal order, in [0, 1].

    A pair is discordant when the sign of the wall difference and the sign of the causal
    difference disagree. Pairs tied on either clock are excluded from the denominator (they carry
    no ordering information), so a fully-tied clock yields 0.0 rather than a divide-by-zero.
    """
    n = len(samples)
    discordant = 0
    comparable = 0
    for i in range(n):
        for j in range(i + 1, n):
            sw = _sign(samples[i].wall_ts - samples[j].wall_ts)
            sc = _sign(samples[i].causal_seq - samples[j].causal_seq)
            if sw == 0 or sc == 0:
                continue
            comparable += 1
            if sw != sc:
                discordant += 1
    return discordant / comparable if comparable else 0.0


def observe_three_clock(
    samples: Sequence[ClockSample], limits: ThreeClockLimits = ThreeClockLimits()
) -> ThreeClockObservation:
    """Measure three-clock disagreement over ``samples`` under ``limits`` (fail-closed).

    The residuals are computed from whatever data are present, but ``ok`` is granted only when the
    sample floor and the wall span are met AND every computed residual is within its bound.
    """
    reasons: List[str] = []
    n = len(samples)

    # --- fail-closed preconditions ---
    if n < limits.min_samples:
        # below the floor we do not trust any statistic; abstain outright.
        return ThreeClockObservation(
            n=n,
            epsilon_order=None,
            staleness_s=None,
            epsilon_rate=None,
            epsilon_phase=None,
            ok=False,
            reasons=[f"insufficient samples (n={n} < min_samples={limits.min_samples})"],
        )

    by_wall = sorted(samples, key=lambda s: s.wall_ts)
    wall_span = by_wall[-1].wall_ts - by_wall[0].wall_ts
    if wall_span <= 0:
        return ThreeClockObservation(
            n=n,
            epsilon_order=None,
            staleness_s=None,
            epsilon_rate=None,
            epsilon_phase=None,
            ok=False,
            reasons=["non-positive wall span (all samples share a wall timestamp)"],
        )

    # --- residuals ---
    epsilon_order = _epsilon_order(samples)

    staleness_s = max(
        by_wall[i + 1].wall_ts - by_wall[i].wall_ts for i in range(len(by_wall) - 1)
    )

    if limits.nominal_rate_hz is not None and limits.nominal_rate_hz > 0:
        wall_rate = (n - 1) / wall_span
        epsilon_rate = abs(wall_rate - limits.nominal_rate_hz) / limits.nominal_rate_hz
    else:
        causal_span = by_wall[-1].causal_seq - by_wall[0].causal_seq
        epsilon_rate = abs(causal_span - (n - 1)) / (n - 1)

    epsilon_phase: Optional[float] = None
    if limits.epoch_period_s is not None and limits.epoch_period_s > 0:
        first = by_wall[0]
        mismatched = 0
        for s in by_wall:
            predicted = first.epoch + int((s.wall_ts - first.wall_ts) // limits.epoch_period_s)
            if s.epoch != predicted:
                mismatched += 1
        epsilon_phase = mismatched / n

    # --- gate (fail-closed: every computed residual must be within bound) ---
    if epsilon_order > limits.max_epsilon_order:
        reasons.append(f"epsilon_order {epsilon_order:.4f} > {limits.max_epsilon_order}")
    if staleness_s > limits.max_staleness_s:
        reasons.append(f"staleness_s {staleness_s:.4f} > {limits.max_staleness_s}")
    if epsilon_rate > limits.max_epsilon_rate:
        reasons.append(f"epsilon_rate {epsilon_rate:.4f} > {limits.max_epsilon_rate}")
    if epsilon_phase is not None and epsilon_phase > limits.max_epsilon_phase:
        reasons.append(f"epsilon_phase {epsilon_phase:.4f} > {limits.max_epsilon_phase}")

    return ThreeClockObservation(
        n=n,
        epsilon_order=epsilon_order,
        staleness_s=staleness_s,
        epsilon_rate=epsilon_rate,
        epsilon_phase=epsilon_phase,
        ok=not reasons,
        reasons=reasons,
    )
