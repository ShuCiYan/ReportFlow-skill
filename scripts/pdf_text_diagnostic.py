#!/usr/bin/env python3
import argparse,re
from pypdf import PdfReader
ap=argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('--out',required=True); a=ap.parse_args(); r=PdfReader(a.pdf)
with open(a.out,'w',encoding='utf-8') as f:
 for i,p in enumerate(r.pages,1):
  raw=p.extract_text() or ''; norm=re.sub(r'\s+','',raw)
  lines=[x.strip() for x in raw.splitlines() if x.strip()]
  c=[x for x in lines[:20] if re.search(r'第\s*[一二三四五]\s*章|chapter[- ]?[1-5]',x,re.I)]
  f.write(f'=== PAGE {i} ===\nRAW:\n{raw}\nNORMALIZED:\n{norm}\nTOP_ZONE_CANDIDATES:\n{c}\n\n')
print(f'PDF_TEXT_DIAGNOSTIC={a.out} PAGES={len(r.pages)}')
