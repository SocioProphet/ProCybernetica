# Reconciliation

This directory turns captured blueprint source-state into canonical repository decisions.

Capture preserves source state.

Reconciliation compares sources, records conflicts, and recommends v0 canonical contracts.

Implementation follows reconciliation.

## Current reconciliation targets

- schema and envelope family;
- lifecycle states and transition events;
- promotion/evaluation decision vocabulary;
- package and CLI naming;
- provisional files that need correction before v0.

## Rule

Do not erase source variation. Record where the blueprint corpus differs, then recommend a canonical v0 form with rationale.
