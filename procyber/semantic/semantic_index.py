"""⑤ INDEX — the fifth organ of the knowledge-memory spine. A nearest-neighbour index over
SemanticHasher codes: store an id's ℂ^D hypervector as a compact binary code, then retrieve the
semantically-closest ids by Hamming popcount instead of a dense similarity sweep.

This is the retrieval face of semantic hashing (semantic_hash.py): Hamming distance over signed-random
-projection codes tracks the VSA angle (E[H/n] = θ/π), so ranking by Hamming ranks by semantic
similarity. Two consumers, one index: (a) recall over the twin medium / association graph, and (b) the
mesh — `codes_hex` exports exactly the `{ref_id, code}` a hyper-feed-manifest.v0 publishes, so a node's
index IS its federation advertisement (peers match by Hamming without moving raw vectors).

Clean-room, deterministic (the hasher is seeded), pure-Python over numpy. Theorems in
tests/test_semantic_index.py: self-retrieval at distance 0, rank agreement with exact VSA similarity,
threshold recall, and manifest-code round-trip with SemanticHasher.hamming.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import numpy as np

from procyber.semantic.semantic_hash import SemanticHasher

__all__ = ["SemanticIndex"]


@dataclass
class SemanticIndex:
    """A Hamming nearest-neighbour index over a shared SemanticHasher. `add` an id's hypervector, then
    `query` for the nearest ids. Ties break by id, so retrieval is deterministic."""

    hasher: SemanticHasher
    _codes: Dict[str, np.ndarray] = field(default_factory=dict, repr=False)

    def add(self, key: str, hv: np.ndarray) -> "SemanticIndex":
        """Index `key` by the code of its ℂ^D hypervector. Re-adding an id replaces its code."""
        self._codes[key] = self.hasher.encode(hv)
        return self

    def add_code(self, key: str, code: np.ndarray) -> "SemanticIndex":
        """Index a pre-computed code (e.g. one received from a peer's manifest)."""
        self._codes[key] = code
        return self

    def __len__(self) -> int:
        return len(self._codes)

    def __contains__(self, key: str) -> bool:
        return key in self._codes

    def query(self, hv: np.ndarray, k: int = 5, *, max_hamming: Optional[int] = None) -> List[Tuple[str, int]]:
        """The `k` nearest ids to `hv` as (id, hamming), nearest first (ties by id). `max_hamming`
        bounds the radius — beyond it is 'not similar enough', not a forced neighbour."""
        return self.query_code(self.hasher.encode(hv), k, max_hamming=max_hamming)

    def query_code(self, code: np.ndarray, k: int = 5, *, max_hamming: Optional[int] = None) -> List[Tuple[str, int]]:
        """`query` from a raw code — the mesh's path: a peer's query code against this node's index."""
        scored = [(key, SemanticHasher.hamming(code, c)) for key, c in self._codes.items()]
        if max_hamming is not None:
            scored = [(key, h) for key, h in scored if h <= max_hamming]
        scored.sort(key=lambda t: (t[1], t[0]))
        return scored[:k]

    def similarity(self, key_a: str, key_b: str) -> float:
        """Estimated VSA similarity between two indexed ids (cos(π·H/n_bits))."""
        return self.hasher.similarity_estimate(self._codes[key_a], self._codes[key_b])

    def codes_hex(self) -> Dict[str, str]:
        """Export `{id: hex-code}` — exactly a hyper-feed-manifest.v0's `{ref_id, code}` payload, so a
        node's index publishes as its federation advertisement (peers match by Hamming, no raw data)."""
        return {key: code.tobytes().hex() for key, code in self._codes.items()}
