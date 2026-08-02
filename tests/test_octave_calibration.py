"""Tests for the octave calibration — the Da'at falsifier, both ways.

Pins three things with teeth: (1) `lift` is a constant octave step (the isometry that grounds
Poincare<->layer); (2) SEVEN is derived, not chosen — it is the smallest full reptend prime, so
the septimal division of a cyclic interval is itself cyclically exact; (3) the naive claim
"Da'at is the identity (a point)" is FALSE — the identity is identity-up-to-octave, and register
is an independent coordinate.
"""

from __future__ import annotations

import math

import pytest

from procyber.semantic.semantic_algebra import ground, lift, prim
from procyber.semantic.octave_calibration import (
    OCTAVE_STEP,
    STEPS_PER_OCTAVE,
    Pitch,
    chroma,
    hyperbolic_depth,
    hyperbolic_distance,
    is_full_reptend_prime,
    lift_octave,
    multiplicative_order,
    poincare_radius,
    residue_cycle,
)


# --------------------------------------------------------------------------- #
# Why SEVEN — derived, not imported
# --------------------------------------------------------------------------- #


def test_seven_is_the_smallest_full_reptend_prime():
    # 2,3,5 are not full reptend in base 10 (2,5 terminate; 3 has period 1, not p-1);
    # 7 is the FIRST prime whose reciprocal has the maximal period p-1 = 6.
    assert not is_full_reptend_prime(2)
    assert not is_full_reptend_prime(3)
    assert not is_full_reptend_prime(5)
    assert is_full_reptend_prime(7)
    assert STEPS_PER_OCTAVE == 7


def test_one_seventh_is_the_cyclic_number_142857():
    # period 6 = 7-1; the repetend is 142857; 142857 * 7 == 999999 (closes exactly).
    assert multiplicative_order(10, 7) == 6
    repetend = "".join(str((10 ** k // 7) % 10) for k in range(1, 7))
    assert repetend == "142857"
    assert 142857 * 7 == 999999


def test_septimal_residues_traverse_the_complete_cycle():
    # the residues 10^k mod 7 are a permutation of {1..6} — a complete, exact cyclic system.
    assert sorted(residue_cycle(7)) == [1, 2, 3, 4, 5, 6]


# --------------------------------------------------------------------------- #
# lift is a constant octave step (the isometry grounding Poincare<->layer)
# --------------------------------------------------------------------------- #


def test_lift_is_a_constant_hyperbolic_step_at_every_octave():
    for octave in range(0, 6):
        p = Pitch(octave=octave, step=0)
        assert math.isclose(hyperbolic_distance(p, lift_octave(p)), OCTAVE_STEP)


def test_seven_even_steps_close_the_octave_exactly():
    # 7 equal sub-steps of OCTAVE_STEP/7 sum to exactly one octave.
    base = Pitch(octave=1, step=0)
    for k in range(STEPS_PER_OCTAVE - 1):
        a, b = Pitch(1, k), Pitch(1, k + 1)
        assert math.isclose(hyperbolic_distance(a, b), OCTAVE_STEP / STEPS_PER_OCTAVE)
    # stepping the full seven lands exactly on the next octave's fundamental
    assert math.isclose(hyperbolic_depth(Pitch(2, 0)) - hyperbolic_depth(base), OCTAVE_STEP)


def test_radius_is_monotone_and_stays_in_the_open_ball():
    depths = [hyperbolic_depth(Pitch(o, s)) for o in range(4) for s in range(STEPS_PER_OCTAVE)]
    radii = [poincare_radius(d) for d in depths]
    assert radii == sorted(radii)          # monotone in depth
    assert all(0.0 <= r < 1.0 for r in radii)  # inside the Poincare ball


# --------------------------------------------------------------------------- #
# The Da'at falsifier — identity is up-to-octave, not a point (both ways)
# --------------------------------------------------------------------------- #


def test_chroma_is_invariant_under_lift_the_identity_recurs():
    for k in range(STEPS_PER_OCTAVE):
        p = Pitch(octave=0, step=k)
        assert chroma(p) == chroma(lift_octave(p))  # octave-equivalence: I = I at each level


def test_identity_is_up_to_octave_not_a_single_point():
    # same chroma at different octaves are octave-equivalent (SAME identity)...
    lo, hi = Pitch(0, 3), Pitch(2, 3)
    assert chroma(lo) == chroma(hi)
    # ...but they sit at DIFFERENT hyperbolic depth: register is a real, independent coordinate.
    # So "Da'at is a single identity point" is FALSE; "identity up to octave" is what holds.
    assert hyperbolic_depth(lo) != hyperbolic_depth(hi)


def test_different_chroma_are_not_the_same_identity():
    assert chroma(Pitch(1, 2)) != chroma(Pitch(1, 5))  # the reject path


# --------------------------------------------------------------------------- #
# Kernel connection: the kernel `lift` IS one octave
# --------------------------------------------------------------------------- #


def test_kernel_lift_is_one_octave_and_ground_recovers_the_chroma():
    t = prim("FST")
    up = lift(t)
    assert up.layer == t.layer + 1        # one octave up (register +1)
    assert ground(up) == t                # ground∘lift = id: the chroma/identity recurs
