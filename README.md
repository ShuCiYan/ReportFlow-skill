# ReportFlow

**A workflow for professional research reports**

Let AI do more than “write a report”—make it work through a real research process.

> Think clearly first, research carefully next, explain clearly last.

From framing the question and gathering evidence to analysis, writing, chapter review, and final publication, ReportFlow turns complex research into a workflow that can be traced, resumed, and verified.

[English](README.md) | [简体中文](README.zh-CN.md)

## What is ReportFlow?

ReportFlow is not a prompt that asks AI to write a report, and it is not a fixed outline with new headings. It first clarifies the decision a reader needs to make, builds an architecture that fits the question, links important judgments to concrete evidence, reviews chapters progressively, and checks the actual HTML and PDF that will be delivered.

The repository includes an embodied-intelligence example, but ReportFlow also fits industry, company, competitor, market-entry, and investment-theme research.

## Why do you need ReportFlow?

Many AI reports begin writing before the question is clear, treat one citation as sufficient proof, hide missing data behind fluent prose, reuse the same chapter skeleton, and stop when a PDF exports.

ReportFlow turns these failure points into explicit checks: define scope and evidence needs, preserve Unknown, Disputed, and Disclosure Gap states, record claim-to-source relationships, and recheck dependent chapters when a key premise changes.

**Research depth can vary. Research integrity cannot.**

## Ordinary AI reports vs. ReportFlow

| Ordinary AI report | ReportFlow |
| --- | --- |
| Start writing from a broad topic | Define the decision, audience, and research questions first |
| A citation is treated as sufficient | Check claim–evidence fit |
| Missing information becomes a definite claim | Preserve unknowns, disputes, and disclosure gaps |
| Every project uses the same outline | Let the question and evidence needs shape the architecture |
| Review once at the end | Review chapters progressively and reopen dependencies when needed |
| PDF export is the finish line | Check rendered pages, pagination, and the table of contents |

## The five-stage workflow

`FRAME → RESEARCH → WRITE → REVIEW → PUBLISH`

1. **Frame** — define the decision, audience, scope, time range, and deliverable.
2. **Research** — build an evidence ledger, source trail, conflict record, and actively seek evidence that could weaken the current view.
3. **Write** — turn facts into bounded answers instead of source-by-source summaries.
4. **Review** — review paragraphs, chapters, and cross-chapter dependencies; reopen downstream work when a key premise changes.
5. **Publish** — assemble editable HTML, render PDF, rasterize pages, and reconcile layout and page references.

## Three research modes

| Mode | Best for | What changes |
| --- | --- | --- |
| **Rapid** | 8–12 page executive briefs and competitor scans | Narrow scope and fast architecture; no full publication audit by default |
| **Standard** | Internal industry or company research | More complete evidence tracking, citations, and chapter review |
| **Publication** | Investor-facing or public reports | Full evidence governance, dependency checks, progressive review, rendering, and publication QA |

The mode changes depth and delivery gates, not the standard for facts, citations, or evidence boundaries.

## First use

Start with a request such as:

> I need an 8–10 page competitor analysis of Luckin and Cotti for our coffee brand leadership team. Focus on what we should learn and what we should not copy.

ReportFlow should recommend Rapid, ask only questions that could change the research design, produce a Research Brief, and build chapters around what the competitors did, why it worked, and what is not transferable. For a public deep-research report, choose Publication and keep the project state, evidence ledger, and claim–evidence map with the workspace.

## Core capabilities

- **Research design** — frame the problem, define scope and audience, generate a dynamic architecture, and record key decisions.
- **Evidence system** — maintain a `claim → evidence → original source` chain, conflict records, counter-evidence, and disclosure gaps; do not silently upgrade pilots, orders, deliveries, or revenue into stronger claims.
- **Progressive chapter review** — apply chapter gates, dependency checks, claim–evidence fit, and content-value checks; reopen downstream chapters when premises change.
- **Model and method selection** — choose methods for the question, and track research, validation, and communication methods separately with their limits.
- **Search, knowledge, and data** — stop when additional evidence no longer changes the answer; promote validated knowledge for reuse and keep definitions and calculation steps reviewable.
- **Publication quality** — check renderers, PDF page count, rasterized pages, contact sheets, long tables, figure captions, sources, and table-of-contents page numbers.

`HTML correct ≠ PDF correct.`  
`PDF generated ≠ publication finished.`

## Output formats

ReportFlow currently supports Research Briefs, evidence and project files, editable Master HTML, checked publication PDFs, and PPTX / DOCX transformations of validated research results.

PPTX and DOCX are secondary delivery formats. They do not replace the validated research source.

## Good fits

Industry and market research, company research, competitor analysis, market entry, technology commercialization, policy research, and investment themes where evidence boundaries must remain visible.

## What ReportFlow will not do for you

- Invent missing data to make a report look complete;
- force a popular analytical model onto an unsuitable question;
- turn company promotional language into verified fact;
- treat pilots, orders, deliveries, revenue, and profit as the same evidence;
- declare a report complete because a PDF exported;
- replace the researcher’s final judgment.

It does not replace expert judgment, audited data, legal advice, academic peer review, or investment advisers, and is not designed for fully unattended high-stakes decisions.

## Reference example

`examples/embodied-intelligence/` demonstrates an embodied-intelligence robotics industry and commercialization study, including dynamic architecture, evidence chains, disclosure handling, chapter review, Master HTML, PDF page reconciliation, and page-by-page visual inspection.

It is a reference implementation, not ReportFlow’s only use case or a fixed chapter template.

## Installation and quick start

### For regular users

Install the repository as a Codex Skill, then tell ReportFlow what you want to research. It starts with research design instead of immediately producing a long document without scope or evidence records.

### For developers and advanced users

```bash
git clone https://github.com/ShuCiYan/ReportFlow-skill.git
cd ReportFlow-skill
python scripts/dependency_check.py <project-state.yaml>
python scripts/discover_renderers.py
```

At project start, read `project/project-state.yaml`; if it does not exist, initialize it from `project/state.template.yaml`. Projects should also maintain `project-manifest.yaml` and `decision-log.yaml`.

## Publication Runtime

The research core does not require a PDF renderer. A runtime is needed only for publication output. Read `publication/runtime/README.md`, check the environment, and prepare Chromium and Poppler in an isolated environment. Do not commit browser binaries, caches, or generated PDFs.

GitHub Actions provides smoke and publication-regression workflows to validate HTML, PDF, rasterized pages, contact sheets, and table-of-contents reconciliation in a clean environment. CI proves reproducibility; it does not replace human visual review.

## Repository structure

```text
SKILL.md                    workflow contract
project/                    manifests, state, and dependency definitions
templates/                  briefs, evidence ledgers, and review templates
models/                     model cards and routing guidance
methods/                    analytical, communication, and validation methods
knowledge/                  knowledge promotion and distillation rules
data/                       calculation manifests and data helpers
publication/                HTML, PDF, runtime, and publication gates
scripts/                    executable helpers
tests/                      acceptance and regression tests
.github/workflows/          publication smoke and regression CI
```

## Current version

**ReportFlow v1.0** includes research-question and scope design, dynamic report architecture, evidence management, claim tracking, progressive review, dependency checks, model and method recommendations, search and knowledge reuse, CSV / XLSX analysis, Master HTML, PDF publication and visual inspection, and PPTX / DOCX output transformations.

## Future directions

- Expand the validated methods library;
- add reference cases across more industries and task types;
- improve installation across platforms;
- expand publication and presentation templates;
- add more regression and benchmark tests.

## License

MIT. See [LICENSE](LICENSE).
