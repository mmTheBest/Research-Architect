---
name: research-architect-intake
description: Collects the target reference papers, desired paper outcome, project state, materials, constraints, and next deliverable for the Research Architect workflow.
---

# Research Architect Intake

Use this branch before reference analysis, brainstorming, study design, evidence organization, or drafting.

## Goal

Create a minimal project configuration and source inventory. The user may know the paper they want to emulate while remaining unsure about the research steps. Capture the target paper first, then ask only for missing information that changes the adaptation.

## Required questions

1. Which paper or papers represent the kind of work the user wants to produce?
2. Which strengths should be learned from them: question framing, theory use, study design, evidence sequence, analysis strategy, evidence displays, argument structure, or writing organization?
3. What is the user's topic, question, or project direction?
4. What materials already exist: notes, datasets, documents, code, studies, observations, interviews, figures, tables, quotations, draft fragments, or references?
5. What immediate output is needed: adapted research options, research plan, first draft, or revision plan?
6. Which constraints materially affect the design: time, access, participant recruitment, data, archives, equipment, computation, collaborators, ethics, or methods?
7. Should sources be read from local files, specified paths, or web search?

When the user only says “I want to write a paper like this,” infer likely strengths from the paper and record them as provisional. Avoid turning intake into a long questionnaire.

## Target-reference configuration

Record each target paper in `target_references`:

| Field | Meaning |
|---|---|
| `source_id` | Stable source ID |
| `path_or_identifier` | Local path, DOI, URL, or repository location |
| `role` | `primary_exemplar`, `secondary_exemplar`, `method_reference`, or `citation_source` |
| `user_target_reason` | What the user values, when stated |
| `desired_similarity` | Research functions to learn from |
| `verification_status` | Access and verification state |

Use `primary_exemplar` only for papers whose overall research logic should guide the adaptation. A paper may have more than one role, but exemplar use and citation support remain separate checks.

## Outputs

Create:

```text
paper_output/project_config.json
paper_output/source_map.md
paper_output/source_inventory.md
```

Use `templates/project_config.json` as the schema when available.

## Source inventory schema

| Source ID | Type | Path/Location | Description | User-Provided? | Reference Role | Evidence Status | Use In Workflow |
|---|---|---|---|---|---|---|---|

## Routing decision

- When at least one target reference exists, route first to the target-reference pass of `research-architect-literature`.
- When no target reference exists, route to `research-architect-brainstorm`, then identify candidate exemplars during literature mapping.
- When results exist without literature positioning, route to `research-architect-literature` before drafting.
- When evidence is absent, mark the workflow as research planning.

## Rules

- Treat user-provided files as relevant inputs with explicit verification states.
- Separate raw notes, research evidence, literature sources, and target exemplars.
- Record what the user wants to learn from each target paper.
- Preserve the difference between transferable research logic and source-specific content.
- Record human-participant, privacy, access, and data-governance constraints whenever applicable.
