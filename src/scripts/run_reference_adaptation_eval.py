#!/usr/bin/env python3
"""Score reference-adaptation outputs against fixture contracts.

The harness is deterministic and offline. It expects generated artifacts to
already exist, then scores their coverage of the fixture's expected behavior.
"""
from __future__ import annotations

import argparse
import json
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PASS_THRESHOLD = 85.0

REQUIRED_ARTIFACTS = [
    "exemplar_logic_profile.md",
    "exemplar_adaptation_plan.md",
    "study_design_brief.md",
    "claim_register.md",
]

DIMENSION_WEIGHTS = {
    "extraction_coverage": 20.0,
    "adaptation_validity": 25.0,
    "design_family_fit": 15.0,
    "actionability": 15.0,
    "claim_control": 15.0,
    "copying_risk_control": 10.0,
}


@dataclass(frozen=True)
class DimensionScore:
    name: str
    score: float
    max_score: float
    covered: int
    total: int
    missing: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "score": self.score,
            "max_score": self.max_score,
            "covered": self.covered,
            "total": self.total,
            "missing": self.missing,
        }


@dataclass(frozen=True)
class FixtureScore:
    fixture_id: str
    title: str
    design_family: str
    artifact_dir: str
    total_score: float
    passed: bool
    critical_failures: list[str]
    dimension_scores: dict[str, DimensionScore]

    def to_dict(self) -> dict[str, Any]:
        return {
            "fixture_id": self.fixture_id,
            "title": self.title,
            "design_family": self.design_family,
            "artifact_dir": self.artifact_dir,
            "total_score": self.total_score,
            "pass_threshold": PASS_THRESHOLD,
            "passed": self.passed,
            "critical_failures": self.critical_failures,
            "dimension_scores": {
                name: score.to_dict()
                for name, score in self.dimension_scores.items()
            },
        }


def normalize_text(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return re.sub(r"\s+", " ", normalized).strip()


def phrase_present(phrase: str, text: str) -> bool:
    normalized_phrase = normalize_text(phrase)
    normalized_text = normalize_text(text)
    if not normalized_phrase:
        return False
    return f" {normalized_phrase} " in f" {normalized_text} "


def score_phrases(
    name: str,
    phrases: list[str],
    text: str,
    max_score: float,
) -> DimensionScore:
    if not phrases:
        return DimensionScore(name, max_score, max_score, 0, 0, [])

    missing = [phrase for phrase in phrases if not phrase_present(phrase, text)]
    covered = len(phrases) - len(missing)
    score = round(max_score * covered / len(phrases), 2)
    return DimensionScore(name, score, max_score, covered, len(phrases), missing)


def load_fixture(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_artifact_bundle(artifact_dir: Path) -> tuple[str, list[str]]:
    missing: list[str] = []
    chunks: list[str] = []

    for relative_path in REQUIRED_ARTIFACTS:
        path = artifact_dir / relative_path
        if not path.exists() or path.stat().st_size == 0:
            missing.append(relative_path)
            continue
        chunks.append(path.read_text(encoding="utf-8"))

    return "\n\n".join(chunks), missing


def score_adaptation_validity(fixture: dict[str, Any], text: str) -> DimensionScore:
    moves = fixture["expected"]["required_adaptation_moves"]
    expected_items: list[str] = []
    for move in moves:
        expected_items.extend(
            [
                move["reference_move"],
                move["decision"],
                move["required_user_action"],
            ]
        )
    return score_phrases(
        "adaptation_validity",
        expected_items,
        text,
        DIMENSION_WEIGHTS["adaptation_validity"],
    )


def score_actionability(fixture: dict[str, Any], text: str) -> DimensionScore:
    actions = [
        move["required_user_action"]
        for move in fixture["expected"]["required_adaptation_moves"]
    ]
    return score_phrases(
        "actionability",
        actions,
        text,
        DIMENSION_WEIGHTS["actionability"],
    )


def score_claim_control(
    fixture: dict[str, Any],
    text: str,
    forbidden_hits: list[str],
) -> DimensionScore:
    boundaries = fixture["expected"]["required_claim_boundaries"]
    boundary_score = score_phrases("claim_control", boundaries, text, 12.0)
    no_forbidden_score = 3.0 if not forbidden_hits else 0.0
    missing = list(boundary_score.missing)
    if forbidden_hits:
        missing.extend(f"forbidden inference present: {hit}" for hit in forbidden_hits)

    return DimensionScore(
        "claim_control",
        round(boundary_score.score + no_forbidden_score, 2),
        DIMENSION_WEIGHTS["claim_control"],
        boundary_score.covered + (0 if forbidden_hits else 1),
        boundary_score.total + 1,
        missing,
    )


def score_copying_risk_control(fixture: dict[str, Any], text: str) -> DimensionScore:
    context_bound_elements = fixture["target_reference"]["context_bound_elements"]
    context_score = score_phrases(
        "copying_risk_control",
        context_bound_elements,
        text,
        7.0,
    )
    boundary_terms = [
        "copying boundary",
        "transfer boundary",
        "context difference",
        "context-bound",
        "must not copy",
    ]
    has_boundary_term = any(phrase_present(term, text) for term in boundary_terms)
    missing = list(context_score.missing)
    if not has_boundary_term:
        missing.append("copying or transfer boundary marker")

    return DimensionScore(
        "copying_risk_control",
        round(context_score.score + (3.0 if has_boundary_term else 0.0), 2),
        DIMENSION_WEIGHTS["copying_risk_control"],
        context_score.covered + (1 if has_boundary_term else 0),
        context_score.total + 1,
        missing,
    )


def find_forbidden_inferences(fixture: dict[str, Any], text: str) -> list[str]:
    return [
        inference
        for inference in fixture["expected"]["forbidden_inferences"]
        if phrase_present(inference, text)
    ]


def score_fixture(fixture: dict[str, Any], artifact_dir: Path) -> FixtureScore:
    text, missing_artifacts = read_artifact_bundle(artifact_dir)
    expected = fixture["expected"]
    forbidden_hits = find_forbidden_inferences(fixture, text)

    dimension_scores = {
        "extraction_coverage": score_phrases(
            "extraction_coverage",
            expected["required_extraction_dimensions"],
            text,
            DIMENSION_WEIGHTS["extraction_coverage"],
        ),
        "adaptation_validity": score_adaptation_validity(fixture, text),
        "design_family_fit": score_phrases(
            "design_family_fit",
            [fixture["design_family"]],
            text,
            DIMENSION_WEIGHTS["design_family_fit"],
        ),
        "actionability": score_actionability(fixture, text),
        "claim_control": score_claim_control(fixture, text, forbidden_hits),
        "copying_risk_control": score_copying_risk_control(fixture, text),
    }

    critical_failures = [
        f"Missing required artifact: {artifact}" for artifact in missing_artifacts
    ]
    critical_failures.extend(
        f"Forbidden inference present: {inference}"
        for inference in forbidden_hits
    )

    total_score = round(
        sum(score.score for score in dimension_scores.values()),
        2,
    )
    passed = total_score >= PASS_THRESHOLD and not critical_failures

    return FixtureScore(
        fixture_id=fixture["fixture_id"],
        title=fixture["title"],
        design_family=fixture["design_family"],
        artifact_dir=str(artifact_dir),
        total_score=total_score,
        passed=passed,
        critical_failures=critical_failures,
        dimension_scores=dimension_scores,
    )


def load_fixtures(fixture_dir: Path) -> list[dict[str, Any]]:
    return [
        load_fixture(path)
        for path in sorted(fixture_dir.glob("*.json"))
    ]


def summarize_results(results: list[FixtureScore], elapsed_seconds: float) -> dict[str, Any]:
    fixtures_total = len(results)
    fixtures_passed = sum(1 for result in results if result.passed)
    average_score = (
        round(sum(result.total_score for result in results) / fixtures_total, 2)
        if fixtures_total
        else 0.0
    )
    return {
        "fixtures_total": fixtures_total,
        "fixtures_passed": fixtures_passed,
        "fixtures_failed": fixtures_total - fixtures_passed,
        "average_score": average_score,
        "pass_threshold": PASS_THRESHOLD,
        "elapsed_seconds": round(elapsed_seconds, 4),
        "passed": fixtures_total > 0 and fixtures_passed == fixtures_total,
    }


def build_markdown_report(suite_result: dict[str, Any]) -> str:
    summary = suite_result["summary"]
    lines = [
        "# Reference Adaptation Eval Report",
        "",
        "## Summary",
        "",
        f"- Fixtures: {summary['fixtures_passed']}/{summary['fixtures_total']} passed",
        f"- Average score: {summary['average_score']}",
        f"- Pass threshold: {summary['pass_threshold']}",
        f"- Runtime: {summary['elapsed_seconds']} seconds",
        f"- Overall: {'PASS' if summary['passed'] else 'FAIL'}",
        "",
        "## Fixture Results",
        "",
    ]

    for result in suite_result["fixtures"]:
        lines.extend(
            [
                f"### {result['fixture_id']} - {'PASS' if result['passed'] else 'FAIL'}",
                "",
                f"- Title: {result['title']}",
                f"- Design family: {result['design_family']}",
                f"- Score: {result['total_score']}/{sum(DIMENSION_WEIGHTS.values())}",
                f"- Artifact directory: `{result['artifact_dir']}`",
                "",
                "| Dimension | Score | Coverage |",
                "|---|---:|---:|",
            ]
        )
        for name, score in result["dimension_scores"].items():
            lines.append(
                f"| {name} | {score['score']}/{score['max_score']} | "
                f"{score['covered']}/{score['total']} |"
            )

        if result["critical_failures"]:
            lines.extend(["", "Critical failures:"])
            lines.extend(f"- {failure}" for failure in result["critical_failures"])

        missing_items = [
            (dimension, missing)
            for dimension, score in result["dimension_scores"].items()
            for missing in score["missing"]
        ]
        if missing_items:
            lines.extend(["", "Missing scored items:"])
            lines.extend(
                f"- {dimension}: {missing}"
                for dimension, missing in missing_items
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_reports(output_dir: Path, suite_result: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "scores.json").write_text(
        json.dumps(suite_result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (output_dir / "report.md").write_text(
        build_markdown_report(suite_result),
        encoding="utf-8",
    )


def run_suite(
    fixture_dir: Path,
    generated_root: Path,
    output_dir: Path,
) -> dict[str, Any]:
    started = time.perf_counter()
    fixtures = load_fixtures(fixture_dir)
    results = [
        score_fixture(fixture, generated_root / fixture["fixture_id"])
        for fixture in fixtures
    ]
    elapsed_seconds = time.perf_counter() - started
    suite_result = {
        "summary": summarize_results(results, elapsed_seconds),
        "fixtures": [result.to_dict() for result in results],
    }
    write_reports(output_dir, suite_result)
    return suite_result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Score generated Research Architect reference-adaptation artifacts.",
    )
    parser.add_argument(
        "--fixture-dir",
        default="evals/reference_adaptation",
        type=Path,
        help="Directory containing reference-adaptation fixture JSON files.",
    )
    parser.add_argument(
        "--generated-root",
        required=True,
        type=Path,
        help="Directory containing one artifact bundle per fixture_id.",
    )
    parser.add_argument(
        "--output-dir",
        default=Path("eval_runs/reference_adaptation/latest"),
        type=Path,
        help="Directory for scores.json and report.md.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    suite_result = run_suite(args.fixture_dir, args.generated_root, args.output_dir)
    summary = suite_result["summary"]
    print(
        "Reference adaptation eval: "
        f"{summary['fixtures_passed']}/{summary['fixtures_total']} passed, "
        f"average score {summary['average_score']}, "
        f"runtime {summary['elapsed_seconds']}s"
    )
    raise SystemExit(0 if summary["passed"] else 1)


if __name__ == "__main__":
    main()
