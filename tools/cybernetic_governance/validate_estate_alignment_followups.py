#!/usr/bin/env python3
"""Validate estate-alignment follow-up fixtures for #15, #16, and #17.

This validator checks public-synthetic adapter fixtures and conformance notes.
It does not implement Ontogenesis validation, model routing, model-governance
runtime, guardrail runtime, workstation runtime, terminal runtime, browser
runtime, dashboard runtime, or UI implementation.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "tests" / "fixtures" / "estate-alignment" / "estate-alignment-followups.synthetic.json"
CONFORMANCE_DOC = ROOT / "docs" / "integration" / "ESTATE_ALIGNMENT_FOLLOWUP_CONFORMANCE.md"

REQUIRED_ISSUES = {"#15", "#16", "#17"}
REQUIRED_FAMILIES = {"ontogenesis", "foundry_model_governance", "operator_workstation"}
REQUIRED_MAPS = {
    "docs/integration/ontogenesis-governance-map.md",
    "docs/integration/foundry-model-governance-map.md",
    "docs/integration/workstation-operator-surface-map.md",
}

REQUIRED_ACCEPTANCE = {
    "#15": [
        "validated claims include ontology refs",
        "validated claims include validation evidence",
        "ProCybernetica references Ontogenesis artifacts instead of duplicating ontology schemas",
    ],
    "#16": [
        "Foundry maturity can be represented as a public score slice",
        "model-route evidence can be represented as a public score slice",
        "EvaluationResult and PromotionDecision examples can cite external model-governance surfaces",
    ],
    "#17": [
        "operator/gateway surfaces preserve identity, scope, policy refs, evidence refs, replay/receipt path, approval posture, and public-safe projection",
        "dashboards are treated as operator review surfaces",
        "CommandEnvelope and CapabilityDescriptor examples can reference upstream operator surfaces without owning terminal/browser/runtime behavior",
    ],
}

REQUIRED_DOC_PHRASES = [
    "validated semantic claims must carry ontology_ref and validation evidence refs",
    "model-governance evidence rows must cite external owning surfaces",
    "operator/gateway surfaces must preserve identity, scope, policy refs, evidence refs, replay/receipt path, approval posture, and public-safe projection",
    "Public score slices may reference",
    "must not claim ownership",
]


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing fixture file: {path}") from None


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"missing doc file: {path}") from None


def validate_fixture(record: dict[str, Any]) -> dict[str, Any]:
    diagnostics: list[str] = []
    issue_ref = record.get("issue_ref")

    if issue_ref not in REQUIRED_ISSUES:
        diagnostics.append(f"unexpected issue_ref: {issue_ref}")
    if record.get("adapter_family") not in REQUIRED_FAMILIES:
        diagnostics.append(f"unexpected adapter_family: {record.get('adapter_family')}")
    if record.get("map_ref") not in REQUIRED_MAPS:
        diagnostics.append(f"unexpected map_ref: {record.get('map_ref')}")
    if not record.get("external_owner"):
        diagnostics.append("external_owner is required")
    if not record.get("payload"):
        diagnostics.append("payload is required")
    if not record.get("non_claims"):
        diagnostics.append("non_claims are required")

    expected_acceptance = REQUIRED_ACCEPTANCE.get(str(issue_ref), [])
    observed_acceptance = record.get("acceptance_checks", [])
    missing_acceptance = [item for item in expected_acceptance if item not in observed_acceptance]
    if missing_acceptance:
        diagnostics.append(f"missing acceptance checks: {missing_acceptance}")

    payload = record.get("payload", {})
    if issue_ref == "#15":
        if not payload.get("ontology_ref"):
            diagnostics.append("#15 fixture must include ontology_ref")
        if not payload.get("shacl_report_ref") or not payload.get("ledger_ref"):
            diagnostics.append("#15 fixture must include SHACL and ledger refs")
        if payload.get("claim_status") != "validated":
            diagnostics.append("#15 fixture must model a validated claim")
    if issue_ref == "#16":
        for key in ["foundry_maturity_ref", "model_route_ref", "evaluation_result_ref", "promotion_decision_ref", "public_score_slice_ref"]:
            if not payload.get(key):
                diagnostics.append(f"#16 fixture missing {key}")
    if issue_ref == "#17":
        for key in ["operator_surface_ref", "command_envelope_ref", "capability_descriptor_ref", "receipt_ref", "replay_ref", "policy_ref", "approval_ref", "dashboard_surface_ref", "public_projection_ref"]:
            if not payload.get(key):
                diagnostics.append(f"#17 fixture missing {key}")

    return {
        "fixture_id": record.get("fixture_id", "<missing>"),
        "issue_ref": issue_ref,
        "adapter_family": record.get("adapter_family"),
        "passed": not diagnostics,
        "diagnostics": diagnostics,
    }


def validate() -> dict[str, Any]:
    fixture = load_json(FIXTURE)
    conformance = read(CONFORMANCE_DOC)
    records = fixture.get("fixtures", [])
    results = [validate_fixture(record) for record in records]

    observed_issues = {result["issue_ref"] for result in results}
    observed_families = {result["adapter_family"] for result in results}

    coverage_results = [
        {
            "check_id": "required-issues-covered",
            "passed": observed_issues == REQUIRED_ISSUES,
            "diagnostics": [] if observed_issues == REQUIRED_ISSUES else [f"observed issues {sorted(observed_issues)}"],
        },
        {
            "check_id": "required-adapter-families-covered",
            "passed": observed_families == REQUIRED_FAMILIES,
            "diagnostics": [] if observed_families == REQUIRED_FAMILIES else [f"observed families {sorted(observed_families)}"],
        },
    ]

    for phrase in REQUIRED_DOC_PHRASES:
        coverage_results.append(
            {
                "check_id": f"conformance-doc:{phrase[:40]}",
                "passed": phrase in conformance,
                "diagnostics": [] if phrase in conformance else [f"missing phrase: {phrase}"],
            }
        )

    all_results = results + coverage_results
    return {
        "validator": "estate_alignment_followups.validator.v1",
        "passed": all(result["passed"] for result in all_results),
        "fixture_count": len(records),
        "results": all_results,
        "non_claims": fixture.get("non_claims", [
            "No upstream runtime implementation is introduced.",
            "No upstream schemas are copied or redefined."
        ]),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = validate()
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: estate alignment follow-ups")
        else:
            print("FAIL: estate alignment follow-ups", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
