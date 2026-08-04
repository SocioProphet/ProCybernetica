"""③ ONTOLOGY — the third organ of the knowledge-memory spine: ground the Aristotelian reading in the
AtomSpace type-inheritance lattice (the KKO / KBpedia substrate). Aristotle's primary/secondary substance
distinction (Categories §5) IS the instance/class distinction a type lattice is built from, so the
mapping is a faithful translation, not an invention:

  substance, SECONDARY subject  ("A man is an animal")  → InheritanceLink(man, animal)     a SUBCLASS edge
  substance, PRIMARY subject    ("Socrates is a man")   → MemberLink(Socrates, man)         an INSTANCE-of edge
  an accident (quality/relation/quantity/…)             → EvaluationLink(has_<cat>, List(S, V))  a property/relation

These are standard OpenCog AtomSpace atom types (ConceptNode / PredicateNode / InheritanceLink / MemberLink
/ EvaluationLink / ListLink) — the type lattice a PLN/atomspace reasoner walks. Grounding each ConceptNode
to a specific KKO class IRI (kko:Generals, kko:AttributesTypes, …) is the next step and needs the KKO
ontology; the lattice STRUCTURE — which the reasoner actually inherits over — is what this organ commits.

Deterministic, fail-closed (no predication ⇒ no atom), clean-room, pure-Python.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

from procyber.discourse.categories import (
    PRIMARY, Predication, RELATION, SUBSTANCE, analyze,
)

__all__ = ["Atom", "concept", "predicate_node", "inheritance", "member", "evaluation",
           "predication_to_atoms", "to_atomspace"]


@dataclass(frozen=True)
class Atom:
    """An AtomSpace atom: a NODE carries a `name`; a LINK carries `outgoing` atoms. `type` is the
    OpenCog atom type (ConceptNode, InheritanceLink, …)."""

    type: str
    name: str = ""
    outgoing: Tuple["Atom", ...] = field(default_factory=tuple)


def concept(name: str) -> Atom:
    return Atom("ConceptNode", name=name)


def predicate_node(name: str) -> Atom:
    return Atom("PredicateNode", name=name)


def inheritance(sub: Atom, sup: Atom) -> Atom:
    """sub ⊑ sup — a SUBCLASS edge in the type lattice (secondary substance)."""
    return Atom("InheritanceLink", outgoing=(sub, sup))


def member(instance: Atom, cls: Atom) -> Atom:
    """instance ∈ cls — an INSTANCE-of edge (primary substance)."""
    return Atom("MemberLink", outgoing=(instance, cls))


def evaluation(pred: Atom, *args: Atom) -> Atom:
    """pred(args…) — a property/relation as EvaluationLink over a ListLink of arguments."""
    return Atom("EvaluationLink", outgoing=(pred, Atom("ListLink", outgoing=tuple(args))))


def predication_to_atoms(p: Predication) -> List[Atom]:
    """One Aristotelian predication → the atoms it asserts in the type lattice."""
    subj = concept(p.subject)
    if p.category == SUBSTANCE:
        cls = concept(p.predicate)
        # PRIMARY subject = an individual ⇒ instance-of; SECONDARY = a universal ⇒ subclass.
        return [member(subj, cls)] if p.subject_kind == PRIMARY else [inheritance(subj, cls)]
    if p.category == RELATION:
        return [evaluation(predicate_node(p.predicate), subj, concept(p.object or ""))]
    # quality / quantity / the other accidents inhere in the subject as a unary predicate.
    return [evaluation(predicate_node("has_" + p.category), subj, concept(p.predicate))]


def to_atomspace(text: str) -> List[Atom]:
    """Text → the AtomSpace atoms its predications license (fail-closed: no copula ⇒ no atom)."""
    atoms: List[Atom] = []
    for p in analyze(text):
        atoms.extend(predication_to_atoms(p))
    return atoms
