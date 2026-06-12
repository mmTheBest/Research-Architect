#!/usr/bin/env python3
"""Check whether a Research Architect run has the expected artifact trail."""
from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED_FOR_PLAN = [
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

REQUIRED_FOR_DRAFT = REQUIRED_FOR_PLAN + [
    "analysis_plan.md",
    "evaluation_plan.md",
    "experiment_registry.md",
    "threats_to_validity.md",
    "evidence_bank.md",
    "claim_register.md",
    "figure_asset_map.md",
    "claim_strength_calibration.md",
    "citation_support_bank.md",
    "section_blueprints.md",
    "writing_rationale_matrix.md",
    "first_draft/main.md",
]


def check_file(path: Path) -> tuple[str, bool, str]:
    if not path.exists():
        return (str(path), False, "missing")
    if path.is_file() and path.stat().st_size == 0:
        return (str(path), False, "empty")
    return (str(path), True, "ok")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", nargs="?", default="paper_output")
    parser.add_argument("--mode", choices=["plan", "draft"], default="draft")
    args = parser.parse_args()

    root = Path(args.output_dir)
    required = REQUIRED_FOR_PLAN if args.mode == "plan" else REQUIRED_FOR_DRAFT
    rows = [check_file(root / rel) for rel in required]
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
