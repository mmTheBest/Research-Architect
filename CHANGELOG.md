# Changelog

The current repository state is treated as the initial version.

## v0.3.1 - 2026-07-01

- Added a deterministic reference-adaptation eval harness that scores generated artifact bundles against the four existing fixtures.
- Added unit coverage for fixture scoring, critical failures, report generation, and package-validator inclusion.
- Documented the eval scoring contract, pass threshold, and expected first-baseline behavior.
- Rebuilt the Codex skill package and release artifact with the new eval tooling.

## v0.3.0 - 2026-06-24

- Made target reference papers first-class workflow inputs.
- Added exemplar logic profiling and exemplar-to-project adaptation planning.
- Added design-family routing for quantitative, qualitative, case-based, historical, mixed-methods, conceptual, review, computational, and experimental research.
- Generalized study, evidence, claim, display, drafting, and audit contracts across research traditions.
- Added four reference-adaptation fixtures and a fixture validator.
- Preserved compatibility with `experiment_registry.md` and `figure_asset_map.md` while introducing field-general artifact names.

## Planned future versions

- Add executable skill evals for realistic reference-adaptation and manuscript-construction tasks.
- Expand validation to cover source-of-truth drift, generated artifact consistency, and claim-to-source alignment.
- Tune skill descriptions so Codex and Claude route to the right branch skill with fewer false triggers.

## v0.3.1 - 2026-07-01（中文）

- 增加 deterministic reference-adaptation eval harness，可根据四个现有 fixture 对生成的 artifact bundle 评分。
- 增加 fixture scoring、critical failures、report generation 和 package-validator inclusion 的单元测试覆盖。
- 文档化 eval scoring contract、pass threshold 和首次 baseline 的预期行为。
- 使用新的 eval 工具重新构建 Codex skill package 和 release artifact。

## v0.3.0 - 2026-06-24（中文）

- 将目标参考文献设为 workflow 的一等输入。
- 增加参考文献研究逻辑拆解和参考文献到用户课题的适配计划。
- 增加适用于定量、定性、案例、历史、混合方法、概念、综述、计算和实验研究的 design-family routing。
- 将 study、evidence、claim、display、draft 和 audit contract 扩展到不同研究范式。
- 增加四个参考文献适配 fixture 和对应 validator。
- 在引入通用 artifact 名称的同时保留对 `experiment_registry.md` 和 `figure_asset_map.md` 的兼容。

## 后续计划

- 增加面向真实参考文献适配和论文构建任务的可执行 skill evals。
- 扩展 validation，覆盖 source-of-truth drift、生成产物一致性和 claim-to-source alignment。
- 调整 skill descriptions，让 Codex 和 Claude 更稳定地路由到正确的 branch skill。
