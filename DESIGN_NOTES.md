# Design Notes

This optimized package intentionally shifts from exemplar-centered reference engineering to research-spine-centered paper construction.

## Why this framing

The core user pain is not lack of sentences. The hard part is constructing a research object that can become a paper:

```text
idea -> question -> literature gap -> study design -> evidence -> claim -> draft
```

The suite therefore treats prose as the final stage of a research workflow.

## Why branch skills

The branch structure allows users to stop at the actual bottleneck:

- no idea: use brainstorming;
- too much literature: use literature mapping;
- no executable plan: use design;
- results but no story: use evidence and claim register;
- draft exists but weak: use audit;
- complete path needed: use the orchestrator.

## Why `src/` is the source of truth

`src/` now owns the canonical skill definitions, references, templates, and scripts. `dist/codex/skills/` is generated install output, and `release/` contains packaged install artifacts. The previous top-level `skills/` duplicate was removed to avoid source drift.

## Why no rank-label calibration

A rigorous first paper should be calibrated by the available evidence, audience, format, and constraints, not by a rank label. The package therefore removes the earlier rank-label framing.
