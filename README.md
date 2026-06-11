# Research Architect Skill Suite

[English](README.en.md) | 简体中文

**Research Architect** 是一套用于科研选题、研究设计和论文写作的 workflow skill suite。它把论文写作中最容易卡住的部分拆成可执行步骤：从参考文献中提炼选题思路，判断题目难度，明确 research gap，定义创新点，设计实验，组织证据，并把零散材料收束成清晰的论文主线。

论文写作中常见的问题有：选题边界太宽，创新点表达模糊，实验链条松散，claim 超出证据强度，参考文献只被用作 citation，而未真正转化为研究设计的参照系。Research Architect 的目标是把这些隐性问题显性化，并把每一步转化为可检查、可修改、可审计的研究产物。

## Mental model

![Research Architect mental model](assets/research-architect-mental-model.png)

Research Architect 可以端到端运行，也可以按阶段调用。核心思想是保留从原始想法到 research spine、study design、evidence、claim、citation support、draft 和 audit 的透明轨迹。

## 核心思路

Research Architect 的核心方法是：**对标你的参考文献，拆解优秀文献的研究结构，模仿文献背后的科研思路，再围绕你的课题设计实验、组织证据、明确创新点，并形成可写成论文的研究主线。**

这里的“对标参考文献”关注研究结构：一篇好论文如何提出问题，如何缩小题目，如何定义 gap，如何设置实验，如何安排 baseline 和 control，如何把实验结果组织成 figures，如何让每个 claim 获得恰当证据支撑。

## 它解决的核心痛点

写论文时常见的卡点通常包括：

- 文献读了很多，选题思路仍然停留在大方向；
- 研究问题看起来重要，具体 gap 仍然模糊；
- 创新点可以被描述出来，证据链还没有跟上；
- 题目难度持续扩张，实验范围越来越难收束；
- 实验结果已经存在，论文主线仍然松散；
- figures 像结果堆叠，缺少清晰的叙事功能；
- claim 写得很强，证据强度还停留在 association 或 observation；
- 参考文献被放进 introduction，却没有真正指导 study design。

Research Architect 会把这些问题拆成具体任务，并生成中间文件，让研究者看到一个想法如何一步步变成 research question、hypothesis、study design、analysis plan、evidence bank、claim register 和 manuscript draft。

## 工作流

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

这条链路会保留从原始想法到论文初稿的完整研究轨迹。每个阶段都会生成可复核的中间产物，帮助用户检查研究逻辑、实验设计、证据边界和写作结构。

## 如何从参考文献中学习研究设计

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

用户可以借助这种拆解，把优秀论文中的研究逻辑迁移到自己的课题中：学习它们如何设计问题、组织方法、安排实验、控制 claim，并建立适合自己材料和证据强度的论文结构。

## 如何帮助形成选题思路

Research Architect 会把选题过程拆成一组可回答的问题：

1. 这个方向对应哪一类研究范式？
2. 参考文献已经建立了哪些共识？
3. 当前领域还留下哪些可切入的 gap？
4. 哪个 gap 更适合当前阶段的数据、技术、时间和资源条件？
5. 当前题目的难度来自数据、方法、验证、理论，还是写作结构？
6. 创新点来自新问题、新数据、新方法、新组合、新验证方式，还是更清晰的 evidence framework？
7. 主要 claim 需要哪些实验、分析和对照来支撑？
8. 哪些结果适合作为 main figures，哪些结果适合作为 supplement？

这些问题会把“我想做一个方向”推进成更具体的研究判断：我要回答什么问题，为什么值得做，难度在哪里，创新点在哪里，需要哪些实验来支撑。

## 如何帮助设计实验

Research Architect 会把参考文献中的实验设计逻辑转化为适合当前课题的 study design。它会帮助规划：

- 核心实验；
- baseline；
- control；
- ablation；
- robustness check；
- validation experiment；
- failure case；
- threats to validity；
- evaluation metrics；
- claim-strength boundary。

实验设计会直接服务于论文主线。每个实验对应一个明确问题，每个结果支撑一个具体 claim，每个 claim 对应一个证据强度等级。

## 如何帮助定义创新点

Research Architect 会把“创新点”拆成更具体的类型。常见创新点包括：

- 提出一个更清晰的问题；
- 使用一个新的数据组合；
- 建立一个新的分析流程；
- 改进一个已有方法的应用场景；
- 引入更严格的 benchmark；
- 增加更可信的 validation；
- 提供更清楚的 evidence hierarchy；
- 把已有领域中分散的思路整合成一个可复用 framework。

系统会进一步检查这个创新点需要哪些实验、对照、引用和结果来支撑，帮助创新点从一句概括变成论文中可以被审稿人评估的 contribution。

## 输出结果

一次完整运行会在 `paper_output/` 下留下完整的研究构建轨迹，包括：

- research spine；
- source inventory；
- literature map；
- study design；
- analysis plan；
- experiment registry；
- evidence bank；
- claim register；
- citation support bank；
- writing rationale matrix；
- manuscript draft；
- audit report。

这些文件共同构成一个可追踪、可复核、可修改的论文构建过程。用户可以从中看到每个研究判断的来源、每个实验的目的、每个 claim 的证据基础，以及初稿中每个部分承担的功能。

## 使用边界

参考文献的作用是提供研究结构、problem framing、方法逻辑、实验顺序、证据标准和写作组织方式。用户自己的数据、实验结果、分析输出和证据材料始终是论文内容的基础。Research Architect 会根据证据强度控制 claim 的表达，让论文主张与实际材料保持一致。

## 安装方式

从仓库根目录运行以下命令。

**Codex:**

```bash
mkdir -p "$HOME/.codex/skills" && cp -R dist/codex/skills/* "$HOME/.codex/skills/"
```

**Claude Code:**

```bash
mkdir -p "$HOME/.claude/skills" && cp -R dist/codex/skills/* "$HOME/.claude/skills/"
```

安装后调用主 skill：

```text
research-architect
```

也可以在只需要某个阶段时直接调用 branch skills。
