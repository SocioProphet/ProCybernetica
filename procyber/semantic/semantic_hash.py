"""Semantic hashing for the VSA substrate — compact binary codes whose Hamming distance tracks
semantic distance, so nearest-neighbour retrieval over the twin medium / association graph is a
popcount instead of a dense similarity sweep.

Construction (clean-room; the science is public): signed random projections / SimHash (Charikar,
2002) over the real embedding of a ℂ^D hypervector. A complex hypervector a ∈ ℂ^D embeds as the
real vector [Re a ; Im a] ∈ ℝ^{2D}, whose cosine equals Re⟨a,b⟩/(‖a‖‖b‖) — exactly
procyber.semantic.vsa.similarity. Projecting onto n fixed random hyperplanes and taking signs
yields n bits; for signed random projections the expected fraction of differing bits between two
codes is θ/π, where θ is the angle — so Hamming distance is a calibrated estimate of the semantic
angle (Hinton & Salakhutdinov's semantic-hashing idea, on the VSA metric).

Deterministic: the projection is seeded. Theorems in tests/test_semantic_hash.py: self-identity,
orthogonal ⇒ ~half the bits differ, the Hamming↔similarity calibration cos(π·H/n), and rank
agreement with exact VSA similarity for nearest-neighbour retrieval.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

__all__ = ["SemanticHasher"]


@dataclass
class SemanticHasher:
    """Signed-random-projection hasher: `encode` a ℂ^D hypervector to an `n_bits` code, then
    compare codes by `hamming` (popcount) or `similarity_estimate` (calibrated to vsa.similarity)."""

    d: int
    n_bits: int = 128
    seed: int = 0
    _R: np.ndarray = field(init=False, repr=False)

    def __post_init__(self) -> None:
        if self.n_bits % 8 != 0:
            raise ValueError("n_bits must be a multiple of 8 (codes are byte-packed)")
        rng = np.random.default_rng(self.seed)
        # n_bits random hyperplanes in the real embedding ℝ^{2d} of ℂ^d
        self._R = rng.standard_normal((self.n_bits, 2 * self.d))

    def encode(self, hv: np.ndarray) -> np.ndarray:
        """Encode a ℂ^D hypervector to a byte-packed `n_bits` code (uint8 array of n_bits//8)."""
        if hv.shape != (self.d,):
            raise ValueError(f"expected a ℂ^{self.d} hypervector, got shape {hv.shape}")
        x = np.concatenate([hv.real, hv.imag])
        bits = (self._R @ x) >= 0.0
        return np.packbits(bits)

    @staticmethod
    def hamming(a: np.ndarray, b: np.ndarray) -> int:
        """Hamming distance between two byte-packed codes (number of differing bits)."""
        return int(np.unpackbits(np.bitwise_xor(a, b)).sum())

    def similarity_estimate(self, a: np.ndarray, b: np.ndarray) -> float:
        """Estimate vsa.similarity from two codes: cos(π · Hamming / n_bits). For signed random
        projections E[Hamming/n_bits] = θ/π, so this inverts the calibration back to cosine."""
        return float(np.cos(np.pi * self.hamming(a, b) / self.n_bits))
