# ReportFlow

Evidence-led workflow for decision-grade research reports.

This repository is the **Canonical Development Repository**. The Codex-installed runtime copy is maintained separately at `~/.codex/skills/embodied-report-chapter-workflow/` for compatibility. Do not edit the installed copy as the release source.

Start with `SKILL.md`. Run `python scripts/dependency_check.py` and the tests under `tests/`. Publication requires an available local renderer or the portable runtime in `publication/runtime/`; browser binaries and generated PDFs are never committed.

## Output transformation

Sprint 4 provides editable PPTX and DOCX executive outputs from the frozen Master HTML. Run `python scripts/build_sprint4_outputs.py` from the development repository. The generated files are written to `outputs/sprint4_release/` in the parent project and should be visually rendered before delivery.
