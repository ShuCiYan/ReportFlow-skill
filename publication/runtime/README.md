# Reproducible Publication Runtime

Build and run from the repository root:

```bash
docker build -f /path/to/skill/publication/runtime/Dockerfile -t reportflow-publication .
docker run --rm -v "$PWD:/reportflow" reportflow-publication outputs/MASTER_REPORT_EDITABLE_v1.html --out-dir /reportflow/outputs/publication
```

The image contains Playwright Chromium and Poppler. It does not write browser binaries or generated artifacts into the repository image; outputs are written to the mounted output directory.
