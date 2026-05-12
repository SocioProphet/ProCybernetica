# Repository ownership map — Atlas, FCBCP, HSP-Map, Trueman Mesh, and HPL capture

Status: seed map v0.1.

Owner: ProCybernetica reconciliation track.

Purpose: assign each capture domain to an accountable repository while preserving authority boundaries across the SocioProphet / SourceOS stack.

This map is not a runtime dependency graph. It is a capture and accountability map.

## 1. Authority principles

1. Ownership does not imply universal authority.
2. A repo may own doctrine but not execution.
3. A repo may own planning but not authorization.
4. A repo may own human-boundary claims but not human actuation.
5. A repo may own world-model actions but not unchecked world intervention.
6. A repo may stage schemas locally during reconciliation, but canonical schema promotion may belong elsewhere.
7. Atlas validity never bypasses policy, trust surface, consent, redress, or evidence-tier gates.

## 2. Primary repo roles

| Repo | Primary role | Must own | Must not own |
|---|---|---|---|
| `SocioProphet/ProCybernetica` | Doctrine, reconciliation, conformance law, protection layer, status vocabulary, claim boundary, control-node mapping | HPL doctrine, Atlas reconciliation, claim-boundary register, evidence tiers, policy-status vocabulary, conformance plan | Human raw evidence, live runtime execution, private telemetry, final SourceOS canonical schemas before promotion |
| `SocioProphet/human-digital-twin` | Human-boundary profile, Ω readiness, consented claims, privacy/minimization, FCBCP/HSP-Map research profile | HDT HPL adoption, FCBCP docs, HSP-Map schema, human export envelope, negative tests, research-only fixtures | Human actuation runtime, raw private evidence export by default, world-chart governance |
| `SocioProphet/gaia-world-model` | Earth/world-model profile, curation vault, canonical ontology, validation, action templates, reports | GAIA HPL adoption, affected-population review, world Atlas profile, action report templates | Human claim export, human actuation, ProCybernetica doctrine authority, Superconscious planning authority |
| `SocioProphet/superconscious` | Thin cognition/planning loop, policy-admission requests, safe traces, replay/benchmark emission | HPL planning adoption, HPLScope event, Atlas planning adapter, blocked-plan fixtures | Schema authority, execution authority, human actuation authority, GAIA action promotion, HDT export authorization |

## 3. Adjacent authority repos

These repos are not the first capture targets here, but the ownership map must reserve their authority.

| Repo / authority | Role in final system |
|---|---|
| `SourceOS-Linux/sourceos-spec` | Canonical SourceOS schema promotion after reconciliation where applicable |
| `SocioProphet/agentplane` | Execution evidence and replay authority |
| `SocioProphet/sociosphere` | Workspace topology, project/issue routing, registry governance |
| Guardrail / Policy Fabric | Policy admission and gate decisions |
| Agent Registry | Identity, grants, skills, tools, sessions, memory grants |
| `SocioProphet/model-router` | Model route decisions |
| `SocioProphet/model-governance-ledger` | Model consent, promotion, and governance receipts |
| SourceOS runtime repos | Runtime substrate, local service declarations, trust surfaces |

## 4. Domain ownership

| Domain | Name | Primary owner | Adopters / consumers | Capture phase |
|---|---|---|---|---|
| D0 | Human Protection Layer | ProCybernetica | HDT, GAIA, Superconscious, future Atlas profiles | doctrine captured, reconciliation open |
| D1 | Digital Control Atlas | ProCybernetica | GAIA, HDT, Superconscious | needs reconciliation doc |
| D2 | FCBCP v1.0 | human-digital-twin | ProCybernetica, Superconscious | needs HDT docs and research-only profile |
| D3 | HSP-Map | human-digital-twin | GAIA, ProCybernetica | needs schema and atlas docs |
| D4 | Trueman Mesh | human-digital-twin | Superconscious, ProCybernetica | needs simulation-only program profile |
| D5 | Validated precursor science | human-digital-twin | ProCybernetica | needs citation-backed doctrine doc |
| D6 | Negative claim boundary / wave-genetics firewall | ProCybernetica | HDT, Superconscious | partially captured in HPL, needs register |
| D7 | Materials and instrumentation stack | human-digital-twin | ProCybernetica | needs research documentation; no runtime |
| D8 | Biological mechanism spine | human-digital-twin | ProCybernetica | needs mechanism doc and time-scale ladder |
| D9 | GAIA world-action safety | gaia-world-model | ProCybernetica | adoption stub committed; needs templates/tests |
| D10 | Superconscious planning safety | superconscious | ProCybernetica | adoption stub committed; needs fixtures/tests |
| D11 | ProCybernetica control-node law | ProCybernetica | SourceOS spec, AgentPlane, all adopters | needs mapping doc |
| D12 | Evidence, replay, provenance, publication boundary | ProCybernetica | all adopters | partially captured; needs conformance plan |

## 5. Ownership by artifact class

| Artifact class | Owner | Notes |
|---|---|---|
| Doctrine / reconciliation | ProCybernetica | Public-first, sanitize narrowly |
| Human-boundary claim envelope | human-digital-twin | Must include Ω, evidence tier, consent, minimization, redress, policy status |
| World-action template | gaia-world-model | Must include provenance, affected-population review, reversibility, report path |
| Planning/trace event | superconscious | Must include HPLScope and policy-admission state |
| Claim-boundary register | ProCybernetica | Downstream repos consume blocked mechanism labels |
| Evidence-tier vocabulary | ProCybernetica | Downstream repos consume; SourceOS spec may later canonicalize schema |
| Status vocabulary | ProCybernetica | Must not collapse into pass/fail |
| FCBCP/HSP schemas | human-digital-twin | Research-only default; no actuation runtime |
| GAIA reports | gaia-world-model | Must be generated and attributable |
| Superconscious traces | superconscious | Safe operational facts only; no raw private chain-of-thought or private evidence |
| Replay evidence | AgentPlane | External authority; Superconscious emits compatible artifacts |
| Canonical schemas | SourceOS spec or owning canonical schema repo after reconciliation | ProCybernetica may stage candidates |

## 6. Cross-repo flow

### Human-boundary flow

```text
Atlas / FCBCP research construct
  -> HDT evidence claim
  -> Ω evaluation
  -> HPL gate evaluation
  -> policy decision
  -> minimal export or block
```

### World-action flow

```text
Atlas world construct
  -> GAIA Curation Vault / source provenance
  -> canonical ontology entrypoint
  -> validation
  -> action template
  -> affected-population review
  -> report
  -> policy decision
```

### Planning flow

```text
Task input
  -> Superconscious HPLScope.assessed
  -> plan only / request policy / block
  -> safe operational trace
  -> AgentPlane-compatible evidence and replay plan
```

### Doctrine flow

```text
Source material
  -> ProCybernetica capture ledger
  -> reconciliation docs
  -> decision records
  -> schema candidates
  -> conformance plan
  -> downstream adoption
```

## 7. Do-not-cross boundaries

- HDT must not authorize human actuation.
- Superconscious must not authorize execution.
- GAIA must not bypass CV/provenance and affected-population review.
- ProCybernetica must not freeze schemas before reconciliation.
- Atlas validity must not imply exportability or permission.
- Research-only profiles must not be promoted to operational profiles without explicit review.
- Raw private human evidence must not be public by default.
- Unsupported mechanisms must not become planning assumptions.

## 8. Capture next steps by repo

### ProCybernetica

1. Finish capture ledger rows.
2. Add Digital Control Atlas reconciliation doc.
3. Add claim-boundary register.
4. Add evidence/status vocabulary docs.
5. Add Fractal Control Node mapping.
6. Draft HPL v0 decision record after reconciliation.

### Human Digital Twin

1. Add FCBCP v1 spec.
2. Add HSP-Map spec and schema.
3. Add Trueman Mesh simulation-only profile.
4. Add negative mechanism tests.
5. Add human export envelope tests.

### GAIA

1. Add affected-population review template.
2. Add Atlas world-profile doc.
3. Add action report template.
4. Add blocked-risk fixture.
5. Wire HPL checks into validation plan.

### Superconscious

1. Add HPLScope event fixture.
2. Add Atlas planning adapter doc.
3. Add blocked-plan fixture.
4. Add tests proving planning does not authorize execution.
5. Ensure HPL status is preserved in replay/benchmark artifacts.
