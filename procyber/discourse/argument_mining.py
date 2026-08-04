"""Argument mining — the one new organ of the argumentation surface. Turns a message into a
*typed argument graph*: claims, their premises, and the support/attack relations between them —
the structure a scalar "engagement" score throws away.

This v1 is a **deterministic, rule-based** extractor over discourse connectives (Mann & Thompson's
rhetorical relations; the "because / therefore / however" cues that a millennium of argumentation
theory — back to Aristotle's premise→conclusion — reads as structure). It is fail-closed: it never
invents a relation a connective does not license, so an unmarked sentence is a bare claim, not a
hallucinated argument. An LLM-backed miner is a drop-in behind the `Miner` protocol — same output
type, richer extraction — but the rule-based baseline is what we can prove.

Composes upward without coupling: `mine` optionally feeds entity co-occurrences to any object with
a `co_occur(a, b)` method — e.g. `procyber.semantic.dynamics.AssociativeMemory` (the ① memory
organ) — so repeated claim/entity pairs consolidate. It is duck-typed, so this module carries no
import dependency on the dynamics organ.

Theorems in tests/test_argument_mining.py: premise→claim support, premise→conclusion support,
rebuttal attack (intra- and inter-sentence), no-marker⇒bare-claim (no hallucinated structure),
determinism, and the co-occurrence hand-off.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from itertools import combinations
from typing import Dict, List, Optional, Protocol, Tuple

__all__ = [
    "CLAIM", "PREMISE", "SUPPORT", "ATTACK",
    "Unit", "Relation", "ArgumentGraph", "Miner", "mine",
]

# roles
CLAIM = "claim"
PREMISE = "premise"
# relation kinds
SUPPORT = "support"
ATTACK = "attack"

# Discourse connectives, mapped to how they wire the segments they join.
#   support_backward : "<claim> BECAUSE <premise>"      → premise --support--> claim
#   support_forward  : "<premise> THEREFORE <claim>"    → premise --support--> claim
#   attack           : "<claim> HOWEVER <rebuttal>"     → rebuttal --attack--> claim
_SUPPORT_BACKWARD = ("because", "since", "given that", "due to")
_SUPPORT_FORWARD = ("therefore", "thus", "hence", "consequently")
_ATTACK = ("however", "but", "although", "though", "yet", "nevertheless", "whereas",
           "on the other hand", "on the contrary")

_MARKERS: Dict[str, str] = {}
_MARKERS.update({m: "support_backward" for m in _SUPPORT_BACKWARD})
_MARKERS.update({m: "support_forward" for m in _SUPPORT_FORWARD})
_MARKERS.update({m: "attack" for m in _ATTACK})

# Words that are capitalised for grammar (sentence-initial / pronouns / the markers) rather than
# because they name an entity — excluded from the co-occurrence signal.
_ENTITY_STOP = {
    "the", "a", "an", "it", "he", "she", "they", "we", "you", "i", "this", "that", "these",
    "those", "there", "here", "but", "however", "therefore", "because", "since", "thus", "hence",
    "although", "though", "yet", "so", "and", "or", "if", "when", "then",
}


class Miner(Protocol):
    """The extraction contract. A rule-based `mine` satisfies it; an LLM-backed miner is a drop-in."""

    def __call__(self, text: str, *, cooccurrence_sink: Optional["CooccurrenceSink"] = None) -> "ArgumentGraph":
        ...


class CooccurrenceSink(Protocol):
    """Anything that consolidates entity associations — e.g. dynamics.AssociativeMemory."""

    def co_occur(self, a: str, b: str) -> None:
        ...


@dataclass(frozen=True)
class Unit:
    """An argumentative discourse unit."""

    id: str
    text: str
    role: str  # CLAIM | PREMISE


@dataclass(frozen=True)
class Relation:
    """A directed argumentative relation between units (source → target)."""

    source: str
    target: str
    kind: str  # SUPPORT | ATTACK


@dataclass
class ArgumentGraph:
    """The typed fragment an argument miner emits — ready for the discourse graph (hellgraph)."""

    units: List[Unit] = field(default_factory=list)
    relations: List[Relation] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "units": [{"id": u.id, "text": u.text, "role": u.role} for u in self.units],
            "relations": [{"source": r.source, "target": r.target, "kind": r.kind} for r in self.relations],
        }


def _split_sentences(text: str) -> List[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]


def _first_marker(text: str) -> Optional[Tuple[int, int, str, str]]:
    """Earliest connective in `text`: (start, end, marker, direction). Word-boundary, case-insensitive."""
    best: Optional[Tuple[int, int, str, str]] = None
    for marker, direction in _MARKERS.items():
        m = re.search(rf"\b{re.escape(marker)}\b", text, re.IGNORECASE)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), m.end(), marker, direction)
    return best


def _leading_marker(sentence: str) -> Optional[Tuple[str, str, str]]:
    """If `sentence` opens with a connective ("However, X"): (marker, direction, rest)."""
    for marker, direction in _MARKERS.items():
        m = re.match(rf"^{re.escape(marker)}\b[\s,]*", sentence, re.IGNORECASE)
        if m:
            return marker, direction, sentence[m.end():].strip()
    return None


def _entities(text: str) -> List[str]:
    """Named entities (capitalised words that aren't grammar-capitalised), lowercased, de-duplicated."""
    out: List[str] = []
    for w in re.findall(r"\b[A-Z][A-Za-z]+\b", text):
        lw = w.lower()
        if lw not in _ENTITY_STOP and lw not in out:
            out.append(lw)
    return out


def mine(text: str, *, cooccurrence_sink: Optional[CooccurrenceSink] = None) -> ArgumentGraph:
    """Extract the argument graph from `text`. Deterministic and fail-closed: only connective-
    licensed relations are emitted. Optionally feeds entity co-occurrences to `cooccurrence_sink`."""
    graph = ArgumentGraph()
    counter = [0]

    def add(segment: str, role: str) -> Unit:
        u = Unit(id=f"u{counter[0]}", text=segment.strip(), role=role)
        counter[0] += 1
        graph.units.append(u)
        return u

    prev_claim: Optional[str] = None  # id of the last claim, for inter-sentence relations

    for sentence in _split_sentences(text):
        lead = _leading_marker(sentence)
        if lead is not None and prev_claim is not None and lead[2]:
            _, direction, rest = lead
            if direction == "attack":
                u = add(rest, CLAIM)
                graph.relations.append(Relation(u.id, prev_claim, ATTACK))
                prev_claim = u.id
                continue
            if direction == "support_forward":  # "Therefore, X" — the prior claim supports X
                u = add(rest, CLAIM)
                graph.relations.append(Relation(prev_claim, u.id, SUPPORT))
                prev_claim = u.id
                continue

        hit = _first_marker(sentence)
        if hit is not None and hit[0] > 0 and sentence[hit[1]:].strip():
            _, end, _, direction = hit
            before, after = sentence[:hit[0]].strip(" ,;"), sentence[end:].strip(" ,;")
            if direction == "support_backward":       # claim BECAUSE premise
                claim, premise = add(before, CLAIM), add(after, PREMISE)
                graph.relations.append(Relation(premise.id, claim.id, SUPPORT))
                prev_claim = claim.id
            elif direction == "support_forward":       # premise THEREFORE claim
                premise, claim = add(before, PREMISE), add(after, CLAIM)
                graph.relations.append(Relation(premise.id, claim.id, SUPPORT))
                prev_claim = claim.id
            else:                                       # claim HOWEVER rebuttal
                claim, rebuttal = add(before, CLAIM), add(after, CLAIM)
                graph.relations.append(Relation(rebuttal.id, claim.id, ATTACK))
                prev_claim = claim.id
        else:
            prev_claim = add(sentence, CLAIM).id  # no connective ⇒ a bare claim, no invented relation

    if cooccurrence_sink is not None:
        for u in graph.units:
            for a, b in combinations(_entities(u.text), 2):
                cooccurrence_sink.co_occur(a, b)

    return graph
