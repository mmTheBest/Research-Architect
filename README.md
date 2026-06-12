# Research Architect Skill Suite

[English](#english) | [简体中文](#chinese)

<a id="chinese"></a>

## 简体中文

[English](#english) | 简体中文

**Research Architect** 是一套用于科研选题、研究设计和论文写作的 workflow skill suite。它把论文写作中最容易卡住的部分拆成可执行步骤：从参考文献中提炼选题思路，判断题目难度，明确 research gap，定义创新点，设计实验，组织证据，并把零散材料收束成清晰的论文主线。

论文写作中常见的问题有：选题边界太宽，创新点表达模糊，实验链条缺少逻辑，claim 超出证据强度，缺少科学严谨度。Research Architect 的目标就是清楚地指出这些问题并系统地解决他们。

### Mental model

![Research Architect mental model](assets/research-architect-mental-model.png)

Research Architect 可以端到端运行，也可以按阶段调用。核心思想是保留从原始想法到 research spine、study design、evidence、claim、citation support、draft 和 audit 的透明轨迹。

### Quick start

安装后先运行：

```text
research-architect
```

示例任务：

```text
I have a broad idea: genetic regulation in lung cancer.
Use Research Architect to propose feasible research-question options,
then help me choose one and build the research spine.
```

### 核心思路

Research Architect 的核心方法是：**对标你的参考文献，拆解优秀文献的研究结构，模仿文献背后的科研思路，再围绕你的课题设计实验、组织证据、明确创新点，并形成可写成论文的研究主线。**

这里的“对标参考文献”关注研究结构：一篇好论文如何提出问题，如聚焦题目，如何定义 gap，如何设置实验，如何安排 baseline 和 control，如何把实验结果组织成 figures，如何让每个 claim 获得恰当证据支撑。

### 它解决的核心困境是

- 文献读了很多，选题思路仍然停留在大方向；
- 研究问题看起来重要，具体 gap 仍然模糊；
- 创新点有了，却缺少有力的证据链支撑；
- 实验结果已经存在，却难以转化为一个完整的故事；
- 图表不知道展示哪些数据，缺少清晰的叙事功能；
- claim 写得很强，证据强度还停留在 association 或 observation；
- 参考文献被放进 introduction，却没有真正指导 study design。

### 工作流

```text
原始想法
  -> 参考文献与方法范例映射
  -> 选题思路与 research gap
  -> research spine
  -> study design
  -> 实验与分析计划
  -> evidence bank
  -> claim register
  -> citation support bank
  -> section blueprint
  -> 初稿
  -> 审计与修改队列
```

### 如何从参考文献中学习研究设计

Research Architect 会把参考文献当作“科研设计范例”来拆解，重点分析：

- 文献如何提出 problem；
- 文献如何缩小选题范围；
- 文献如何控制研究难度；
- 文献如何定义 research gap；
- 文献如何提出创新点；
- 文献如何把创新点转化为实验设计；
- 文献如何安排 baseline、control、ablation 和 validation；
- 文献如何组织 figures；
- 文献如何把结果转化为有边界的 claim；
- 文献如何用引用和证据支撑论文叙事。

### 如何帮助形成选题思路

Research Architect 会把选题过程拆成一组可回答的问题：

1. 这个方向对应哪一类研究范式？
2. 参考文献已经建立了哪些共识？
3. 当前领域还留下哪些可切入的 gap？
4. 哪个 gap 更适合当前阶段的数据、技术、时间和资源条件？
5. 当前题目的难度来自数据、方法、验证、理论，还是写作结构？
6. 创新点来自新问题、新数据、新方法、新组合、新验证方式，还是更清晰的 evidence framework？
7. 主要 claim 需要哪些实验、分析和对照来支撑？
8. 哪些结果适合作为 main figures，哪些结果适合作为 supplement？

### 如何帮助设计实验

Research Architect 会把参考文献中的实验设计逻辑转化为适合当前课题的 study design。它会帮助规划核心实验、baseline、control、ablation、robustness check、validation experiment、failure case、threats to validity、evaluation metrics 和 claim-strength boundary。

### 如何帮助定义创新点

Research Architect 会把“创新点”拆成更具体的类型，例如更清晰的问题、新的数据组合、新的分析流程、已有方法的新应用场景、更严格的 benchmark、更可信的 validation、更清楚的 evidence hierarchy，或把分散思路整合成可复用 framework。

### 输出结果

一次完整运行会在 `paper_output/` 下留下完整的研究构建轨迹，包括 research spine、source inventory、literature map、study design、analysis plan、experiment registry、evidence bank、claim register、citation support bank、writing rationale matrix、manuscript draft 和 audit report。

### 安装方式

从仓库根目录运行以下命令。Codex 的实际安装目录是 `${CODEX_HOME:-$HOME/.codex}/skills`。

**Codex:**

```bash
CODEX_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills" && mkdir -p "$CODEX_SKILLS_DIR" && cp -R dist/codex/skills/. "$CODEX_SKILLS_DIR/"
```

**Claude Code:**

```bash
CLAUDE_SKILLS_DIR="${CLAUDE_HOME:-$HOME/.claude}/skills" && mkdir -p "$CLAUDE_SKILLS_DIR" && cp -R dist/codex/skills/. "$CLAUDE_SKILLS_DIR/"
```

也可以使用 release artifact：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}" && tar -xzf release/research-architect-codex-skills.tar.gz -C "${CODEX_HOME:-$HOME/.codex}"
```

安装后调用主 skill：

```text
research-architect
```

也可以在只需要某个阶段时直接调用 branch skills。

### 仓库结构和 source of truth

`src/` 是唯一源头：

- `src/skills/` 保存 skill definitions；
- `src/references/` 保存共享参考资料；
- `src/templates/` 保存输出模板；
- `src/scripts/` 保存验证、索引和 release 构建脚本。

### 使用边界

参考文献的作用是提供研究结构、problem framing、方法逻辑、实验顺序、证据标准和写作组织方式。用户自己的数据、实验结果、分析输出和证据材料始终是论文内容的基础。Research Architect 会根据证据强度控制 claim 的表达，让论文主张与实际材料保持一致。

### License

本项目使用 MIT License。详见 [LICENSE](LICENSE)。

### Changelog

后续版本会继续推进 skill evals、扩展 validation，并调整 skill descriptions，让 Codex 和 Claude 更稳定地路由到正确的 branch skill。详见 [CHANGELOG.md](CHANGELOG.md)。

<a id="english"></a>

## English

English | [简体中文](#chinese)

**Research Architect** is a research workflow skill suite for moving from a raw topic, partial materials, or scattered results to a coherent research-paper draft.

It provides an end-to-end research workflow for building a study from scratch: selecting a research question, conducting a focused literature review, identifying the research gap, designing the study, organizing evidence, controlling claims, planning figures, managing citation support, and drafting an auditable manuscript. The skill turns early-stage research ideas into a structured, reproducible path from brainstorming to a credible first draft.

### Mental model

![Research Architect mental model](assets/research-architect-mental-model.png)

Research Architect can run end-to-end or one branch at a time. The core idea is simple: preserve a transparent trail from raw idea to research spine, study design, evidence, claims, citation support, draft, and audit.

### Quick start

After installation, start with:

```text
research-architect
```

Example task:

```text
I have a broad idea: genetic regulation in lung cancer.
Use Research Architect to propose feasible research-question options,
then help me choose one and build the research spine.
```

### Core idea

Research Architect helps you learn research design from reference papers. It decomposes strong papers into reusable research structure: how they frame a problem, narrow scope, define the gap, set up experiments, choose baselines and controls, organize figures, and keep each claim within its evidence boundary.

The goal is to transfer the research logic behind good papers into your own project without copying their text, figures, data, results, citation choices, or claims.

### Problems it addresses

- You have read many papers but still only have a broad topic.
- The direction sounds important, but the concrete research gap is unclear.
- The contribution can be described, but the evidence chain is weak.
- The topic keeps expanding and the experiment scope becomes hard to control.
- Results exist, but the paper story is loose.
- Figures look like result dumps instead of argument-bearing evidence.
- Claims are stronger than the design supports.
- References appear in the introduction but do not actually guide study design.

### Workflow

```text
Raw idea
  -> Literature and exemplar mapping
  -> Research-question options and research gap
  -> Research spine
  -> Study design
  -> Experiment and analysis plan
  -> Evidence bank
  -> Claim register
  -> Citation support bank
  -> Section blueprint
  -> First draft
  -> Audit and revision queue
```

### How it learns from reference papers

Research Architect treats references as research-design examples. It analyzes:

- how a paper frames the problem;
- how it narrows the topic;
- how it controls difficulty;
- how it defines the research gap;
- how it expresses contribution;
- how contribution becomes study design;
- how baselines, controls, ablations, and validation are arranged;
- how figures are organized;
- how results become bounded claims;
- how citations and evidence support the manuscript narrative.

### How it helps form research-question options

Research Architect pushes a broad topic into concrete research judgment by asking:

1. What research paradigm does this direction belong to?
2. What has prior work already established?
3. Which gaps remain open and answerable?
4. Which gap fits the available data, methods, time, and resources?
5. Does difficulty come from data, method, validation, theory, or writing structure?
6. Does the contribution come from a new question, dataset, method, combination, validation strategy, or evidence framework?
7. What experiments, analyses, and controls are needed for the central claim?
8. Which results belong in main figures and which belong in supplementary material?

### How it helps design studies

Research Architect converts the design logic learned from references into a project-specific study design. It helps plan core experiments, baselines, controls, ablations, robustness checks, validation experiments, failure cases, threats to validity, evaluation metrics, and claim-strength boundaries.

### How it helps define contribution

Research Architect breaks "contribution" into more concrete types, such as a clearer research question, a new data combination, a new analysis workflow, a new application context for an existing method, a stricter benchmark, more credible validation, a clearer evidence hierarchy, or a reusable framework that integrates scattered ideas.

### Outputs

A complete run leaves a transparent trail under `paper_output/`, including research spine, source inventory, literature map, study design, analysis plan, experiment registry, evidence bank, claim register, citation support bank, writing rationale matrix, manuscript draft, and audit report.

### Installation

Run one of these commands from the repository root. The actual Codex install path is `${CODEX_HOME:-$HOME/.codex}/skills`.

**Codex:**

```bash
CODEX_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills" && mkdir -p "$CODEX_SKILLS_DIR" && cp -R dist/codex/skills/. "$CODEX_SKILLS_DIR/"
```

**Claude Code:**

```bash
CLAUDE_SKILLS_DIR="${CLAUDE_HOME:-$HOME/.claude}/skills" && mkdir -p "$CLAUDE_SKILLS_DIR" && cp -R dist/codex/skills/. "$CLAUDE_SKILLS_DIR/"
```

You can also install from the release artifact:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}" && tar -xzf release/research-architect-codex-skills.tar.gz -C "${CODEX_HOME:-$HOME/.codex}"
```

After installation, call the main skill as:

```text
research-architect
```

Branch skills can also be called directly when only one stage is needed.

### Repository layout and source of truth

`src/` is the single source of truth:

- `src/skills/` stores skill definitions;
- `src/references/` stores shared reference material;
- `src/templates/` stores output templates;
- `src/scripts/` stores validation, indexing, and release-building scripts.

### Safety boundary

External papers are used to learn structure, problem framing, method logic, experiment sequencing, evidence standards, and writing organization. User-provided data, results, analyses, and evidence remain authoritative. Research Architect calibrates claim language to the strength of the available evidence.

### License

This project is released under the MIT License. See [LICENSE](LICENSE).

### Changelog

Future versions will add skill evals, expand validation, and tune skill descriptions so Codex and Claude route to the right branch skill more reliably. See [CHANGELOG.md](CHANGELOG.md).
