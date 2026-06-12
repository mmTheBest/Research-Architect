#!/usr/bin/env python3
"""Create a simple source_index.md from a folder tree."""
from __future__ import annotations

import argparse
from pathlib import Path

EXT_ROLES = {
    ".pdf": "reference_or_report",
    ".bib": "bibliography",
    ".ris": "bibliography",
    ".md": "notes_or_draft",
    ".txt": "notes_or_data",
    ".csv": "data_or_table",
    ".tsv": "data_or_table",
    ".xlsx": "data_or_table",
    ".png": "figure_or_image",
    ".jpg": "figure_or_image",
    ".jpeg": "figure_or_image",
    ".tex": "draft_or_source",
    ".docx": "draft_or_document",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", nargs="?", default=".")
    parser.add_argument("--output", default="paper_output/reference_materials/source_index.md")
    args = parser.parse_args()

    root = Path(args.input_dir)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    files = [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]
    lines = [
        "# Source Index",
        "",
        "| Source ID | Type | Path | Why Included | Used For | Verification Status |",
        "|---|---|---|---|---|---|",
    ]
    for i, path in enumerate(files, 1):
        role = EXT_ROLES.get(path.suffix.lower(), "unknown")
        rel = path.relative_to(root) if path.is_relative_to(root) else path
        lines.append(f"| S{i:03d} | {role} | `{rel}` | to review | TBD | unverified |")

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out} with {len(files)} sources")


if __name__ == "__main__":
    main()
