#!/usr/bin/env python3
"""Validate the Research Architect skill suite layout."""
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_SKILLS = [
    "research-architect",
    "research-architect-intake",
    "research-architect-brainstorm",
    "research-architect-literature",
    "research-architect-design",
    "research-architect-evidence",
    "research-architect-citation",
    "research-architect-draft",
    "research-architect-audit",
]

REQUIRED_REFERENCES = [
    "operating-principles.md",
    "end-to-end-workflow.md",
    "research-spine.md",
    "brainstorming-framework.md",
    "literature-map-framework.md",
    "design-family-grammars.md",
    "study-design-framework.md",
    "claim-evidence-framework.md",
    "first-draft-architecture.md",
    "citation-support-bank.md",
    "quality-gates.md",
    "ethics-and-boundaries.md",
]

REQUIRED_TEMPLATES = [
    "project_config.json",
    "exemplar_logic_profile.md",
    "exemplar_adaptation_plan.md",
    "study_design_brief.md",
    "study_component_registry.csv",
    "evidence_bank.csv",
    "claim_register.csv",
    "evidence_display_map.csv",
    "section_blueprints.md",
    "writing_rationale_matrix.csv",
]

REQUIRED_SCRIPTS = [
    "build_release.py",
    "first_paper_artifact_check.py",
    "make_source_index.py",
    "validate_skill_package.py",
    "check_reference_adaptation_fixtures.py",
]

BANNED_PHRASES = [
    "prestige-label calibration",
    "venue-specific reverse engineering as required frame",
    "unsupported field-specific assumption",
    "copy exemplar content",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def check_skill_dir(skills_dir: Path, label: str) -> None:
    if not skills_dir.exists():
        fail(f"missing {label}: {skills_dir}")
    for skill in REQUIRED_SKILLS:
        skill_dir = skills_dir / skill
        skill_md = skill_dir / "SKILL.md"
        manifest = skill_dir / "manifest.yaml"
        readme = skill_dir / "README.md"
        if not skill_md.exists():
            fail(f"missing {skill_md}")
        if not manifest.exists():
            fail(f"missing {manifest}")
        if readme.exists():
            fail(f"installable skill folder should not include README.md: {readme}")
        text = skill_md.read_text(encoding="utf-8")
        if not text.startswith("---"):
            fail(f"{skill_md} is missing YAML front matter")
        for phrase in BANNED_PHRASES:
            if phrase.lower() in text.lower():
                fail(f"banned phrase '{phrase}' found in {skill_md}")


def check_required_files(directory: Path, required: list[str], label: str) -> None:
    if not directory.exists():
        fail(f"missing {label}: {directory}")
    for name in required:
        path = directory / name
        if not path.exists():
            fail(f"missing {label} file: {path}")
        if path.is_file() and path.stat().st_size == 0:
            fail(f"empty {label} file: {path}")


def check_reference_fixtures(root: Path) -> None:
    fixture_dir = root / "evals" / "reference_adaptation"
    expected = {
        "quantitative_associational.json",
        "qualitative_interpretive.json",
        "comparative_case.json",
        "mixed_methods.json",
    }
    if not fixture_dir.exists():
        fail(f"missing reference-adaptation fixtures: {fixture_dir}")
    missing = sorted(name for name in expected if not (fixture_dir / name).exists())
    if missing:
        fail(f"missing reference-adaptation fixture files: {', '.join(missing)}")


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    if not root.exists():
        fail(f"root does not exist: {root}")

    if (root / "skills").exists():
        fail("top-level skills/ duplicate should not exist; use src/skills as source and dist/codex/skills as output")

    check_skill_dir(root / "src" / "skills", "source skills")
    check_skill_dir(root / "dist" / "codex" / "skills", "generated Codex skills")

    check_required_files(root / "src" / "references", REQUIRED_REFERENCES, "source reference")
    check_required_files(root / "src" / "templates", REQUIRED_TEMPLATES, "source template")
    check_required_files(root / "src" / "scripts", REQUIRED_SCRIPTS, "source script")
    check_reference_fixtures(root)

    release = root / "release" / "research-architect-codex-skills.tar.gz"
    checksums = root / "release" / "SHA256SUMS"
    if not release.exists():
        fail(f"missing release artifact {release}")
    if not checksums.exists():
        fail(f"missing release checksums {checksums}")

    generated_root = root / "dist" / "codex" / "skills" / "research-architect"
    check_required_files(generated_root / "references", REQUIRED_REFERENCES, "generated reference")
    check_required_files(generated_root / "templates", REQUIRED_TEMPLATES, "generated template")
    check_required_files(generated_root / "scripts", REQUIRED_SCRIPTS, "generated script")

    print("PASS: Research Architect skill package structure is valid.")


if __name__ == "__main__":
    main()
