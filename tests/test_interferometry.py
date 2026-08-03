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
    H = vsa.bundle_bound(list(zip(objs, refs)))
    return H, objs, refs, rng


def test_no_fringe_on_identical_states():
    H, _, refs, _ = _medium(5, 1)
    assert np.max(np.abs(itf.fringe(H, H))) < 1e-9
    assert itf.drift(H, H) < 1e-9
    assert itf.is_tampered(H, H) is False
    assert all(d < 1e-9 for d in itf.drift_map(H, H, refs).values())


def test_drift_map_localizes_the_changed_context():
    H, objs, refs, rng = _medium(5, 2)
    objs2 = list(objs)
    objs2[2] = vsa.random_hv(D, rng)  # change only context #2's attestation
    H2 = vsa.bundle_bound(list(zip(objs2, refs)))
    dm = itf.drift_map(H, H2, refs)
    changed = max(dm, key=dm.get)
    assert changed == 2, f"drift_map pointed at {changed}, not the changed context 2 ({dm})"
    assert dm[2] > 3 * max(dm[i] for i in dm if i != 2), f"change not isolated: {dm}"


def test_subthreshold_fringe_beats_score():
    # THE thesis: one changed record among N barely moves the scalar similarity (∝ 1/N) yet
    # lights up sharply in the per-reference fringe. The prophet reads fringes, not scores.
    N = 32
    H, objs, refs, rng = _medium(N, 3)
    objs2 = list(objs)
    objs2[7] = vsa.random_hv(D, rng)
    H2 = vsa.bundle_bound(list(zip(objs2, refs)))
    scalar = vsa.similarity(H, H2)          # the "score" read
    fringe_at_change = itf.drift_map(H, H2, refs)[7]  # the phase read
    assert scalar > 0.9, f"scalar moved too much to make the point: {scalar:.3f}"
    assert fringe_at_change > 0.4, f"fringe failed to detect the sub-threshold change: {fringe_at_change:.3f}"
    assert fringe_at_change > 4 * (1.0 - scalar), "fringe not sharper than the score"


def test_tamper_is_evident():
    H, objs, refs, rng = _medium(8, 4)
    objs2 = list(objs)
    objs2[0] = vsa.random_hv(D, rng)
    H_tampered = vsa.bundle_bound(list(zip(objs2, refs)))
    assert itf.is_tampered(H, H_tampered) is True
    assert itf.is_tampered(H, H) is False


def test_reads_over_vrf_minted_references():
    # Integration: the references are VRF-minted (vrf.py), and the diff still localises.
    sk, _ = vrf.keygen(seed=bytes(range(32)))
    rng = np.random.default_rng(9)
    contexts = [f"ctx-{i}".encode() for i in range(4)]
    refs = [vrf.context_reference(vrf.mint(sk, c)) for c in contexts]
    objs = [vsa.random_hv(D, rng) for _ in contexts]
    H = vsa.bundle_bound(list(zip(objs, refs)))
    objs2 = list(objs); objs2[1] = vsa.random_hv(D, rng)
    H2 = vsa.bundle_bound(list(zip(objs2, refs)))
    assert max(itf.drift_map(H, H2, refs), key=itf.drift_map(H, H2, refs).get) == 1
