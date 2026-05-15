from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CROSS_REF = ROOT / "docs" / "falsification" / "observable-cross-reference.md"
OWNERS = ROOT / "docs" / "falsification" / "observable-owners.md"
FIXTURE = ROOT / "tests" / "fixtures" / "falsification" / "falsification-fixtures.synthetic.json"
COVERAGE_VALIDATOR = ROOT / "scripts" / "validate_falsification_coverage.py"
FIXTURE_VALIDATOR = ROOT / "scripts" / "validate_falsification_fixture.py"


def extract_json_block(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```json\s*\n(?P<payload>.*?)\n```", text, flags=re.DOTALL)
    assert match, f"missing JSON block in {path}"
    return json.loads(match.group("payload"))


def test_falsification_coverage_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, str(COVERAGE_VALIDATOR)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "PASS: falsification coverage registry validates" in result.stdout


def test_falsification_fixture_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, str(FIXTURE_VALIDATOR)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "PASS: validated" in result.stdout


def test_owner_registry_is_non_empty_and_unique() -> None:
    payload = extract_json_block(OWNERS)
    owners = payload["owners"]
    owner_ids = [owner["owner_id"] for owner in owners]

    assert owners
    assert len(owner_ids) == len(set(owner_ids))
    assert "procybernetica-doctrine" in owner_ids
    assert "runtime-plane-owner" in owner_ids
    assert "maintainer-review" in owner_ids


def test_fixture_backed_observables_have_synthetic_fixtures() -> None:
    cross_ref = extract_json_block(CROSS_REF)
    fixture_payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    fixture_ids = {fixture["observable_id"] for fixture in fixture_payload["fixtures"]}

    required_ids = {
        observable["id"]
        for observable in cross_ref["observables"]
        if observable["fixture_status"] in {"fixture_required", "fixture_present"}
    }

    assert required_ids
    assert required_ids <= fixture_ids


def test_runtime_only_observables_are_marked_monitoring() -> None:
    cross_ref = extract_json_block(CROSS_REF)
    offenders = [
        observable["id"]
        for observable in cross_ref["observables"]
        if "runtime-telemetry" in observable["evidence_class"]
        and observable["fixture_status"] not in {"runtime_monitoring", "fixture_required", "fixture_present"}
    ]

    assert offenders == []
