"""Theorems of semantic hashing (procyber.semantic.semantic_hash) — compact codes whose Hamming
distance is a calibrated estimate of vsa.similarity. Deterministic (seeded projection + vectors).
"""
from __future__ import annotations

import numpy as np
import pytest

from procyber.semantic import semantic_hash as sh
from procyber.semantic import vsa

D = 1024
NB = 512


def _hasher() -> sh.SemanticHasher:
    return sh.SemanticHasher(d=D, n_bits=NB, seed=7)


def _rng(s: int = 0) -> np.random.Generator:
    return np.random.default_rng(s)


def test_encode_is_deterministic_and_self_identical():
    h = _hasher()
    a = vsa.random_hv(D, _rng(1))
    assert sh.SemanticHasher.hamming(h.encode(a), h.encode(a)) == 0
    assert h.similarity_estimate(h.encode(a), h.encode(a)) == 1.0


def test_orthogonal_vectors_differ_in_about_half_the_bits():
    # THEOREM: near-orthogonal vectors (sim ~ 0) have Hamming ~ n_bits/2 (angle ~ π/2).
    h = _hasher()
    rng = _rng(2)
    hams = [sh.SemanticHasher.hamming(h.encode(vsa.random_hv(D, rng)), h.encode(vsa.random_hv(D, rng)))
            for _ in range(20)]
    assert 0.4 * NB < float(np.mean(hams)) < 0.6 * NB


def test_hamming_calibrates_to_vsa_similarity():
    # THEOREM (calibration): similarity_estimate ≈ vsa.similarity across the range of angles.
    h = _hasher()
    rng = _rng(3)
    for _ in range(12):
        a = vsa.random_hv(D, rng)
        other = vsa.random_hv(D, rng)
        for t in (0.0, 0.5, 1.0, 3.0):        # a blend spanning high→low similarity to `a`
            b = a + t * other
            true = vsa.similarity(a, b)
            est = h.similarity_estimate(h.encode(a), h.encode(b))
            assert abs(est - true) < 0.15, f"t={t}: est {est:.3f} vs true {true:.3f}"


def test_nearest_by_hamming_matches_nearest_by_similarity():
    # THEOREM (retrieval): the code-space nearest neighbour is the metric-space nearest neighbour.
    h = _hasher()
    rng = _rng(4)
    query = vsa.random_hv(D, rng)
    near = query + 0.15 * vsa.random_hv(D, rng)          # deliberately close
    far = [vsa.random_hv(D, rng) for _ in range(6)]      # orthogonal-ish
    cands = [near] + far
    qc = h.encode(query)
    by_ham = min(range(len(cands)), key=lambda i: sh.SemanticHasher.hamming(qc, h.encode(cands[i])))
    by_sim = max(range(len(cands)), key=lambda i: vsa.similarity(query, cands[i]))
    assert by_ham == by_sim == 0                          # `near` wins in both spaces


def test_n_bits_must_be_byte_aligned():
    with pytest.raises(ValueError):
        sh.SemanticHasher(d=D, n_bits=100)
