"""Associative-memory dynamics for the semantic substrate — the *temporal* organ that the static
VSA/HRR medium (procyber.semantic.vsa) and the Multiverseal Twin (procyber.semantic.twin) lack:
how associations between entities STRENGTHEN with repetition, CONSOLIDATE from a transient trace
into a durable one, and FADE-BUT-PERSIST without reinforcement.

Construction (clean-room; the science is public and long-standing):
- **Two-timescale Hebbian plasticity.** A reinforcement carries a fast variable and a slow one.
  It potentiates the fast variable (a saturating jump toward 1); the slow variable integrates the
  *fast* one, so it consolidates only under repetition. This is the complementary fast/slow split
  of the complementary-learning-systems account (McClelland, McNaughton & O'Reilly, 1995) and the
  cascade model of synaptic memory (Fusi, Drew & Abbott, 2005); Hebbian potentiation is Hebb (1949).
  The law is exposed as `potentiate` / `relax` / `combine` so both edge weights (here) and node
  strengths (the living twin medium) share one construction.
- **Graceful forgetting.** Between reinforcements both variables decay, the fast one much faster
  than the slow one, so a single reinforcement leaves only a transient trace while a consolidated
  one persists long after — graceful degradation at the edge, never a cliff.
- **Bounded spreading activation** for read (Collins & Loftus, 1975): seeds are pinned, activation
  propagates along effective-weight edges under a contraction (damping < 1) for a fixed number of
  hops, and the most-activated nodes are returned. Bounded and terminating by construction — a
  governed loop, not an open one.

Binds upward (world-model + ontogenesis): the association graph is a world-model of entity
relations; `consolidated_associations` is the durable projection a twin medium should reflect and
the shaped edge-set ontogenesis should ingest — this module produces upward, it is not a
downward-only consumer.

Deterministic: the dynamics are a pure function of the event/tick sequence (no RNG). Theorems in
tests/test_dynamics.py: consolidation-requires-repetition, fade-but-persist, recency-is-not-
persistence, bounded spreading activation, associative & multi-hop retrieval.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from itertools import combinations
from typing import Dict, Hashable, Iterable, List, Sequence, Tuple

Entity = Hashable
Edge = Tuple[Entity, Entity]

__all__ = ["AssociativeMemory", "combine", "potentiate", "relax"]


def combine(fast: float, slow: float) -> float:
    """Combine the fast and slow variables into one effective weight in [0,1] (noisy-OR), monotone
    in both — recent OR consolidated reads as strong."""
    return fast + slow - fast * slow


def potentiate(fast: float, slow: float, *, fast_gain: float, slow_gain: float) -> Tuple[float, float]:
    """One reinforcement event under the two-timescale law: the fast variable jumps toward 1
    (saturating), and the slow variable integrates the *new* fast so it consolidates only under
    repetition. Reusable for both edge weights and node strengths."""
    f = fast + fast_gain * (1.0 - fast)
    s = slow + slow_gain * f * (1.0 - slow)
    return f, s


def relax(fast: float, slow: float, *, fast_decay: float, slow_decay: float, steps: int = 1) -> Tuple[float, float]:
    """Decay `steps` ticks with no reinforcement — fast much faster than slow (fade-but-persist)."""
    if steps <= 0:
        return fast, slow
    return fast * (1.0 - fast_decay) ** steps, slow * (1.0 - slow_decay) ** steps


@dataclass
class AssociativeMemory:
    """A directed association graph with coupled fast/slow edge variables.

    The parameters are plasticity rates; the defaults give a ~20x fast-vs-slow decay separation,
    so a single co-occurrence is transient while a repeated one consolidates and persists.
    """

    fast_gain: float = 0.5       # α: saturating potentiation of the fast variable per co-occurrence
    slow_gain: float = 0.2       # β: rate the slow variable integrates the (high) fast variable
    fast_decay: float = 0.4      # per-tick fractional decay of the fast variable
    slow_decay: float = 0.02     # per-tick fractional decay of the slow variable (<< fast_decay)
    spread_damping: float = 0.5  # γ: per-hop contraction for spreading activation (< 1 ⇒ bounded)

    _fast: Dict[Edge, float] = field(default_factory=dict, init=False, repr=False)
    _slow: Dict[Edge, float] = field(default_factory=dict, init=False, repr=False)
    _out: Dict[Entity, set] = field(default_factory=dict, init=False, repr=False)

    # ---- write path ----
    def observe(self, entities: Iterable[Entity]) -> None:
        """Ingest a document's co-occurring entities: reinforce every unordered pair once."""
        items = list(dict.fromkeys(entities))  # de-duplicate, preserve arrival order
        for a, b in combinations(items, 2):
            self.co_occur(a, b)

    def co_occur(self, a: Entity, b: Entity) -> None:
        """Reinforce the association between `a` and `b` (symmetric potentiation)."""
        if a == b:
            return
        for i, j in ((a, b), (b, a)):
            f, s = potentiate(
                self._fast.get((i, j), 0.0), self._slow.get((i, j), 0.0),
                fast_gain=self.fast_gain, slow_gain=self.slow_gain,
            )
            self._fast[(i, j)] = f
            self._slow[(i, j)] = s
            self._out.setdefault(i, set()).add(j)

    def tick(self, steps: int = 1) -> None:
        """Advance time `steps` with no reinforcement: decay both variables (fast >> slow)."""
        if steps <= 0:
            return
        for e in list(self._fast):
            self._fast[e], self._slow[e] = relax(
                self._fast[e], self._slow[e],
                fast_decay=self.fast_decay, slow_decay=self.slow_decay, steps=steps,
            )

    # ---- inspection ----
    def fast(self, a: Entity, b: Entity) -> float:
        return self._fast.get((a, b), 0.0)

    def slow(self, a: Entity, b: Entity) -> float:
        return self._slow.get((a, b), 0.0)

    def effective(self, a: Entity, b: Entity) -> float:
        """Read-time association strength (fast ⊕ slow, noisy-OR, in [0,1])."""
        return combine(self._fast.get((a, b), 0.0), self._slow.get((a, b), 0.0))

    def consolidated_associations(self, threshold: float = 0.25) -> List[Tuple[Entity, Entity, float]]:
        """Durable associations (slow variable ≥ `threshold`), strongest first — the long-term
        projection a twin medium reflects and ontogenesis ingests. Unordered pairs, de-duplicated."""
        seen: set = set()
        out: List[Tuple[Entity, Entity, float]] = []
        for (a, b), s in self._slow.items():
            key = frozenset((a, b))
            if s >= threshold and key not in seen:
                seen.add(key)
                out.append((a, b, s))
        out.sort(key=lambda t: t[2], reverse=True)
        return out

    # ---- read path: bounded spreading activation ----
    def spread(self, seeds: Sequence[Entity], steps: int = 3) -> Dict[Entity, float]:
        """Propagate activation from `seeds` along effective-weight edges for `steps` hops.

        Seeds are pinned to 1.0 (sources); each hop contracts by `spread_damping` < 1 and clamps
        to [0,1], so activation is bounded and the loop terminates in exactly `steps` — a governed
        read, never an open one. A node farther from every seed receives strictly less activation.
        """
        act: Dict[Entity, float] = {s: 1.0 for s in seeds}
        for _ in range(max(0, steps)):
            nxt: Dict[Entity, float] = {s: 1.0 for s in seeds}
            for i, ai in act.items():
                for j in self._out.get(i, ()):  # outgoing edges (symmetric with co_occur)
                    w = self.effective(i, j)
                    nxt[j] = min(1.0, nxt.get(j, 0.0) + self.spread_damping * w * ai)
            act = nxt
        return act

    def recall(self, seeds: Sequence[Entity], k: int = 5, steps: int = 3) -> List[Tuple[Entity, float]]:
        """Top-`k` most-activated non-seed entities for `seeds` — associative retrieval."""
        act = self.spread(seeds, steps=steps)
        seedset = set(seeds)
        ranked = [(n, a) for n, a in act.items() if n not in seedset and a > 0.0]
        ranked.sort(key=lambda t: t[1], reverse=True)
        return ranked[:k]
