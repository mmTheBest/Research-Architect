---
name: research-architect-audit
description: Audits reference-logic extraction, project adaptation, design-family fit, evidence traceability, citation integrity, inference boundaries, copying risk, and draft completeness.
---

# Research Architect Audit

Use this branch before declaring the first draft complete.

## Inputs

Read all available artifacts under:

```text
paper_output/
```

Especially:

```text
project_config.json
exemplar_logic_profile.md
exemplar_adaptation_plan.md
confirmed_research_spine.md
study_design_brief.md
study_component_registry.md
evidence_bank.md
claim_register.md
evidence_display_map.md
citation_support_bank.md
section_blueprints.md
writing_rationale_matrix.md
first_draft/main.md
```

Use compatible legacy artifacts when the canonical file is absent.

## Required outputs

Create:

```text
paper_output/audit_report.md
paper_output/revision_queue.md
```

## Audit gates

| Gate | Blocking Failure Examples |
|---|---|
| Target-reference logic | target paper summarized without extracting load-bearing research moves or strengths |
| Adaptation validity | topic nouns changed while design assumptions, context, or evidence needs remain unexamined |
| Research spine clarity | no bounded phenomenon/tension/question/contribution/scope |
| Feasibility | claim depends on evidence, access, participants, sources, or warrants that are unavailable and unplanned |
| Literature grounding | sources are listed without mapping concepts, theories, debates, methods, evidence standards, or gaps |
| Design-family fit | validity criteria or manuscript logic come from an incompatible research tradition |
| Study-design validity | selection, evidence generation, analysis, comparison/warrant, credibility, or inference boundary is missing |
| Evidence traceability | central claims lack evidence IDs, citation IDs, locators, or explicit limitation language |
| Evidence-display logic | display has no argument function, hides context, or states a stronger claim than the evidence permits |
| Citation integrity | citation is invented, unverifiable, irrelevant, or used beyond its support |
| Non-copying | wording, source-specific claims, data, display content, or rhetorical sequence is too close to the exemplar |
| Draft completeness | the design family requires methods, positionality, source criticism, integration, counterargument, limitations, or findings that are absent |
| Inference-boundary control | causal, prevalence, transfer, theoretical, normative, mechanistic, or policy claims exceed the available warrant |

## Audit report schema

| Gate | Status | Evidence Checked | Problem Found | Required Fix | Upstream Owner | Severity |
|---|---|---|---|---|---|---|

Severity values:

- `BLOCKED`: required before the draft can be used;
- `MAJOR`: weakens the central research logic or claim;
- `MINOR`: improves clarity, transparency, or presentation;
- `PASS`: no issue found.

## Revision queue schema

| Priority | Fix | Affected Section | Required Upstream Artifact | Owner/Next Action | Verification Criterion |
|---|---|---|---|---|---|

## Rules

- Route structural failures to the artifact that owns the decision.
- Weak target-paper analysis returns to `research-architect-literature`.
- Superficial or infeasible adaptation returns to `research-architect-literature` or `research-architect-brainstorm`.
- Weak design-family logic returns to `research-architect-design`.
- Weak evidence or claims return to `research-architect-evidence`.
- Weak citation support returns to `research-architect-citation`.
- Prose revision follows upstream correction.
