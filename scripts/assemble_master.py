#!/usr/bin/env python3
import argparse,html,json,os,yaml
ap=argparse.ArgumentParser(); ap.add_argument('--manifest',required=True); ap.add_argument('--out',required=True); a=ap.parse_args(); m=yaml.safe_load(open(a.manifest))
parts=[f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>{html.escape(m.get("title","ReportFlow Report"))}</title>']
for css in m.get('stylesheets',[]): parts.append(f'<link rel="stylesheet" href="{html.escape(css)}">')
parts.append('</head><body><main class="report">'); parts.append(f'<header class="report-cover"><h1>{html.escape(m.get("title",""))}</h1><p>{html.escape(m.get("subtitle",""))}</p></header>')
for f in m.get('chapters',[]):
 t=open(f).read(); body=t.split('<body>',1)[1].rsplit('</body>',1)[0] if '<body>' in t else t; parts.append(f'<section class="chapter" data-source="{html.escape(f)}">{body}</section>')
parts.append('</main></body></html>'); open(a.out,'w').write(''.join(parts)); print(json.dumps({'out':os.path.abspath(a.out),'chapters':len(m.get('chapters',[]))}))
