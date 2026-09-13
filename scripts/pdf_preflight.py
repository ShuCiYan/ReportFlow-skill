#!/usr/bin/env python3
import argparse,json,os,sys
from pypdf import PdfReader
ap=argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('--out',required=True); a=ap.parse_args()
checks={"exists":os.path.exists(a.pdf),"nonzero":False,"pages":0,"text_layer":False,"a4_pages":True}
if checks['exists']:
 checks['nonzero']=os.path.getsize(a.pdf)>0
 try:
  r=PdfReader(a.pdf); checks['pages']=len(r.pages); checks['text_layer']=any((p.extract_text() or '').strip() for p in r.pages[:3])
  for p in r.pages:
   w=float(p.mediabox.width); h=float(p.mediabox.height)
   if abs(w-595.28)>8 or abs(h-841.89)>8: checks['a4_pages']=False
 except Exception as e: checks['error']=str(e)
checks['pass']=checks['exists'] and checks['nonzero'] and checks['pages']>0 and checks['a4_pages']
json.dump(checks,open(a.out,'w'),ensure_ascii=False,indent=2); print(json.dumps(checks,ensure_ascii=False)); sys.exit(0 if checks['pass'] else 1)
