---
name: research-architect-intake
description: Collects project state, materials, constraints, and desired output for the Research Architect workflow.
---

# First Paper Intake

Use this branch before any brainstorming, literature mapping, design, or drafting.

## Goal

Create a minimal but complete project configuration and source inventory. Do not overwhelm the user with a long questionnaire. Ask only for missing information that changes the workflow.

## Required questions

1. What is the raw topic, question, or project direction?
2. What materials already exist: notes, data, code, experiments, figures, draft fragments, references?
3. What is the desired immediate output: brainstormed ideas, research plan, first draft, or revision plan?
4. What are the constraints: time, data access, equipment, computation, collaborators, ethics, methods that must or cannot be used?
5. Should references be read from local files, specified paths, or web search?

## Outputs

Create:

```text
paper_output/project_config.json
paper_output/source_map.md
paper_output/source_inventory.md
```

Use `templates/project_config.json` as the schema when available.

## Source inventory schema

| Source ID | Type | Path/Location | Description | User-Provided? | Evidence Status | Use In Workflow |
|---|---|---|---|---|---|---|

## Rules

- Treat all user-provided files as potentially relevant but not automatically reliable evidence.
- Separate raw notes from verified results.
- Separate literature sources from user evidence.
- If the user has no results yet, mark the workflow as research planning, not first-draft generation.
- If the user has results but no literature map, route to `research-architect-literature` before drafting.
