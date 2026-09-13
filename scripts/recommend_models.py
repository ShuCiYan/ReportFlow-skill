#!/usr/bin/env python3
"""Small deterministic baseline recommender; human review remains required."""
import argparse,re,yaml
from pathlib import Path
ap=argparse.ArgumentParser(); ap.add_argument('request'); a=ap.parse_args(); lib=yaml.safe_load(open(Path(__file__).resolve().parents[1] / 'models' / 'library.yaml'))['models']
text=a.request.lower(); ranked=[]
aliases={'留存':'retention','tco':'unit economics','经济性':'unit economics','验证':'experiment','竞品':'competition','竞争':'competition','价值链':'value chain','saas':'saas','转化':'conversion'}
for k,v in aliases.items():
 if k in text: text += ' '+v
for m in lib:
 hits=sum(1 for s in m.get('selection_signals',[]) if s.lower() in text)
 if hits: ranked.append((hits,m))
for _,m in sorted(ranked,key=lambda x:-x[0])[:3]: print(f"{m['id']}\t{m['name']}\t{m['status']}\t{m['purpose']}")
