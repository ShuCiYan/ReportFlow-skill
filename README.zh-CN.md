# ReportFlow｜证据驱动的研究报告全流程工作流

ReportFlow 先明确决策目标，再管理证据、形成判断、逐步复核并完成出版。具身智能内容仅是参考实现，不限制其他行业报告。

Sprint 1 已提供研究简报、项目 Manifest/State、证据台账、Claim 映射、冲突日志、章节复核和恢复模板。

## 出版环境

研究核心不要求 PDF renderer，只有 Publication 输出需要。先运行 `scripts/discover_renderers.py` 检测环境，再运行 `scripts/setup_publication_env.py` 查看安全方案；默认不做全局或静默安装。优先考虑隔离环境中的 Playwright Chromium，也可按能力使用系统浏览器、WeasyPrint 或 wkhtmltopdf。切换 renderer 后必须重新做 PDF 视觉、分页和 TOC 检查。
