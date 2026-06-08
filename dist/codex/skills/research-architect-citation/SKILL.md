---
name: research-architect-citation
description: Builds a claim-level citation support bank for background, positioning, methods, interpretation, and limitations.
---

# First Paper Citation Support

Use this branch after literature mapping and before first-draft writing.

## Purpose

Build a citation support bank. This is separate from exemplar learning.

- Exemplar learning teaches structure.
- Citation support justifies specific literature statements.

## Inputs

Read:

```text
paper_output/project_config.json
paper_output/concept_dossier.md
paper_output/sota_gap_map.md
paper_output/confirmed_research_spine.md
paper_output/claim_register.md when available
paper_output/reference_materials/source_index.md
```

## Required output

Create:

```text
paper_output/citation_support_bank.md
```

Use:

| Citation ID | Full Reference or Stable Identifier | Year | Source Type | Supports Section | Support Claim Sentence | Why It Fits | Verification Status | Notes |
|---|---|---|---|---|---|---|---|---|

## Candidate count

Default target: 30 high-quality candidate sources. If the project is narrow or the user provides fewer sources, produce fewer and explicitly mark coverage gaps.

## Verification statuses

- `verified`: metadata and claim support checked;
- `partial`: likely relevant but claim support requires checking;
- `needs_user_file`: source inaccessible without user-provided file;
- `reject`: not suitable for citation.

## Rules

- Never invent bibliography entries.
- Never cite a paper for a claim it does not support.
- Prefer sources with clear claim relevance over superficially similar titles.
- Use a coherent subset in the draft; do not dump all candidates.
- Mark uncertainty rather than hiding it.
