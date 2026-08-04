"""Theorems of Aristotelian category typing (procyber.discourse.categories) — the copula predication
core, deterministic and fail-closed."""
from __future__ import annotations

from procyber.discourse import argument_mining as am
from procyber.discourse import categories as cat


def test_ten_categories_with_substance_primary():
    assert len(cat.CATEGORIES) == 10
    assert cat.SUBSTANCE in cat.CATEGORIES
    assert len(cat.ACCIDENTS) == 9 and cat.SUBSTANCE not in cat.ACCIDENTS
    assert cat.PRIMARY != cat.SECONDARY


def test_is_a_class_is_secondary_substance_instance_of():
    # "Socrates is a man" ⇒ socrates (primary/instance) is an instance of man (secondary/class).
    (p,) = cat.analyze("Socrates is a man.")
    assert p.subject == "socrates" and p.subject_kind == cat.PRIMARY
    assert p.category == cat.SUBSTANCE and p.predicate == "man"


def test_is_adjective_is_quality():
    (p,) = cat.analyze("The sky is blue.")
    assert p.category == cat.QUALITY and p.predicate == "blue"


def test_comparative_than_is_relation():
    (p,) = cat.analyze("Sparta is larger than Athens.")
    assert p.category == cat.RELATION and p.predicate == "larger" and p.object == "athens"


def test_numeral_predicate_is_quantity():
    (p,) = cat.analyze("The army is 300.")
    assert p.category == cat.QUANTITY and p.predicate == "300"


def test_no_copula_is_fail_closed():
    # No predication pattern ⇒ nothing forced.
    assert cat.analyze("Charge the hill.") == []


def test_common_noun_subject_is_secondary():
    (p,) = cat.analyze("A dog is an animal.")
    assert p.subject == "dog" and p.subject_kind == cat.SECONDARY
    assert p.category == cat.SUBSTANCE and p.predicate == "animal"


def test_categorize_graph_types_argument_units():
    # ③ typing rides on ② extraction: each mined unit is typed by the predication it licenses.
    g = am.mine("Socrates is wise because Socrates is a philosopher.")
    typed = cat.categorize_graph(g)
    cats = {p.category for preds in typed.values() for p in preds}
    assert cat.QUALITY in cats and cat.SUBSTANCE in cats
