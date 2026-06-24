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

They are contract fixtures rather than scored model outputs. Run:

```bash
python src/scripts/check_reference_adaptation_fixtures.py
```

A future evaluation harness should execute the skills on these inputs and score extraction accuracy, adaptation validity, actionability, design-family fit, claim control, and copying risk.
