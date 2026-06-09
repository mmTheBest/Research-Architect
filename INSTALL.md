# Installation

## One-line installation

Run one of these commands from the package root after downloading or cloning this repository.

**Codex:**

```bash
mkdir -p "$HOME/.codex/skills" && cp -R dist/codex/skills/* "$HOME/.codex/skills/"
```

**Claude Code:**

```bash
mkdir -p "$HOME/.claude/skills" && cp -R dist/codex/skills/* "$HOME/.claude/skills/"
```

## Flat skill installation

The one-line commands above copy every folder under:

```text
dist/codex/skills/
```

to your local skill folder.

Expected layout after copying:

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

## Self-contained references

Shared references and templates are included under:

```text
src/references/
src/templates/
src/scripts/
```

If your skill host expects each skill to be fully self-contained, copy `src/references`, `src/templates`, and `src/scripts` into the relevant skill folder.

## Validation

Run:

```bash
python src/scripts/validate_skill_package.py .
```

A valid package should report all required skill folders and supporting files as present.
