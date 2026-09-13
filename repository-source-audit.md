# Repository Source Audit

Date: 2026-09-13

## Canonical locations

- Canonical Development Repository: `reportflow-skill/` in this workspace.
- Installed Runtime Copy: `~/.codex/skills/embodied-report-chapter-workflow/`.
- The prior project directory contains report outputs and is not the ReportFlow source repository.

The installed skill was copied into this repository and then audited for portability. Publication runtime, regression fixture, scripts, templates, models, methods, adapters, data, visual and tests are included. Generated report HTML/PDF outputs and browser caches are intentionally excluded.

## Findings

- Source and installed copy were separate before consolidation.
- Several scripts used author-machine absolute paths; those were replaced with repository-relative resolution where applicable.
- The repository has no authorized GitHub remote; CI cannot yet be executed remotely.
- Local Git is initialized here only; no push or remote creation was performed.
