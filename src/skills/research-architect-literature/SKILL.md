---
name: research-architect-literature
description: Builds a structured literature, gap, and exemplar map for first-paper construction without copying exemplar content.
---

# First Paper Literature and Exemplar Mapping

Use this branch after brainstorming and before confirming the research spine.

## Purpose

Turn sources into a research map:

- concepts and definitions;
- methods and baselines;
- evidence standards;
- unresolved gaps;
- structural lessons from exemplars.

This is not a general summary of papers.

## Inputs

Read:

```text
paper_output/project_config.json
paper_output/source_inventory.md
paper_output/idea_candidate_matrix.md
```

## Source roles

Assign each source one or more roles:

| Role | Purpose |
|---|---|
| Concept source | Defines problem, construct, or task |
| Method source | Provides approach or analysis method |
| Baseline/control source | Provides comparison logic |
| Benchmark/data source | Provides dataset, protocol, or measurement norm |
| Theory/mechanism source | Supports interpretation |
| Exemplar source | Teaches structure and evidence sequence only |

## Required outputs

Create:

```text
paper_output/reference_materials/source_index.md
paper_output/concept_dossier.md
paper_output/corpus_inventory.md
paper_output/exemplar_method_map.md
paper_output/sota_gap_map.md
paper_output/motivation_options_after_literature.md
```

## Gap map schema

| Gap ID | Candidate Gap | What Prior Work Already Shows | What Remains Unresolved | Evidence Needed | User Feasibility | Claim Strength | Risk |
|---|---|---|---|---|---|---|---|

## Exemplar map schema

| Exemplar ID | Why Included | Research Spine | Evidence Sequence | Figure/Result Functions | Baseline/Control Logic | Reusable Structural Lesson | Forbidden Copying Risk |
|---|---|---|---|---|---|---|---|

## Motivation options

Generate 2-5 candidate research spines:

| Option | One-Sentence Research Spine | Core Contribution | Required Evidence | Why It Matters | Why It Is Feasible | Main Risk | Scope Boundary |
|---|---|---|---|---|---|---|---|

Stop and ask the user to choose, modify, or reject options. After confirmation, write:

```text
paper_output/confirmed_research_spine.md
```

## Rules

- Do not treat exemplar sources as citation support unless their claim support is separately verified.
- Do not force a gap if prior work already solves it.
- Prefer precise gaps that can be tested over broad gaps that only sound impressive.
- Mark uncertain source claims as `needs_verification`.
