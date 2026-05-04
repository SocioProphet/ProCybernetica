# 20-Turn Integration Plan

Status: active

Purpose: integrate ProCybernetica with the current SocioProphet, SourceOS-Linux, SociOS-Linux, and mdheller estate over a bounded 20-turn execution window, then stop at a stable public-review point.

## Operating posture

This plan follows:

- `docs/integration/ESTATE_ALIGNMENT_AUDIT.md`
- `docs/integration/RECENT_CONTRIBUTION_ALIGNMENT.md`
- `docs/decisions/0001-public-first-transparency.md`
- `docs/decisions/0002-v0-contract-scope.md`
- `AGENTS.md`

ProCybernetica remains the public constitutional standard, doctrine-as-code, schema/profile, conformance, and reference-kit layer.

Runtime, deployment, ontology release, semantic serialization, workstation, boot, and evidence surfaces remain owned by their canonical repositories.

## Definition of a good stopping point

At the end of the 20-turn window, the repository should have:

1. Clear estate mappings for AgentPlane, semantic-serdes/SHIR, ontogenesis, SourceOS/SociOS, Prophet Platform, and HolographMe.
2. v0 schema/profile contracts reconciled against those mappings.
3. Public synthetic fixtures that validate through CI.
4. A minimal public reference CLI that validates the practicum fixtures and emits a report.
5. Integration issues opened for downstream adapters, not runtime duplication.
6. Documentation that clearly states what ProCybernetica owns versus what upstream repos own.
7. A stable completion readout and remaining backlog.

## Non-goals during this 20-turn window

- Do not build a full runtime platform inside ProCybernetica.
- Do not duplicate AgentPlane evidence artifacts.
- Do not duplicate semantic-serdes or SHIR contracts.
- Do not duplicate ontogenesis ontology release discipline.
- Do not duplicate SourceOS/SociOS typed contracts.
- Do not implement Prophet Platform runtime services.
- Do not ingest private or uncleared raw data.

## Turn plan

### Turn 1 — Integration control plan

Deliverables:

- Add this 20-turn integration plan.
- Add integration stop criteria.
- Create or update an integration epic issue.

### Turn 2 — AgentPlane evidence map

Deliverables:

- `docs/integration/agentplane-evidence-map.md`
- Map ProCybernetica envelopes to AgentPlane Validation, Placement, Run, Replay, Promotion, Reversal, Session, and other evidence artifacts.

### Turn 3 — semantic-serdes / SHIR map

Deliverables:

- `docs/integration/semantic-serdes-shir-map.md`
- Map Claim/Event/Trace/Replay/Surface concepts to semantic-serdes and SHIR.

### Turn 4 — ontogenesis governance map

Deliverables:

- `docs/integration/ontogenesis-governance-map.md`
- Map claims, ontology refs, SHACL gates, ledgers, signatures, and generated artifacts.

### Turn 5 — SourceOS/SociOS contract map

Deliverables:

- `docs/integration/sourceos-socios-contract-map.md`
- Map SourceOS/SociOS contracts to ProCybernetica evidence and node surfaces.

### Turn 6 — Prophet Platform record map

Deliverables:

- `docs/integration/prophet-platform-record-map.md`
- Map FogStack, identity, office runtime, eval fabric, AgentPlane/PolicyPlane linkage, and parity readiness records.

### Turn 7 — HolographMe / Genesis-Inception map

Deliverables:

- `docs/integration/holographme-genesis-inception-map.md`
- Map HolographMe schema/governance/operating model into Genesis/Inception/K3 backlog.

### Turn 8 — Functional Model / Foundry / Model Router map

Deliverables:

- `docs/integration/foundry-model-governance-map.md`
- Map functional-model-surfaces, model-router, model-governance-ledger, guardrail-fabric, and Professional Intelligence surfaces.

### Turn 9 — Workstation/operator UX map

Deliverables:

- `docs/integration/workstation-operator-surface-map.md`
- Map source-os, workstation-contracts, agent-term, TurtleTerm, BearBrowser, and socioprophet-web UX/control-plane surfaces.

### Turn 10 — Schema reconciliation update

Deliverables:

- Update `docs/reconciliation/SCHEMA_PROFILE_RECONCILIATION.md`
- Identify schemas to keep, map, defer, or adapt.

### Turn 11 — Profile reconciliation update

Deliverables:

- Reconcile lifecycle, K3, BT, promotion, and public release profiles against integration maps.

### Turn 12 — Adapter backlog

Deliverables:

- `docs/integration/ADAPTER_BACKLOG.md`
- List concrete adapters with owning upstream repo and ProCybernetica contract touched.

### Turn 13 — Public conformance plan

Deliverables:

- `docs/conformance/README.md`
- Define v0 conformance ladder and public checks.

### Turn 14 — CI/conformance hardening

Deliverables:

- Ensure CI validates schemas, fixtures, and practicum report path.
- Add missing tests if gaps remain.

### Turn 15 — Scoring/dashboard publication next step

Deliverables:

- Add public sample schema/fixture plan for full scoring bodies.
- Open issue for raw/sanitized artifact publication if still pending.

### Turn 16 — README and Start Here integration refresh

Deliverables:

- Update README and `docs/START_HERE.md` to reflect mapping-complete state.

### Turn 17 — Downstream issue fanout

Deliverables:

- Ensure ProCybernetica issues exist for every downstream adapter and no duplicate issues remain open.

### Turn 18 — Stable public review checklist

Deliverables:

- `docs/PUBLIC_REVIEW_CHECKLIST.md`
- Check public-first, estate alignment, schema/profile readiness, fixtures, CI, and integration maps.

### Turn 19 — Completion ledger

Deliverables:

- `docs/INTEGRATION_STATUS.md`
- Percent completion by lane and known gaps.

### Turn 20 — Stop point

Deliverables:

- Final repo status update.
- Close completed issues where appropriate.
- Leave only clean backlog issues.
- Stop at stable public-review state.

## Work channels tracked

| Channel | Target by Turn 20 |
| --- | --- |
| Blueprint capture | stable, no further expansion except addenda audit |
| Estate alignment | complete for canonical upstream surfaces |
| Schema/profile v0 | reconciled enough for public review |
| Public fixtures | validating in CI |
| Reference CLI | validates fixtures and emits report |
| Scoring/dashboard | public methodology and samples complete; raw artifact publication planned or started |
| Platform integration | mapped, not implemented in this repo |
| Agent lanes | clean issues for downstream work |

## Stop discipline

If a turn reveals new scope, it becomes a follow-up issue unless it blocks the v0 public-review state.

The goal is convergence, not exhaustiveness.
