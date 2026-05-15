#!/usr/bin/env python3
"""Validate the 20-turn integration epic closeout.

This validator checks the public-review closeout artifacts for #14. It verifies
that the required turn-plan artifacts exist, the integration status table marks
all turns complete, the public-review checklist preserves non-claim boundaries,
and README/START_HERE no longer describe the repository as merely provisional
capture/reconciliation mode.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_PATHS = [
    "docs/integration/20_TURN_INTEGRATION_PLAN.md",
    "docs/integration/ADAPTER_BACKLOG.md",
    "docs/conformance/README.md",
    "docs/PUBLIC_REVIEW_CHECKLIST.md",
    "docs/INTEGRATION_STATUS.md",
    "README.md",
    "docs/START_HERE.md",
]

TURN_EVIDENCE = {
    1: "docs/integration/20_TURN_INTEGRATION_PLAN.md",
    2: "docs/integration/agentplane-evidence-map.md",
    3: "docs/integration/semantic-serdes-shir-map.md",
    4: "docs/integration/ontogenesis-governance-map.md",
    5: "docs/integration/sourceos-socios-contract-map.md",
    6: "docs/integration/prophet-platform-record-map.md",
    7: "docs/integration/holographme-genesis-inception-map.md",
    8: "docs/integration/foundry-model-governance-map.md",
    9: "docs/integration/workstation-operator-surface-map.md",
    10: "docs/reconciliation/SCHEMA_PROFILE_RECONCILIATION.md",
    11: "docs/profiles/V0_PROFILE_NORMALIZATION_STATUS.md",
    12: "docs/integration/ADAPTER_BACKLOG.md",
    13: "docs/conformance/README.md",
    18: "docs/PUBLIC_REVIEW_CHECKLIST.md",
    19: "docs/INTEGRATION_STATUS.md",
}

REQUIRED_MAKE_TARGETS = [
    "v0-schemas-ci",
    "profiles-ci",
    "cybernetic-governance-ci",
    "dependency-control-ci",
    "agentic-ops-ci",
    "bridges-ci",
    "certificate-v13-ci",
    "shacl-ci",
    "agentplane-binding-ci",
    "proof-pack-ci",
    "lawful-learning-ci",
    "hpl-ci",
    "book-xi-slice-a-ci",
    "civic-stack-ci",
    "estate-alignment-followups-ci",
]

REQUIRED_STATUS_PHRASES = [
    "The bounded 20-turn integration lane reached stable public-review state.",
    "| 20 | Stop point | complete |",
    "#32 CI Observation Ledger",
    "G7+ proof-pack / colimit / evidence-cocone",
    "downstream runtime adapters in owning repos",
]

REQUIRED_CHECKLIST_PHRASES = [
    "CI observation ledger issue remains open by design.",
    "Passing this checklist does not claim production readiness",
    "runtime implementation remains in owning upstream repos",
]

README_REQUIRED = [
    "stable public-review state",
    "docs/INTEGRATION_STATUS.md",
    "docs/PUBLIC_REVIEW_CHECKLIST.md",
    "docs/conformance/README.md",
    "Public-review readiness is not production-readiness",
]

START_HERE_REQUIRED = [
    "v0 public-review mode",
    "docs/INTEGRATION_STATUS.md",
    "docs/PUBLIC_REVIEW_CHECKLIST.md",
    "docs/conformance/README.md",
    "Leave the CI Observation Ledger open by design",
]

NON_CLAIMS = [
    "production runtime readiness",
    "live deployment",
    "runtime enforcement",
    "empirical model performance",
    "civic runtime operation",
    "human-impacting authorization",
    "downstream adapter implementation",
]


def read(path: str) -> str:
    full = ROOT / path
    try:
        return full.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"missing required path: {path}") from None


def check(condition: bool, check_id: str, diagnostics: list[str]) -> dict[str, Any]:
    return {"check_id": check_id, "passed": condition, "diagnostics": [] if condition else diagnostics}


def contains_all(check_id: str, text: str, phrases: list[str]) -> dict[str, Any]:
    missing = [phrase for phrase in phrases if phrase not in text]
    return check(not missing, check_id, [f"missing phrases: {missing}"])


def validate() -> dict[str, Any]:
    results: list[dict[str, Any]] = []

    for path in REQUIRED_PATHS:
        results.append(check((ROOT / path).exists(), f"path-exists:{path}", [f"missing {path}"]))

    for turn, path in TURN_EVIDENCE.items():
        results.append(check((ROOT / path).exists(), f"turn-{turn}-evidence:{path}", [f"missing turn {turn} evidence {path}"]))

    status = read("docs/INTEGRATION_STATUS.md")
    checklist = read("docs/PUBLIC_REVIEW_CHECKLIST.md")
    conformance = read("docs/conformance/README.md")
    readme = read("README.md")
    start_here = read("docs/START_HERE.md")
    makefile = read("Makefile")

    results.append(contains_all("integration-status-closeout", status, REQUIRED_STATUS_PHRASES))
    results.append(contains_all("public-review-checklist-boundary", checklist, REQUIRED_CHECKLIST_PHRASES))
    results.append(contains_all("readme-public-review-refresh", readme, README_REQUIRED))
    results.append(contains_all("start-here-public-review-refresh", start_here, START_HERE_REQUIRED))
    results.append(contains_all("integration-non-claims", status, NON_CLAIMS))
    results.append(contains_all("conformance-targets", conformance, REQUIRED_MAKE_TARGETS))
    results.append(contains_all("makefile-targets", makefile, REQUIRED_MAKE_TARGETS))

    passed = all(result["passed"] for result in results)
    return {
        "validator": "integration_closeout.validator.v1",
        "passed": passed,
        "results": results,
        "non_claims": [
            "Public-review closeout does not claim production readiness.",
            "Runtime implementation remains in owning upstream repositories.",
            "The CI Observation Ledger remains open by design."
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = validate()
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: integration closeout validates")
        else:
            print("FAIL: integration closeout validates", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
