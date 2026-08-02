"""Octave calibration of the layer grading — Da'at as self-similar identity, with teeth.

"Da'at = the identity" is refined here from a *point* into a *scale*. Index 2 is the octave
generator: the 2:1 ratio is the interval of octave-equivalence, at which a pitch returns to
itself one level up (real psychoacoustics, not mysticism). It is also the base of the
log/hyperbolic metric the manuscript's order-of-magnitude spectrum demands. So:

  * the `layer` grading is the OCTAVE index (log2 of scale);
  * `lift` (layer + 1) is +1 octave = a CONSTANT hyperbolic step — the isometry claim;
  * each octave is divided EVENLY into 7 steps; a pitch is (octave, step in 0..6);
  * `chroma` (the step, octave-invariant) is the identity that recurs: octave-equivalence,
    which is exactly the kernel's `ground(lift(t)) == t`.

Why seven, derived not imported. 7 is the smallest FULL REPTEND PRIME in base 10: 1/7 has the
maximal repeating period p-1 = 6, its repetend 142857 is the cyclic number (its multiples are
rotations; 142857 * 7 = 999999), and the residues 10^k mod 7 traverse the complete cycle
{1..6}. So the septimal division is the smallest subdivision of a cyclic interval that is
itself cyclically exact — Mach's economy picks the least such divisor, and it is 7. This is
number theory and acoustics — public, clean-room-safe — and it is what the user's
"septual divisors have repeating decimal remainders that are cyclic and exact" states.

Spoken word and tone. The octave is the identity of a *tone*; meaning rides pitch (prosody,
tone languages, vowel formants). The calibration is therefore the bridge from the abstract
grading to spoken semantics — the natural seam for a multiscript/phonetic layer.

This module is also the FALSIFIER for the naive claim "Da'at is the identity (a point)": it
shows chroma is invariant under lift (identity recurs) AND that register is an independent
coordinate — so the identity is identity-UP-TO-OCTAVE, self-similar, not a single point.
Both directions are tested.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


#: Each octave is divided evenly into seven steps (see module docstring for why 7).
STEPS_PER_OCTAVE = 7

#: Hyperbolic distance from origin per octave — the CONSTANT step that `lift` must realise.
OCTAVE_STEP = 1.0


# --------------------------------------------------------------------------- #
# Why seven: full reptend prime / cyclic exactness
# --------------------------------------------------------------------------- #


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True


def multiplicative_order(base: int, modulus: int) -> int:
    """The least k>0 with base**k ≡ 1 (mod modulus); 0 if base, modulus are not coprime."""
    if math.gcd(base, modulus) != 1:
        return 0
    order, value = 1, base % modulus
    while value != 1:
        value = (value * base) % modulus
        order += 1
    return order


def is_full_reptend_prime(p: int, base: int = 10) -> bool:
    """True when 1/p has the maximal repeating period p-1 — its reciprocal is a cyclic number."""
    return _is_prime(p) and multiplicative_order(base, p) == p - 1


def residue_cycle(p: int, base: int = 10) -> tuple:
    """The residues base**k mod p for k=1..(period). For a full reptend prime this is the
    complete cyclic system {1..p-1} — the septimal division traverses the whole group."""
    cycle, value = [], base % p
    for _ in range(multiplicative_order(base, p)):
        cycle.append(value)
        value = (value * base) % p
    return tuple(cycle)


# --------------------------------------------------------------------------- #
# The pitch: (octave, chroma) under octave-equivalence
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Pitch:
    octave: int  # register / layer (log2 scale)
    step: int    # chroma within the octave, 0..STEPS_PER_OCTAVE-1

    def __post_init__(self) -> None:
        if not 0 <= self.step < STEPS_PER_OCTAVE:
            raise ValueError(f"step must be in 0..{STEPS_PER_OCTAVE - 1}, got {self.step}")


def hyperbolic_depth(p: Pitch) -> float:
    """Hyperbolic distance from the origin (the fundamental) to this pitch — a constant
    OCTAVE_STEP per octave with 7 even sub-steps (the logarithmic/octave calibration)."""
    return (p.octave + p.step / STEPS_PER_OCTAVE) * OCTAVE_STEP


def poincare_radius(depth: float) -> float:
    """Euclidean radius in the Poincare ball for a hyperbolic depth from the origin
    (manuscript eq 83: the exponential map's radial squashing)."""
    return math.tanh(depth / 2.0)


def hyperbolic_distance(a: Pitch, b: Pitch) -> float:
    """Radial hyperbolic distance between two pitches, along the diameter geodesic."""
    return abs(hyperbolic_depth(a) - hyperbolic_depth(b))


def chroma(p: Pitch) -> int:
    """The octave-invariant identity — the pitch class, preserved by lift (octave-equivalence)."""
    return p.step


def lift_octave(p: Pitch) -> Pitch:
    """Up one octave: same chroma, next register. The calibration-level `lift`."""
    return Pitch(octave=p.octave + 1, step=p.step)
