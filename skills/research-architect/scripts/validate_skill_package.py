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
    "study-design-framework.md",
    "claim-evidence-framework.md",
    "first-draft-architecture.md",
    "citation-support-bank.md",
    "quality-gates.md",
    "ethics-and-boundaries.md",
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


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    if not root.exists():
        fail(f"root does not exist: {root}")

    skills_dir = root / "dist" / "codex" / "skills"
    if not skills_dir.exists():
        fail("missing dist/codex/skills")

    for skill in REQUIRED_SKILLS:
        skill_md = skills_dir / skill / "SKILL.md"
        manifest = skills_dir / skill / "manifest.yaml"
        if not skill_md.exists():
            fail(f"missing {skill_md}")
        if not manifest.exists():
            fail(f"missing {manifest}")
        text = skill_md.read_text(encoding="utf-8")
        if not text.startswith("---"):
            fail(f"{skill_md} is missing YAML front matter")
        for phrase in BANNED_PHRASES:
            if phrase.lower() in text.lower():
                fail(f"banned phrase '{phrase}' found in {skill_md}")

    ref_dir = root / "src" / "references"
    if not ref_dir.exists():
        fail("missing src/references")
    for ref in REQUIRED_REFERENCES:
        if not (ref_dir / ref).exists():
            fail(f"missing reference {ref}")

    template_dir = root / "src" / "templates"
    if not template_dir.exists() or not any(template_dir.iterdir()):
        fail("missing templates")

    print("PASS: Research Architect skill package structure is valid.")


if __name__ == "__main__":
    main()
