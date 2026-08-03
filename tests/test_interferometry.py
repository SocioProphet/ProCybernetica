"""Theorems of the twin's interferometric read (procyber.semantic.interferometry, spec §C)."""
from __future__ import annotations

import numpy as np

from procyber.semantic import interferometry as itf
from procyber.semantic import vrf, vsa

D = 1024


def _medium(n: int, seed: int):
    rng = np.random.default_rng(seed)
    objs = [vsa.random_hv(D, rng) for _ in range(n)]
    refs = [vsa.random_hv(D, rng) for _ in range(n)]
    return vsa.bundle_bound(list(zip(objs, refs))), objs, refs, rng


def test_no_fringe_on_identical_states():
    H, _, _, _ = _medium(5, 1)
    assert np.max(np.abs(itf.fringe(H, H))) < 1e-9
    assert itf.is_tampered(H, H) is False
    assert itf.provenance_moved(H, H) is False


def test_tamper_is_evident():
    H, objs, refs, rng = _medium(8, 4)
    objs2 = list(objs)
    objs2[0] = vsa.random_hv(D, rng)  # one record rewritten
    assert itf.is_tampered(H, vsa.bundle_bound(list(zip(objs2, refs)))) is True
    assert itf.is_tampered(H, H) is False


def test_fringes_not_scores__same_value_different_provenance():
    # THE thesis: an attestation of the SAME value under a DIFFERENT provenance (reference) has
    # identical magnitude — a score read sees no change — but a nonzero phase fringe. Phase is
    # who bound it; magnitude is the raw value. The prophet reads the fringe.
    rng = np.random.default_rng(3)
    value = vsa.random_hv(D, rng)
    prov_A = vsa.random_hv(D, rng)
    prov_B = vsa.random_hv(D, rng)
    record_A = vsa.bind(value, prov_A)
    record_B = vsa.bind(value, prov_B)
    assert itf.magnitude_similarity(record_A, record_B) == \
        __import__("pytest").approx(1.0, abs=1e-9), "magnitudes must be identical (score is blind)"
    assert itf.phase_energy(record_A, record_B) > 0.5, "the fringe must see the provenance change"
    assert itf.provenance_moved(record_A, record_B) is True


def test_fringe_is_local_to_where_state_moved():
    # A change confined to a slice of components leaves the fringe ~0 elsewhere — a map of *where*.
    rng = np.random.default_rng(5)
    a = vsa.random_hv(D, rng)
    b = a.copy()
    b[100:110] = vsa.random_hv(10, rng)  # move only 10 components
    f = np.abs(itf.fringe(a, b))
    assert np.max(f[:100]) < 1e-9 and np.max(f[110:]) < 1e-9
    assert np.max(f[100:110]) > 1e-6


def test_reads_over_vrf_minted_references():
    # Integration with vrf.py: same value under two VRF-minted context references ⇒ provenance moved.
    sk, _ = vrf.keygen(seed=bytes(range(32)))
    rng = np.random.default_rng(9)
    value = vsa.random_hv(D, rng)
    r1 = vrf.context_reference(vrf.mint(sk, b"ctx-1"))
    r2 = vrf.context_reference(vrf.mint(sk, b"ctx-2"))
    assert itf.provenance_moved(vsa.bind(value, r1), vsa.bind(value, r2)) is True
