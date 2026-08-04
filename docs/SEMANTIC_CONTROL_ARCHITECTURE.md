# Semantic Control Architecture

Status: architecture record for the kernel in `procyber/semantic/` · SPEC_VERSION 0.2.0

`SEMANTIC_COORDINATE_ALGEBRA.md` is the provenance register and conformance sheet: it
answers *why the algebra is unencumbered* and *what the tests pin*. This document
answers the other question — **what the algebra is for**, and which parts of that
architecture exist today.

The vocabulary here matches the shipped `contracts/AgentCoordinateVector.v0.1.json`
axis names. It is a coordinate system, not a cosmology: each axis is a named position
in a control architecture, and the tests are the only thing that gives any of them
meaning.

---

## 1. The claim in one sentence

A governed agent is **a eleven-coordinate state vector, driven by a three-level
cascade whose middle column is an explicit meet of an expansive and a restrictive
operator, recursively fibred so every coordinate can itself be a full agent,
exchanging typed boundary objects under an explicit share/withhold equilibrium.**

The engineering payoff is not the framing. It is that the two combining operators
turn out to be **categorical duals** — `pushout` (glue) and `pullback` (restrict) —
reconciled by a single `meet`. Naming them as duals is what collapses a dozen ad-hoc
merge and filter paths into two composable operations with one shared reconciliation.

---

## 2. The eleven coordinates

| Axis | Engineering coordinate | Operator | Where it lives |
|---|---|---|---|
| `keter` | charter / mandate — given, never computed | — | admission receipt; the work order |
| `chochmah` | hypothesis generation; high recall, low precision | generate | retrieval expansion |
| `binah` | elaboration — candidate to fully-typed plan | structure | planner |
| `daat` | internal model **+ the share/withhold balance** | hold | `semantic_algebra` + `internal_model` |
| `chesed` | expansive — admit, generalise, glue | **pushout** | `semantic_algebra.pushout` |
| `gevurah` | restrictive — constrain, falsify, redact, deny | **pullback** | `semantic_algebra.pullback` |
| `tiferet` | reconciliation of the two arms | **meet** | `semantic_algebra.meet` |
| `netzach` | continuity — durable commitment, retry | persist | outbox (external) |
| `hod` | measurement, instrumentation, when to stop | measure | resource contract (external) |
| `yesod` | the single serialisation channel | serialise | `serialization_channel` |
| `malchut` | world-effect and its receipt | effect | side-effect boundary (external) |

Two readings that drive the design:

**The middle column decides; the arms do not.** `meet` returns the lattice minimum,
so an expansive signal can never carry a decision on its own — its meet with a
restrictive signal cannot exceed the restrictive one. The same `meet` serves
`Truth = Law × Evidence`. One implementation, two call sites; a second copy is how
the two drift apart.

**Abstention is a value, not a control-flow accident.** `BOTTOM` is carried, absorbed
by `meet`, undefined under `distance`, and never grounded into an address. "I cannot
decide from within this system" is a result, not a `None` to be smuggled through a
return path.

---

## 3. Fibration — coordinates that are themselves agents

Each coordinate may be delegated to a full sub-agent with its own eleven
coordinates. The projection is unique by construction: two routers would mean two
incompatible base spaces and the fibration would be ill-defined. This is why a single
router interface is an invariant rather than a preference.

Depth is bounded by charter, not by code — which is only safe once a depth budget
lands in the resource contract (open, §5).

---

## 4. Boundary crossing

Fibre-to-fibre and system-to-external exchange crosses three tiers, with cost rising
in the novelty of the work:

| Tier | Sub-boundary | Carried |
|---|---|---|
| Knowledge | syntactic / semantic / administrative | schema hash; lexicon reference; control distance |
| Value | realisation / propagation | whose interest is served; how value flows back |
| Ecosystem | resource control / interdependence | grant under which the resource is held; what breaks on failure |

`contracts/BoundaryTransition.v0.2.json` carries the nine actantial roles (root,
initiator, interactant, recipient, cause, time, place, intention, manner) — standard
case grammar, and a complete non-redundant frame for a governed action record.

`SemanticAddress.skeleton()` is the privacy lever that falls out of this: an address
is language-independent, so structure can travel while the descriptor and evidence
pointer stay behind. A counterparty computes distance against the skeleton without
receiving the subject.

---

## 5. Build status — honest

**Built** (`procyber/semantic/`, 428 tests, every guard exercised on its refusal path):

- `semantic_algebra` — terms, add/mul, distance, `pushout`/`pullback`/`meet`,
  `bind_tiered`, `lift`⊣`ground`, `SemanticAddress`, pluralistic `Lexicon`s, `BOTTOM`
- `agent_coordinate_vector` — the eleven axes; ten or twelve is rejected
- `boundary_transition_actants` — the nine roles
- `abstraction_level_gate` — measures abstraction-level mismatch, the quantity the
  earlier grounding board never measured
- `intent_address` — the 23×6 intent grid as a slice of the algebra
- `spectral_grounding` — supermodularity = `meet`, per-cell clipping = half-space
  `pullback`, proven both ways
- `market_paradigm` — cross-source superset; see `SEMANTIC_MARKET_PARADIGM.md`
- `internal_model` — the `daat` organ: five admit rules, five withhold rules, and the
  equilibrium between them. The admit arm is the maximum over applicable rules (the
  best case for sharing); the withhold arm is the minimum (the most restrictive
  ceiling governs); the decision is their `meet`. Because `meet` is the lattice
  minimum and absorbs `BOTTOM`, **an admit signal cannot authorise a share on its
  own, and an arm that was never evaluated abstains rather than defaulting open** —
  both fall out of the algebra rather than needing a special case.
- `serialization_channel` — the `yesod` chokepoint. `emit` is the only function that
  produces a `WireEnvelope`, and it **refuses unless the caller presents a share
  decision that clears**. `daat` decides, `yesod` transmits, and transmission is not
  reachable without a decision — an agent cannot route around its own equilibrium by
  serialising somewhere else, because there is nowhere else. The invariant is checked
  against the real tree by `single_channel_violations`, not asserted in prose.
- `retention_probe` — incorporation gated on a retained-task probe. `incorporate`
  probes, applies, probes again, and **returns the original object** when a retained
  task regresses beyond tolerance, so a rollback is "return what you already had"
  rather than an undo that has to be correct. An empty probe refuses rather than
  clearing, because a gate that passes everything is worse than no gate: it looks
  like one.

**Not built:**

- **depth budget** for the fibration (§3).
- **`hod` / `malchut` wiring** — resource contract declared per fibre, and the
  effect receipt carrying the coordinate vector. External to this kernel.

---

## 6. Open questions

1. **Charter authorship.** `keter` is defined as given, not computed. That argues it
   must be human-signed and underivable — unsettled.
2. **`daat` ownership** — one internal model per agent, or one per counterparty?
   Asynchronous exchange argues per-relationship, which multiplies state.
3. **Novelty scoring provenance.** If a sender scores its own novelty, the cheap
   crossing path is gameable. Likely a restrictive-side estimate.
4. **Trusted distance.** Structural distance is derivable and therefore Law-side. If
   an agent self-assigns its address, that trust is misplaced — the same question as
   (3) with sharper consequences.
