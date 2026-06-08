# Research Architect Skill Suite

**Research Architect** is a research workflow skill suite for moving from a raw topic, partial materials, or scattered results to a coherent research-paper draft.

It provides an end-to-end research workflow for building a study from scratch: selecting a research question, conducting a focused literature review, identifying the research gap, designing the study, organizing evidence, controlling claims, planning figures, managing citation support, and drafting an auditable manuscript. The skill turns early-stage research ideas into a structured, reproducible path from brainstorming to a credible first draft.

## Installable skill folders

The main installable folders are under:

```text
dist/codex/skills/
```

For a flat skill installation, copy the contents of `dist/codex/skills/` into your local skill directory.

The primary entrypoint is:

```text
research-architect
```

Branch skills can also be called directly when only one stage is needed.

## Core workflow

```text
Intake
  -> Brainstorm
  -> Literature and exemplar mapping
  -> Confirm research spine
  -> Study design
  -> Evidence and claim bank
  -> Citation support bank
  -> Section blueprint and writing rationale matrix
  -> First draft
  -> Audit and revision queue
```

## Output philosophy

A successful run does not only produce a draft. It leaves a transparent research trail under `paper_output/`, including the research spine, source inventory, literature map, study design, evidence bank, claim register, writing rationale matrix, draft, and audit report.

## Safety boundary

External papers are used to learn structure, problem framing, rhetoric, and evidence expectations. They are not templates for copying text, figures, data, results, citations, or claims. User-provided evidence remains authoritative for the user’s paper.
