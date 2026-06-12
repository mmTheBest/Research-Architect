# Installation

## One-line installation

Run one of these commands from the repository root after downloading or cloning this repository.

**Codex:**

```bash
CODEX_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills" && mkdir -p "$CODEX_SKILLS_DIR" && cp -R dist/codex/skills/. "$CODEX_SKILLS_DIR/"
```

**Claude Code:**

```bash
CLAUDE_SKILLS_DIR="${CLAUDE_HOME:-$HOME/.claude}/skills" && mkdir -p "$CLAUDE_SKILLS_DIR" && cp -R dist/codex/skills/. "$CLAUDE_SKILLS_DIR/"
```

## Release artifact installation

The repository includes a packaged release artifact:

```text
release/research-architect-codex-skills.tar.gz
```

Install it into Codex with:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}" && tar -xzf release/research-architect-codex-skills.tar.gz -C "${CODEX_HOME:-$HOME/.codex}"
```

Install it into Claude Code with:

```bash
mkdir -p "${CLAUDE_HOME:-$HOME/.claude}" && tar -xzf release/research-architect-codex-skills.tar.gz -C "${CLAUDE_HOME:-$HOME/.claude}"
```

## Expected layout after installation

```text
skills/research-architect/SKILL.md
skills/research-architect-intake/SKILL.md
skills/research-architect-brainstorm/SKILL.md
skills/research-architect-literature/SKILL.md
skills/research-architect-design/SKILL.md
skills/research-architect-evidence/SKILL.md
skills/research-architect-citation/SKILL.md
skills/research-architect-draft/SKILL.md
skills/research-architect-audit/SKILL.md
```

## Source of truth

`src/` is the canonical source tree. `dist/codex/skills/` and `release/` are generated outputs.

To rebuild generated outputs from `src/`, run:

```bash
python src/scripts/build_release.py
```

## Validation

Run:

```bash
python src/scripts/validate_skill_package.py .
```

A valid package should report all required source skills, generated install skills, supporting files, and release artifacts as present.
