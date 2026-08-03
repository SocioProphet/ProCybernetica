# Market Paradigm — cross-source superset

Status: `procyber/semantic/market_paradigm.py` · 40 tests · SPEC_VERSION 0.1.0

A companion to `SEMANTIC_CONTROL_ARCHITECTURE.md`. That document covers the control
architecture; this one covers the first substantial *consumer* of the algebra —
merging many segmented-claim sources into one map that can say where it is wrong and
where it is silent.

---

## 1. The observation that makes this tractable

An analyst market report looks like a document to be summarised. Structurally it is
a **root paradigm**: a multi-dimensional matrix whose axes are held constant or
varied, which is exactly what `semantic_algebra.distribute` generates. A report
covering component × deployment × organisation-size × vertical × region is a
five-axis paradigm whose cells carry claims.

Once that is seen, merging N reports stops being a summarisation problem and becomes
an **iterated pushout along shared axes** — and `pushout` already refuses to glue
over a disagreement. Contradictory figures therefore surface as named contradictions
instead of averaging into a number nobody can trace back to a source.

## 2. Axes

```
offering · modality · vertical · geography · actor
```

Cell keys always follow that canonical order regardless of declaration order, so two
maps built independently produce comparable keys.

`actor` values are **resolved entity IRIs, not display strings**. Cross-source
identity — two sources naming one organisation differently must join; two genuinely
different organisations must not — is a separate, harder problem solved upstream by
cross-document entity resolution. This module takes the resolved IRI as input and
performs no name matching of its own.

## 3. What a merge guarantees

| Behaviour | Rationale |
|---|---|
| axis **values** union | one source covering more verticals than another is coverage, not conflict |
| axis **sets** must match | merging a map that has an `actor` axis into one that does not would silently marginalise over the vendor dimension — the quiet collapse that makes a merged map untraceable |
| claims accumulate per cell | the merge never reduces; reduction happens at `reconcile`, where it can be inspected |

## 4. Reconciliation

`reconcile(claims, as_of=None) -> (verdict, contradiction | None)`

- Sources that agree → `meet` of their verdicts. The lattice minimum, so the most
  cautious source governs.
- Values disagreeing beyond `VALUE_TOLERANCE` (10%) → `BOTTOM` **and** a named
  `Contradiction` carrying every source and every value. No verdict is produced; the
  disagreement travels instead of collapsing.
- Incommensurable units → `Contradiction`, same treatment.
- A claim with no number is still a claim. Structural assertions ("this actor
  operates in this vertical") are first-class; forcing a number would invent data.

The 10% tolerance is deliberate. Analyst figures are estimates, and demanding exact
equality would report contradictions everywhere and train readers to ignore them.

## 5. Staleness is a refusal, not a filter

A forecast has a horizon. Read past that horizon it is history, not prediction, and
treating an elapsed forecast as current is the failure this module exists to make
impossible.

`Claim.is_stale(as_of)` is true once the horizon has elapsed. `reconcile` then
**downgrades** the verdict one step rather than dropping the claim — what was
believed at the time remains evidence of what was believed at the time. `stale_claims`
enumerates them; `twin_manifest(as_of=...)` counts them.

Worked example: a 2018 report forecasting to 2023, read in 2026, has a fully elapsed
horizon. Its structure is still useful; its numbers are no longer a forecast, and the
verdict says so without anyone having to remember.

## 6. Gaps are the product

`gaps()` enumerates cells in the axis product with no claim at all, and never
interpolates them. `twin_manifest` leads with `cellsTotal`, `coverage`, and `gaps`
before anything it does know.

A market surface that shows only its filled cells reads as authoritative regardless
of how thin it is. Interpolating an uncovered cell is how a market map becomes
fiction, and a superset that reports where it is silent is worth more than one that
implies completeness.

`superset([])` returns `BOTTOM`, not an empty map: "no sources" and "sources that
found nothing" are different claims about the world and must not share a
representation.

## 7. Twin binding

| Twin tier | Axis |
|---|---|
| world | `geography` |
| industry | `vertical` |
| entity | `actor` |
| capability | `offering` |

`modality` (deployment, scale) deliberately owns no tier — it cuts across all four.

`twin_projection` re-keys by the tier's axis value and **retains every claim**. The
projection changes the key, never the evidence: a twin that summarises on the way in
cannot later answer why it believes something.

That the axes fall out cleanly onto the twin tiers is weak evidence the decomposition
is real rather than imposed — independent analyst practice converged on the same cut.

## 8. Boundaries

- **No ingestion.** This module has no parser, no scraper, no source adapter. It
  operates on `Claim`s that something else produced, which keeps it stdlib-only and
  keeps source-specific licence terms at the adapter boundary rather than in the
  kernel.
- **No name matching** (§2).
- **No interpolation** (§6).
- **No averaging** (§4).

## 9. Not built

- **Adapters.** Nothing yet turns a source into `Claim`s. The intended first one
  consumes resolved cross-document entity events for the `actor` axis; it belongs in
  the consuming platform, not here.
- **Weighting.** All sources currently carry equal weight at `reconcile`. Source
  reliability is a real signal and is not modelled; adding it means deciding who
  scores reliability, which is the same trust question the architecture record leaves
  open (`SEMANTIC_CONTROL_ARCHITECTURE.md` §6).
- **Temporal series.** A claim has one horizon, not a curve. Multi-period forecasts
  currently decompose into separate claims.
