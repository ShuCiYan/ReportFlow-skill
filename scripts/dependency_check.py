#!/usr/bin/env python3
import argparse,yaml
ap=argparse.ArgumentParser(); ap.add_argument('state'); a=ap.parse_args(); s=yaml.safe_load(open(a.state)) or {}
changed={c.get('chapter') for c in s.get('chapters',[]) if c.get('changed_definition') or c.get('status')=='reopened'}
for c in s.get('chapters',[]):
 if c.get('dependency') in {f'chapter-{x}-definition' for x in changed}: c['status']='reopened'
s['dependency_check']='REQUIRED' if changed else 'CLEAR'; open(a.state,'w').write(yaml.safe_dump(s,allow_unicode=True,sort_keys=False)); print(s['dependency_check'])
