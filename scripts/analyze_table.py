#!/usr/bin/env python3
"""Reproducible CSV/XLSX summary without modifying the input."""
import argparse,csv,json,os
ap=argparse.ArgumentParser(); ap.add_argument('input'); ap.add_argument('--column',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
if a.input.lower().endswith('.csv'):
 rows=list(csv.DictReader(open(a.input,newline='')))
else:
 try:
  import pandas as pd; rows=pd.read_excel(a.input).to_dict('records')
 except Exception as e: raise SystemExit('XLSX requires /opt/anaconda3/bin/python with pandas/openpyxl: '+str(e))
vals=[float(r[a.column]) for r in rows if r.get(a.column) not in (None,'')]
result={'input_file':os.path.abspath(a.input),'rows':len(rows),'non_null':len(vals),'sum':sum(vals),'mean':sum(vals)/len(vals) if vals else None,'column':a.column}
json.dump(result,open(a.out,'w'),ensure_ascii=False,indent=2); print(json.dumps(result,ensure_ascii=False))
