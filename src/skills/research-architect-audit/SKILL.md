---
name: research-architect-audit
description: Audits the first-paper workflow artifacts and draft for spine clarity, evidence traceability, citation integrity, copying risk, and overclaiming.
---

# First Paper Audit

Use this branch before declaring the first draft complete.

## Inputs

Read all available artifacts under:

```text
paper_output/
```

Especially:

```text
confirmed_research_spine.md
evidence_bank.md
claim_register.md
citation_support_bank.md
section_blueprints.md
writing_rationale_matrix.md
first_draft/main.md
```

## Required outputs

Create:

```text
paper_output/audit_report.md
paper_output/revision_queue.md
```

## Audit gates

| Gate | Blocking Failure Examples |
|---|---|
| Research spine clarity | no bounded problem/gap/claim/scope |
| Feasibility | claim depends on evidence not available or planned |
| Literature grounding | sources summarized but not mapped to gap/method/baseline |
| Study design validity | no comparison/control/evaluation criteria when needed |
| Evidence traceability | claims lack evidence IDs or citation IDs |
| Figure logic | figure has no argument function or caption overclaims |
| Citation integrity | invented, unverifiable, or misused citations |
| Non-copying | text/figure/claim too close to exemplar source |
| Draft completeness | missing methods, limitations, or results needed for claim |
| Overclaim control | causal/general/mechanistic claims exceed design |

## Audit report schema

| Gate | Status | Evidence Checked | Problem Found | Required Fix | Severity |
|---|---|---|---|---|---|

Severity values:

- `BLOCKED`: must fix before using the draft;
- `MAJOR`: weakens central argument;
- `MINOR`: improves clarity or polish;
- `PASS`: no issue found.

## Revision queue schema

| Priority | Fix | Affected Section | Required Upstream Artifact | Owner/Next Action |
|---|---|---|---|---|

## Rules

- Do not silently fix major logic failures only in prose. Route back to the upstream artifact that owns the failure.
- If the claim register is weak, return to `research-architect-evidence`.
- If citations are weak, return to `research-architect-citation`.
- If the motivation is weak or unsupported, return to `research-architect-literature` or `research-architect-brainstorm`.
- If the study cannot support the claim, return to `research-architect-design`.
