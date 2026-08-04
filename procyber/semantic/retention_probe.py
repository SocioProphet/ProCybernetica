"""Retention probe — incorporate foreign experience without forgetting.

An agent that takes in another agent's experience can get worse at what it already
knew. The failure is quiet: the new task improves, the old one degrades, and nothing
in the incorporation path notices because nothing measured the old task.

This module makes the measurement mandatory and the rollback structural. Every
incorporation is: probe the retained tasks, apply, probe again, and **revert if any
retained task regressed beyond tolerance**. There is no path that applies without
probing, because `incorporate` does both and returns the resulting state.

Why a pure function
-------------------
`incorporate` never mutates. It returns the state to use — either the new one or the
original — so a rollback is just "return what you already had" rather than an undo
that has to be correct. An undo path that is exercised rarely is an undo path that
does not work, and this design deletes the category.

On the tolerance
----------------
Measurement is noisy, so an exact-equality bar would revert on nothing but noise and
be switched off within a week. `DEFAULT_TOLERANCE` is the fraction of the prior score
a retained task may lose before it counts as regression. It is a parameter because
the right value depends on the metric's variance, and a caller that has measured its
variance should say so.

The honest limit
----------------
A probe only covers the tasks it is given. This module cannot tell you that a task
you did not probe is fine — it reports what it measured and nothing more, which is
why `IncorporationOutcome` carries the probed task names rather than a bare verdict.

Pure and local-first: stdlib only, no network.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable, Dict, Mapping, Tuple, TypeVar

SPEC_VERSION = "0.1.0"

#: Fraction of its prior score a retained task may lose before it counts as regression.
DEFAULT_TOLERANCE = 0.02

S = TypeVar("S")


class ProbeError(ValueError):
    """Raised when a probe cannot support a decision at all.

    Distinct from regression: "the probe disagreed with itself about which tasks
    exist" is not evidence of safety, and must not be reported as a clean pass.
    """


@dataclass(frozen=True)
class Regression:
    """One retained task that got worse."""

    task: str
    before: float
    after: float

    @property
    def lost(self) -> float:
        return self.before - self.after

    @property
    def fraction(self) -> float:
        return self.lost / self.before if self.before else float("inf")

    def describe(self) -> str:
        return f"{self.task}: {self.before:.4g} -> {self.after:.4g} ({self.fraction:.1%} lost)"


@dataclass(frozen=True)
class IncorporationOutcome:
    """What happened, in enough detail to argue with."""

    incorporated: bool
    rolled_back: bool
    probed: Tuple[str, ...]
    regressions: Tuple[Regression, ...]
    tolerance: float

    @property
    def reason(self) -> str:
        if self.rolled_back:
            worst = max(self.regressions, key=lambda r: r.fraction)
            return f"rolled back: {worst.describe()} exceeds tolerance {self.tolerance:.1%}"
        if not self.probed:
            return "no retained tasks probed — incorporation refused"
        return f"incorporated: {len(self.probed)} retained task(s) held within tolerance"

    def to_json(self) -> Dict[str, object]:
        return {
            "specVersion": SPEC_VERSION,
            "incorporated": self.incorporated,
            "rolledBack": self.rolled_back,
            "probed": list(self.probed),
            "regressions": [r.describe() for r in self.regressions],
            "tolerance": self.tolerance,
            "reason": self.reason,
        }


def find_regressions(
    before: Mapping[str, float],
    after: Mapping[str, float],
    tolerance: float = DEFAULT_TOLERANCE,
) -> Tuple[Regression, ...]:
    """Retained tasks that lost more than `tolerance` of their prior score.

    Raises if the two probes disagree about which tasks exist: a task that vanished
    between probes is a broken probe, and treating it as "no regression" would report
    the most alarming possible result as the safest one.
    """
    if set(before) != set(after):
        missing = sorted(set(before) ^ set(after))
        raise ProbeError(f"probes disagree on task set: {missing}")

    found = []
    for task, prior in before.items():
        current = after[task]
        if current >= prior:
            continue
        regression = Regression(task=task, before=prior, after=current)
        # Strictly greater: a task may lose exactly `tolerance` and still pass. The
        # isclose guard is load-bearing, not decoration — `1.0 - 0.02` is 0.98 to a
        # float, whose loss fraction is 0.020000000000000018, so a bare `>` reverts
        # at exactly the documented limit.
        at_limit = math.isclose(regression.fraction, tolerance, rel_tol=1e-9, abs_tol=1e-12)
        if regression.fraction > tolerance and not at_limit:
            found.append(regression)
    return tuple(sorted(found, key=lambda r: -r.fraction))


def incorporate(
    state: S,
    *,
    apply: Callable[[S], S],
    probe: Callable[[S], Mapping[str, float]],
    tolerance: float = DEFAULT_TOLERANCE,
) -> Tuple[S, IncorporationOutcome]:
    """Probe, apply, probe again, and revert if a retained task regressed.

    Returns `(state_to_use, outcome)`. On rollback the returned state is the original
    object — not a reconstruction of it — so there is no undo to get wrong.

    Refuses when the probe reports no retained tasks: an empty probe would clear
    every incorporation, which is worse than no gate because it looks like one.
    """
    before = dict(probe(state))
    if not before:
        return state, IncorporationOutcome(
            incorporated=False,
            rolled_back=False,
            probed=(),
            regressions=(),
            tolerance=tolerance,
        )

    candidate = apply(state)
    after = dict(probe(candidate))
    regressions = find_regressions(before, after, tolerance)
    probed = tuple(sorted(before))

    if regressions:
        return state, IncorporationOutcome(
            incorporated=False,
            rolled_back=True,
            probed=probed,
            regressions=regressions,
            tolerance=tolerance,
        )

    return candidate, IncorporationOutcome(
        incorporated=True,
        rolled_back=False,
        probed=probed,
        regressions=(),
        tolerance=tolerance,
    )
