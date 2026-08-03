"""Theorems of the Multiverseal Twin capstone (procyber.semantic.twin) — the composed object."""
from __future__ import annotations

import numpy as np
import pytest

from procyber.semantic import interferometry as itf
from procyber.semantic import twin as tw
from procyber.semantic import vrf, vsa

D = vrf.DEFAULT_D
SEED_A = bytes(range(32))
SEED_B = bytes(range(1, 33))


def _val(seed: int) -> vsa.HV:
    return vsa.random_hv(D, np.random.default_rng(seed))


def test_attest_then_recall_roundtrips():
    t = tw.MultiversealTwin(seed=SEED_A)
    v = _val(1)
    t.attest(b"alice#reputation", v)
    assert vsa.similarity(t.recall(b"alice#reputation"), v) == pytest.approx(1.0, abs=1e-9)


def test_reference_at_ingest_hides_the_value():
    # The value is not stored bare: the medium reveals nothing without the context reference,
    # and illuminating with a different context yields noise.
    t = tw.MultiversealTwin(seed=SEED_A)
    v = _val(2)
    t.attest(b"ctx-real", v)
    t.attest(b"ctx-other", _val(3))
    assert abs(vsa.similarity(t.medium(), v)) < 0.1                       # medium hides v
    wrong = vrf.reference_hv(vrf.mint(t._sk, b"ctx-other").proof, D)
    assert abs(vsa.similarity(vsa.unbind(t.medium(), wrong), v)) < 0.2     # wrong ref = noise


def test_only_the_core_mints_a_verifiable_reference():
    t = tw.MultiversealTwin(seed=SEED_A)
    ref = t.attest(b"ctx", _val(4))
    assert t.verify(ref) is True
    forged = vrf.VerifiableReference(b"ctx", b"\x00" * 64, t.verify_key)
    assert t.verify(forged) is False


def test_medium_is_tamper_evident():
    t = tw.MultiversealTwin(seed=SEED_A)
    t.attest(b"a", _val(5))
    snapshot = t.medium().copy()
    assert t.is_tampered(snapshot) is False
    t.attest(b"b", _val(6))               # a new attestation moves the medium
    assert t.is_tampered(snapshot) is True


def test_same_value_different_sovereign_is_score_blind_fringe_visible():
    # Two twins attest the SAME value under the SAME context but different master keys — same
    # magnitude (a score sees identical) but different provenance (the fringe sees it).
    v = _val(7)
    a = tw.MultiversealTwin(seed=SEED_A); a.attest(b"ctx", v)
    b = tw.MultiversealTwin(seed=SEED_B); b.attest(b"ctx", v)
    assert itf.magnitude_similarity(a.medium(), b.medium()) == pytest.approx(1.0, abs=1e-9)
    assert itf.provenance_moved(a.medium(), b.medium()) is True


def test_empty_twin_has_no_medium():
    with pytest.raises(ValueError):
        tw.MultiversealTwin(seed=SEED_A).medium()
