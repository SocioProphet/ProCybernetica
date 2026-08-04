"""Theorems of the living (temporal) twin medium (procyber.semantic.twin.TemporalTwin) — the
associative dynamics wired into the twin: an unrehearsed attestation fades from the medium while a
re-attested one stays sharp, on the same two-timescale law as the association graph. The base
twin's reference-gated guarantees are unchanged (a subclass only *weights* admitted records).
"""
from __future__ import annotations

import numpy as np

from procyber.semantic import twin as tw
from procyber.semantic import vsa


def _val(seed: int) -> vsa.HV:
    return vsa.random_hv(1024, np.random.default_rng(seed))


def test_temporal_twin_attest_and_recall_when_fresh():
    # A fresh temporal twin behaves like the base twin: attest → recall the value with high fidelity.
    core = tw.TemporalTwin(seed=bytes(range(32)))
    v = _val(1)
    ref = core.attest(b"alice#reputation", v)
    assert core.verify(ref) is True
    assert vsa.similarity(core.recall(b"alice#reputation"), v) > 0.9


def test_unrehearsed_memory_fades_rehearsed_persists():
    # THEOREM (living medium): after time passes, an unrehearsed context fades from the medium
    # while a re-attested one stays sharp — a forgetting curve over the reference-gated store.
    core = tw.TemporalTwin(seed=bytes(range(32)))
    va, vb = _val(1), _val(2)
    core.attest(b"A", va)
    core.attest(b"B", vb)
    fid_b_fresh = vsa.similarity(core.recall(b"B"), vb)
    for _ in range(4):
        core.attest(b"A", va)      # rehearse A
    core.tick(15)                  # time passes without touching B
    fid_a = vsa.similarity(core.recall(b"A"), va)
    fid_b = vsa.similarity(core.recall(b"B"), vb)
    assert fid_b < fid_b_fresh             # B faded
    assert fid_a > fid_b                   # rehearsed A outlives unrehearsed B
    assert core.strength(b"A") > core.strength(b"B")


def test_strength_is_bounded_and_monotone_under_rehearsal():
    core = tw.TemporalTwin(seed=bytes(range(32)))
    v = _val(3)
    core.attest(b"C", v)
    s1 = core.strength(b"C")
    for _ in range(5):
        core.attest(b"C", v)
    s2 = core.strength(b"C")
    assert 0.0 <= s1 <= s2 <= 1.0          # rehearsal strengthens, stays bounded


def test_base_twin_medium_is_unchanged():
    # The base MultiversealTwin is untouched — its medium is the plain (unweighted) bundle.
    base = tw.MultiversealTwin(seed=bytes(range(32)))
    v = _val(4)
    base.attest(b"x", v)
    assert vsa.similarity(base.recall(b"x"), v) > 0.99
    assert not hasattr(base, "strength")   # temporal API lives only on the subclass
