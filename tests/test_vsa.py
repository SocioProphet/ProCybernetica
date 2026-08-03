"""Theorems of the VSA/HRR twin substrate (procyber.semantic.vsa).

These discharge the CONSTRUCTION+THEOREM tiers of the Multiverseal-Twin spec §1/§A:
exact reference inversion, reference-gated hiding & reconstruction, and the ε/JL capacity
bound (fidelity ~1/√N, graceful — never catastrophic). Deterministic (fixed seeds).
"""
from __future__ import annotations

import numpy as np
import pytest

from procyber.semantic import vsa

D = 1024


def _rng(seed: int = 7) -> np.random.Generator:
    return np.random.default_rng(seed)


def test_bind_unbind_is_exact_inverse():
    # Unit-magnitude components ⇒ conj is the exact inverse under elementwise bind.
    rng = _rng()
    a, b = vsa.random_hv(D, rng), vsa.random_hv(D, rng)
    assert vsa.similarity(vsa.unbind(vsa.bind(a, b), b), a) == pytest.approx(1.0, abs=1e-9)


def test_bind_is_dissimilar_to_its_operands():
    # A bound pair hides its parts: bind(a,b) is ~orthogonal to a and to b.
    rng = _rng()
    a, b = vsa.random_hv(D, rng), vsa.random_hv(D, rng)
    c = vsa.bind(a, b)
    assert abs(vsa.similarity(c, a)) < 0.1
    assert abs(vsa.similarity(c, b)) < 0.1


def _bundle_pairs(n: int, seed: int):
    rng = _rng(seed)
    objs = [vsa.random_hv(D, rng) for _ in range(n)]
    refs = [vsa.random_hv(D, rng) for _ in range(n)]
    H = vsa.bundle_bound(list(zip(objs, refs)))
    return H, objs, refs, rng


def _mean_right_ref_fidelity(H, objs, refs) -> float:
    return float(np.mean([vsa.similarity(vsa.reconstruct(H, refs[j]), objs[j]) for j in range(len(objs))]))


def _max_wrong_ref_leakage(H, objs, rng) -> float:
    # Illuminate with references that bound nothing → must be noise against every object.
    wrong = [vsa.random_hv(D, rng) for _ in range(5)]
    return max(abs(vsa.similarity(vsa.reconstruct(H, w), o)) for w in wrong for o in objs)


def test_reference_gated_hiding_and_reconstruction():
    # THEOREM (twin §1): the right reference reconstructs its object; a wrong one yields noise.
    H, objs, refs, rng = _bundle_pairs(6, seed=11)
    fidelity = _mean_right_ref_fidelity(H, objs, refs)
    leakage = _max_wrong_ref_leakage(H, objs, rng)
    assert fidelity > 0.25, f"right-reference reconstruction too weak: {fidelity:.3f}"
    assert leakage < 0.15, f"a wrong reference leaked signal: {leakage:.3f}"
    assert fidelity > 3 * leakage, f"reference-gating margin too small: {fidelity:.3f} vs {leakage:.3f}"


def test_epsilon_capacity_degrades_gracefully():
    # THEOREM (twin §A.1, JL): fidelity falls ~1/√N as more items share the medium, but stays
    # cleanly above the noise floor — graceful degradation, not catastrophic corruption.
    f_small = _mean_right_ref_fidelity(*_bundle_pairs(4, seed=3)[:3])
    f_large = _mean_right_ref_fidelity(*_bundle_pairs(48, seed=3)[:3])
    Hn, objsn, _, rngn = _bundle_pairs(48, seed=3)
    noise = _max_wrong_ref_leakage(Hn, objsn, rngn)
    assert f_small > f_large, f"fidelity did not decrease with load: {f_small:.3f} -> {f_large:.3f}"
    assert f_large > 2 * noise, f"sub-threshold not clean (lost, not degraded): {f_large:.3f} vs noise {noise:.3f}"
    # ~1/√N law: the ratio should track sqrt(48/4)=~3.46 within a factor of 2.
    assert 0.5 < (f_small / f_large) / np.sqrt(48 / 4) < 2.0


def test_bundle_requires_input():
    with pytest.raises(ValueError):
        vsa.bundle([])
