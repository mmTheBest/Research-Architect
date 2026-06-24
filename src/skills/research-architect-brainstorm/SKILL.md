---
name: research-architect-brainstorm
description: Converts a target paper's transferable logic, a raw topic, and available materials into distinct feasible research-question and adaptation options.
---

# Research Architect Brainstorm

Use this branch after intake. When target references exist, run the target-reference pass of `research-architect-literature` first so brainstorming can adapt known research logic rather than guess from the topic alone.

## Inputs

Read:

```text
paper_output/project_config.json
paper_output/source_map.md
paper_output/source_inventory.md
paper_output/exemplar_logic_profile.md        # when target references exist
paper_output/exemplar_adaptation_plan.md      # preliminary version when available
```

## Brainstorming lenses

Generate candidates using these lenses:

1. **Reference-logic lens:** Which question-forming, theory, design, evidence, analysis, and argument principles make the target paper work?
2. **Adaptation lens:** What is the user's project analogue, and which context-dependent assumptions require replacement?
3. **Problem lens:** What unresolved tension, contradiction, practical concern, or conceptual limitation is visible?
4. **Material lens:** What can the user measure, observe, interpret, compare, trace, derive, review, or test?
5. **Method and inquiry lens:** Which design family and logic of inquiry can generate a defensible answer?
6. **Warrant lens:** What empirical, interpretive, comparative, theoretical, or argumentative warrant can support the claim?
7. **Disconfirmation lens:** Which negative case, rival explanation, counterexample, sensitivity test, or boundary condition would clarify scope?
8. **Reader-value lens:** What would a skeptical reader learn that existing work does not already establish?

## Required outputs

Create:

```text
paper_output/problem_landscape.md
paper_output/idea_candidate_matrix.md
paper_output/research_question_options.md
paper_output/feasibility_filter.md
```

## Candidate matrix

Use:

| Candidate ID | Problem or Tension | Candidate Research Question | Reference Logic Inherited | Required Adaptation | User-Specific Contribution | Needed Evidence or Warrant | Available Material | Missing Material | Feasibility | Mismatch Risk | Claim Risk | Next Action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Option requirements

Each target-driven option must state:

- which strength of the reference paper it preserves;
- which source-specific assumption it replaces;
- how the user's context creates an independent contribution;
- what evidence or argumentative warrant is required;
- which design family is provisionally selected;
- what action the user should take first;
- what claim remains supportable if the full target design is infeasible.

Options should differ in research logic, evidence path, or contribution. Topic paraphrases do not count as distinct options.

## Filtering

Classify candidates as:

- `advance`: coherent, answerable, and feasible enough for literature positioning;
- `needs_more_material`: promising with a clearly identified missing input;
- `defer`: useful after a simpler or narrower study is completed;
- `reject`: already answered, unsupported, structurally mismatched, or lacking a defensible inquiry path.

Conceptual, critical, interpretive, and normative projects can advance when they have explicit premises, source-selection logic, argumentative warrants, counterarguments, and scope.

## Output behavior

Present 2-5 candidate directions and explain the reference-derived logic behind each. The final research spine remains a user decision after literature positioning.
