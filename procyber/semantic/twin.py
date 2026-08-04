"""The Multiverseal Twin — the P2 capstone composing the VSA medium (vsa), VRF references (vrf),
and the interferometric read (interferometry) into a federation-facing identity/reputation
projection of a sovereign core.

The sovereign CORE holds a master key (msk); the TWIN is the object that touches the untrusted
world, carries imported reputation, and is watched/replayed by relying parties. Two invariants
from the spec are enforced by construction here:

- **Reference-at-ingest (§B).** A value is admissible only *bound against a VRF-minted context
  reference* — never stored bare. `attest` mints the reference (only the core key can) and folds
  `bind(value, r_c)` into the medium; there is no code path that stores a bare value.
- **Reads are interferometric (§C).** `diff`/`is_tampered` return the fringe between two twin
  states, not a scalar score — phase is provenance.

Everything is proof-carrying: only the core mints (vrf), reconstruction needs the reference
(vsa reference-gated hiding), and any write to the medium is tamper-evident (interferometry).

`TemporalTwin` extends the capstone with a LIVING medium: attestations reinforce a two-timescale
strength (procyber.semantic.dynamics) and the medium weights each record by it, so an unrehearsed
association fades-but-persists while a re-attested one stays sharp — memory with a forgetting curve.
"""
from __future__ import annotations

import numpy as np

from procyber.semantic import dynamics
from procyber.semantic import interferometry as itf
from procyber.semantic import vrf, vsa

__all__ = ["MultiversealTwin", "TemporalTwin"]


class MultiversealTwin:
    """A sovereign identity/reputation twin. Construct with an optional 32-byte `seed` for a
    deterministic (sealed) core; otherwise the master key is random."""

    def __init__(self, seed: bytes | None = None, d: int = vrf.DEFAULT_D) -> None:
        self._sk, self.verify_key = vrf.keygen(seed)
        self.d = d
        # context (bytes) -> (VerifiableReference, bound record = bind(value, r_c))
        self._records: dict[bytes, tuple[vrf.VerifiableReference, vsa.HV]] = {}

    def attest(self, context: bytes, value: vsa.HV) -> vrf.VerifiableReference:
        """Ingest an attestation of `value` under `context`. Mints the context reference (only
        this core can), binds the value against it (reference-at-ingest — never bare), and folds
        it into the medium. Returns the verifiable reference relying parties check."""
        if value.shape != (self.d,):
            raise ValueError(f"value must be a ℂ^{self.d} hypervector")
        ref = vrf.mint(self._sk, context)
        r_c = vrf.reference_hv(ref.proof, self.d)
        self._records[context] = (ref, vsa.bind(value, r_c))
        return ref

    def medium(self) -> vsa.HV:
        """The bundled twin state H = Σ bound records — the federation-facing projection. Opaque
        without a reference (a hiding commitment to its contents)."""
        if not self._records:
            raise ValueError("empty twin — nothing attested")
        return vsa.bundle(rec for _, rec in self._records.values())

    def recall(self, context: bytes) -> vsa.HV:
        """Reconstruct the value attested under `context` by illuminating the medium with its
        reference (approximate — carries crosstalk from the other records)."""
        ref, _ = self._records[context]
        return vsa.reconstruct(self.medium(), vrf.reference_hv(ref.proof, self.d))

    def verify(self, ref: vrf.VerifiableReference) -> bool:
        """True iff `ref` is a genuine reference (its proof verifies). Relying parties call this;
        they cannot forge a reference this — or any — twin would accept."""
        return vrf.verify(ref)

    def diff(self, other_medium: vsa.HV) -> np.ndarray:
        """Interferometric read against another twin state — the fringe, not a score (§C)."""
        return itf.fringe(self.medium(), other_medium)

    def is_tampered(self, snapshot: vsa.HV) -> bool:
        """True iff the medium has moved since `snapshot` — holographic tamper-evidence."""
        return itf.is_tampered(snapshot, self.medium())


class TemporalTwin(MultiversealTwin):
    """A Multiverseal Twin whose medium is LIVING: each attestation reinforces its context's
    two-timescale strength (procyber.semantic.dynamics), and the federation-facing `medium` weights
    every bound record by that strength. An association re-attested often stays sharp; one left
    unrehearsed decays-but-persists (fast ≫ slow) and its recall fidelity fades — memory with a
    forgetting curve, on the same construction as the association graph.

    The base twin's guarantees are unchanged: reference-at-ingest, only-the-core-mints, tamper-
    evident reads. Strength only *weights* records already admitted the reference-gated way.
    """

    def __init__(self, seed: bytes | None = None, d: int = vrf.DEFAULT_D, *,
                 fast_gain: float = 0.5, slow_gain: float = 0.2,
                 fast_decay: float = 0.4, slow_decay: float = 0.02) -> None:
        super().__init__(seed, d)
        self._fast: dict[bytes, float] = {}
        self._slow: dict[bytes, float] = {}
        self._gains = (fast_gain, slow_gain)
        self._decays = (fast_decay, slow_decay)

    def attest(self, context: bytes, value: vsa.HV) -> vrf.VerifiableReference:
        ref = super().attest(context, value)
        f, s = dynamics.potentiate(
            self._fast.get(context, 0.0), self._slow.get(context, 0.0),
            fast_gain=self._gains[0], slow_gain=self._gains[1],
        )
        self._fast[context], self._slow[context] = f, s
        return ref

    def tick(self, steps: int = 1) -> None:
        """Advance time `steps` with no reinforcement: every context's strength decays (fast ≫ slow)."""
        for c in list(self._fast):
            self._fast[c], self._slow[c] = dynamics.relax(
                self._fast[c], self._slow[c],
                fast_decay=self._decays[0], slow_decay=self._decays[1], steps=steps,
            )

    def strength(self, context: bytes) -> float:
        """Current consolidated strength of `context` in [0,1] (recent ⊕ durable)."""
        return dynamics.combine(self._fast.get(context, 0.0), self._slow.get(context, 0.0))

    def medium(self) -> vsa.HV:
        """The LIVING federation-facing medium: Σ strength(context) · bound record. Unrehearsed
        records fade from it; re-attested ones stay sharp."""
        if not self._records:
            raise ValueError("empty twin — nothing attested")
        return vsa.bundle(self.strength(ctx) * rec for ctx, (_, rec) in self._records.items())
