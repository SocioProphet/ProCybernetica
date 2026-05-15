from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "cybernetic_governance" / "validate_profiles.py"
PROFILE_DIR = ROOT / "profiles"

REQUIRED_PROFILES = {
    "controlplane_state_machine.yaml",
    "promotion_policy.example.yaml",
    "bt_semantic_profile.yaml",
    "k3_bridge_lifecycle.yaml",
}


def run_validator() -> dict:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def load_yaml(name: str) -> dict:
    return yaml.safe_load((PROFILE_DIR / name).read_text(encoding="utf-8"))


def test_v0_profile_validator_passes() -> None:
    payload = run_validator()
    assert payload["passed"] is True
    assert payload["profile_count"] == 4
    assert all(result["passed"] for result in payload["results"])


def test_required_profiles_exist_and_are_public_yaml() -> None:
    for profile in REQUIRED_PROFILES:
        path = PROFILE_DIR / profile
        assert path.exists()
        loaded = load_yaml(profile)
        assert loaded["profile_id"].startswith("procybernetica.")
        assert loaded["schema_version"] == "0.1.0"
        assert "source_basis" in loaded


def test_controlplane_profile_encodes_reconciled_v0_node_lifecycle() -> None:
    profile = load_yaml("controlplane_state_machine.yaml")
    assert profile["states"] == [
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
    assert set(profile["terminal_states"]) == {"retired", "finalized"}
    assert "transition_aliases" in profile
    assert all(transition["evidence_required"] is True for transition in profile["transitions"])


def test_promotion_profile_encodes_adr_0002_vocabulary_and_authority_budgets() -> None:
    profile = load_yaml("promotion_policy.example.yaml")
    decisions = set(profile["accepted_decisions"])
    assert decisions == set(profile["authority_budgets"])
    assert "rollback-required" in decisions
    assert "revoke-authority" in decisions
    assert profile["thresholds"]["require_replay_refs"] is True
    assert profile["thresholds"]["require_policy_refs"] is True
    assert profile["thresholds"]["require_evidence_refs"] is True


def test_bt_profile_records_semantic_boundary_not_runtime_ownership() -> None:
    profile = load_yaml("bt_semantic_profile.yaml")
    assert profile["tick_model"] == "root_to_leaf_sequential"
    assert profile["halt_policy"] == "explicit_halt_required"
    assert profile["execution_boundary"]["procybernetica_does_not_own"]
    assert profile["observability"]["replay_reference_required_for_promotion"] is True


def test_k3_profile_keeps_domain_refs_and_lifecycle_separate() -> None:
    profile = load_yaml("k3_bridge_lifecycle.yaml")
    assert profile["initial_state"] == "INIT_SESSION"
    assert set(profile["terminal_states"]) == {"REVOKE", "ROLLBACK"}
    assert "domain_object_ref_pattern" in profile
    assert "SocioProphet/HolographMe" in profile["ownership_boundary"]["upstream_domain_owners"]
    assert all(transition["evidence_required"] is True for transition in profile["transitions"])
