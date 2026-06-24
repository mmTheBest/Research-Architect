#!/usr/bin/env python3
"""Validate reference-adaptation fixture contracts."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

EXPECTED_FILES = {
    "quantitative_associational.json": "quantitative_associational",
    "qualitative_interpretive.json": "qualitative_interpretive",
    "comparative_case.json": "case_comparative_historical_process",
    "mixed_methods.json": "mixed_methods",
}

REQUIRED_TOP_LEVEL = {
    "fixture_id",
    "title",
    "design_family",
    "target_reference",
    "user_project",
    "expected",
}

REQUIRED_TARGET_KEYS = {
    "research_logic",
    "strengths",
    "context_bound_elements",
}

REQUIRED_USER_KEYS = {
    "topic",
    "available_materials",
    "constraints",
}

REQUIRED_EXPECTED_KEYS = {
    "required_extraction_dimensions",
    "required_adaptation_moves",
    "required_design_components",
    "required_claim_boundaries",
    "forbidden_inferences",
}

ALLOWED_DECISIONS = {
    "TRANSFER",
    "ADAPT",
    "REPLACE",
    "OMIT_WITH_RATIONALE",
}


def fail(message: str) -> None:
    raise ValueError(message)


def require_nonempty_list(obj: dict[str, Any], key: str, label: str) -> list[Any]:
    value = obj.get(key)
    if not isinstance(value, list) or not value:
        fail(f"{label}.{key} must be a non-empty list")
    return value


def validate_fixture(path: Path, expected_family: str) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path}: invalid JSON: {exc}")

    missing = REQUIRED_TOP_LEVEL - set(data)
    if missing:
        fail(f"{path}: missing top-level keys: {sorted(missing)}")

    if data["design_family"] != expected_family:
        fail(
            f"{path}: design_family={data['design_family']!r}; "
            f"expected {expected_family!r}"
        )

    for key in ("target_reference", "user_project", "expected"):
        if not isinstance(data[key], dict):
            fail(f"{path}: {key} must be an object")

    missing_target = REQUIRED_TARGET_KEYS - set(data["target_reference"])
    if missing_target:
        fail(f"{path}: target_reference missing {sorted(missing_target)}")

    missing_user = REQUIRED_USER_KEYS - set(data["user_project"])
    if missing_user:
        fail(f"{path}: user_project missing {sorted(missing_user)}")

    missing_expected = REQUIRED_EXPECTED_KEYS - set(data["expected"])
    if missing_expected:
        fail(f"{path}: expected missing {sorted(missing_expected)}")

    require_nonempty_list(data["target_reference"], "research_logic", "target_reference")
    require_nonempty_list(data["target_reference"], "strengths", "target_reference")
    require_nonempty_list(data["target_reference"], "context_bound_elements", "target_reference")
    require_nonempty_list(data["expected"], "required_extraction_dimensions", "expected")
    moves = require_nonempty_list(data["expected"], "required_adaptation_moves", "expected")
    require_nonempty_list(data["expected"], "required_design_components", "expected")
    require_nonempty_list(data["expected"], "required_claim_boundaries", "expected")
    require_nonempty_list(data["expected"], "forbidden_inferences", "expected")

    for index, move in enumerate(moves):
        if not isinstance(move, dict):
            fail(f"{path}: adaptation move {index} must be an object")
        required = {"reference_move", "decision", "required_user_action"}
        missing_move = required - set(move)
        if missing_move:
            fail(f"{path}: adaptation move {index} missing {sorted(missing_move)}")
        if move["decision"] not in ALLOWED_DECISIONS:
            fail(
                f"{path}: adaptation move {index} uses invalid decision "
                f"{move['decision']!r}"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "fixture_dir",
        nargs="?",
        default="evals/reference_adaptation",
        help="Directory containing the four reference-adaptation JSON fixtures.",
    )
    args = parser.parse_args()

    fixture_dir = Path(args.fixture_dir)
    if not fixture_dir.exists():
        raise SystemExit(f"missing fixture directory: {fixture_dir}")

    errors: list[str] = []
    for filename, family in EXPECTED_FILES.items():
        path = fixture_dir / filename
        if not path.exists():
            errors.append(f"missing fixture: {path}")
            continue
        try:
            validate_fixture(path, family)
        except ValueError as exc:
            errors.append(str(exc))

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)

    print(
        "PASS: reference-adaptation fixtures cover quantitative, qualitative, "
        "comparative-case, and mixed-methods designs."
    )


if __name__ == "__main__":
    main()
