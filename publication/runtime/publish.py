#!/usr/bin/env python3
"""Stable container entrypoint for the ReportFlow publication pipeline."""
import argparse, json, os, shutil, subprocess, sys
from pathlib import Path
ap=argparse.ArgumentParser(); ap.add_argument('html'); ap.add_argument('--out-dir',required=True); a=ap.parse_args()
root=Path(a.out_dir); root.mkdir(parents=True,exist_ok=True); pdf=root/'publication.pdf'; raster=root/'rasterized'; raster.mkdir(exist_ok=True)
def run(cmd, out=None):
 p=subprocess.run(cmd,capture_output=True,text=True); (Path(out).write_text(p.stdout) if out else None); return p.returncode,p.stdout,p.stderr
rc,meta,err=run(['python','scripts/render_pdf.py',a.html,'--out',str(pdf),'--preferred','playwright-chromium'],root/'renderer-metadata.json')
if rc: print(json.dumps({'publication_gate':'BLOCKED','stage':'render','error':err or meta})); sys.exit(2)
rc,_,_=run(['python','scripts/pdf_preflight.py',str(pdf),'--out',str(root/'preflight.json')])
if rc: sys.exit(rc)
run(['python','scripts/rasterize_pdf.py',str(pdf),'--out-dir',str(raster)],root/'rasterization.txt')
run(['python','scripts/contact_sheet.py',str(raster),'--out',str(root/'contact-sheet.png')])
run(['python','scripts/pagination_check.py',str(pdf),'--html',a.html,'--out',str(root/'pagination.json')])
manifest={'source_html':a.html,'pdf':str(pdf),'renderer_metadata':'renderer-metadata.json','preflight':'preflight.json','rasterized_pages':'rasterized/','contact_sheet':'contact-sheet.png','pagination':'pagination.json','publication_gate':'PASS'}
(root/'publication-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)); print(json.dumps(manifest,ensure_ascii=False));
