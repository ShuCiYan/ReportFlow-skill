# PDF Render and Inspection

Render with `scripts/render_pdf.py`. Required loop: `Render Pass 1 → rasterize pages → inspect clipping/overflow/overlap/wrapping/source visibility → fix HTML/CSS/SVG → Render Again`. A PDF is not complete without rasterized inspection evidence. Preserve original HTML and never silently overwrite it.
