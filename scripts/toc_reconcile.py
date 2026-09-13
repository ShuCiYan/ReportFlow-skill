#!/usr/bin/env python3
import argparse,json,re
from pypdf import PdfReader

CN=['一','二','三','四','五']
HEADING={f'chapter-{i}':re.compile(rf'^\s*第\s*{c}\s*章\s*[｜|:]') for i,c in enumerate(CN,1)}

def detect_chapter_starts(page_texts):
    """Detect only line-anchored chapter headings, never TOC/source mentions."""
    hits={k:[] for k in HEADING}
    for page_no,text in enumerate(page_texts,1):
        if re.search(r'目录|table of contents|contents|资料来源|sources|附录|appendix', text or '', re.I):
            continue
        lines=[x.strip() for x in (text or '').splitlines() if x.strip()][:20]
        for line in lines:
            for key,pat in HEADING.items():
                compact=re.sub(r'\s+','',line)
                if pat.search(line) or re.search(rf'^第\s*{CN[int(key.split("-")[1])-1]}\s*章',compact): hits[key].append(page_no)
    starts={k:v[0] for k,v in hits.items() if len(v)==1}
    valid=(len(starts)==5 and all(len(v)==1 for v in hits.values()))
    pages=[starts[k] for k in sorted(starts,key=lambda x:int(x.split('-')[1]))]
    valid=valid and len(set(pages))==5 and pages==sorted(pages) and min(pages,default=0)>2
    return starts,valid,hits

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('--out',required=True); a=ap.parse_args(); r=PdfReader(a.pdf)
 starts,valid,hits=detect_chapter_starts([(p.extract_text() or '') for p in r.pages])
 result={'page_count':len(r.pages),'chapter_start_pages':starts,'candidate_hits':hits,'toc_reconciled':valid,'method':'line-anchored chapter headings only; TOC/source mentions and duplicate or out-of-order hits invalidate reconciliation'}
 json.dump(result,open(a.out,'w'),ensure_ascii=False,indent=2); print(json.dumps(result,ensure_ascii=False)); raise SystemExit(0 if valid else 1)

if __name__=='__main__': main()
