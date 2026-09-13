---
name: reportflow
description: Evidence-led workflow for framing, researching, writing, reviewing, and publishing decision-grade reports with AI assistance and human judgment.
metadata:
  short-description: ReportFlow｜证据驱动的研究报告全流程工作流
---

# ReportFlow｜证据驱动的研究报告全流程工作流

ReportFlow 是由本 Skill 调度的一套可维护、可恢复、可审计的研究报告系统，不是单一 Prompt、固定章节模板或具身智能专用框架。具身智能材料仅作为 `examples/embodied-intelligence/` 的参考实现。

## North Star

事实优先于完成；证据优先于叙事；逻辑优先于模板；人工判断优先于自动生成；最终呈现优先于源文件看起来正确。研究深度可以变化，研究诚信不能降低。

## 用户主流程

对用户保持五个阶段：`FRAME → RESEARCH → WRITE → REVIEW → PUBLISH`（设计 → 研究 → 写作 → 审核 → 出版）。内部阶段按需展开，但不得跳过上游退出条件：

`Brainstorm & Scope → Research Brief → Depth Selection → Dynamic Architecture → Evidence Management → Critical Thinking → Progressive Review → Publication`。

## 运行入口与项目状态

1. 进入项目时读取 `project/project-state.yaml`（若不存在则从 `project/state.template.yaml` 初始化），判断当前阶段、深度、未关闭 Gate 和恢复点。
2. 解析用户已经提供的信息，只询问会改变研究设计的问题；不得重复询问已知信息。
3. 把每次关键范围、问题、模型、来源取舍和 Gate 决定写入 `decision-log.yaml`。
4. 任何阶段只有在对应 Artifact 存在且 Gate 通过后才可进入下一阶段；中断时保存 checkpoint，恢复时从最近未通过 Gate 继续。

## Brainstorm & Scope → Research Brief

正式搜索前必须生成 `research-brief.md`，至少包含：Research Topic、Audience、Decision Goal、Scope、Geography、Time Range、Existing Materials、Deadline、Recommended Depth、Core Research Questions、Proposed Architecture、Core/Supporting/Context、Evidence Needs、Recommended Methods、Visual Intent、Deliverables 和 Open Decisions。

深度只使用三档：

- **Rapid**：可减少出版级审计，但不降低事实、引用和证据边界标准。
- **Standard**：包含研究架构、证据追踪、正式引用、章节与跨章节复核及必要图表。
- **Publication**：增加完整证据治理、渲染/分页/出版 QA 与 Freeze。

目录必须由 `Decision Goal → Research Questions → Evidence Needs` 动态产生，并记录 Architecture Rationale；不得要求固定章数、篇幅、图表数或固定模型。

## Evidence Management

每个重要 Claim 建立：`Claim → Evidence → Original Source`。使用 `templates/evidence-ledger.csv`、`templates/claim-evidence-map.csv` 和 `templates/conflict-log.csv`。

- 区分 Confirmed、Unknown、Disclosure Gap、Not Comparable、Disputed。
- Source quality 依 Claim 类型判断；优先原始、审计、监管、客户、采购和原始研究来源。
- 执行 Claim Strength Check：不得把 Demo、Pilot、订单、交付、验收、运行、收入、回款、利润、复购或 ROI 静默升级为更强结论。
- 搜索停止条件：新增证据不再改变 Answer、Confidence、Boundary、Competing Explanation 或 Investment Meaning 时停止，并记录 Stop Rule。

## Progressive Chapter Review

长报告必须按以下层级保存检查结果：`Paragraph → Chapter → Block → Cross-Chapter`。使用 `templates/chapter-review.md` 和 `templates/cross-chapter-review.md`。

章节状态只能是：`draft → reviewing → approved → final`；发现材料性问题时可转 `reopened`。章节只有在 Chapter Gate、Dependency Check、Claim–Evidence Fit、标题兑现和内容价值检查通过后，才能进入下一状态。用户本人批准才可记录 `HUMAN REVIEW = APPROVED`。

## 方法选择

需要分析方法时先查 `models/library.yaml` 与 `models/recommender.md`，再决定是否使用或设计新方法。模型、验证方法和表达方法必须分开；不得因为库中存在某模型就机械套用。每次使用记录：`Method | Purpose | Why fit | Applicability | Limitation | Evidence required`。验证方法见 `methods/validation/README.md`；模型状态使用 `core / extended / experimental`，实验性模型必须说明适用边界。

## Output Contract

所有项目都必须维护 `project-manifest.yaml`、`project-state.yaml` 和 `decision-log.yaml`。输出可按深度选择 Research Report、Executive Brief 或其他格式；本 Sprint 只实现研究核心，不假设 PDF、PPT 或 DOCX 已经可用。

## Reference routing

- 项目状态字段：`project/manifest.schema.yaml`、`project/state.schema.yaml`、`project/decision-log.schema.yaml`
- 可复制模板：`templates/`
- 搜索适配与失败降级：`adapters/search/contract.yaml`、`adapters/search/fallback.md`
- 本地知识与晋升：`adapters/knowledge/README.md`、`knowledge/promotion.md`、`knowledge/distillation.md`
- 数据分析：`data/calculation-manifest.yaml`、`scripts/analyze_table.py`
- 出版链路：`visual/design-tokens.yaml`、`publication/`、`scripts/assemble_master.py`、`scripts/render_pdf.py`、`scripts/html_qa.py`
- Renderer Discovery / Fallback：`scripts/discover_renderers.py`、`scripts/rasterize_pdf.py`；渲染器切换必须记录 preferred/actual/fallback reason，并重新做视觉检查。
- 具身智能参考实现：`examples/embodied-intelligence/` 与现有 `references/chapter-question-map.md`
- Sprint 1 范围说明：`references/sprint-1-research-core.md`

## Hard boundaries

不得因已有旧报告、已有来源或框架而跳过当前项目的问题定义、证据记录、冲突处理和渐进复核。AI 可以检索、抽取、比较和提出反例；人工负责决策目标、范围、证据裁决、最终结论和发布批准。
