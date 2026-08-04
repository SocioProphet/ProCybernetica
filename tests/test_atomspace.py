"""Theorems of ③ the ontology organ (procyber.ontology.atomspace): Aristotle's primary/secondary
substance become instance/subclass edges in the AtomSpace type lattice; accidents become evaluations."""
from __future__ import annotations

from procyber.ontology.atomspace import (
    concept, evaluation, inheritance, member, predicate_node, predication_to_atoms, to_atomspace,
)
from procyber.discourse.categories import analyze


def _atoms(text):
    return to_atomspace(text)


def test_secondary_substance_is_a_subclass_edge():
    # THEOREM: "A man is an animal" (secondary substance) ⇒ InheritanceLink(man, animal) — a SUBCLASS
    # edge the type lattice inherits over.
    (a,) = _atoms("A man is an animal.")
    assert a == inheritance(concept("man"), concept("animal"))
    assert a.type == "InheritanceLink"


def test_primary_substance_is_an_instance_edge():
    # THEOREM: "Socrates is a man" (primary substance = an individual) ⇒ MemberLink(Socrates, man) —
    # instance-of, distinct from subclass. This IS the primary/secondary distinction the lattice needs.
    (a,) = _atoms("Socrates is a man.")
    assert a == member(concept("socrates"), concept("man"))
    assert a.type == "MemberLink"


def test_accident_is_an_evaluation_over_a_predicate():
    # THEOREM: a quality inheres in the subject as EvaluationLink(has_quality, List(subject, value)).
    (a,) = _atoms("Cats are great.")
    assert a == evaluation(predicate_node("has_quality"), concept("cats"), concept("great"))
    assert a.type == "EvaluationLink" and a.outgoing[0] == predicate_node("has_quality")
    assert a.outgoing[1].type == "ListLink"


def test_relation_evaluates_over_both_terms():
    # THEOREM: "Bob is taller than Alice" ⇒ EvaluationLink(taller, List(Bob, Alice)).
    (a,) = _atoms("Bob is taller than Alice.")
    assert a == evaluation(predicate_node("taller"), concept("bob"), concept("alice"))


def test_fail_closed_and_composes_a_lattice():
    # THEOREM: no copula ⇒ no atom; a multi-sentence text builds the connected lattice of its readings.
    assert to_atomspace("Run now.") == []
    atoms = to_atomspace("Socrates is a man. A man is an animal.")
    assert len(atoms) == 2
    types = {a.type for a in atoms}
    assert types == {"MemberLink", "InheritanceLink"}  # instance chained under a subclass — a real lattice
    # sanity: the mapping agrees with the analyzer it is built on
    assert len(atoms) == len(analyze("Socrates is a man. A man is an animal."))
