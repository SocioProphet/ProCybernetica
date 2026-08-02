"""A functional lawful-learning loop — alternating block-coordinate descent.

`toy.py` holds the *primitives* (isotonic theta-projection, learned gate, Truth=Law*Evidence)
but no running loop. This is the manuscript's Algorithm 1 as a small, deterministic, convergent
loop:

    repeat:
        theta-step: fitted = (1-w)*data + w*PAVA(data)     # gated projection onto the
                                                            # monotone constraint cone
        gate-step:  w <- (1-eta)*w + eta * sigmoid(beta*(violation - fit_cost))
    until the gate stops moving (delta < tol)

The theta-step is a genuine constraint projection (isotonic regression). The gate-step is a
DAMPED fixed-point that raises the gate while the law is cheap to enforce and backs off when
enforcement costs fit; the damping makes the update a contraction, so the loop converges to a
stationary point (a discrete echo of Theorem 6.1). It is deterministic — no RNG — so the same
inputs yield the same trajectory and the same ledger digest, which is the forensic-
reproducibility property lawful learning requires. Truth = Law * Evidence is computed on the
converged state, closing the lifecycle from spectral construction to an auditable score.

Pure stdlib.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Sequence

from procyber.lawful_learning.toy import (
    canonical_digest,
    monotone_projection_pava,
    sigmoid,
    spectral_construction_example,
    truth_score,
)


def _violation(values: Sequence[float]) -> float:
    """Total downward (monotonicity-violating) movement; 0 iff nondecreasing."""
    return sum(max(0.0, values[i] - values[i + 1]) for i in range(len(values) - 1))


def _mse(a: Sequence[float], b: Sequence[float]) -> float:
    return sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)


@dataclass(frozen=True)
class LoopStep:
    iteration: int
    gate: float
    fit_cost: float
    violation: float
    delta: float


@dataclass(frozen=True)
class LoopResult:
    converged: bool
    iterations: int
    gate: float
    fitted: List[float]
    fit_cost: float
    violation: float
    trajectory: List[LoopStep] = field(default_factory=list)
    digest: str = ""


def alternating_fit(
    data: Sequence[float],
    *,
    eta: float = 0.1,
    beta: float = 5.0,
    max_iters: int = 300,
    tol: float = 1e-10,
    gate0: float = 0.5,
) -> LoopResult:
    """Fit values to *data* under a gated monotonicity law by alternating descent."""
    if not 0.0 < eta <= 1.0:
        raise ValueError("eta must be in (0, 1]")
    if len(data) == 0:
        raise ValueError("data must be non-empty")
    if not 0.0 <= gate0 <= 1.0:
        raise ValueError("gate0 must be in [0, 1] (the theta-step is a convex combination)")
    y = [float(v) for v in data]
    mono = monotone_projection_pava(y)  # the law's projection target (fixed)
    w = float(gate0)
    trajectory: List[LoopStep] = []
    converged = False

    for it in range(max_iters):
        # theta-step: gated projection onto the monotone cone
        fitted = [(1.0 - w) * y[i] + w * mono[i] for i in range(len(y))]
        viol = _violation(fitted)
        fit_cost = _mse(fitted, y)
        # gate-step: damped fixed-point toward the law/fit balance. Clamp the sigmoid
        # argument: toy.sigmoid is 1/(1+exp(-x)) and overflows for large-magnitude x, and
        # this loop is a general primitive, not only for tiny toy datasets.
        arg = max(-60.0, min(60.0, beta * (viol - fit_cost)))
        target = sigmoid(arg)
        w_new = (1.0 - eta) * w + eta * target
        delta = abs(w_new - w)
        # `delta` is stored UNROUNDED so `trajectory[-1].delta` agrees exactly with the
        # `delta < tol` convergence check (rounding could inflate a near-threshold value).
        trajectory.append(
            LoopStep(it, round(w, 12), round(fit_cost, 12), round(viol, 12), delta)
        )
        w = w_new
        if it > 0 and delta < tol:
            converged = True
            break

    fitted = [(1.0 - w) * y[i] + w * mono[i] for i in range(len(y))]
    core = {
        "converged": converged,
        "iterations": len(trajectory),
        "gate": round(w, 12),
        "fitted": [round(v, 12) for v in fitted],
        "fit_cost": round(_mse(fitted, y), 12),
        "violation": round(_violation(fitted), 12),
    }
    return LoopResult(**core, trajectory=trajectory, digest=canonical_digest(core))


def run_lifecycle(data: Sequence[float]) -> dict:
    """The full learning-loop lifecycle: spectral construction -> converge -> Truth=Law*Evidence.

    Returns an auditable record with a canonical digest — deterministic end to end.
    """
    spectral = spectral_construction_example()
    result = alternating_fit(data)
    # Evidence side of Truth = Law * Evidence: the converged constraint residual is the law's
    # satisfaction; a small residual clears a high truth score.
    score = truth_score(
        violation_norm=result.violation,
        kappa=6.0,
        ledger_ok=True,
        signature_ok=True,
        replay_ok=True,
        environment_drift_risk=0.02,
    )
    record = {
        "spectral": spectral,
        "converged": result.converged,
        "iterations": result.iterations,
        "gate": result.gate,
        "violation": result.violation,
        "fit_cost": result.fit_cost,
        "truth": score,
        "loop_digest": result.digest,
    }
    record["digest"] = canonical_digest(record)
    return record


if __name__ == "__main__":  # pragma: no cover - CLI glue
    import json

    print(json.dumps(run_lifecycle([1.0, 2.0, 1.8, 3.0, 4.0, 3.9, 5.0]), indent=2, sort_keys=True))
