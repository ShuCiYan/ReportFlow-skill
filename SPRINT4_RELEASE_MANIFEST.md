# ReportFlow v1.0.0 — Sprint 4 Release Manifest

## Included outputs

- `ReportFlow_Embodied_Intelligence_Executive_Brief.pptx` — editable 8-slide management brief.
- `ReportFlow_Embodied_Intelligence_Executive_Brief.docx` — editable one-page management brief.
- `pptx_render/` and `docx_render/` — local visual QA renders; retained outside the source repository package.

## Source and publication boundary

The full research Master HTML remains the source of truth. PPTX and DOCX are output transformations and do not introduce new research claims. Publication PDF reproducibility is covered by Sprint 3 CI artifacts.

## Release checks

- PPTX rendered to 8 slides and inspected at full size.
- DOCX rendered through the bundled LibreOffice runtime; CJK font fallback was verified.
- Sprint 3 baseline remains frozen at `84752b6`.
