---
name: research-architect-brainstorm
description: Converts a raw topic or scattered materials into feasible research-question candidates and candidate research spines.
---

# First Paper Brainstorm

Use this branch after intake and before literature mapping when the user needs to turn a vague direction into a paper-capable idea.

## Inputs

Read:

```text
paper_output/project_config.json
paper_output/source_map.md
paper_output/source_inventory.md
```

## Brainstorming lenses

Generate candidates using these lenses:

1. **Problem lens:** What unresolved problem or bottleneck is visible?
2. **Material lens:** What can the user actually analyze, build, observe, or test?
3. **Method lens:** What method, model, experiment, theory, or framework could be compared, extended, simplified, or evaluated?
4. **Evidence lens:** What claim could be supported with feasible evidence?
5. **Failure lens:** Where might the approach fail, and would that failure clarify scope?
6. **Reader-value lens:** What would a reader learn that is not obvious from prior work?

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

| Candidate ID | Problem | Candidate Research Question | Possible Contribution | Needed Evidence | Available Evidence | Missing Evidence | Feasibility | Novelty Risk | Claim Risk | Next Test |
|---|---|---|---|---|---|---|---|---|---|---|

## Filtering

Classify candidates as:

- `advance`: strong enough for literature mapping;
- `needs_more_material`: promising but missing evidence;
- `defer`: too broad, too risky, or not answerable;
- `reject`: unsupported or already solved.

## Output behavior

Present 2-5 candidate research directions. Do not choose final motivation alone. The final spine must be confirmed after literature mapping.
