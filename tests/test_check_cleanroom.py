"""Tests for the clean-room guard — both ways.

The guard must (a) pass on the actual framework files as shipped, (b) BITE on a real
leak, and (c) exclude itself. A guard only ever seen to pass is not a guard.
"""

from __future__ import annotations

from pathlib import Path

from procyber.semantic.check_cleanroom import (
    FRAMEWORK_FILES,
    framework_files,
    scan_paths,
)


def test_the_shipped_framework_is_clean():
    # the real surface, as committed, must have no third-party marks
    assert scan_paths(framework_files()) == []


def test_the_guard_bites_on_a_real_leak(tmp_path: Path):
    leak = tmp_path / "leaky.py"
    # the exact class of leak the review caught: naming the third-party metalanguage
    leak.write_text("# derived from the IEML dictionary\nx = 1\n", encoding="utf-8")
    hits = scan_paths([str(leak)])
    assert len(hits) == 1
    assert hits[0][1] == 1  # line number
    assert hits[0][2].lower() == "ieml"


def test_the_guard_catches_each_forbidden_mark(tmp_path: Path):
    for token in ("IEML", "INTLEKT", "Lévy", "Levy"):
        f = tmp_path / f"{token}.md"
        f.write_text(f"see {token} for background\n", encoding="utf-8")
        assert scan_paths([str(f)]), f"{token} should have been flagged"


def test_the_guard_excludes_itself(tmp_path: Path):
    # even if the checker is explicitly passed to itself, it must not flag its own
    # forbidden-pattern source — a scanner that flags itself is broken.
    self_path = Path(__file__).resolve().parents[1] / "procyber" / "semantic" / "check_cleanroom.py"
    assert scan_paths([str(self_path)]) == []


def test_framework_manifest_excludes_the_guard_and_its_test():
    # self-exclusion by construction: the manifest must not list the guard/its test.
    assert not any("check_cleanroom" in rel for rel in FRAMEWORK_FILES)


def test_manifest_covers_every_shipped_kernel_module():
    """A module added without being registered must FAIL, not pass silently.

    The manifest is hand-maintained, so the failure mode is a new kernel module
    that the clean-room never scans while the check still reports OK. That is a
    green control not covering the artifact — the exact thing this suite exists
    to prevent. Discovered live: market_paradigm.py shipped and the scan count
    did not move.
    """
    pkg = Path(__file__).resolve().parents[1] / "procyber" / "semantic"
    shipped = {
        f"procyber/semantic/{p.name}"
        for p in pkg.glob("*.py")
        if p.name not in {"__init__.py", "check_cleanroom.py"}
    }
    unregistered = shipped - set(FRAMEWORK_FILES)
    assert not unregistered, (
        "kernel modules missing from FRAMEWORK_FILES (clean-room would skip them): "
        f"{sorted(unregistered)}"
    )
