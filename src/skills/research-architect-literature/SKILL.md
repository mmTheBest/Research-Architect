---
name: research-architect-literature
description: Decomposes target papers into transferable research logic, maps that logic onto the user's project, and builds the literature and gap structure needed for an independent study.
---

# Research Architect Literature and Exemplar Analysis

Use this branch in two passes when target references exist, or once after brainstorming when they do not.

## Purpose

Turn target papers and surrounding literature into:

- an explanation of how the target paper works;
- a functional account of its strengths;
- a design-family classification;
- a project-specific adaptation plan;
- a map of concepts, methods, comparisons, evidence standards, debates, and gaps;
- candidate research spines grounded in feasible evidence or warrants.

The output should teach the user what to do and why each step is necessary.

## Pass 1 — Target-reference analysis

Run before ordinary brainstorming when `project_config.json` contains `target_references`.

Read:

```text
paper_output/project_config.json
paper_output/source_inventory.md
target reference files
```

Create:

```text
paper_output/exemplar_logic_profile.md
paper_output/exemplar_adaptation_plan.md
```

At this stage, the adaptation plan may contain provisional user-project analogues and explicit questions that materially affect the design.

## Pass 2 — Literature positioning and final adaptation

Run after candidate questions exist.

Read:

```text
paper_output/project_config.json
paper_output/source_inventory.md
paper_output/idea_candidate_matrix.md
paper_output/research_question_options.md
paper_output/exemplar_logic_profile.md        # when target references exist
paper_output/exemplar_adaptation_plan.md      # preliminary version when available
```

## Source roles

Assign each source one or more roles:

| Role | Purpose |
|---|---|
| Primary exemplar | Supplies the overall research logic the user wants to learn from |
| Secondary exemplar | Supplies a particular design, analysis, display, or rhetorical strength |
| Concept source | Defines the phenomenon, construct, or task |
| Theory source | Defines or motivates a theoretical or conceptual orientation |
| Method source | Provides data-generation, analysis, or interpretive procedures |
| Comparison/warrant source | Provides baseline, counterfactual, negative-case, rival-explanation, or argumentative logic |
| Benchmark/data source | Provides a dataset, corpus, protocol, instrument, archive, or measurement norm |
| Citation source | Supports a specific literature claim after separate verification |

## Required outputs

Create:

```text
paper_output/reference_materials/source_index.md
paper_output/concept_dossier.md
paper_output/corpus_inventory.md
paper_output/exemplar_method_map.md
paper_output/exemplar_logic_profile.md        # when target references exist
paper_output/exemplar_adaptation_plan.md      # when target references exist
paper_output/sota_gap_map.md
paper_output/motivation_options_after_literature.md
```

## Exemplar logic profile

Use `templates/exemplar_logic_profile.md`. Analyze:

- research object and starting tension;
- theory or conceptual role;
- research-question move;
- contribution type;
- unit, participant, case, site, document, corpus, or sample-selection logic;
- evidence generation;
- analysis or interpretation logic;
- comparison, counterfactual, rival explanation, negative case, or counterargument;
- validity and credibility logic;
- result and evidence-display sequence;
- rhetorical sequence;
- limitation and inference-boundary strategy;
- context-dependent assumptions;
- transferable strengths;
- copying boundaries.

Explain why each load-bearing move works.

## Adaptation plan

Use `templates/exemplar_adaptation_plan.md`.

| Transfer ID | Reference Move | Why It Works | Transferable Principle | User-Project Analogue | Required Evidence or Material | Decision | Context Difference | Feasibility | Copying Boundary | Next Action |
|---|---|---|---|---|---|---|---|---|---|---|

Allowed decisions:

- `TRANSFER`: the principle fits with only project-specific implementation;
- `ADAPT`: the function transfers and the design changes materially;
- `REPLACE`: the reference move is incompatible and another move serves the same function;
- `OMIT_WITH_RATIONALE`: the function is unnecessary for the user's bounded claim.

Every load-bearing reference move receives a decision. Topic substitution without design reasoning fails the adaptation.

## Gap map schema

| Gap ID | Candidate Gap or Tension | What Prior Work Establishes | What Remains Unresolved | Required Evidence or Warrant | User Feasibility | Possible Claim | Design Family | Risk |
|---|---|---|---|---|---|---|---|---|

## Exemplar method map schema

| Exemplar ID | Why Included | Research Spine | Logic of Inquiry | Evidence Sequence | Evidence-Display Functions | Comparison or Warrant Logic | Reusable Structural Lesson | Context Boundary | Copying Risk |
|---|---|---|---|---|---|---|---|---|---|

## Motivation options

Generate 2-5 candidate research spines:

| Option | One-Sentence Research Spine | Reference Logic Preserved | Required Adaptation | User-Specific Contribution | Required Evidence or Warrant | Why It Matters | Why It Is Feasible | Main Risk | Scope Boundary |
|---|---|---|---|---|---|---|---|---|---|

Stop for the user to choose, modify, or reject the options. After confirmation, write:

```text
paper_output/confirmed_research_spine.md
```

## Rules

- Keep exemplar learning separate from citation support.
- Preserve source-specific claims, wording, data, findings, figures, quotation choices, and citation choices as source-specific.
- Infer the design family from the target paper and project; record uncertainty when hybrid or ambiguous.
- Verify that prior work leaves the proposed gap or tension unresolved.
- Prefer an adaptation the user can execute over a superficial imitation of a resource-intensive design.
- Mark uncertain source claims as `needs_verification`.
- Record contradictory sources and rival interpretations.
