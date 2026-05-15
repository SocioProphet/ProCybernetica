# Falsification Observable Owners

Status: v0.1 machine-checkable registry  
Issue: #45  
Publication state: public  
Runtime claim: none

This document defines the owner registry used by `scripts/validate_falsification_coverage.py`. The JSON block is intentionally machine-readable. Edit owner records there, not only in prose.

```json
{
  "registry_version": "v1",
  "owners": [
    {
      "owner_id": "procybernetica-doctrine",
      "role": "Doctrine owner",
      "responsibility": "Maintains falsification doctrine, publication boundary, claim discipline, source ambiguity handling, and human-review posture.",
      "escalation": "maintainer-review",
      "downstream_boundary": "Does not own runtime enforcement or production telemetry."
    },
    {
      "owner_id": "procybernetica-schema",
      "role": "Schema and fixture owner",
      "responsibility": "Maintains JSON Schema, SHACL/Rego handoff notes, fixture contracts, validation expectations, and schema-testable falsification coverage.",
      "escalation": "maintainer-review",
      "downstream_boundary": "Does not own downstream runtime implementation."
    },
    {
      "owner_id": "procybernetica-ci",
      "role": "Repository validation owner",
      "responsibility": "Maintains repository-local validation scripts, Makefile targets, fixture checks, and CI coverage for public falsification artifacts.",
      "escalation": "maintainer-review",
      "downstream_boundary": "Does not claim live monitoring coverage."
    },
    {
      "owner_id": "estate-adapter-owner",
      "role": "Cross-repository adapter owner",
      "responsibility": "Maintains anti-fork boundaries, cross-repo evidence freshness, adapter follow-ups, and ownership mapping where another estate repo owns the contract or runtime surface.",
      "escalation": "maintainer-review",
      "downstream_boundary": "References downstream owners rather than duplicating their surfaces in ProCybernetica."
    },
    {
      "owner_id": "runtime-plane-owner",
      "role": "Runtime surface owner",
      "responsibility": "Owns downstream runtime telemetry, policy enforcement, side-effect records, cancellation behavior, capability invocation telemetry, and deployment mitigations outside ProCybernetica.",
      "escalation": "maintainer-review",
      "downstream_boundary": "ProCybernetica may define doctrine and validation contracts but does not assert production runtime readiness here."
    },
    {
      "owner_id": "maintainer-review",
      "role": "Human review owner",
      "responsibility": "Handles ambiguous, high-impact, privacy-sensitive, dignity-sensitive, or cross-boundary falsification cases that require explicit review rather than automatic promotion.",
      "escalation": "maintainer-review",
      "downstream_boundary": "May assign follow-up work to doctrine, schema, CI, adapter, or runtime owners."
    }
  ]
}
```

## Non-claims

This registry assigns responsibility for repository validation and doctrine follow-up. It does not claim that production telemetry, runtime enforcement, or external estate integrations are implemented in this repository.
