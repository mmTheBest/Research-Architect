---
name: research-architect
description: End-to-end research brainstorming and first-paper construction workflow from raw idea or materials to research spine, study design, evidence bank, first draft, and audit.
---

# Research Architect Orchestrator

Use this skill when the user wants to build a research paper from scratch, turn scattered research materials into a first draft, or create a rigorous plan before writing.

This is not a prose-polishing skill. It is a research-construction workflow. The goal is to produce a transparent trail from idea to claim to evidence to draft.

## Operating principle

The paper is organized around a confirmed **research spine**:

```text
problem -> motivation -> gap -> approach -> evidence -> bounded claim -> scope
```

The skill must build and verify this spine before drafting.

## Non-negotiable boundaries

- Never fabricate data, results, metrics, p-values, citations, figures, or experimental claims.
- Never copy text, figures, claims, or citation choices from exemplar papers.
- External papers teach structure, evidence expectations, and rhetorical function only.
- User evidence is authoritative for user claims.
- If the evidence is missing, produce a research plan, not a false first draft.
- Do not calibrate ambition by prestige labels. Calibrate only by evidence, feasibility, audience, and format constraints provided by the user.
- Avoid field-specific assumptions unless the user provides the field and asks for them.

## Required configuration

Prefer reading `paper_output/project_config.json`. If missing, route to `research-architect-intake` or ask only the missing fields that materially affect the next step.

Required fields:

| Field | Meaning |
|---|---|
| `workflow` | `brainstorm_from_scratch`, `build_from_materials`, `draft_from_results`, or `revise_existing_draft` |
| `topic_or_raw_idea` | User's current idea or research direction |
| `current_assets` | Notes, data, code, experiments, figures, draft fragments, references |
| `constraints` | Time, access, methods, data, ethics, collaborators, resources |
| `desired_output` | Research plan, first draft, or revision plan |
| `reference_mode` | `local_first`, `specified_paths`, or `web` |
| `reference_paths` | Local paths to notes, PDFs, datasets, or drafts when available |
| `citation_target_count` | Default 30 candidate citation-support sources |
| `confirmed_research_spine` | Empty until user confirmation |

## Route

1. **Intake.** Use `research-architect-intake`. Create `project_config.json`, `source_map.md`, and `source_inventory.md`.
2. **Brainstorm.** Use `research-architect-brainstorm`. Create candidate questions and feasibility filters.
3. **Literature and exemplar mapping.** Use `research-architect-literature`. Build concept, method, baseline, gap, and exemplar maps. Exemplar learning is structural only.
4. **Motivation/spine confirmation.** Present 2-5 candidate research spines. Stop for user confirmation. Write `confirmed_research_spine.md` only after confirmation.
5. **Study design.** Use `research-architect-design`. Convert the confirmed spine into research questions, data/material needs, method, baselines/controls, evaluation criteria, robustness checks, and failure cases.
6. **Evidence bank.** Use `research-architect-evidence` when results or materials exist. If results do not exist, output an execution plan and stop before first-draft writing.
7. **Citation support.** Use `research-architect-citation`. Build a claim-level citation support bank separate from exemplar learning.
8. **Blueprint.** Create `section_blueprints.md` and `writing_rationale_matrix.md`. The matrix is the execution plan for drafting.
9. **First draft.** Use `research-architect-draft`. Draft only from the confirmed spine, evidence bank, claim register, citation bank, and rationale matrix.
10. **Audit.** Use `research-architect-audit`. Do not declare completion until the audit has no blocking failures.

## Standard output directory

Use:

```text
paper_output/
```

Required artifacts for a full run:

```text
project_config.json
source_map.md
source_inventory.md
problem_landscape.md
idea_candidate_matrix.md
research_question_options.md
feasibility_filter.md
reference_materials/source_index.md
concept_dossier.md
corpus_inventory.md
exemplar_method_map.md
sota_gap_map.md
motivation_options_after_literature.md
confirmed_research_spine.md
study_design_brief.md
analysis_plan.md
evaluation_plan.md
experiment_registry.md
threats_to_validity.md
evidence_bank.md
claim_register.md
figure_asset_map.md
claim_strength_calibration.md
citation_support_bank.md
section_blueprints.md
writing_rationale_matrix.md
first_draft/main.md
audit_report.md
revision_queue.md
final_artifact_manifest.md
```

## Writing rationale matrix requirement

Before writing the first draft, create `writing_rationale_matrix.md` with this schema:

| Row ID | Manuscript Unit | Planned Function | Research-Spine Link | Literature/Exemplar Pattern Learned | Evidence or Citation Anchor | Planned Text Move | Claim Boundary | Final Check |
|---|---|---|---|---|---|---|---|---|

The first row must justify the whole-work throughline. Subsequent rows must follow the intended draft in the smallest useful argument-bearing units: section, subsection, paragraph group, result block, figure, table, assumption, baseline, limitation, or discussion move.

If most rows say only “improve clarity” or “write background,” the blueprint is too shallow. Return to brainstorming, literature mapping, or study design.

## Quality gate

Read `references/quality-gates.md`. A draft is blocked if:

- no confirmed research spine exists;
- central claims lack evidence IDs or citation IDs;
- citations are unverified or misused;
- result language exceeds evidence strength;
- method details are insufficient to evaluate the claim;
- limitations are absent;
- exemplar use creates copying risk.
