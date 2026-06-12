#!/usr/bin/env python3
"""Build Research Architect install output and release artifact from src/."""
from __future__ import annotations

import hashlib
import shutil
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
SRC_SKILLS = SRC / "skills"
DIST_SKILLS = ROOT / "dist" / "codex" / "skills"
RELEASE_DIR = ROOT / "release"
ARTIFACT_NAME = "research-architect-codex-skills.tar.gz"

SHARED_DIRS = ["references", "templates", "scripts"]
ORCHESTRATOR = "research-architect"


def copytree_clean(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def remove_skill_readmes(root: Path) -> None:
    for readme in root.glob("*/README.md"):
        readme.unlink()


def copy_shared_resources() -> None:
    target = DIST_SKILLS / ORCHESTRATOR
    for name in SHARED_DIRS:
        source = SRC / name
        if source.exists():
            copytree_clean(source, target / name)


def build_dist() -> None:
    if not SRC_SKILLS.exists():
        raise SystemExit(f"missing source skills: {SRC_SKILLS}")
    copytree_clean(SRC_SKILLS, DIST_SKILLS)
    remove_skill_readmes(DIST_SKILLS)
    copy_shared_resources()


def build_release() -> Path:
    RELEASE_DIR.mkdir(parents=True, exist_ok=True)
    artifact = RELEASE_DIR / ARTIFACT_NAME
    if artifact.exists():
        artifact.unlink()
    with tarfile.open(artifact, "w:gz") as tar:
        tar.add(DIST_SKILLS, arcname="skills")
    digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
    (RELEASE_DIR / "SHA256SUMS").write_text(f"{digest}  {ARTIFACT_NAME}\n", encoding="utf-8")
    return artifact


def main() -> None:
    build_dist()
    artifact = build_release()
    print(f"Built {artifact.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
