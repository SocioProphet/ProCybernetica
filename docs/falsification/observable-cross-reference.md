# Falsification Observable Cross-Reference

Status: v0.1 machine-checkable registry  
Issue: #45  
Publication state: public  
Runtime claim: none

This registry operationalizes `docs/falsification/unified-falsification-v1.0.md` without claiming runtime telemetry. The JSON block is parsed by `scripts/validate_falsification_coverage.py`.

```json
{
  "registry_version": "v1",
  "source_doctrine": "docs/falsification/unified-falsification-v1.0.md",
  "owners_registry": "docs/falsification/observable-owners.md",
  "expected_architectural_layers": [
    "source_provenance",
    "schema_conformance",
    "promotion_replay",
    "reasoning_evidence",
    "authority_control",
    "publication_boundary",
    "estate_alignment",
    "capability_dependency",
    "bridge_mapping"
  ],
  "expected_ci_invariants": [
    "source_anchor_visible",
    "schema_status_explicit",
    "promotion_requires_evidence",
    "reasoning_not_evidence",
    "authority_scope_visible",
    "publication_boundary_preserved",
    "estate_owner_not_forked",
    "runtime_only_marked_monitoring",
    "fixture_backing_declared"
  ],
  "observables": [
    {"id":"F1.1","layer":"source_provenance","severity":"high","condition":"Doctrine or schema claim lacks source anchor, issue anchor, or proposal marker.","detection_mechanism":"static_cross_reference","revision_direction":"doctrine_revision; claim_hold","owner":"procybernetica-doctrine","evidence_class":"human-review; ci-testable","fixture_status":"no_fixture_required","ci_invariants":["source_anchor_visible"]},
    {"id":"F1.2","layer":"source_provenance","severity":"moderate","condition":"Source ambiguity is erased instead of recorded.","detection_mechanism":"human_review","revision_direction":"doctrine_revision","owner":"procybernetica-doctrine","evidence_class":"human-review","fixture_status":"no_fixture_required","ci_invariants":["source_anchor_visible"]},
    {"id":"F1.3","layer":"source_provenance","severity":"critical","condition":"Private or sensitive source evidence is committed without redaction boundary.","detection_mechanism":"secret_scan_and_human_review","revision_direction":"deployment_hold; doctrine_revision; audit_escalation","owner":"maintainer-review","evidence_class":"ci-testable; human-review","fixture_status":"no_fixture_required","ci_invariants":["publication_boundary_preserved"]},
    {"id":"F1.4","layer":"source_provenance","severity":"moderate","condition":"Artifact is claimed as mirrored when only a summary exists.","detection_mechanism":"periodic_audit","revision_direction":"doctrine_revision; claim_hold","owner":"procybernetica-doctrine","evidence_class":"human-review; periodic-audit","fixture_status":"no_fixture_required","ci_invariants":["source_anchor_visible"]},

    {"id":"F2.1","layer":"schema_conformance","severity":"high","condition":"A provisional schema is treated as canonical before reconciliation freeze.","detection_mechanism":"static_phrase_review","revision_direction":"schema_revision; doctrine_revision","owner":"procybernetica-schema","evidence_class":"human-review; ci-testable","fixture_status":"no_fixture_required","ci_invariants":["schema_status_explicit"]},
    {"id":"F2.2","layer":"schema_conformance","severity":"high","condition":"Certificate, bridge, or governance schema lacks companion validation coverage or explicit deferred status.","detection_mechanism":"schema_inventory","revision_direction":"schema_revision; claim_hold","owner":"procybernetica-schema","evidence_class":"schema-testable; ci-testable","fixture_status":"deferred_until_schema","ci_invariants":["schema_status_explicit","fixture_backing_declared"]},
    {"id":"F2.3","layer":"schema_conformance","severity":"high","condition":"Enum drift emerges between doctrine, schema, fixture, and downstream contract.","detection_mechanism":"enum_inventory","revision_direction":"schema_revision; adapter_revision","owner":"procybernetica-schema","evidence_class":"ci-testable","fixture_status":"deferred_until_schema","ci_invariants":["schema_status_explicit"]},
    {"id":"F2.4","layer":"schema_conformance","severity":"critical","condition":"Positive fixture passes while violating a named invariant.","detection_mechanism":"fixture_validation","revision_direction":"schema_revision; deployment_hold","owner":"procybernetica-ci","evidence_class":"fixture-testable","fixture_status":"fixture_required","ci_invariants":["fixture_backing_declared"]},
    {"id":"F2.5","layer":"schema_conformance","severity":"high","condition":"Negative fixture fails for the wrong reason or passes.","detection_mechanism":"fixture_validation","revision_direction":"schema_revision; ci-testable repair","owner":"procybernetica-ci","evidence_class":"fixture-testable","fixture_status":"fixture_required","ci_invariants":["fixture_backing_declared"]},

    {"id":"F3.1","layer":"promotion_replay","severity":"critical","condition":"Soft-lane output is promoted without evidence, policy, audit, and promotion decision.","detection_mechanism":"fixture_validation_and_human_review","revision_direction":"claim_hold; doctrine_revision; schema_revision","owner":"procybernetica-doctrine","evidence_class":"fixture-testable; human-review","fixture_status":"fixture_present","ci_invariants":["promotion_requires_evidence","fixture_backing_declared"]},
    {"id":"F3.2","layer":"promotion_replay","severity":"high","condition":"Replay path is absent for a promoted artifact or decision.","detection_mechanism":"schema_validation","revision_direction":"claim_hold; schema_revision","owner":"procybernetica-schema","evidence_class":"schema-testable","fixture_status":"deferred_until_schema","ci_invariants":["promotion_requires_evidence"]},
    {"id":"F3.3","layer":"promotion_replay","severity":"high","condition":"Reversal or supersession path is missing.","detection_mechanism":"schema_validation_and_human_review","revision_direction":"schema_revision; doctrine_revision","owner":"procybernetica-schema","evidence_class":"schema-testable; human-review","fixture_status":"deferred_until_schema","ci_invariants":["promotion_requires_evidence"]},
    {"id":"F3.4","layer":"promotion_replay","severity":"high","condition":"Promotion decision does not identify evidence level.","detection_mechanism":"fixture_validation","revision_direction":"claim_hold; schema_revision","owner":"procybernetica-schema","evidence_class":"fixture-testable","fixture_status":"fixture_required","ci_invariants":["promotion_requires_evidence","fixture_backing_declared"]},

    {"id":"F4.1","layer":"reasoning_evidence","severity":"high","condition":"Reasoning operations are conflated with evidence.","detection_mechanism":"claim_boundary_lint_and_human_review","revision_direction":"doctrine_revision; claim_hold","owner":"procybernetica-doctrine","evidence_class":"human-review; ci-testable","fixture_status":"no_fixture_required","ci_invariants":["reasoning_not_evidence"]},
    {"id":"F4.2","layer":"reasoning_evidence","severity":"high","condition":"Cairnmarks are indistinguishable from Steles.","detection_mechanism":"schema_validation_and_human_review","revision_direction":"schema_revision; doctrine_revision","owner":"procybernetica-schema","evidence_class":"schema-testable; human-review","fixture_status":"deferred_until_schema","ci_invariants":["schema_status_explicit","reasoning_not_evidence"]},
    {"id":"F4.3","layer":"reasoning_evidence","severity":"critical","condition":"Defeasible support is treated as silent authority.","detection_mechanism":"human_review_and_runtime_monitoring","revision_direction":"claim_hold; runtime_mitigation; schema_revision","owner":"maintainer-review","evidence_class":"human-review; runtime-telemetry","fixture_status":"runtime_monitoring","ci_invariants":["authority_scope_visible","runtime_only_marked_monitoring"]},
    {"id":"F4.4","layer":"reasoning_evidence","severity":"critical","condition":"Reasoning trace references expose private chain or sensitive material.","detection_mechanism":"secret_scan_and_human_review","revision_direction":"deployment_hold; doctrine_revision","owner":"maintainer-review","evidence_class":"human-review","fixture_status":"no_fixture_required","ci_invariants":["publication_boundary_preserved","reasoning_not_evidence"]},

    {"id":"F5.1","layer":"authority_control","severity":"critical","condition":"Authority chain is absent for governed action.","detection_mechanism":"schema_validation_and_runtime_monitoring","revision_direction":"runtime_mitigation; schema_revision; deployment_hold","owner":"runtime-plane-owner","evidence_class":"schema-testable; runtime-telemetry","fixture_status":"runtime_monitoring","ci_invariants":["authority_scope_visible","runtime_only_marked_monitoring"]},
    {"id":"F5.2","layer":"authority_control","severity":"critical","condition":"Tool or capability scope is broader than declared policy.","detection_mechanism":"runtime_monitoring_and_periodic_audit","revision_direction":"runtime_mitigation; deployment_hold","owner":"runtime-plane-owner","evidence_class":"runtime-telemetry; periodic-audit","fixture_status":"runtime_monitoring","ci_invariants":["authority_scope_visible","runtime_only_marked_monitoring"]},
    {"id":"F5.3","layer":"authority_control","severity":"high","condition":"Side effects are not recorded or are misclassified as no-op.","detection_mechanism":"runtime_monitoring_and_fixture_validation","revision_direction":"runtime_mitigation; schema_revision","owner":"runtime-plane-owner","evidence_class":"runtime-telemetry; fixture-testable","fixture_status":"runtime_monitoring","ci_invariants":["authority_scope_visible","runtime_only_marked_monitoring"]},
    {"id":"F5.4","layer":"authority_control","severity":"critical","condition":"Break-glass or cancellation path fails closed incorrectly or silently succeeds.","detection_mechanism":"runtime_monitoring_and_periodic_audit","revision_direction":"runtime_mitigation; deployment_hold; audit_escalation","owner":"runtime-plane-owner","evidence_class":"runtime-telemetry; periodic-audit","fixture_status":"runtime_monitoring","ci_invariants":["authority_scope_visible","runtime_only_marked_monitoring"]},

    {"id":"F6.1","layer":"publication_boundary","severity":"critical","condition":"Public artifact contains private or sensitive evidence.","detection_mechanism":"secret_scan_and_human_review","revision_direction":"deployment_hold; audit_escalation; doctrine_revision","owner":"maintainer-review","evidence_class":"ci-testable; human-review","fixture_status":"no_fixture_required","ci_invariants":["publication_boundary_preserved"]},
    {"id":"F6.2","layer":"publication_boundary","severity":"moderate","condition":"Artifact is withheld under vague privacy language.","detection_mechanism":"human_review","revision_direction":"doctrine_revision; claim_hold","owner":"procybernetica-doctrine","evidence_class":"human-review","fixture_status":"no_fixture_required","ci_invariants":["publication_boundary_preserved"]},
    {"id":"F6.3","layer":"publication_boundary","severity":"moderate","condition":"Public-safe substitute is missing for a withheld artifact category.","detection_mechanism":"periodic_audit","revision_direction":"doctrine_revision; schema_revision","owner":"procybernetica-doctrine","evidence_class":"periodic-audit","fixture_status":"periodic_audit","ci_invariants":["publication_boundary_preserved"]},
    {"id":"F6.4","layer":"publication_boundary","severity":"high","condition":"Redaction removes the evidentiary structure needed for review.","detection_mechanism":"human_review","revision_direction":"doctrine_revision; claim_hold","owner":"procybernetica-doctrine","evidence_class":"human-review","fixture_status":"no_fixture_required","ci_invariants":["publication_boundary_preserved"]},

    {"id":"F7.1","layer":"estate_alignment","severity":"high","condition":"ProCybernetica forks a contract already owned by another repository.","detection_mechanism":"estate_mapping_review","revision_direction":"adapter_revision; schema_revision","owner":"estate-adapter-owner","evidence_class":"human-review; periodic-audit","fixture_status":"periodic_audit","ci_invariants":["estate_owner_not_forked"]},
    {"id":"F7.2","layer":"estate_alignment","severity":"high","condition":"Runtime ownership is displaced into ProCybernetica.","detection_mechanism":"human_review","revision_direction":"doctrine_revision; adapter_revision; deployment_hold","owner":"estate-adapter-owner","evidence_class":"human-review","fixture_status":"no_fixture_required","ci_invariants":["estate_owner_not_forked"]},
    {"id":"F7.3","layer":"estate_alignment","severity":"moderate","condition":"Adapter boundary is absent after an estate mapping declares one.","detection_mechanism":"periodic_audit_and_issue_link_check","revision_direction":"adapter_revision; claim_hold","owner":"estate-adapter-owner","evidence_class":"periodic-audit; ci-testable","fixture_status":"periodic_audit","ci_invariants":["estate_owner_not_forked"]},
    {"id":"F7.4","layer":"estate_alignment","severity":"moderate","condition":"Cross-repo evidence is cited without freshness or version boundary.","detection_mechanism":"manifest_or_pr_review","revision_direction":"adapter_revision; claim_hold","owner":"estate-adapter-owner","evidence_class":"human-review; ci-testable","fixture_status":"no_fixture_required","ci_invariants":["estate_owner_not_forked"]},

    {"id":"F8.1","layer":"capability_dependency","severity":"high","condition":"Dependency ancestry concentrates around a single evidence source.","detection_mechanism":"synthetic_dependency_fixture_and_runtime_monitoring","revision_direction":"schema_revision; claim_hold; runtime_mitigation","owner":"procybernetica-schema","evidence_class":"fixture-testable; runtime-telemetry","fixture_status":"fixture_required","ci_invariants":["fixture_backing_declared","runtime_only_marked_monitoring"]},
    {"id":"F8.2","layer":"capability_dependency","severity":"critical","condition":"Cancellation paths produce silent contradictions.","detection_mechanism":"fixture_validation_and_runtime_monitoring","revision_direction":"schema_revision; runtime_mitigation; deployment_hold","owner":"runtime-plane-owner","evidence_class":"fixture-testable; runtime-telemetry","fixture_status":"fixture_required","ci_invariants":["fixture_backing_declared","runtime_only_marked_monitoring"]},
    {"id":"F8.3","layer":"capability_dependency","severity":"critical","condition":"Adaptive feedback loop gain exceeds stability threshold.","detection_mechanism":"runtime_monitoring_or_synthetic_simulation","revision_direction":"runtime_mitigation; deployment_hold; doctrine_revision","owner":"runtime-plane-owner","evidence_class":"runtime-telemetry","fixture_status":"runtime_monitoring","ci_invariants":["runtime_only_marked_monitoring"]},
    {"id":"F8.4","layer":"capability_dependency","severity":"high","condition":"Capability-tier invocation rate exceeds expected baseline.","detection_mechanism":"runtime_monitoring_and_periodic_audit","revision_direction":"runtime_mitigation; audit_escalation; deployment_hold","owner":"runtime-plane-owner","evidence_class":"runtime-telemetry; periodic-audit","fixture_status":"runtime_monitoring","ci_invariants":["runtime_only_marked_monitoring"]},

    {"id":"B1","layer":"bridge_mapping","severity":"critical","condition":"Human actor maps to reputation or governance consequence without consent evidence.","detection_mechanism":"fixture_validation","revision_direction":"schema_revision; claim_hold; deployment_hold","owner":"procybernetica-schema","evidence_class":"fixture-testable","fixture_status":"fixture_required","ci_invariants":["fixture_backing_declared","publication_boundary_preserved"]},
    {"id":"B2","layer":"bridge_mapping","severity":"critical","condition":"Candidate proof pack maps to promoted Stele certificate.","detection_mechanism":"fixture_validation","revision_direction":"schema_revision; claim_hold","owner":"procybernetica-schema","evidence_class":"fixture-testable","fixture_status":"fixture_required","ci_invariants":["fixture_backing_declared","promotion_requires_evidence"]},
    {"id":"B3","layer":"bridge_mapping","severity":"critical","condition":"Undecided certificate fails open into Atlas admission.","detection_mechanism":"fixture_validation","revision_direction":"schema_revision; deployment_hold","owner":"procybernetica-schema","evidence_class":"fixture-testable","fixture_status":"fixture_required","ci_invariants":["fixture_backing_declared"]},
    {"id":"B4","layer":"bridge_mapping","severity":"critical","condition":"Pattern C or prohibited pattern is admitted.","detection_mechanism":"fixture_validation","revision_direction":"schema_revision; deployment_hold","owner":"procybernetica-schema","evidence_class":"fixture-testable","fixture_status":"fixture_required","ci_invariants":["fixture_backing_declared"]}
  ]
}
```

## Non-claims

This registry records validation coverage and planned detection mechanisms. Entries marked `runtime_monitoring`, `periodic_audit`, or `deferred_until_schema` are not represented as implemented runtime telemetry or complete schema coverage.
