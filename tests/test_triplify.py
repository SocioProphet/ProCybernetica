"""Theorems of ④ triplification (procyber.lod.triplify): each Aristotelian predication becomes exactly
one RDF triple, the category fixing the predicate; substance uses standard rdf:type; fail-closed."""
from __future__ import annotations

from procyber.lod.triplify import DISC_NS, RDF_TYPE, Triple, triplify


def _one(text: str) -> Triple:
    ts = triplify(text)
    assert len(ts) == 1, f"expected one triple from {text!r}, got {ts}"
    return ts[0]


def test_substance_is_a_standard_rdf_type_triple():
    # THEOREM: "S is a P" ⇒ (S, rdf:type, P) — interoperable with any RDF/SPARQL consumer.
    t = _one("Socrates is a man.")
    assert t == Triple("socrates", RDF_TYPE, "man", "substance")


def test_quality_is_an_accident_predicate():
    t = _one("Cats are great.")
    assert t.subject == "cats" and t.predicate == DISC_NS + "has_quality" and t.object == "great"


def test_relation_carries_the_comparative_and_object():
    # THEOREM: "S is …-er than O" ⇒ (S, disc:<comparative>, O).
    t = _one("Bob is taller than Alice.")
    assert t == Triple("bob", DISC_NS + "taller", "alice", "relation")


def test_quantity_is_how_much():
    t = _one("The team is 5.")
    assert t == Triple("team", DISC_NS + "hasQuantity", "5", "quantity")


def test_multi_sentence_yields_a_triple_each_and_fail_closed():
    # THEOREM: one triple per licensed predication; a sentence with no copula licenses nothing.
    ts = triplify("Socrates is a man. The sun rises. Dogs are loyal.")
    assert len(ts) == 2  # the copula-less middle sentence yields nothing
    assert ("socrates", RDF_TYPE, "man") in {(t.subject, t.predicate, t.object) for t in ts}
    assert triplify("") == [] and triplify("Run fast now.") == []
