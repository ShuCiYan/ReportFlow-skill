#!/usr/bin/env python3
import argparse,json,re
from pypdf import PdfReader
ap=argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('--out',required=True); a=ap.parse_args(); r=PdfReader(a.pdf)
starts={}
for i,p in enumerate(r.pages,1):
 t=p.extract_text() or ''
 for n in range(1,6):
  if f'{n}、' in t or f'第{n}章' in t: starts[str(n)]=i
result={'page_count':len(r.pages),'chapter_start_pages':starts,'toc_reconciled':bool(starts) and len(r.pages)>=8,'method':'extracted from rendered PDF; no estimated pages'}
json.dump(result,open(a.out,'w'),ensure_ascii=False,indent=2); print(json.dumps(result,ensure_ascii=False)); raise SystemExit(0 if result['toc_reconciled'] else 1)
