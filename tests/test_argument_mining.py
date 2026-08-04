"""Theorems of the argument-mining organ (procyber.discourse.argument_mining) — a deterministic,
fail-closed extractor: a discourse connective licenses structure, and nothing else does.
"""
from __future__ import annotations

from procyber.discourse import argument_mining as am


def _role(g: am.ArgumentGraph, uid: str) -> str:
    return next(u.role for u in g.units if u.id == uid)


def _text(g: am.ArgumentGraph, uid: str) -> str:
    return next(u.text for u in g.units if u.id == uid)


def test_because_makes_premise_support_claim():
    # THEOREM: "<claim> because <premise>" ⇒ premise --support--> claim.
    g = am.mine("Cats are great because they purr.")
    assert len(g.units) == 2 and len(g.relations) == 1
    r = g.relations[0]
    assert r.kind == am.SUPPORT
    assert _role(g, r.source) == am.PREMISE and _role(g, r.target) == am.CLAIM
    assert "purr" in _text(g, r.source)


def test_therefore_makes_premise_support_conclusion():
    # THEOREM: "<premise> therefore <claim>" ⇒ premise --support--> claim (Aristotle's inference).
    g = am.mine("He studied therefore he passed.")
    assert len(g.relations) == 1 and g.relations[0].kind == am.SUPPORT
    r = g.relations[0]
    assert _role(g, r.source) == am.PREMISE and _role(g, r.target) == am.CLAIM
    assert "studied" in _text(g, r.source)


def test_however_across_sentences_is_attack():
    # THEOREM: a sentence opening with a contrast marker attacks the prior claim.
    g = am.mine("It was sunny. However, it was cold.")
    atk = next(r for r in g.relations if r.kind == am.ATTACK)
    assert "cold" in _text(g, atk.source)    # the rebuttal
    assert "sunny" in _text(g, atk.target)   # attacks the prior claim


def test_but_within_a_sentence_is_attack():
    g = am.mine("The plan is good but it is expensive.")
    assert len(g.relations) == 1 and g.relations[0].kind == am.ATTACK
    atk = g.relations[0]
    assert "expensive" in _text(g, atk.source) and "good" in _text(g, atk.target)


def test_bare_sentence_is_a_claim_with_no_invented_relation():
    # Fail-closed: no connective ⇒ no hallucinated structure.
    g = am.mine("The sky is blue.")
    assert len(g.units) == 1 and g.units[0].role == am.CLAIM
    assert g.relations == []


def test_empty_text_is_empty_graph():
    g = am.mine("")
    assert g.units == [] and g.relations == []


def test_deterministic():
    text = "Alice trusts Charlie because Charlie is honest. However, Bob disagrees."
    assert am.mine(text).to_dict() == am.mine(text).to_dict()


def test_feeds_cooccurrences_to_the_sink():
    # Composes with the memory organ (dynamics.AssociativeMemory) via a duck-typed co_occur sink —
    # no import coupling to the dynamics module.
    seen = []

    class Sink:
        def co_occur(self, a, b):
            seen.append(frozenset((a, b)))

    am.mine("Alice trusts Charlie because Charlie is honest.", cooccurrence_sink=Sink())
    assert frozenset(("alice", "charlie")) in seen


def test_graph_fragment_is_hellgraph_shaped():
    d = am.mine("Sparta will win because Sparta is disciplined.").to_dict()
    assert set(d) == {"units", "relations"}
    assert all(set(u) == {"id", "text", "role"} for u in d["units"])
    assert all(set(r) == {"source", "target", "kind"} for r in d["relations"])
    assert d["relations"][0]["kind"] == am.SUPPORT
