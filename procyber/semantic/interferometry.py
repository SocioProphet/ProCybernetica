"""Interferometric diff — the twin's primary read (spec §C): "return the fringe, not the score".

The default read of two identity states is NOT "return the reputation number". It is the
*interference* between them — the phase fringe that appears exactly where state moved. This is
what earns the name "prophet": reading phase detects change far below the magnitude at which a
scalar score would budge (sub-threshold sensitivity), and because the medium is holographic,
a local unauthorised write perturbs the fringe globally (tamper-evidence for free).

Reads, all over the ℂ^D VSA medium (vsa.py):

    fringe(a, b)                     elementwise phase difference angle(a ⊙ conj(b)) — 0 where equal
    drift(a, b)                      scalar summary in [0,1] (1 - similarity) — the *lagging* indicator
    drift_map(H_live, H_stored, refs) per-context drift by unbinding each reference — WHICH context moved
    is_tampered(H_orig, H_now)       any fringe beyond tol ⇒ the medium was written

`refs` are the VRF-minted context references (vrf.py). Proven in tests/test_interferometry.py,
including the load-bearing property: a change one bundled record makes barely moves the scalar
similarity (∝ 1/N) yet lights up sharply in the per-reference fringe — fringe ≫ score.
"""
from __future__ import annotations

import numpy as np

from procyber.semantic import vsa

__all__ = ["fringe", "drift", "drift_map", "is_tampered", "DEFAULT_TOL"]

DEFAULT_TOL = 1e-6


def fringe(a: vsa.HV, b: vsa.HV) -> np.ndarray:
    """Elementwise phase difference between two states — the interference pattern. ~0 where
    the states agree, nonzero where they moved. This is the live drift/tamper map (§C, Live)."""
    return np.angle(a * np.conjugate(b))


def drift(a: vsa.HV, b: vsa.HV) -> float:
    """Scalar drift in [0,1] (1 - similarity) — the *score* view, kept only as a summary. The
    point of the twin is that this lags the fringe (see drift_map): use it for display, not detection."""
    return float(np.clip(1.0 - vsa.similarity(a, b), 0.0, 1.0))


def drift_map(h_live: vsa.HV, h_stored: vsa.HV, references) -> dict[int, float]:
    """Per-context drift: unbind both media with each reference and measure how much the
    reconstructed object moved. Reveals WHICH bound context changed, not just that something did.
    Returns {reference_index: drift_in_[0,1]}."""
    out: dict[int, float] = {}
    for i, r in enumerate(references):
        out[i] = drift(vsa.unbind(h_live, r), vsa.unbind(h_stored, r))
    return out


def is_tampered(h_original: vsa.HV, h_current: vsa.HV, tol: float = DEFAULT_TOL) -> bool:
    """True iff the current medium differs from the original beyond `tol`. Holographic: because
    every record is spread across all components, a local unauthorised write shows up in the
    global fringe — you can detect tamper without knowing what was altered (§C)."""
    return bool(np.max(np.abs(fringe(h_current, h_original))) > tol)
