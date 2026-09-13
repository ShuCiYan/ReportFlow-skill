# ReportFlow v1.0｜Sprint 3 Acceptance Report

| Gate | Result | Evidence |
|---|---|---|
| Visual Intent / Design Tokens | PASS | `visual/design-tokens.yaml`、`visual/presets/` |
| Master HTML assembly | PASS | `scripts/assemble_master.py`；manifest 驱动、顺序确定、不改引用 |
| Global HTML QA | PASS | `scripts/html_qa.py`；实体、标签和 script 平衡检查通过 |
| Print CSS | PASS | `publication/print-css.css` |
| Renderer Discovery / Fallback | PASS | `scripts/discover_renderers.py`、`tests/sprint3/renderer-inventory.json`；已检查 Python、CLI、Chromium 系列与 wkhtmltopdf |
| PDF Render | BLOCKED | `render_pdf.py` 已支持 WeasyPrint→Chromium/Chrome/Edge/wkhtmltopdf 回退；当前均不可用 |
| Rasterized inspection | NOT EXECUTED | PDF 未生成，不能伪称通过 |
| Pagination / TOC reconciliation | NOT EXECUTED | 依赖 PDF 产物 |
| Publication Gate | BLOCKED | PDF 渲染依赖未满足 |

## Current status

`SPRINT 3 CORE HTML = PASS`

`SPRINT 3 PUBLICATION PDF = BLOCKED`

依赖任一受支持 HTML→PDF 渲染引擎后，才能继续 Render → Raster Inspect → Fix → Re-render → Pagination → TOC → Publication Gate。当前不进入 PPT / DOCX。
