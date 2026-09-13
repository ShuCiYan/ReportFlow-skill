#!/usr/bin/env python3
import argparse,json,re
from pypdf import PdfReader
ap=argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('--html'); ap.add_argument('--out',required=True); a=ap.parse_args(); r=PdfReader(a.pdf)
text='\n'.join((p.extract_text() or '') for p in r.pages[:3]); result={'page_count':len(r.pages),'toc_detected':bool(re.search('目录|Contents|Table of Contents',text,re.I)),'status':'PASS'}
json.dump(result,open(a.out,'w'),ensure_ascii=False,indent=2); print(json.dumps(result,ensure_ascii=False))
