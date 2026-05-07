"""Toy worked examples for calibrated lawful learning.

No live data are used. The examples are deterministic formal calculations.
"""

from __future__ import annotations

import hashlib
import json
import math
from typing import List, Sequence


def spectral_construction_example() -> dict:
    """Return the worked spectral/unitary/spatial/Poincare example.

    Uses the 3x3 illustrative operator:
        [[2, .5, 0],
         [.5, 1, 0],
         [0, 0, .3]]
    """
    lambda1 = (3.0 + math.sqrt(2.0)) / 2.0
    lambda2 = (3.0 - math.sqrt(2.0)) / 2.0
    lambda3 = 0.3

    unitary_u = (1.0 + 2.0 * math.cos(math.pi / 6.0)) / 3.0

    sx = 0.4 * lambda1 + 0.1 * lambda2 + 0.0 * lambda3 + 0.2 * unitary_u
    sy = 0.0 * lambda1 + 0.3 * lambda2 + 0.2 * lambda3 + 0.1 * unitary_u
    sz = 0.1 * lambda1 + 0.0 * lambda2 + 0.5 * lambda3 + 0.2 * unitary_u

    norm = math.sqrt(sx * sx + sy * sy + sz * sz)
    denom = 1.0 + norm
    p = (sx / denom, sy / denom, sz / denom)

    return {
        "lambda": (lambda1, lambda2, lambda3),
        "u": unitary_u,
        "s": (sx, sy, sz),
        "poincare": p,
        "poincare_norm": math.sqrt(sum(v * v for v in p)),
    }


def differences(values: Sequence[float]) -> List[float]:
    """Return adjacent first differences."""
    return [values[i + 1] - values[i] for i in range(len(values) - 1)]


def monotone_projection_pava(values: Sequence[float]) -> List[float]:
    """Pool-adjacent-violators projection for nondecreasing sequences."""
    blocks: list[list[float | int]] = []
    for value in values:
        blocks.append([float(value), 1])
        while len(blocks) >= 2 and blocks[-2][0] > blocks[-1][0]:
            total = float(blocks[-2][0]) * int(blocks[-2][1]) + float(blocks[-1][0]) * int(blocks[-1][1])
            count = int(blocks[-2][1]) + int(blocks[-1][1])
            blocks[-2:] = [[total / count, count]]
    out: list[float] = []
    for mean, count in blocks:
        out.extend([float(mean)] * int(count))
    return out


def dominance_slack(
    dominant_slopes: Sequence[float],
    subordinate_slopes: Sequence[float],
    gate: float,
    mu_min: float,
    mu_max: float,
) -> dict:
    """Compute slack and slack penalty for a dominance violation."""
    if not 0.0 <= gate <= 1.0:
        raise ValueError("gate must be in [0, 1]")
    if mu_max < mu_min:
        raise ValueError("mu_max must be >= mu_min")

    diffs = [a - b for a, b in zip(dominant_slopes, subordinate_slopes)]
    slack = [max(0.0, -d) for d in diffs]
    mu = mu_min + (mu_max - mu_min) * gate
    penalty = sum(mu * s * s for s in slack)
    return {"differences": diffs, "slack": slack, "mu": mu, "penalty": penalty}


def edgeworth_project_f11(f00: float, f10: float, f01: float, f11: float) -> dict:
    """Project a 2x2 cell onto nonnegative Edgeworth complementarity."""
    cross = f11 - f10 - f01 + f00
    required_f11 = f10 + f01 - f00
    projected_f11 = max(f11, required_f11)
    projected_cross = projected_f11 - f10 - f01 + f00
    return {
        "cross_difference": cross,
        "required_f11": required_f11,
        "projected_f11": projected_f11,
        "projected_cross_difference": projected_cross,
    }


def sigmoid(x: float) -> float:
    """Numerically simple logistic function for toy examples."""
    return 1.0 / (1.0 + math.exp(-x))


def learned_gate(statistic: float, threshold: float, temperature: float) -> float:
    """Compute a calibrated logistic threshold gate."""
    if temperature <= 0:
        raise ValueError("temperature must be positive")
    return sigmoid((statistic - threshold) / temperature)


def truth_score(
    violation_norm: float,
    kappa: float,
    ledger_ok: bool,
    signature_ok: bool,
    replay_ok: bool,
    environment_drift_risk: float,
) -> dict:
    """Compute T=L*E for an illustrative lawful-learning claim."""
    if violation_norm < 0:
        raise ValueError("violation_norm must be nonnegative")
    if kappa < 0:
        raise ValueError("kappa must be nonnegative")
    if not 0.0 <= environment_drift_risk <= 1.0:
        raise ValueError("environment_drift_risk must be in [0, 1]")

    lawful = math.exp(-kappa * violation_norm)
    evidence = (
        (1.0 if ledger_ok else 0.0)
        * (1.0 if signature_ok else 0.0)
        * (1.0 if replay_ok else 0.0)
        * (1.0 - environment_drift_risk)
    )
    return {"L": lawful, "E": evidence, "T": lawful * evidence}


def canonical_digest(payload: dict) -> str:
    """Return a deterministic illustrative SHA-256 digest over canonical JSON."""
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def end_to_end_example() -> dict:
    """Run the toy pipeline from spectral state to operational truth score."""
    spectral = spectral_construction_example()
    violation_norm = 0.07
    kappa = math.log(2.0) / 0.07
    score = truth_score(
        violation_norm=violation_norm,
        kappa=kappa,
        ledger_ok=True,
        signature_ok=True,
        replay_ok=True,
        environment_drift_risk=0.02,
    )
    digest = canonical_digest({"spectral": spectral, "violation_norm": violation_norm, "score": score})
    return {"spectral": spectral, "violation_norm": violation_norm, "kappa": kappa, "truth": score, "digest": digest}


if __name__ == "__main__":
    print(json.dumps(end_to_end_example(), indent=2, sort_keys=True))
