"""Tests for the cluster-member record renderer (cluster-member.v1 vocabulary)."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "examples" / "triune" / "lab" / "triune-lab.synthetic.yaml"
SCHEMA_PATH = ROOT / "schemas" / "triune" / "cluster-member.v1.json"

_renderer_path = ROOT / "tools" / "triune" / "render-cluster-member.py"
_spec = importlib.util.spec_from_file_location("render_cluster_member", _renderer_path)
assert _spec and _spec.loader
_mod = importlib.util.module_from_spec(_spec)
sys.modules["render_cluster_member"] = _mod
_spec.loader.exec_module(_mod)

load_inventory = _mod.load_inventory
resolve_member = _mod.resolve_member
render = _mod.render


def _schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _render(member: str, live: bool = False, status: str = "observed") -> dict:
    inventory = load_inventory(INVENTORY)
    entry = resolve_member(inventory, member)
    return render(entry, inventory, live=live, operator="test-operator", status=status)


@pytest.mark.parametrize("member", ["genesys", "k3-a", "k3-b", "inception-i1", "inception-i2", "inception-i3"])
def test_every_inventory_member_renders_schema_valid(member: str) -> None:
    record = _render(member)
    jsonschema.validate(record, _schema())


@pytest.mark.parametrize(
    "member,role",
    [("genesys", "genesys"), ("k3-a", "twin_bastion"), ("inception-i1", "inception")],
)
def test_member_role_mapping_is_canonical(member: str, role: str) -> None:
    assert _render(member)["member_role"] == role


def test_certificate_kind_and_schema_version() -> None:
    record = _render("inception-i1")
    assert record["certificate_kind"] == "triune_cluster_member"
    assert record["schema_version"] == "1.0.0"


def test_kubeconfig_contents_are_never_embedded() -> None:
    record = _render("inception-i1")
    blob = json.dumps(record)
    for marker in ("apiVersion:", "client-certificate-data", "client-key-data", "BEGIN CERTIFICATE"):
        assert marker not in blob
    assert record["endpoints"]["kubeconfig_secret_ref"].startswith("local://kubeconfigs/")


def test_workstation_and_bastion_have_no_endpoints_block() -> None:
    assert "endpoints" not in _render("genesys")
    assert "endpoints" not in _render("k3-a")


def test_default_deny_is_false_until_evidence() -> None:
    record = _render("inception-i1")
    assert record["networking"]["default_deny"] is False
    assert any("default_deny" in claim for claim in record["non_claims"])


def test_safety_status_is_honestly_unknown() -> None:
    record = _render("inception-i1")
    safety = record["safety_status"]
    assert safety["gate_result"] == "unknown"
    assert safety["epsilon_eff"] == 0.0
    assert safety["lambda_b"] == 0.0
    assert any("gate_result=unknown" in claim for claim in record["non_claims"])


def test_live_flag_records_runtime_partial() -> None:
    synthetic = _render("inception-i1", live=False)
    live = _render("inception-i1", live=True)
    assert synthetic["execution_status"] == "synthetic_fixture"
    assert live["execution_status"] == "runtime_partial"
    jsonschema.validate(live, _schema())


def test_federation_mode_comes_from_inventory() -> None:
    assert _render("inception-i1")["networking"]["federation_mode"] == "cilium_clustermesh"


def test_unknown_member_raises_with_known_list() -> None:
    inventory = load_inventory(INVENTORY)
    with pytest.raises(ValueError, match="not found in inventory"):
        resolve_member(inventory, "no-such-member")


def test_ledger_entry_uses_canonical_shape() -> None:
    entry = _render("inception-i1")["ledger_entry"]
    assert set(entry) == {"event_id", "event_type", "created_at"}
    assert entry["event_type"] == "cluster_member_record_created"


def test_non_mapping_inventory_is_refused(tmp_path: Path) -> None:
    """Fail closed: an empty file parses as None and a list/scalar root parses as a
    non-mapping; either would crash resolve_member() on .get(). load_inventory must
    refuse with a clear error instead."""
    empty = tmp_path / "empty.yaml"
    empty.write_text("", encoding="utf-8")
    with pytest.raises(ValueError, match="must be a YAML mapping"):
        load_inventory(empty)

    list_root = tmp_path / "list.yaml"
    list_root.write_text("- a\n- b\n", encoding="utf-8")
    with pytest.raises(ValueError, match="must be a YAML mapping"):
        load_inventory(list_root)
