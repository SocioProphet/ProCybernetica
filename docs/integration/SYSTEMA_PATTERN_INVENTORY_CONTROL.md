# Systema Pattern Inventory Control

Status: draft v0.1
Turn: 1 / 28
Owner repository: `SocioProphet/ProCybernetica`

## Purpose

This file is the public control ledger for absorbing the Fuller/Synergetics pattern system into the SocioProphet, SourceOS-Linux, and SociOS-Linux estate without schema sprawl, runtime duplication, or source laundering.

Systema is the estate-level operating grammar for a public cybernetic knowledge and control machine. It treats concepts, claims, agents, repositories, runtimes, tools, models, policies, evidence, maps, manuals, metrics, and world-model layers as lawful nodes inside replayable feedback loops.

The Fuller/Synergetics material is useful because it exposes a pattern inventory:

```text
dictionary -> concept system -> catalog -> evaluated access -> projection -> frequency -> triangulated evidence -> membrane -> tensegrity -> world-pattern inventory -> design science -> livingry
```

ProCybernetica owns the constitutional law, doctrine, profiles, conformance posture, public examples, and fanout ledger. It must not duplicate downstream runtime, ontology release, search, geospatial, SourceOS, AgentPlane, or platform deployment surfaces.

## Source-confidence rule

The Fuller/Synergetics upload inventory is not a fully authoritative text corpus. Many source cards are visual-only, sparse OCR, or partial OCR. OCR is candidate evidence, not final truth.

Therefore:

1. A Fuller-derived term may enter as a candidate concept.
2. A Fuller-derived quote may not become a load-bearing quotation without source-card confidence or manual review.
3. A Fuller-derived doctrine may be used operationally only when translated into explicit scope, owner, evidence, tests, and failure modes.
4. Analogy is not proof.
5. A source-card ID, extraction confidence, and review state must be preserved when a concept or claim is promoted.

## Estate ownership map

| Layer | Owner repo | Systema role |
| --- | --- | --- |
| Constitutional doctrine and conformance | `SocioProphet/ProCybernetica` | Public control law, doctrine-as-code, profiles, examples, conformance, public-review ledger |
| Concept dictionary / ontology | `SocioProphet/ontogenesis` | JSON-LD/OWL/SHACL concept records, promotion gates, vocabulary drift, relation primitives |
| Evaluated access / catalog search | `SocioProphet/sherlock-search` | Catalog-as-access-device results: usefulness, trust, availability, reproducibility, source confidence |
| World-pattern inventory | `SocioProphet/gaia-world-model` | Mini-Earth/data-tetrahedron model, geodesic routes, projection/frequency ledgers, scenario evidence |
| Execution evidence / tensegrity runtime | `SocioProphet/agentplane` | Bundle -> Validate -> Place -> Run -> Evidence -> Replay; agent action tension members |
| Platform runtime and deployment | `SocioProphet/prophet-platform` | Running services, deployment topology, platform contracts, runtime bridges |
| Delivery metrics | `SocioProphet/delivery-excellence` | Dymaxion metrics, entropy ledger, verified capability per resource |
| CI/RBAC/OTEL/GitOps standards | `SocioProphet/prophet-platform-standards` | Triangulated evidence, membrane boundaries, periodic experience, release gates |
| SourceOS typed contracts | `SourceOS-Linux/sourceos-spec` | Canonical SourceOS/SociOS schemas, events, policy, provenance, agent-plane contracts |
| Local-first state integrity | `SourceOS-Linux/sourceos-syncd` | State membranes, repair plans, event coalescing, operator narrative, local evidence |
| Agent machine substrate | `SourceOS-Linux/agent-machine` | Agent workload substrate, activation decisions, cache/model/runtime membranes |
| Education/manual commons | Alexandrian Academy / docs lane | Design-science curriculum, manuals, build/repair/validation playbooks |

## Pattern inventory

| Pattern | Operational meaning | Primary owner | First artifact target | State |
| --- | --- | --- | --- | --- |
| Dictionary Doctrine | A concept is a source-anchored, cross-referenced, promoted object, not just a word | `ontogenesis` | `docs/specs/systema-concept-entry-v0.md` | candidate |
| Catalog-as-Access-Device | Search returns evaluated access, not mere similarity | `sherlock-search` | `docs/doctrine/catalog-as-access-device.md` | candidate |
| Words as Industrial Tool | Vocabulary is interoperability infrastructure | `ontogenesis`, `semantic-serdes`, `sherlock-search` | vocabulary drift gate | candidate |
| Periodic Experience | Dynamic systems require cadence, replay windows, drift, and bitemporal state | ProCybernetica, platform standards | `docs/patterns/periodic-experience.md` | candidate |
| Membrane Doctrine | Boundaries admit, block, transform, log, witness, redact, and revoke | SourceOS, AgentPlane, Policy Fabric | `profiles/membrane_boundary_profile.yaml` | candidate |
| Sweepout / Reachability | Capability has radius and scope; reach expands only through evidence | AgentPlane, agent-registry | `docs/specs/capability-radius-v0.md` | candidate |
| Triangulated Evidence | Consequential claims/actions require assertion + evidence + independent witness | platform standards | `docs/patterns/triangulated-evidence.md` | candidate |
| Tetrahedral Minimum System | Minimum viable system has actor + artifact + evidence + governance | ProCybernetica | conformance invariant | candidate |
| Tensegrity Architecture | Local compression members are cohered by continuous policy/evidence/provenance tension | AgentPlane | `docs/doctrine/tensegrity-runtime-contract.md` | candidate |
| Geodesic Relation | A path is least-action under declared topology, metric, time, and projection | GAIA, Sherlock, observability | `docs/specs/geodesic-route-relation-v0.md` | candidate |
| Projection Loss | Any lowering from source to representation must declare information loss | semantic-serdes, GAIA, Sherlock | `profiles/projection_loss_profile.yaml` | candidate |
| Frequency Ledger | Scale is subdivision/resolution/cadence, not generic repetition | GAIA, ProCybernetica | `profiles/frequency_ledger_profile.yaml` | candidate |
| Jitterbug Phase Transition | System phases must preserve declared invariants as form changes | ProCybernetica, AgentPlane | phase parity checks | candidate |
| Dymaxion Metrics | Verified service per resource burden; no "more with less" without denominator | delivery-excellence | `docs/metrics/dymaxion-performance-per-pound.md` | candidate |
| Entropy Accounting | Track stale context, duplicate schemas, dead branches, failed loops, drift, trust drag | delivery-excellence | `docs/metrics/entropy-ledger.md` | candidate |
| Manual Commons | Release is incomplete without build, validation, repair, and failure-mode manuals | ProCybernetica and all repos | `docs/manuals/` | candidate |
| Livingry Classification | Artifacts are classified by constructive, neutral, dual-use, weaponry, or unknown purpose | ProCybernetica, SCOPE-D, Policy Fabric | livingry policy profile | candidate |
| Cybernetic Oversteer | Detect oscillation, overcorrection, patch churn, repeated reversals, policy flip-flops | AgentPlane, Delivery Excellence | oversteer indicators | candidate |
| Nonsimultaneous Comprehensibility | Finite systems must be addressable and progressively revealable | Sherlock, Ontogenesis, UI | concept/source drilldown requirements | candidate |
| Media Transition Doctrine | AI/local-first/agent systems are governance reorientation events, not tool upgrades | ProCybernetica | media transition doctrine | candidate |
| Octet Truss Reuse Law | Reuse is structural only when join rules are explicit | platform standards, sourceos-spec | shared-structure conformance | candidate |

## Promotion states

Systema patterns use these states:

```text
candidate -> in_progress -> landed -> validated -> adopted -> deprecated | contested
```

Definitions:

- `candidate`: source-backed or strategically useful, but not yet implemented.
- `in_progress`: issue or PR exists in the owning repo.
- `landed`: artifact exists on main branch.
- `validated`: artifact has examples, fixtures, or tests.
- `adopted`: downstream repo consumes it.
- `deprecated`: replaced by newer doctrine or contract.
- `contested`: unresolved contradiction or ownership conflict.

## Required gates

### Source-confidence gate

Every source-derived concept must include:

```yaml
source_confidence:
  source_ref: required
  extraction_confidence: A | B | C | D | E
  review_state: unreviewed | candidate | manually_reviewed | independently_verified | rejected
  quote_boundary: exact | paraphrase | operational_translation | analogy
```

### Triangulated-evidence gate

Every consequential claim must include at least three stabilizers:

```text
assertion + evidence + independent witness
implementation + test + provenance
actor + policy + receipt
artifact + hash + replay
model_output + source + verifier
```

### Projection-loss gate

Every transformation from source to representation must declare:

```yaml
projection_loss:
  source_surface: required
  target_surface: required
  preserves: []
  loses: []
  distortion_risks: []
  confidence_effect: required
```

### Membrane accounting gate

Every boundary must declare:

```yaml
membrane:
  admits: []
  blocks: []
  transforms: []
  logs: []
  witnesses: []
  redacts: []
  revokes: []
```

### Capability-radius gate

Every agent capability must declare:

```yaml
capability_radius:
  sensing_range: required
  action_range: required
  communication_range: required
  temporal_range: required
  external_effect_range: required
  escalation_required: boolean
```

### Dymaxion and entropy gate

Every performance claim must include:

```yaml
dymaxion_metric:
  useful_verified_service: required
  denominator:
    material: optional
    energy: optional
    labor: optional
    compute: optional
    cost: optional
    time: optional
    review_minutes: optional
    maintenance: optional
    policy_exceptions: optional
    attack_surface: optional
  baseline: required
  uncertainty: required
  evidence_refs: required
```

### Manual commons gate

A mature artifact should include:

```text
purpose
parts / dependencies
build steps
validation steps
repair steps
failure modes
known limitations
revision history
public-safe evidence examples
```

## Turn ledger

| Turn | Target | Repo | Output |
| --- | --- | --- | --- |
| 1 | Systema control files | ProCybernetica | this file + estate plan |
| 2 | Fuller/Synergetics source capture | ProCybernetica | source-confidence doctrine capture |
| 3 | Anti-pattern and conformance spine | ProCybernetica | anti-patterns, triangulated evidence, membrane docs |
| 4 | Profile layer | ProCybernetica | source confidence, projection loss, frequency, capability radius profiles |
| 5 | Issue fanout | ProCybernetica | downstream issues |
| 6 | Concept-entry model | Ontogenesis | SHACL/JSON-LD spec |
| 7 | Seed concept inventory | Ontogenesis | Dymaxion, tensegrity, geodesic, membrane, etc. |
| 8 | Vocabulary drift detector | Ontogenesis | drift SHACL and examples |
| 9 | Concept promotion ladder | Ontogenesis | promotion lifecycle |
| 10 | Catalog doctrine | Sherlock | evaluated access docs |
| 11 | Catalog examples | Sherlock | concept/tool/manual result examples |
| 12 | Search projection loss | Sherlock | confidence/projection docs |
| 13 | World-pattern inventory | GAIA | Mini-Earth/data-tetrahedron docs |
| 14 | Geodesic/frequency examples | GAIA | route/projection/frequency examples |
| 15 | Livingry scenarios | GAIA | resource coordination scenario |
| 16 | Tensegrity runtime | AgentPlane | tension-member contract |
| 17 | Capability radius | AgentPlane | reachability examples |
| 18 | Oversteer detector | AgentPlane | churn/oscillation indicators |
| 19 | Agent Machine membrane | agent-machine | activation membrane example |
| 20 | State membrane | sourceos-syncd | membrane event example |
| 21 | Dymaxion metrics | delivery-excellence | verified service/resource docs |
| 22 | Entropy ledger | delivery-excellence | entropy metrics |
| 23 | Evidence/membrane standards | prophet-platform-standards | patterns and PR template |
| 24 | Runtime bridge | prophet-platform | Systema evidence bridge |
| 25 | Manual commons | ProCybernetica | manuals |
| 26 | Cross-repo validation | ProCybernetica | validation index |
| 27 | Public review package | ProCybernetica | checklist and status ledger |
| 28 | v0 closure | ProCybernetica | clean backlog and v0 declaration |

## Non-goals for v0

- Do not add a large new schema family in ProCybernetica.
- Do not duplicate AgentPlane runtime evidence.
- Do not duplicate Ontogenesis ontology release discipline.
- Do not duplicate Sherlock runtime search implementation.
- Do not duplicate SourceOS/SociOS typed contracts.
- Do not build GAIA simulation runtime in ProCybernetica.
- Do not promote low-confidence Fuller/OCR text as authoritative doctrine.
- Do not let analogy become proof.

## Definition of Systema v0 done

Systema v0 is ready for public review when:

1. ProCybernetica has this control file, estate absorption plan, source-confidence doctrine, profiles, conformance docs, and manuals.
2. Ontogenesis has a concept-entry model and seed concepts.
3. Sherlock has evaluated-access result requirements and examples.
4. GAIA has world-pattern inventory and projection/frequency doctrine.
5. AgentPlane has tensegrity runtime and capability-radius examples.
6. SourceOS surfaces have membrane/state-integrity mapping.
7. Delivery Excellence has Dymaxion and entropy metrics.
8. Platform Standards has triangulated evidence and membrane patterns.
9. Prophet Platform has a runtime bridge plan.
10. Every downstream work item has an issue, owner, status, and validation command.
