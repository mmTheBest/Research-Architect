---
name: research-architect-draft
description: Builds a field-appropriate research-paper draft from the confirmed spine, adapted reference logic, evidence bank, claim register, citation bank, evidence displays, and writing rationale matrix.
---

# Research Architect Draft

Use this branch after the upstream research-construction artifacts exist.

## Blocking inputs

Draft only when these files or compatible equivalents are available:

```text
paper_output/confirmed_research_spine.md
paper_output/evidence_bank.md
paper_output/claim_register.md
paper_output/citation_support_bank.md
paper_output/evidence_display_map.md
paper_output/section_blueprints.md
paper_output/writing_rationale_matrix.md
paper_output/exemplar_adaptation_plan.md      # required when target references exist
```

Read `figure_asset_map.md` as the compatible specialized equivalent of `evidence_display_map.md`.

When evidence is incomplete, produce or update the research execution plan.

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

Choose a structure that fits the selected design family, research spine, target-paper functions, and evidence mode. Supported architectures include:

- hypothesis-led quantitative article;
- causal or explanatory evaluation;
- qualitative thematic or interpretive article;
- grounded or process-model article;
- single-case or comparative-case article;
- historical or archival argument;
- mixed-methods article;
- conceptual, critical, normative, or theory-building article;
- policy analysis;
- systematic, scoping, or integrative review;
- computational, experimental, or design/build/evaluation article.

The target paper supplies functional lessons. Its exact headings, section proportions, display sequence, and rhetoric transfer only when they fit the user's independent inquiry.

## Drafting rules

- The title and abstract compress the confirmed research spine and inference boundary.
- The introduction moves through significance, prior knowledge, unresolved tension, research question, and contribution in the form appropriate to the design family.
- Theory appears in the role declared by the spine and exemplar analysis.
- Methods, sources, or argumentative procedures include enough detail to evaluate the warrant.
- Findings follow the claim-support sequence rather than the chronology of the research process.
- Quantitative results report effect size, uncertainty, and design limits when applicable.
- Qualitative findings preserve context, evidence excerpts, alternative interpretations, and the relationship between data and themes.
- Case and historical findings make chronology, source provenance, and rival explanations visible.
- Mixed-method findings identify integration points and meta-inferences.
- Conceptual and normative arguments expose premises, steps, counterarguments, and applicability limits.
- Discussion distinguishes evidence, interpretation, transfer, and speculation.
- Every central claim maps to evidence IDs, citation IDs, or explicit limitation language.
- Citation support and exemplar learning remain separate.
- Unverified sources remain visibly marked.

## Writing rationale matrix

Use:

| Row ID | Manuscript Unit | Planned Function | Research-Spine Link | Reference-Logic Principle Applied | Project-Specific Adaptation | Evidence or Citation Anchor | Planned Text Move | Claim Boundary | Final Check |
|---|---|---|---|---|---|---|---|---|---|

Write the matrix before or during drafting. Each reference-derived move should identify its research function and project-specific adaptation.

## Output behavior

The first draft may remain rough while retaining logical completeness. Mark uncertain claims with `TODO_VERIFY`, missing evidence with `TODO_EVIDENCE`, adaptation decisions with `TODO_ADAPT`, and citation gaps with `TODO_CITATION`.
