---
name: research-architect-design
description: Converts a confirmed research spine into an executable study, experiment, analysis, or validation plan.
---

# First Paper Study Design

Use this branch after `confirmed_research_spine.md` exists.

## Blocking rule

If the confirmed research spine is missing, return to `research-architect-literature` and obtain user confirmation before designing the study.

## Inputs

Read:

```text
paper_output/confirmed_research_spine.md
paper_output/sota_gap_map.md
paper_output/source_inventory.md
paper_output/project_config.json
```

## Required outputs

Create:

```text
paper_output/study_design_brief.md
paper_output/analysis_plan.md
paper_output/evaluation_plan.md
paper_output/experiment_registry.md
paper_output/threats_to_validity.md
```

## Study design table

| Component | Decision | Rationale | Claim Supported | Risk | Mitigation |
|---|---|---|---|---|---|
| Research question |  |  |  |  |  |
| Unit of analysis |  |  |  |  |  |
| Data/material |  |  |  |  |  |
| Method/approach |  |  |  |  |  |
| Baseline/control |  |  |  |  |  |
| Evaluation criterion |  |  |  |  |  |
| Robustness check |  |  |  |  |  |
| Failure/negative case |  |  |  |  |  |
| Interpretation boundary |  |  |  |  |  |

## Evidence modes

Choose the design logic that matches the project:

- computational;
- experimental;
- theoretical;
- qualitative;
- design/build/evaluation;
- mixed-methods.

Do not force all projects into the same template.

## Rules

- Every experiment, simulation, analysis, proof, or evaluation must support a specific claim or scope boundary.
- Every central claim needs at least one direct evidence path.
- Include baselines, controls, or comparison logic when the claim is comparative.
- Include robustness checks when the claim generalizes beyond one condition.
- Include failure cases when they clarify scope.
- If no feasible design can support the selected spine, return to literature/brainstorming and revise the spine.
