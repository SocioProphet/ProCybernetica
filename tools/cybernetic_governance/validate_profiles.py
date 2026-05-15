#!/usr/bin/env python3
"""Validate ProCybernetica v0 profile normalization.

This validator checks repository-local YAML profiles against the reconciled v0
profile decisions. It does not implement runtime lifecycle machinery, promotion
runtime, behavior-tree execution, or Genesis/Inception runtime services.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
PROFILE_DIR = ROOT / "profiles"

CONTROLPLANE = PROFILE_DIR / "controlplane_state_machine.yaml"
PROMOTION = PROFILE_DIR / "promotion_policy.example.yaml"
BT = PROFILE_DIR / "bt_semantic_profile.yaml"
K3 = PROFILE_DIR / "k3_bridge_lifecycle.yaml"

EXPECTED_NODE_STATES = [
    "unconfigured",
    "configured",
    "inactive",
    "active",
    "degraded",
    "recovery",
    "quarantined",
    "retired",
    "finalized",
]

EXPECTED_NODE_EVENTS = {
    "configure_ok",
    "admission_granted",
    "admission_denied",
    "activate_ok",
    "deactivate",
    "health_degraded",
    "recover_start",
    "recover_ok",
    "recover_failed",
    "quarantine",
    "remediation_ok",
    "revoke",
    "retire",
    "finalize",
}

EXPECTED_PROMOTION_DECISIONS = {
    "reject",
    "shadow-only",
    "limited-authority",
    "full-promotion",
    "quarantine",
    "manual-review",
    "rollback-required",
    "revoke-authority",
}

EXPECTED_K3_STATES = {
    "INIT_SESSION",
    "PROBE_ACCEPT",
    "INJECT_SEED",
    "SEED_PUBLISH",
    "VERIFY_TWIN",
    "TWIN_READY",
    "GATED_HOST_UPDATE",
    "QUARANTINE",
    "REVOKE",
    "ROLLBACK",
}

REQUIRED_PROFILE_FILES = {
    "controlplane_state_machine.yaml": CONTROLPLANE,
    "promotion_policy.example.yaml": PROMOTION,
    "bt_semantic_profile.yaml": BT,
    "k3_bridge_lifecycle.yaml": K3,
}


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing profile: {path}") from None
    if not isinstance(loaded, dict):
        raise SystemExit(f"profile must be a mapping: {path}")
    return loaded


def check(condition: bool, diagnostics: list[str], message: str) -> None:
    if not condition:
        diagnostics.append(message)


def validate_controlplane() -> dict[str, Any]:
    payload = load_yaml(CONTROLPLANE)
    diagnostics: list[str] = []
    states = payload.get("states", [])
    transitions = payload.get("transitions", [])
    events = {transition.get("event") for transition in transitions if isinstance(transition, dict)}

    check(states == EXPECTED_NODE_STATES, diagnostics, "node lifecycle states must match reconciled v0 order")
    check(payload.get("initial_state") == "unconfigured", diagnostics, "initial_state must be unconfigured")
    check(set(payload.get("terminal_states", [])) == {"retired", "finalized"}, diagnostics, "terminal states must be retired/finalized")
    check(EXPECTED_NODE_EVENTS <= events, diagnostics, "canonical lifecycle events missing")
    check("transition_aliases" in payload, diagnostics, "transition_aliases must preserve source aliases")
    check(all(t.get("evidence_required") is True for t in transitions), diagnostics, "every transition must require evidence")
    check("retired" in payload.get("state_meanings", {}), diagnostics, "retired meaning must be explicit")
    check("finalized" in payload.get("state_meanings", {}), diagnostics, "finalized meaning must be explicit")

    return {"profile": "controlplane_state_machine.yaml", "passed": not diagnostics, "diagnostics": diagnostics}


def validate_promotion() -> dict[str, Any]:
    payload = load_yaml(PROMOTION)
    diagnostics: list[str] = []
    decisions = set(payload.get("accepted_decisions", []))
    budgets = set(payload.get("authority_budgets", {}).keys())
    rules = payload.get("decision_rules", [])

    check(decisions == EXPECTED_PROMOTION_DECISIONS, diagnostics, "accepted_decisions must match ADR-0002 vocabulary")
    check(budgets == EXPECTED_PROMOTION_DECISIONS, diagnostics, "authority_budgets must cover every decision")
    check(all(rule.get("decision") in decisions for rule in rules if isinstance(rule, dict)), diagnostics, "all decision_rules must use accepted decisions")
    check(payload.get("thresholds", {}).get("require_replay_refs") is True, diagnostics, "promotion policy must require replay refs")
    check(payload.get("thresholds", {}).get("require_policy_refs") is True, diagnostics, "promotion policy must require policy refs")
    check(payload.get("thresholds", {}).get("require_evidence_refs") is True, diagnostics, "promotion policy must require evidence refs")
    invariants = "\n".join(payload.get("invariants", []))
    check("not direct actuator commands" in invariants, diagnostics, "rollback/revocation governance boundary must be explicit")

    return {"profile": "promotion_policy.example.yaml", "passed": not diagnostics, "diagnostics": diagnostics}


def validate_bt() -> dict[str, Any]:
    payload = load_yaml(BT)
    diagnostics: list[str] = []

    check(payload.get("tick_model") == "root_to_leaf_sequential", diagnostics, "BT tick_model must be pinned")
    check(payload.get("halt_policy") == "explicit_halt_required", diagnostics, "BT halt_policy must be explicit_halt_required")
    check(payload.get("execution_boundary", {}).get("procybernetica_does_not_own"), diagnostics, "BT runtime non-ownership boundary must be explicit")
    check(payload.get("leaf_nodes", {}).get("must_emit_status_events") is True, diagnostics, "BT leaf nodes must emit status events")
    check(payload.get("observability", {}).get("replay_reference_required_for_promotion") is True, diagnostics, "BT profile must require replay reference for promotion")
    check("AgentPlane" not in payload.get("profile_id", ""), diagnostics, "BT profile must remain ProCybernetica semantic profile, not AgentPlane runtime profile")

    return {"profile": "bt_semantic_profile.yaml", "passed": not diagnostics, "diagnostics": diagnostics}


def validate_k3() -> dict[str, Any]:
    payload = load_yaml(K3)
    diagnostics: list[str] = []
    states = set(payload.get("states", []))
    transitions = payload.get("transitions", [])

    check(states == EXPECTED_K3_STATES, diagnostics, "K3 lifecycle states must match reconciled profile")
    check(payload.get("initial_state") == "INIT_SESSION", diagnostics, "K3 initial state must be INIT_SESSION")
    check(set(payload.get("terminal_states", [])) == {"REVOKE", "ROLLBACK"}, diagnostics, "K3 terminal states must be REVOKE/ROLLBACK")
    check("domain_object_ref_pattern" in payload, diagnostics, "K3 profile must reference domain-owned objects without cloning schemas")
    check(all(t.get("evidence_required") is True for t in transitions), diagnostics, "every K3 transition must require evidence")
    owners = set(payload.get("ownership_boundary", {}).get("upstream_domain_owners", []))
    check("SocioProphet/HolographMe" in owners, diagnostics, "K3 profile must preserve HolographMe domain ownership")
    invariants = "\n".join(payload.get("invariants", []))
    check("does not clone domain twin or identity models" in invariants, diagnostics, "K3 domain non-cloning invariant must be explicit")

    return {"profile": "k3_bridge_lifecycle.yaml", "passed": not diagnostics, "diagnostics": diagnostics}


def validate() -> dict[str, Any]:
    file_results = []
    for name, path in REQUIRED_PROFILE_FILES.items():
        file_results.append({"profile": name, "exists": path.exists(), "passed": path.exists(), "diagnostics": [] if path.exists() else ["missing file"]})

    profile_results = [
        validate_controlplane(),
        validate_promotion(),
        validate_bt(),
        validate_k3(),
    ]
    results = file_results + profile_results
    return {
        "validator": "procybernetica_v0_profile.validator.v1",
        "passed": all(result["passed"] for result in results),
        "profile_count": len(REQUIRED_PROFILE_FILES),
        "results": results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = validate()
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: v0 profiles validate")
        else:
            print("FAIL: v0 profiles validate", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
