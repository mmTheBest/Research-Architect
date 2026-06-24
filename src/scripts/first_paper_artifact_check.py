#!/usr/bin/env python3
"""Check whether a Research Architect run has the expected artifact trail."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import TypeAlias

Requirement: TypeAlias = str | tuple[str, ...]

REQUIRED_FOR_PLAN: list[Requirement] = [
    "project_config.json",
    "source_map.md",
    "source_inventory.md",
    "problem_landscape.md",
    "idea_candidate_matrix.md",
    "research_question_options.md",
    "feasibility_filter.md",
    "reference_materials/source_index.md",
    "concept_dossier.md",
    "corpus_inventory.md",
    "exemplar_method_map.md",
    "sota_gap_map.md",
    "motivation_options_after_literature.md",
    "confirmed_research_spine.md",
    "study_design_brief.md",
]

REQUIRED_FOR_DRAFT: list[Requirement] = REQUIRED_FOR_PLAN + [
    "analysis_plan.md",
    "evaluation_plan.md",
    ("study_component_registry.md", "experiment_registry.md"),
    "threats_to_validity.md",
    "evidence_bank.md",
    "claim_register.md",
    ("evidence_display_map.md", "figure_asset_map.md"),
    "claim_strength_calibration.md",
    "citation_support_bank.md",
    "section_blueprints.md",
    "writing_rationale_matrix.md",
    "first_draft/main.md",
]

TARGET_REFERENCE_REQUIRED: list[Requirement] = [
    "exemplar_logic_profile.md",
    "exemplar_adaptation_plan.md",
]


def check_file(path: Path) -> tuple[str, bool, str]:
    if not path.exists():
        return (str(path), False, "missing")
    if path.is_file() and path.stat().st_size == 0:
        return (str(path), False, "empty")
    return (str(path), True, "ok")


def check_requirement(root: Path, requirement: Requirement) -> tuple[str, bool, str]:
    if isinstance(requirement, str):
        return check_file(root / requirement)

    alternatives = [root / rel for rel in requirement]
    valid = [path for path in alternatives if path.exists() and path.stat().st_size > 0]
    label = " OR ".join(str(path) for path in alternatives)
    if valid:
        return (label, True, f"ok: {valid[0]}")
    return (label, False, "all compatible alternatives are missing or empty")


def target_references_declared(root: Path) -> bool:
    config_path = root / "project_config.json"
    if not config_path.exists():
        return False
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False
    refs = config.get("target_references", [])
    return isinstance(refs, list) and len(refs) > 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", nargs="?", default="paper_output")
    parser.add_argument("--mode", choices=["plan", "draft"], default="draft")
    parser.add_argument(
        "--target-reference",
        action="store_true",
        help="Require target-reference analysis artifacts even when project_config.json cannot be inspected.",
    )
    args = parser.parse_args()

    root = Path(args.output_dir)
    required = list(REQUIRED_FOR_PLAN if args.mode == "plan" else REQUIRED_FOR_DRAFT)
    if args.target_reference or target_references_declared(root):
        required.extend(TARGET_REFERENCE_REQUIRED)

    rows = [check_requirement(root, requirement) for requirement in required]
    failed = [row for row in rows if not row[1]]

    print("| Artifact | Status | Note |")
    print("|---|---|---|")
    for path, ok, note in rows:
        status = "PASS" if ok else "FAIL"
        print(f"| {path} | {status} | {note} |")

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
