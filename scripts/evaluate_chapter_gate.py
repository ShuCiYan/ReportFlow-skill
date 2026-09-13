#!/usr/bin/env python3
import argparse,csv,yaml
ap=argparse.ArgumentParser(); ap.add_argument('claim_map'); ap.add_argument('--state',required=True); a=ap.parse_args()
rows=list(csv.DictReader(open(a.claim_map)))
blocked=[r for r in rows if r.get('importance')=='core' and r.get('answer_status') in {'DISPUTED','DISCLOSURE_GAP','UNANSWERABLE'}]
s=yaml.safe_load(open(a.state)) or {}
if blocked:
 s['chapter_gate']='FAIL'; s['gate_reasons']=[r['claim_id']+':'+r['answer_status'] for r in blocked]; s['open_gates']=sorted(set(s.get('open_gates',[]))|{'evidence'}); print('FAIL')
else: s['chapter_gate']='PASS'; print('PASS')
open(a.state,'w').write(yaml.safe_dump(s,allow_unicode=True,sort_keys=False))
