"""Theorems of the twin's verifiable-reference mint/verify (procyber.semantic.vrf, spec §D).

Mint-asymmetry (only the master key mints), verifiability, unforgeability (tamper ⇒ reject),
determinism/uniqueness, fail-closed reference derivation, and integration with the VSA medium
(the minted r_c binds/unbinds and is near-orthogonal across contexts). Deterministic seeds.
"""
from __future__ import annotations

import numpy as np
import pytest

from procyber.semantic import vrf, vsa

SEED = bytes(range(32))  # 32-byte deterministic master key


def test_mint_then_verify_roundtrip():
    sk, _ = vrf.keygen(seed=SEED)
    ref = vrf.mint(sk, b"context:alice@acme#reputation")
    assert vrf.verify(ref) is True


def test_tampered_proof_is_rejected():
    sk, _ = vrf.keygen(seed=SEED)
    ref = vrf.mint(sk, b"ctx")
    bad = bytearray(ref.proof)
    bad[0] ^= 0x01
    assert vrf.verify(vrf.VerifiableReference(ref.context, bytes(bad), ref.verify_key)) is False


def test_wrong_context_is_rejected():
    sk, _ = vrf.keygen(seed=SEED)
    ref = vrf.mint(sk, b"ctx-A")
    assert vrf.verify(vrf.VerifiableReference(b"ctx-B", ref.proof, ref.verify_key)) is False


def test_a_different_key_cannot_verify_it():
    sk, _ = vrf.keygen(seed=SEED)
    _, other_vk = vrf.keygen(seed=bytes(range(1, 33)))
    ref = vrf.mint(sk, b"ctx")
    assert vrf.verify(vrf.VerifiableReference(ref.context, ref.proof, other_vk)) is False


def test_forged_reference_without_master_key_fails():
    # No master key ⇒ no valid proof. A fabricated proof does not verify, and deriving r_c
    # from it is refused (fail-closed) — you cannot mint a usable reference without the key.
    _, vk = vrf.keygen(seed=SEED)
    forged = vrf.VerifiableReference(b"ctx", b"\x00" * 64, vk)
    assert vrf.verify(forged) is False
    with pytest.raises(ValueError):
        vrf.context_reference(forged)


def test_deterministic_mint_and_reference():
    sk1, _ = vrf.keygen(seed=SEED)
    sk2, _ = vrf.keygen(seed=SEED)
    a = vrf.mint(sk1, b"ctx")
    b = vrf.mint(sk2, b"ctx")
    assert a.proof == b.proof  # Ed25519 deterministic ⇒ unique per (key, context)
    assert np.array_equal(vrf.reference_hv(a.proof), vrf.reference_hv(b.proof))


def test_references_are_near_orthogonal_across_contexts():
    sk, _ = vrf.keygen(seed=SEED)
    r1 = vrf.context_reference(vrf.mint(sk, b"ctx-1"))
    r2 = vrf.context_reference(vrf.mint(sk, b"ctx-2"))
    assert abs(vsa.similarity(r1, r2)) < 0.1


def test_minted_reference_gates_a_vsa_record():
    # End-to-end: bind an object against a minted reference; the same verified reference
    # reconstructs it, a different one yields noise. The twin's reference-gated hiding.
    sk, _ = vrf.keygen(seed=SEED)
    ref = vrf.mint(sk, b"ctx:claim-42")
    r_c = vrf.context_reference(ref)
    rng = np.random.default_rng(0)
    obj = vsa.random_hv(vrf.DEFAULT_D, rng)
    medium = vsa.bind(obj, r_c)
    assert vsa.similarity(vsa.unbind(medium, r_c), obj) == pytest.approx(1.0, abs=1e-9)
    wrong = vrf.context_reference(vrf.mint(sk, b"ctx:other"))
    assert abs(vsa.similarity(vsa.unbind(medium, wrong), obj)) < 0.1
