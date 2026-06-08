---
name: research-architect-evidence
description: Builds an evidence bank, claim register, and figure plan from available results or executed study outputs.
---

# First Paper Evidence Bank

Use this branch after study design and after the user has results, observations, simulations, analyses, derivations, figures, or draft claims.

## Blocking rule

If no evidence exists yet, do not draft. Create an execution checklist and return to `research-architect-design`.

## Inputs

Read:

```text
paper_output/confirmed_research_spine.md
paper_output/study_design_brief.md
paper_output/analysis_plan.md
paper_output/evaluation_plan.md
paper_output/experiment_registry.md
source files/results supplied by user
```

## Required outputs

Create:

```text
paper_output/evidence_bank.md
paper_output/claim_register.md
paper_output/figure_asset_map.md
paper_output/claim_strength_calibration.md
paper_output/result_interpretation_notes.md
```

## Evidence bank schema

| Evidence ID | Source/File | Result Type | What It Shows | Related Claim | Strength | Limitations | Figure/Table Candidate | Verification Status |
|---|---|---|---|---|---|---|---|---|

## Claim register schema

| Claim ID | Draft Claim | Claim Level | Evidence IDs | Citation IDs | Required Qualification | Forbidden Overclaim | Status |
|---|---|---|---|---|---|---|---|

## Figure asset map schema

| Figure ID | Argument Function | Evidence IDs | Panel Plan | Main Message | Required Caption Claim | Risk | Status |
|---|---|---|---|---|---|---|---|

## Claim strength labels

Use:

- `direct_result`: directly observed or computed;
- `supported_inference`: reasonable interpretation;
- `comparative`: supported by explicit comparison;
- `mechanistic_or_causal`: only if the design justifies it;
- `speculative`: plausible but untested;
- `unsupported`: remove or redesign evidence.

## Rules

- Do not let a claim enter the draft unless it has evidence, citation support, or explicit limitation language.
- Do not use images as evidence unless their source and meaning are clear.
- Captions must state what the figure shows, not what the author hopes it proves.
- Interpretation must not outrun design.
