# Sprint 3C.1｜Portable Publication Environment

| Check | Result | Evidence |
|---|---|---|
| Renderer capability profiles | PASS | `publication/renderer-capabilities.yaml` |
| Safe bootstrap (detect-only default) | PASS | `scripts/setup_publication_env.py`；无 `--install` 不安装全局依赖 |
| Isolated Playwright package | PASS | `/tmp/reportflow-pub-env` 已安装 Python package |
| Chromium binary bootstrap | BLOCKED | 默认缓存目录权限受限；改用 `/tmp` 路径下载未完成 |
| Renderer discovery | PASS | `scripts/discover_renderers.py`；记录本机与隔离环境状态 |
| Fallback metadata | PASS | `scripts/render_pdf.py` 输出 preferred/actual/fallback_reason |
| CI WORKFLOW | CONFIGURED | `.github/workflows/publication-smoke.yml` |
| CI REPRODUCIBILITY | NOT EXECUTED | No clean-environment run evidence is present. |
| Local PDF render | BLOCKED | 当前无可用 browser binary / WeasyPrint |

## Conclusion

`PORTABLE PUBLICATION ENVIRONMENT = PARTIAL`。

安全 bootstrap、能力画像、回退逻辑和 CI workflow 已配置；尚无干净环境执行证据，因此 CI REPRODUCIBILITY 保持 NOT EXECUTED。本机仍缺少可运行的 Chromium binary，因此不能声称 Local PDF 或 Publication Gate 已通过。
