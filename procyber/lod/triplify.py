"""④ INGEST — triplification (the fourth organ of the knowledge-memory spine). Turns text into RDF
subject–predicate–object triples, the Linked-Open-Data grain the graph, SPARQL surface and the twin
medium all consume. It is the INGEST face of the SAME Aristotelian reading the ontology organ uses:
each predication categories.analyze licenses becomes one triple, so ingestion and typing never drift.

The mapping is principled, not ad hoc — the Aristotelian category fixes the predicate:
  substance  ("S is a P")           → (S, rdf:type, P)                the classic type/class triple
  relation   ("S is …-er than O")   → (S, <disc:predicate>, O)        S stands in a relation to O
  quantity   ("S is <n>")           → (S, disc:hasQuantity, <n>)      how-much
  quality / the other accidents      → (S, disc:has_<category>, V)     an accident inhering in S

Deterministic and fail-closed (a sentence with no copula yields no triple — categories.analyze already
refuses to force a category). `disc:` is the estate's discourse namespace; `rdf:type` is standard so the
type triples interoperate with any RDF/SPARQL consumer. Clean-room, pure-Python.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

from procyber.discourse.categories import (
    Predication, QUANTITY, RELATION, SUBSTANCE, analyze,
)

__all__ = ["Triple", "DISC_NS", "RDF_TYPE", "predication_to_triple", "triplify"]

DISC_NS = "https://schema.srcos.ai/discourse#"   # the estate's discourse-derived predicate namespace
RDF_TYPE = "rdf:type"                             # standard — type triples interoperate with any RDF tool


@dataclass(frozen=True)
class Triple:
    """One RDF statement. `category` is the Aristotelian provenance — which reading licensed the triple."""

    subject: str
    predicate: str
    object: str
    category: str


def predication_to_triple(p: Predication) -> Triple:
    """Map one Aristotelian predication to its RDF triple (the category fixes the predicate)."""
    if p.category == SUBSTANCE:
        return Triple(p.subject, RDF_TYPE, p.predicate, SUBSTANCE)
    if p.category == RELATION:
        # S is …-er than O: the comparative IS the predicate, O the object.
        return Triple(p.subject, DISC_NS + p.predicate, p.object or "", RELATION)
    if p.category == QUANTITY:
        return Triple(p.subject, DISC_NS + "hasQuantity", p.predicate, QUANTITY)
    # quality + the remaining accidents: an accident of `category` inhering in the subject.
    return Triple(p.subject, DISC_NS + "has_" + p.category, p.predicate, p.category)


def triplify(text: str) -> List[Triple]:
    """Text → RDF triples, one per predication the copulas license. Fail-closed (no copula ⇒ no triple)."""
    return [predication_to_triple(p) for p in analyze(text)]
