---
name: research-architect-draft
description: Builds the first complete research-paper draft from the confirmed spine, evidence bank, claim register, citation bank, and writing rationale matrix.
---

# First Paper Draft

Use this branch only after the upstream research-construction artifacts exist.

## Blocking inputs

Do not draft unless these files exist or their equivalents are provided:

```text
paper_output/confirmed_research_spine.md
paper_output/evidence_bank.md
paper_output/claim_register.md
paper_output/citation_support_bank.md
paper_output/section_blueprints.md
paper_output/writing_rationale_matrix.md
```

If evidence is missing, write a research execution plan instead of a draft.

## Required outputs

Create:

```text
paper_output/section_blueprints.md
paper_output/writing_rationale_matrix.md
paper_output/first_draft/main.md
paper_output/final_artifact_manifest.md
```

Optional when useful:

```text
paper_output/first_draft/main.tex
```

## Draft architecture

Choose a structure that fits the research spine and evidence mode. Common functions include:

- title;
- abstract or summary;
- introduction;
- background or related work;
- methods or study design;
- results or analysis;
- discussion;
- limitations;
- conclusion.

Do not force a fixed structure when the project requires a different one.

## Drafting rules

- The abstract must be a compressed version of the research spine.
- The introduction must move from problem to gap to contribution.
- Methods must include enough detail to evaluate the claim.
- Results must follow the evidence chain, not the order in which work happened.
- Discussion must separate interpretation from speculation.
- Limitations must state what the paper does not prove.
- Every central claim must map to evidence IDs or citation IDs.
- Do not cite unverified sources unless explicitly marked as needing verification.

## Writing rationale matrix

Use:

| Row ID | Manuscript Unit | Planned Function | Research-Spine Link | Literature/Exemplar Pattern Learned | Evidence or Citation Anchor | Planned Text Move | Claim Boundary | Final Check |
|---|---|---|---|---|---|---|---|---|

Write this matrix before or while drafting, not after.

## Output behavior

The draft can be rough, but it must be logically complete. Mark uncertain claims with `TODO_VERIFY`, missing results with `TODO_EVIDENCE`, and citation gaps with `TODO_CITATION` rather than hiding them.
