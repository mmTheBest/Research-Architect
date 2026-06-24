---
name: research-architect-evidence
description: Builds a cross-method evidence bank, claim register, evidence-display plan, and claim-strength calibration from executed research materials.
---

# Research Architect Evidence and Claim Architecture

Use this branch after study design and after the user has findings, observations, measurements, interviews, documents, cases, coding outputs, simulations, analyses, derivations, arguments, displays, or draft claims.

## Blocking rule

When no evidence or argumentative material exists, create an execution checklist and return to `research-architect-design`. Drafting begins after the evidence path is explicit.

## Inputs

Read:

```text
paper_output/confirmed_research_spine.md
paper_output/study_design_brief.md
paper_output/analysis_plan.md
paper_output/evaluation_plan.md
paper_output/study_component_registry.md
paper_output/experiment_registry.md            # compatible specialized view when present
paper_output/exemplar_adaptation_plan.md       # when target references exist
source files and research materials supplied by the user
```

## Required outputs

Create:

```text
paper_output/evidence_bank.md
paper_output/claim_register.md
paper_output/evidence_display_map.md
paper_output/claim_strength_calibration.md
paper_output/result_interpretation_notes.md
```

For figure-centered projects, `figure_asset_map.md` may be emitted as a specialized view.

## Evidence bank schema

| Evidence ID | Evidence Type | Source/File | Locator | Context/Population/Case | What It Shows | Warrant Type | Related Claim IDs | Strength | Limitations | Contradictory Evidence | Display Candidate | Verification Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Evidence types may include:

- statistical estimate or model output;
- survey measurement;
- administrative or observational data;
- experiment or simulation result;
- interview excerpt;
- field note or observation;
- document or archival source;
- case event or process-tracing observation;
- coding matrix, category, or theme;
- visual or media artifact;
- conceptual premise or definition;
- argument step, counterexample, or counterargument;
- review-synthesis finding;
- mixed-method joint inference.

## Claim register schema

| Claim ID | Draft Claim | Claim Type | Maximum Strength | Scope/Context | Evidence IDs | Citation IDs | Warrant Type | Rival Explanation Addressed | Generalization Mode | Required Qualification | Forbidden Inference | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Supported claim types:

- `descriptive`;
- `associational`;
- `comparative`;
- `causal`;
- `mechanistic_or_process`;
- `interpretive`;
- `theoretical`;
- `conceptual`;
- `normative`;
- `policy_or_practical`;
- `generalization`;
- `transferability`;
- `speculative`;
- `unsupported`.

## Evidence-display map

| Display ID | Display Type | Argument Function | Evidence IDs | Structure or Panel Plan | Main Message | Allowed Claim | Context Needed | Risk | Status |
|---|---|---|---|---|---|---|---|---|---|

Display types include figures, statistical tables, coefficient plots, quotation tables, coding matrices, case-comparison tables, chronologies, process maps, causal diagrams, conceptual frameworks, document-source matrices, and mixed-method joint displays.

## Warrant and inference controls

- Association supports association unless a causal identification strategy is present.
- Qualitative evidence supports contextualized interpretation and theoretical insight through transparent sampling, analysis, reflexivity, and negative-case handling.
- Case evidence supports within-case inference and analytical generalization when selection and rival explanations are explicit.
- Historical and archival evidence requires source provenance and criticism.
- Conceptual and normative claims require explicit premises, argument steps, and counterarguments.
- Mixed-method claims identify which strand supports each part and how the strands integrate.
- Generalization mode is always named.

## Rules

- Every central claim resolves to evidence, citation support, or explicit limitation language.
- Preserve contradictory, null, negative, and disconfirming material.
- Record exact locators for quotations, documents, tables, figures, datasets, and analysis outputs.
- Evidence displays state what the material supports within its context.
- Interpretation remains within the selected design family and confirmed research spine.
