"""Tests for the clean-room guard — both ways.

The guard must (a) pass on the actual framework files as shipped, (b) BITE on real
copied expression, (c) ALLOW truthful prose comparison, and (d) exclude itself. A
guard only ever seen to pass is not a guard — and a guard that fires on the wrong
thing is worse, because it buys confidence it has not earned.
"""

from __future__ import annotations

from pathlib import Path

from procyber.semantic.check_cleanroom import (
    COORDINATE_CITATION_LIMIT,
    FRAMEWORK_FILES,
    framework_files,
    scan_paths,
)


def test_the_shipped_framework_is_clean():
    assert scan_paths(framework_files()) == []


# --------------------------------------------------------------------------- #
# What the guard must ALLOW — the behaviour change
# --------------------------------------------------------------------------- #


def test_prose_naming_a_third_party_is_allowed(tmp_path: Path):
    """Nominative reference is lawful and is the evidence of independent creation.

    The old guard failed here. It tested the wrong invariant: a name-grep addresses
    neither element of a copying claim, and suppressing comparison forfeits the best
    proof that nothing was taken.
    """
    doc = tmp_path / "comparison.md"
    doc.write_text(
        "Our algebra differs from IEML in that layer is syntactic. "
        "Lévy's dictionary is CC BY-NC-ND and we take none of it.\n",
        encoding="utf-8",
    )
    assert scan_paths([str(doc)]) == []


def test_a_handful_of_cited_coordinate_tokens_is_allowed(tmp_path: Path):
    """Two identifiers quoted to support a factual claim is citation, not lexicon."""
    doc = tmp_path / "cited.md"
    doc.write_text(
        'Inference type is a grammatical inflection there: "E:.s.O:M:.-", '
        'alongside logical mood "E:.s.O:O:.-".\n',
        encoding="utf-8",
    )
    assert scan_paths([str(doc)]) == []


# --------------------------------------------------------------------------- #
# What the guard must BITE on — actual expression
# --------------------------------------------------------------------------- #


def test_transcribed_dictionary_markers_are_flagged(tmp_path: Path):
    """Zero tolerance: their presence means dictionary structure was copied."""
    leak = tmp_path / "leak.md"
    leak.write_text('@rootparadigm type:inflection "E:.M:O:.-".\n', encoding="utf-8")
    hits = scan_paths([str(leak)])
    assert hits
    assert any("dictionary marker" in h[2] for h in hits)


def test_each_dictionary_marker_is_caught(tmp_path: Path):
    for marker in ("@rootparadigm", "@inflection", "@auxiliary", "@junction", "@node"):
        f = tmp_path / f"{marker.strip('@')}.md"
        f.write_text(f"{marker} something\n", encoding="utf-8")
        assert scan_paths([str(f)]), f"{marker} should have been flagged"


def test_bulk_coordinate_tokens_are_flagged_as_lexicon(tmp_path: Path):
    """Past the citation limit it stops reading as citation and becomes a lexicon."""
    leak = tmp_path / "bulk.md"
    tokens = "\n".join(f'"U:{c}:E:."' for c in "SBTUASBTUASBT")
    leak.write_text(tokens + "\n", encoding="utf-8")
    hits = scan_paths([str(leak)])
    assert hits
    assert any("coordinate tokens" in h[2] for h in hits)


def test_the_citation_limit_is_the_actual_boundary(tmp_path: Path):
    """Prove the threshold, not just that something somewhere fires."""
    at_limit = tmp_path / "at.md"
    at_limit.write_text("\n".join(['"U:S:E:."'] * COORDINATE_CITATION_LIMIT), encoding="utf-8")
    assert scan_paths([str(at_limit)]) == []

    over = tmp_path / "over.md"
    over.write_text("\n".join(['"U:S:E:."'] * (COORDINATE_CITATION_LIMIT + 1)), encoding="utf-8")
    assert scan_paths([str(over)])


# --------------------------------------------------------------------------- #
# What the guard must BITE on — naming OUR artifacts with THEIR marks
# --------------------------------------------------------------------------- #


def test_mark_in_a_schema_identity_field_is_flagged(tmp_path: Path):
    leak = tmp_path / "schema.json"
    leak.write_text('{"title": "IEML Address v1", "type": "object"}\n', encoding="utf-8")
    hits = scan_paths([str(leak)])
    assert any("naming our artifact" in h[2] for h in hits)


def test_mark_in_a_python_definition_is_flagged(tmp_path: Path):
    leak = tmp_path / "mod.py"
    leak.write_text("class IemlAddress:\n    pass\n", encoding="utf-8")
    hits = scan_paths([str(leak)])
    assert any("naming our artifact" in h[2] for h in hits)


def test_mark_in_a_filename_is_flagged(tmp_path: Path):
    leak = tmp_path / "ieml_bridge.py"
    leak.write_text("x = 1\n", encoding="utf-8")
    hits = scan_paths([str(leak)])
    assert any("filename" in h[2] for h in hits)


def test_a_mark_in_a_comment_is_not_naming(tmp_path: Path):
    """The distinction the guard now draws: referring to theirs vs naming ours."""
    ok = tmp_path / "mod.py"
    ok.write_text("# unlike IEML, layer is syntactic here\nclass Address:\n    pass\n", encoding="utf-8")
    assert scan_paths([str(ok)]) == []


# --------------------------------------------------------------------------- #
# Self-exclusion and manifest completeness
# --------------------------------------------------------------------------- #


def test_the_guard_excludes_itself():
    self_path = Path(__file__).resolve().parents[1] / "procyber" / "semantic" / "check_cleanroom.py"
    assert scan_paths([str(self_path)]) == []


def test_framework_manifest_excludes_the_guard_and_its_test():
    assert not any("check_cleanroom" in rel for rel in FRAMEWORK_FILES)


def test_manifest_covers_every_shipped_kernel_module():
    """A module added without being registered must FAIL, not pass silently.

    The manifest is hand-maintained, so the failure mode is a new kernel module
    that the clean-room never scans while the check still reports OK. That is a
    green control not covering the artifact. Discovered live: market_paradigm.py
    shipped and the scan count did not move.
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


def test_manifest_covers_every_kernel_doc():
    """Same gap, different artifact class: an unregistered doc is an unscanned doc.

    The kernel's docs share the `SEMANTIC_` prefix precisely so one glob makes this
    check total. A doc added outside that family would not be caught here, which is
    why the prefix is a convention rather than a preference.
    """
    docs = Path(__file__).resolve().parents[1] / "docs"
    shipped = {f"docs/{p.name}" for p in docs.glob("SEMANTIC_*.md")}
    unregistered = shipped - set(FRAMEWORK_FILES)
    assert not unregistered, (
        "kernel docs missing from FRAMEWORK_FILES (clean-room would skip them): "
        f"{sorted(unregistered)}"
    )
