# Profiles

Profiles pin executable semantics that should not be left implicit in prose.

The first profiles cover:

- lifecycle transitions for Fractal Nodes;
- promotion and quarantine thresholds;
- future behavior-tree semantics;
- future Genesis/Inception/K3 bridge semantics.

Profiles are intentionally separate from schemas. Schemas define payload shape. Profiles define admissible behavior, transition law, and operational interpretation.

## Planned profiles

- `controlplane_state_machine.yaml` — lawful node lifecycle transitions.
- `promotion_policy.example.yaml` — example thresholds for promotion, quarantine, and authority budgets.
- `bt_semantic_profile.yaml` — future behavior-tree execution semantics.
- `k3_bridge_lifecycle.yaml` — future Genesis/Inception/Twin bridge transitions.

## Rule

If a runtime behavior changes depending on undocumented assumptions, it should become a profile.
