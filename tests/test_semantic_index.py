"""Theorems of ⑤ the semantic index (procyber.semantic.semantic_index): Hamming NN retrieval over
SemanticHasher codes ranks by semantic similarity, bounds by radius, and exports mesh manifest codes."""
from __future__ import annotations

import numpy as np

from procyber.semantic.semantic_hash import SemanticHasher
from procyber.semantic.semantic_index import SemanticIndex


def _unit(rng, d):
    v = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    return v / np.linalg.norm(v)


def _index(d=96, n_bits=512, seed=0):
    return SemanticIndex(SemanticHasher(d=d, n_bits=n_bits, seed=seed))


def test_self_retrieval_at_distance_zero():
    # THEOREM: an indexed vector retrieves ITSELF first, at Hamming 0 (a code equals itself).
    rng = np.random.default_rng(1)
    idx = _index()
    v = _unit(rng, 96)
    idx.add("self", v).add("other", _unit(rng, 96))
    top = idx.query(v, k=1)
    assert top[0] == ("self", 0)
    assert "self" in idx and len(idx) == 2


def test_ranks_by_semantic_similarity():
    # THEOREM: a near vector (high cosine) ranks ahead of a far one — Hamming order = similarity order.
    rng = np.random.default_rng(2)
    d = 96
    idx = _index(d=d)
    base = _unit(rng, d)
    near = base + 0.05 * (_unit(rng, d))       # a small perturbation ⇒ high cosine
    far = _unit(rng, d)                          # independent ⇒ ~orthogonal
    idx.add("near", near).add("far", far)
    ranked = [k for k, _ in idx.query(base, k=2)]
    assert ranked == ["near", "far"]
    # and the estimated similarity agrees: near is closer than far to base
    idx.add("base", base)
    assert idx.similarity("base", "near") > idx.similarity("base", "far")


def test_radius_bounds_retrieval():
    # THEOREM: max_hamming is a real 'not similar enough' boundary — a far code is excluded, not forced.
    rng = np.random.default_rng(3)
    d = 96
    idx = _index(d=d)
    base = _unit(rng, d)
    idx.add("near", base + 0.02 * _unit(rng, d)).add("far", _unit(rng, d))
    # a tight radius keeps the near neighbour and drops the far one
    hits = idx.query(base, k=5, max_hamming=idx.hasher.n_bits // 8)
    keys = [k for k, _ in hits]
    assert "near" in keys and "far" not in keys


def test_codes_hex_round_trips_as_mesh_manifest_codes():
    # THEOREM: codes_hex exports exactly the {ref_id, code} a hyper-feed-manifest.v0 carries — the hex
    # decodes back to a code SemanticHasher.hamming accepts (the index IS the federation advertisement).
    rng = np.random.default_rng(4)
    idx = _index()
    a, b = _unit(rng, 96), _unit(rng, 96)
    idx.add("r_a", a).add("r_b", b)
    hexes = idx.codes_hex()
    assert set(hexes) == {"r_a", "r_b"} and all(isinstance(h, str) for h in hexes.values())
    code_a = np.frombuffer(bytes.fromhex(hexes["r_a"]), dtype=np.uint8)
    # the decoded code matches the index's own retrieval distance to itself (0)
    assert idx.query_code(code_a, k=1)[0] == ("r_a", 0)
