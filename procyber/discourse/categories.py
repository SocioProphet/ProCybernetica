"""Aristotelian category typing (③ ontology) for the argumentation surface — grounds the units the
argument miner emits in Aristotle's Categories (the praedicamenta): substance and the nine accidents
that can only be predicated OF a substance. This is the ONTOLOGY layer of the knowledge-memory
spine, and it yields the primary/secondary-substance distinction the AtomSpace type lattice / KKO
consumes.

Aristotle §5: a *primary substance* is the individual (Socrates) — an INSTANCE; a *secondary
substance* is its species or genus (man, animal) — a CLASS/universal. The other nine categories
(quantity, quality, relation, place, time, position, state, action, passion) are accidents: they
inhere in a substance and cannot stand on their own.

v1 reads the predication a copula licenses — deterministic and fail-closed:
  "S is a P"          ⇒ S is an instance of the class P   (substance: secondary)
  "S is Q"            ⇒ S has the quality Q                (quality)
  "S is …-er than O"  ⇒ a relation between S and O         (relation)
  "S is <numeral>"    ⇒ how-much                           (quantity)
What no pattern licenses is left UNKNOWN, not forced. A learned/ontology-backed classifier across
all ten categories is the upgrade; the copula core is what we can prove. (Known v1 limit: a
sentence-initial common noun can be mistaken for a proper one — the primary/secondary call is a
capitalisation heuristic, not a parse.)
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, List, Optional

__all__ = [
    "SUBSTANCE", "QUANTITY", "QUALITY", "RELATION", "PLACE", "TIME", "POSITION", "STATE",
    "ACTION", "PASSION", "CATEGORIES", "ACCIDENTS", "UNKNOWN", "PRIMARY", "SECONDARY",
    "Predication", "analyze", "categorize_graph",
]

# The ten categories (Aristotle, Categories 1b25–2a4). Substance is primary; the rest are accidents.
SUBSTANCE = "substance"
QUANTITY = "quantity"
QUALITY = "quality"
RELATION = "relation"
PLACE = "place"        # where
TIME = "time"          # when
POSITION = "position"  # being-in-a-position
STATE = "state"        # having
ACTION = "action"      # doing
PASSION = "passion"    # being-affected

CATEGORIES = (SUBSTANCE, QUANTITY, QUALITY, RELATION, PLACE, TIME, POSITION, STATE, ACTION, PASSION)
ACCIDENTS = tuple(c for c in CATEGORIES if c != SUBSTANCE)  # inhere in a substance, never alone
UNKNOWN = "unknown"

# Substance sub-typing (§5): primary = the individual (instance); secondary = species/genus (class).
PRIMARY = "primary"      # instance      → an AtomSpace instance node
SECONDARY = "secondary"  # class/genus   → an AtomSpace type node

_COPULA = re.compile(r"\b(?:is|are|was|were)\b", re.IGNORECASE)
_SUBJ_STOP = {"the", "a", "an", "this", "that", "these", "those", "it", "he", "she", "they", "we",
              "you", "i", "there"}


def _sentences(text: str) -> List[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]


def _subject(phrase: str) -> tuple[str, str]:
    """(name, kind) for a subject phrase. A capitalised head word reads as a proper noun ⇒ PRIMARY
    (instance); otherwise the head is a common noun ⇒ SECONDARY (class)."""
    words = re.findall(r"[A-Za-z]+", phrase)
    for w in words:
        if w[0].isupper() and w.lower() not in _SUBJ_STOP:
            return w.lower(), PRIMARY
    return (words[-1].lower() if words else phrase.strip().lower()), SECONDARY


def _head(phrase: str) -> str:
    words = re.findall(r"[A-Za-z]+", phrase)
    return words[-1].lower() if words else phrase.strip().lower()


@dataclass(frozen=True)
class Predication:
    """One predication read off a copula: the accident (or secondary substance) predicated of a
    subject. `object` is set only for relations (S is …-er than O)."""

    subject: str
    subject_kind: str  # PRIMARY | SECONDARY
    category: str      # one of CATEGORIES
    predicate: str
    object: Optional[str] = None


def _analyze_sentence(sentence: str) -> Optional[Predication]:
    m = _COPULA.search(sentence)
    if not m:
        return None
    subj_phrase = sentence[:m.start()].strip(" ,.;")
    rest = sentence[m.end():].strip(" ,.;")
    if not subj_phrase or not rest:
        return None
    subject, kind = _subject(subj_phrase)

    # relation: a comparative with "than"
    than = re.search(r"\bthan\b\s+(?P<obj>[A-Za-z]+)", rest, re.IGNORECASE)
    if than and re.search(r"\b(?:more|less)\b|\b\w+er\b", rest, re.IGNORECASE):
        pred = re.split(r"\s+than\b", rest, maxsplit=1, flags=re.IGNORECASE)[0]
        return Predication(subject, kind, RELATION, _head(pred), than.group("obj").lower())

    # quantity: a numeral predicate
    num = re.match(r"(?:about|around|nearly|over|under)?\s*(?P<n>\d[\d,]*)\b", rest, re.IGNORECASE)
    if num:
        return Predication(subject, kind, QUANTITY, num.group("n"), None)

    # substance: "a/an/the <class>" ⇒ instance-of a secondary substance
    cls = re.match(r"(?:an?|the)\s+(?P<cls>[A-Za-z]+)", rest, re.IGNORECASE)
    if cls:
        return Predication(subject, kind, SUBSTANCE, cls.group("cls").lower(), None)

    # else: a bare predicate ⇒ quality
    return Predication(subject, kind, QUALITY, _head(rest), None)


def analyze(text: str) -> List[Predication]:
    """Predications licensed by the copulas in `text` (one per matching sentence). Fail-closed:
    a sentence with no copula pattern yields nothing rather than a forced category."""
    out: List[Predication] = []
    for sentence in _sentences(text):
        p = _analyze_sentence(sentence)
        if p is not None:
            out.append(p)
    return out


def categorize_graph(graph) -> Dict[str, List[Predication]]:
    """Type each unit of an argument graph (procyber.discourse.argument_mining.ArgumentGraph):
    `unit.id` → the predications its text licenses. Substance predications are the instance-of /
    class edges for the discourse graph; quality/relation are the accident edges."""
    return {u.id: analyze(u.text) for u in graph.units}
