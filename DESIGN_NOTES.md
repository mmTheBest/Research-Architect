# Design Notes

## Primary product method

Research Architect starts from the kind of paper the user wants to produce. A target reference paper becomes a research-design object:

```text
target paper
  -> hidden research logic and strengths
  -> transferable design principles
  -> project-specific adaptation
  -> research spine
  -> study actions
  -> evidence and claims
  -> draft
```

The user may recognize a strong target paper while lacking a clear mental model of how its question, evidence, analysis, and argument fit together. Research Architect makes that structure explicit and turns it into instructions the user can execute.

Similarity means comparable research logic, evidence architecture, and argument function. The user's project retains its own question, context, materials, analysis, results, claims, wording, and contribution.

## Why the research spine remains central

Reference-paper analysis supplies the design logic. The confirmed research spine controls the user's project:

```text
phenomenon or problem
  -> significance
  -> unresolved tension
  -> theoretical or conceptual orientation
  -> research question
  -> logic of inquiry
  -> evidence or warrants
  -> bounded contribution
  -> scope
```

Every downstream artifact should sharpen this spine, test whether it is supportable, or turn it into an executable study and auditable manuscript.

## Why design families are adaptive

The orchestrator remains field-general. Each run infers a design family from the target paper and the user's project, then activates an appropriate research grammar. Quantitative, qualitative, case-based, historical, mixed-methods, conceptual, review, computational, and experimental papers use different standards of evidence and inference.

## Why branch skills

The branch structure lets the workflow stop at the actual bottleneck:

- target known but logic unclear: use literature and exemplar analysis;
- broad direction: use brainstorming;
- no executable inquiry: use design;
- findings without an argument: use evidence and claim calibration;
- draft with weak traceability: use audit;
- complete path needed: use the orchestrator.

## Why `src/` is the source of truth

`src/` owns the canonical skill definitions, references, templates, and scripts. `dist/codex/skills/` is generated install output, and `release/` contains packaged install artifacts.

## Why no rank-label calibration

Research ambition is calibrated by evidence, feasibility, audience, and format constraints. Prestige labels do not determine the research design.
