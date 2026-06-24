---
name: research-architect-design
description: Converts a confirmed research spine and exemplar adaptation plan into an executable, field-appropriate inquiry, analysis, validation, and user action plan.
---

# Research Architect Study Design

Use this branch after `confirmed_research_spine.md` exists.

## Blocking rule

When the confirmed research spine is missing, return to `research-architect-literature` for user confirmation. When a target paper exists, also require a usable `exemplar_adaptation_plan.md`.

## Inputs

Read:

```text
paper_output/confirmed_research_spine.md
paper_output/sota_gap_map.md
paper_output/source_inventory.md
paper_output/project_config.json
paper_output/exemplar_logic_profile.md       # when target references exist
paper_output/exemplar_adaptation_plan.md     # when target references exist
```

Read `references/design-family-grammars.md` and select the grammar that matches the target paper, question, and available evidence.

## Required outputs

Create:

```text
paper_output/study_design_brief.md
paper_output/analysis_plan.md
paper_output/evaluation_plan.md
paper_output/study_component_registry.md
paper_output/threats_to_validity.md
```

For experiment-centered or computational projects, also create:

```text
paper_output/experiment_registry.md
```

Read an existing `experiment_registry.md` as a compatible specialized view of the study component registry.

## Study design table

| Component | Decision | Rationale | Reference Principle Adapted | Claim Supported | Risk | Mitigation |
|---|---|---|---|---|---|---|
| Research question |  |  |  |  |  |  |
| Theoretical/conceptual orientation |  |  |  |  |  |  |
| Unit, case, population, or corpus |  |  |  |  |  |  |
| Evidence source or research material |  |  |  |  |  |  |
| Sampling or selection logic |  |  |  |  |  |  |
| Data-generation or source-construction procedure |  |  |  |  |  |  |
| Analysis or interpretation approach |  |  |  |  |  |  |
| Comparison, counterfactual, rival explanation, or warrant |  |  |  |  |  |  |
| Evaluation or credibility criterion |  |  |  |  |  |  |
| Sensitivity, triangulation, or scope check |  |  |  |  |  |  |
| Negative case, counterexample, or failure condition |  |  |  |  |  |  |
| Ethics, access, and researcher-position considerations |  |  |  |  |  |  |
| Inference and transfer boundary |  |  |  |  |  |  |

Use only rows that serve the selected design family and claims.

## Study component registry

Use:

| Component ID | Research Function | User Action | Evidence or Material | Analysis or Interpretation | Comparison or Warrant | Output | Claim Supported | Completion Criterion | Status |
|---|---|---|---|---|---|---|---|---|---|

This registry is the user's action plan. Every row should explain what to do, why it is needed, what artifact it produces, and which claim or boundary it serves.

## Design families

Supported families include:

- quantitative descriptive or associational;
- quantitative causal or explanatory;
- qualitative interpretive;
- case study, comparative, historical, archival, or process-tracing;
- mixed methods;
- theoretical, conceptual, critical, or normative;
- systematic, scoping, or integrative review;
- computational, experimental, or design/build/evaluation.

Hybrid studies may combine grammars when the integration point is explicit.

## Adaptive terminology

Translate the target paper's function rather than copying its vocabulary:

- baseline/control -> comparison, counterfactual, contrast, negative case, rival explanation, or counterargument;
- metric -> evaluation, credibility, or warrant criterion;
- robustness -> sensitivity, triangulation, rival-explanation, dependability, or scope check;
- figure -> evidence display, including tables, quotations, matrices, process maps, conceptual models, and joint displays;
- generalization -> statistical generalization, analytical generalization, theoretical transfer, or contextual transferability.

## Rules

- Every study component must support a claim, rule out an alternative, establish credibility, or define scope.
- Every recommended action should point to the reference-paper function it adapts.
- Match validity criteria to the design family.
- Quantitative association does not support causal language without a causal design.
- Qualitative interpretation requires context, selection logic, researcher role, analytic transparency, and negative-case or alternative-interpretation checks.
- Case and historical work requires case/source selection, source criticism, rival explanations, and bounded inference.
- Conceptual and normative work requires explicit premises, argument steps, counterarguments, and applicability boundaries.
- Mixed-method conclusions require a declared integration point.
- Return to literature or brainstorming when no feasible design can support the selected spine.
