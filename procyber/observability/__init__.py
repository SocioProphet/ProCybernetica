"""Observability instruments for ProCybernetica control law.

The first instrument is the Domain-22 embedded three-clock observability slice
(``three_clock``) — the one platform-buildable piece of the doc3 "time-as-ordering-field"
program. It measures the disagreement between three notions of time (wall / causal / epoch)
and refuses to report below a sample floor (fail-closed, n>=30).
"""

from .three_clock import (  # noqa: F401
    ClockSample,
    ThreeClockLimits,
    ThreeClockObservation,
    observe_three_clock,
)
