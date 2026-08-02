"""Tests for the functional lawful-learning loop — both ways.

Pins that the alternating loop is a REAL learning loop: it converges to a stationary point,
reduces the constraint violation, actually adapts the gate (isn't a one-shot), is
deterministic (forensic reproducibility), and its fixed point is step-size independent.
"""

import pytest

from procyber.lawful_learning.loop import (
    LoopResult,
    alternating_fit,
    run_lifecycle,
    _violation,
)


DATASETS = {
    "monotone_noisy": [1.0, 2.0, 1.8, 3.0, 4.0, 3.9, 5.0],
    "anti_monotone": [5.0, 4.0, 3.0, 2.0, 1.0],
    "zigzag": [1.0, 5.0, 2.0, 6.0, 3.0, 7.0],
    "flat": [2.0, 2.0, 2.0, 2.0],
}


@pytest.mark.parametrize("name", list(DATASETS))
def test_converges_to_a_stationary_point(name):
    r = alternating_fit(DATASETS[name])
    assert r.converged, f"{name} did not converge in {r.iterations} iters"
    # a stationary point: the last gate step is below tolerance
    assert r.trajectory[-1].delta < 1e-10


def test_reduces_constraint_violation():
    # the whole point of the law: the fitted result is at most as non-monotone as the data
    for name, data in DATASETS.items():
        r = alternating_fit(data)
        assert r.violation <= _violation(data) + 1e-12, name


def test_it_actually_learns_not_one_shot():
    # a real loop moves the gate away from its init; a one-shot would not iterate.
    r = alternating_fit(DATASETS["monotone_noisy"], gate0=0.5)
    assert r.iterations > 1
    assert abs(r.gate - 0.5) > 1e-3  # the gate adapted


def test_fixed_point_is_step_size_independent():
    # the converged gate must not depend on eta — proof it's a genuine stationary point,
    # not an artifact of the damping.
    g1 = alternating_fit(DATASETS["anti_monotone"], eta=0.05).gate
    g2 = alternating_fit(DATASETS["anti_monotone"], eta=0.15).gate
    assert abs(g1 - g2) < 1e-6


def test_deterministic_digest_forensic_reproducibility():
    a = alternating_fit(DATASETS["zigzag"])
    b = alternating_fit(DATASETS["zigzag"])
    assert a.digest == b.digest and a.digest != ""


def test_invalid_eta_is_rejected():
    with pytest.raises(ValueError):
        alternating_fit([1.0, 2.0], eta=0.0)


def test_lifecycle_is_end_to_end_and_auditable():
    rec = run_lifecycle(DATASETS["monotone_noisy"])
    assert rec["converged"] is True
    assert set(rec) >= {"spectral", "gate", "violation", "truth", "loop_digest", "digest"}
    assert 0.0 <= rec["truth"]["T"] <= 1.0
    # deterministic top-level digest
    assert run_lifecycle(DATASETS["monotone_noisy"])["digest"] == rec["digest"]
