# Prior-art comparison — IEML
### Companion to `SEMANTIC_CONTROL_ARCHITECTURE.md` · KKO · ontogenesis · graph substrate · twins

Status: **prior-art record.** The kernel is built and shipped; the seam this document
proposed (§4.1, §5 Move 2) exists as `procyber/semantic/semantic_algebra.SemanticAddress`.
What remains unadopted is the third party's *dictionary* — deliberately, see §4.4 and
`SEMANTIC_IP_POSITION.md`.

Published rather than kept internal: truthful comparison with prior art is lawful
nominative reference, and a documented record of what was examined and deliberately
not taken is stronger evidence of independent creation than silence. The clean-room
guard enforces the distinction that actually matters — no copied expression, no
third-party mark naming our artifacts — not the absence of names.
---

## 0. What intlekt.io actually is

INTLEKT Metadata Inc. is **Pierre Lévy's** company (Fellow of the Royal Society of
Canada; collective-intelligence theorist). It is *not* connected to KBpedia /
Bergman / Structured Dynamics — a natural confusion since both sell "computable
semantics," and one that matters because the two are **complementary, not
competing** (§3).

Its single asset is **IEML — Information Economy MetaLanguage**: a constructed
language engineered so that meaning is *computed from form*.

---

## 1. IEML in one page (technically)

**Alphabet — 6 primitives at layer 0:**

| Symbol | Meaning | Role in composition |
|---|---|---|
| `E:` | emptiness / zero / neutral element | marks a symmetry axis; elided when in mode role |
| `U:` | the **virtual** — potential, abstract, immaterial | pole of any binary symmetry |
| `A:` | the **actual** — concrete, tangible, material | opposite pole |
| `S:` | the **sign** — what signifies | place 1 of any ternary symmetry |
| `B:` | the **being** — the interpreter, self-referential | place 2 |
| `T:` | the **thing** — the referent | place 3 |

**Two operations:**
- **Addition** (`+`, commutative, normalized order) — union of same-layer sequences.
  Shorthands: `O: = U:+A:` (dyad), `M: = S:+B:+T:` (triad), `F: = O:+M:` (pentad),
  `I: = E:+F:` (hexad).
- **Multiplication** (`✕`, **non-commutative**, **ternary**) — three Spinozan roles:
  **substance · attribute · mode**. Recursive to layer 4. Layer marked by
  punctuation: `:` `.` `-` `'` `,`. Distributive over addition.

**⇒ The result is a non-commutative ring** over 6 symbols. Only ~3000 elements are
assigned lexical meaning; the rest are uninstantiated variables in the ring. This
cap is deliberate — "to facilitate both automatic semantic computation and cognitive
management."

**Root paradigms** — a morphological function with 1–3 *variable* roles and the rest
constant. Equivalently: a 1-, 2-, or 3-dimensional matrix, i.e. **a symmetry group**.
Every dictionary word belongs to exactly one root paradigm. Four types: `category`
(content word), `inflection`, `auxiliary`, `junction`.

Worked example — the tetrad `O:O:.` is the sensorimotor cycle:

| USL | Word | Direction |
|---|---|---|
| `U:U:E:.` = `wo.` | orientation | inside → inside |
| `U:A:E:.` = `wa.` | action | inside → outside |
| `A:A:E:.` = `we.` | manifestation | outside → outside |
| `A:U:E:.` = `wu.` | perception | outside → inside |

**Syntax — sentences are a 9-role non-commutative multiplication:**

| # | Role | Reads as |
|---|---|---|
| 0 | **root** | the verb / head noun; everything else subordinates to it |
| 1 | **initiator** | subject / first actant |
| 2 | **interactant** | object / second actant |
| 3 | **recipient** | dative / third actant |
| 4 | **cause** | instrument, causality, ontological structure (type-of, part-of) |
| 5 | **time** | duration, moment |
| 6 | **place** | locative |
| 7 | **intention** | purpose, motivation, social context |
| 8 | **manner** | qualitative, quantitative, possessive |

Recursive — any role may hold a whole sentence. Four component types: categories
(`#`), inflections (`~`, ~80, type grammatical class + mood/tense/aspect/inference),
auxiliaries (`*`, 131, role-specific prepositions/cases for roles 4–8), junctions
(`&`, 29, commutative *and/or* and non-commutative *but/therefore*).

**The load-bearing property:** semantic relations — paradigmatic (symmetry /
substitution), syntagmatic (composition), conditional — are **computed from
syntactic similarity**. Edit distance in the code *is* semantic distance. Nothing is
learned; nothing is hand-curated per pair. Lévy: it is "a topos… an algebraic
structure in isomorphic relation with a topological space."

---

## 2. Code and license — the hard facts

| Repo / artifact | License | Last activity | Signal |
|---|---|---|---|
| `IEMLdev/ieml` (Python parser, dictionary, USL) | **GPL-3.0** | **2021-03-08** | 59★, Python 3.5+, cold |
| `IEMLdev/ieml-language` (USL translation DB, CSV) | **none** | 2021-03-10 | 21★ — *no license = all rights reserved* |
| `IEMLdev/ieml-dictionary` | none | 2019-01-25 | 3★ |
| `IEMLdev/ieml-reasoner` | none | 2023-04-14 | 7★ — most recent code |
| `IEMLdev/wiktionary-extractor` | none | 2020-05-09 | 2★ |
| **IEML Dictionary v.1 (2024)** | **CC BY-NC-ND 4.0** © INTLEKT Metadata Inc. | 2024 | the actual asset |
| **IEML Grammar v.1 (2024)** | **CC BY-NC-ND 4.0** | 2024 | " |

### Blocker 1 — licensing (hard stop)
Estate constraint is **MIT/Apache only**. Against that:
- **NC** — no commercial use. The estate is commercial. Blocks the Dictionary outright.
- **ND** — no derivatives. The Dictionary is explicitly scoped to *"literature,
  humanities and social sciences"*; Lévy states the exact sciences are excluded
  because they "have already standardized their special codes." Health twin,
  capital markets, code intelligence **all require extending it** — which ND forbids.
- **GPL-3.0** on the reference implementation — copyleft, would infect any linking service.
- **No license at all** on the database and reasoner — legally the most restrictive
  state possible.

**Nothing in IEML can be vendored today.** Read-only study only. Record in the IP
transfer register.

### Blocker 2 — the code is cold
Core library untouched since March 2021 on Python 3.5+. Bus factor 1–2. Lévy's own
status: research is *"at the fundamental stage"* and the dictionary interface is
*"difficult to navigate."* Adopting this means owning it.

### Blocker 3 — zero empirical evidence
No published benchmark shows IEML improving retrieval, reasoning, or interop.
**And there is a direct scar on record:** the KKO tiered-grounding arm ran
end-to-end at scale (n=350, agentkb1 board) and was **INERT** — 64.0% vs 63.7%
baseline, noise, not promoted. Grounding fired on 345/350 rows and the model did not
exploit it. IEML has strictly *more* machinery and strictly *less* evidence. The
prior must be skepticism.

---

## 3. Why it is nevertheless the best structural fit available

### 3.1 IEML and KKO share a Peircean root
`M: = S: + B: + T:` — **sign, being, thing** — is Peirce's triad
(representamen · interpretant · object). KKO's spine is
Firstness / Secondness / Thirdness, the same commitment. `O: = U: + A:` (virtual /
actual) is potentiality / actuality — the same dyad as the settled matter/form core
already bound to `kko:Matter` / `kko:Forms`.

They are **not rival ontologies. They are the extensional and intensional faces of
one Peircean position:**

| | KKO / KBpedia | IEML |
|---|---|---|
| Answers | *what exists* — identity | *how meaning composes* — structure |
| Method | **enumerative** — 58k RCs, mapped to ~32M Wikidata entities | **generative** — 3000 words + a ring, unbounded composition |
| Relations | curated, asserted, reasoned over OWL | **computed** from syntactic edit distance |
| Gives you | a resolvable anchor (IRI → Wikidata ID) | a decomposable address (substance/attribute/mode, 9 roles) |
| Weakness | says nothing about internal structure of a concept | says nothing about what a concept *refers to* in the world |

Each covers exactly the other's blind spot. **The right design emits both.**

### 3.2 Inference type is a *grammatical inflection*
IEML root paradigm `"E:.s.O:M:.-"` = `// INFERENCE TYPE`, a VERB inflection class
(possibly, conditionally, …). Alongside `// LOGICAL MOOD` `"E:.s.O:O:.-"` —
interrogation / negation / quotation / affirmation.

The estate's epistemic typing (induced / deduced / abduced = Peirce's trichotomy) is
currently *metadata attached to* a claim. In IEML it is **carried in the address of
the claim itself**. A USL cannot be stated without declaring how it was inferred and
whether it is asserted, quoted, denied, or asked. That is precisely the distinction
the counter-test gate needs and currently has to infer.

### 3.3 The layer system fixes a measured failure structurally
The tiered-ontology work exists because the keyed-vec topic space was flat —
94.9% vocab hit but topic max-cos 0.38–0.54, and *intro physics matched a graduate
QFT topic*: wrong abstraction level. The fix was hand-built (UPPER surjection→ MIDDLE
injection← LOWER).

IEML has this natively and principled: layers 0–4, where the morphism between layers
**is the ring multiplication**, and abstraction level is a syntactic property of the
address. You cannot accidentally match across layers, because layer is in the punctuation.

### 3.4 It converges on the same mathematics as the sefirotic model
Part I derives Chesed/Gevurah as **pushout/pullback** and cites the TL paper's
category/topos framing. Lévy independently calls IEML **a topos**. Two unrelated
sources, one mathematical object. IEML is the concrete, computable realization of
what the TL paper only gestures at: the sefirotic operators become ring operations
on USLs, and the `P: TL × TL → TL` fibration becomes recursive role-substitution.

The tetrad `wo → wa → we → wu` (orient → act → manifest → perceive) is a control
loop — the same loop as the TL cascade and the information-seeking pipeline.

---

## 4. Where each estate asset slots in

### 4.1 Ontogenesis — dual addressing
Today `type-operators` / `canon-to-ontogenesis` emit KKO IRIs. Extend to emit a
**`SemanticAddress`**:

```
SemanticAddress:
  iri:        kko:/kbpedia RC IRI      # extension — what it refers to  (Malchut)
  usl:        IEML Uniform Sem. Locator # intension — how it composes    (Binah)
  layer:      0..4                      # abstraction level, syntactic, not learned
  inference:  induced|deduced|abduced   # → IEML inference inflection
  mood:       assert|quote|negate|ask    # → IEML logical mood
```
`usl` stays **null** until licensing clears. The *field and the seam* are not
encumbered; only Lévy's dictionary is.

### 4.2 HellGraph — a Law-side edge source
IEML relations are **derivable**, not observed. In `Truth = Law × Evidence` that puts
them squarely on the **Law** arm: paradigmatic edges (same root paradigm, differing
in one role) and syntagmatic edges (one is a role-filler of the other) are computed
deterministically with no training, no corpus, no embedding.

This is a genuinely new edge class for the graph: edges that come with a **proof of
derivation** rather than a confidence score. Consume vendored, per lane rules — do
not edit the engine.

### 4.3 Digital twin — the 9-role frame is the governed-action schema
A twin's event log needs to record, for every act: who did it, to what, for whom, by
what instrument and why, when, where, to what purpose, in what manner. That is
**exactly roles 1–8**, with the act itself at role 0. IEML did not design this for
agents; it is standard actantial grammar (Tesnière). It happens to be a complete,
non-redundant frame for a governed side-effect record — better than the ad-hoc field
sets in `BoundaryTransition` and `MembraneDecision` today.

**Plus a real privacy lever.** A USL is language-independent code. You can transmit
the *structure* of an event while withholding its natural-language descriptor — share
the skeleton, withhold the surface. That is a concrete mechanism for Gevurah rule
**G2 (linkability risk)** in the Da'at 5C/5G equilibrium, and directly serves the
health-twin de-identification constraint.

### 4.4 Part I (sefirotic) — IEML fills the two named gaps
- The 3-T **semantic** boundary needs a `lexiconRef` with a *computable* value.
  A USL is exactly that: sender and receiver can compute their semantic distance
  without a shared training corpus or a negotiated mapping table.
- **Yesod** (the single serialization channel) needs a boundary-object encoding.
  A USL-typed 9-role frame is that encoding.

---

## 5. The play — three moves, in order

**Move 1 — Ask for the relicense.**
Precedent is direct and successful: KBpedia was open-sourced (CC BY 4.0) after being
asked. Approach Lévy / INTLEKT Metadata Inc. for **CC BY 4.0 on Dictionary + Grammar**
and **Apache-2.0 on a reference implementation**; failing that, a commercial license
from INTLEKT. The pitch writes itself — IEML has had no significant adopter in five
years, and Lévy's stated goal is semantic interoperability, which requires adoption.
Until it clears: **read-only, zero vendoring, no derivative dictionary.**

**Move 2 — Build the seam clean-room, now.**
`SemanticAddress` (§4.1) with `usl` nullable, behind a `SemanticAddressProvider`
interface. Stub provider today; IEML behind the same interface if and when licensing
clears. Identical scaffold-first pattern to control-plane Phase 6 (durable semantics
in-process, real stack swaps in behind the interface). No encumbered bytes enter the
estate.

**Move 3 — Take the one thing that is free: the 9-role action frame.**
Actantial role structure is universal linguistics (Tesnière, case grammar), not IEML
IP. Adopt roles 0–8 as the action frame for `BoundaryTransition.v0.2` and the twin
event log **immediately** — highest value, zero legal risk, no dependency on Lévy.

---

## 6. Gate before belief

Do not adopt on elegance. The KKO board already taught this lesson at a cost.

- **Hypothesis:** compositional addressing controls abstraction level where flat
  embedding does not.
- **Test:** reproduce the exact recorded failure — intro-level physics matching a
  graduate QFT topic — and measure whether layer-typed addressing bars it structurally.
- **Primary metric:** *abstraction-level mismatch rate*, not raw accuracy. The KKO
  arm's accuracy was noise; the interesting quantity was never measured.
- **n ≥ 30 per cell**; run on a model above the 7B ceiling, since the recorded
  inertness may be a small-model failure to exploit injected context rather than a
  failure of grounding.
- **Teeth both ways:** the layer bar must be shown to *reject* a cross-layer match,
  not merely to pass the good cases.

---

## 7. Open questions

1. **Does the ND clause bar even a mapping table?** A KKO-IRI ⟷ USL alignment file
   is arguably a derivative of the Dictionary. Needs a real answer before Move 2 ships
   anything referencing USL strings.
2. **Coverage strategy for exact sciences.** IEML deliberately excludes them. Either
   negotiate the right to extend, or accept IEML for the humanities/social/values
   layer only and keep KBpedia+OCW for STEM — which may in fact be the correct
   architecture regardless of licensing.
3. **`ieml-reasoner`** (2023, unlicensed) is the most recent code and the least
   documented. Worth a read-only look — it may indicate where Lévy intended
   automated inference to sit.
4. **Who computes the USL?** If an agent self-assigns its own semantic address, the
   fast path in the 3-T novelty routing is gameable — same open question as §9.3 of
   Part I, now with a sharper edge because USL distance would be *trusted* as Law.
