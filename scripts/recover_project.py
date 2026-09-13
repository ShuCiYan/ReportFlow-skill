#!/usr/bin/env python3
"""Read a ReportFlow project state and print the next resumable action."""
import argparse, os
import yaml
def load(p,n):
    with open(os.path.join(p,n)) as f:return yaml.safe_load(f) or {}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('project'); a=ap.parse_args(); p=a.project
    m=load(p,'project-manifest.yaml'); s=load(p,'project-state.yaml'); d=load(p,'decision-log.yaml')
    print(yaml.safe_dump({'project':m.get('title'),'stage':s.get('stage'),'depth':s.get('depth'),'active_artifact':s.get('active_artifact'),'open_gates':s.get('open_gates',[]),'last_checkpoint':s.get('last_checkpoint'),'decisions':d.get('decisions',[]),'next_action':('close '+','.join(s.get('open_gates',[]))+' gate' if s.get('open_gates') else 'continue from active_artifact')},allow_unicode=True,sort_keys=False))
if __name__=='__main__': main()
