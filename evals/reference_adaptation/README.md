# Reference-Adaptation Fixtures

These fixtures define the minimum behavior expected from the reference-driven workflow across four research designs:

- quantitative associational;
- qualitative interpretive;
- comparative case/process;
- mixed methods.

Each fixture supplies:

1. a summarized target-paper logic;
2. a new user project;
3. expected extraction dimensions;
4. transfer/adapt/replace decisions;
5. required design components;
6. claim boundaries;
7. prohibited inferences.

The fixtures test the product's central promise: explain why a strong reference paper works, adapt its transferable logic to an independent project, and tell the user what to do next.

They are contract fixtures. First validate that the fixture files themselves are well formed:

```bash
python src/scripts/check_reference_adaptation_fixtures.py
```

Then score generated Research Architect artifact bundles with the deterministic eval harness:

```bash
python src/scripts/run_reference_adaptation_eval.py \
  --generated-root eval_runs/reference_adaptation/generated \
  --output-dir eval_runs/reference_adaptation/latest
```

The generated root must contain one directory per `fixture_id`, for example:

```text
eval_runs/reference_adaptation/generated/RA-REF-QUANT-001/
  exemplar_logic_profile.md
  exemplar_adaptation_plan.md
  study_design_brief.md
  claim_register.md
```

The harness writes:

- `scores.json` for machine-readable tracking;
- `report.md` for review.

## Scoring contract

Each fixture is scored on a 100-point deterministic rubric:

| Dimension | Points |
|---|---:|
| Extraction coverage | 20 |
| Adaptation validity | 25 |
| Design-family fit | 15 |
| Actionability | 15 |
| Claim control | 15 |
| Copying-risk control | 10 |

A fixture passes at 85 or higher only when it has no critical failures. Missing required artifacts and literal forbidden inferences are critical failures.

## Target performance

The harness target is 4/4 fixtures scored, 100% repeatable deterministic scores across reruns, complete `scores.json` and `report.md` output, and local scoring under 10 seconds excluding model generation. The first Research Architect output baseline may score below the pass threshold; that is useful signal for prompt or workflow repair.
