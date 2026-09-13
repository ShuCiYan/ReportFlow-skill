#!/usr/bin/env python3
"""Create a runnable ReportFlow Sprint-1 project from a compact user brief."""
import argparse, json, os, re
from datetime import date
try:
    import yaml
except ImportError:
    raise SystemExit('Use /opt/anaconda3/bin/python (PyYAML required).')

def infer_depth(text):
    if re.search(r'50页|深度研究|投资人|公开发布', text): return 'publication'
    if re.search(r'8.?10页|10页|竞品|给老板', text): return 'rapid'
    return 'standard'

def architecture(topic, depth):
    t=topic.lower()
    if '留存' in t or 'saas' in t:
        return ['现状：留存下降发生在哪里','原因：哪些行为与产品环节解释流失','验证：如何区分相关与因果','方案：优先修复什么并如何试验','指标：如何验证改善是否持续']
    if '商业航天' in t:
        return ['产业边界与需求现实','关键环节的技术与交付门槛','客户、订单与收入证据','价值捕获与竞争位置','3–5年投资情景、风险与跟踪指标']
    return ['竞争对象与用户选择','产品/渠道差异与经营结果','可迁移经验与不可复制因素','行动优先级与验证指标']

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--out',required=True); args=ap.parse_args()
    payload=json.load(open(args.input)); text=payload.get('request',''); topic=payload.get('topic',text)
    depth=payload.get('depth') or infer_depth(text)
    os.makedirs(args.out,exist_ok=True)
    arch=architecture(topic,depth)
    brief={'topic':topic,'audience':payload.get('audience','老板/管理层'),'decision_goal':payload.get('decision_goal',''),'scope':payload.get('scope',''),'geography':payload.get('geography',''),'time_range':payload.get('time_range',''),'depth':depth,'architecture':arch,'priority':{'core':arch[:2],'supporting':arch[2:],'context':[]},'evidence_needs':[],'deliverables':payload.get('deliverables',['research_report'])}
    open(os.path.join(args.out,'research-brief.yaml'),'w').write(yaml.safe_dump(brief,allow_unicode=True,sort_keys=False))
    manifest={'project_id':payload.get('project_id','reportflow-test'),'title':topic,'audience':[brief['audience']],'decision_goal':brief['decision_goal'],'depth':depth,'deliverables':brief['deliverables'],'created_at':str(date.today()),'updated_at':str(date.today())}
    open(os.path.join(args.out,'project-manifest.yaml'),'w').write(yaml.safe_dump(manifest,allow_unicode=True,sort_keys=False))
    state={'project_id':manifest['project_id'],'stage':'brief','depth':depth,'active_artifact':'research-brief.yaml','last_checkpoint':'brief-generated','open_gates':['scope'],'chapters':[],'status':'active','updated_at':str(date.today())}
    open(os.path.join(args.out,'project-state.yaml'),'w').write(yaml.safe_dump(state,allow_unicode=True,sort_keys=False))
    open(os.path.join(args.out,'decision-log.yaml'),'w').write(yaml.safe_dump({'decisions':[{'stage':'brainstorm','decision':f'depth={depth}','rationale':'inferred from request and deliverable'}]},allow_unicode=True,sort_keys=False))
    print(json.dumps({'depth':depth,'architecture':arch,'out':args.out},ensure_ascii=False))
if __name__=='__main__': main()
