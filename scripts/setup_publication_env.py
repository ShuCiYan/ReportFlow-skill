#!/usr/bin/env python3
"""Safe publication environment bootstrap. Detection is default; --install is explicit."""
import argparse,shutil,subprocess,sys,json
ap=argparse.ArgumentParser(); ap.add_argument('--install',action='store_true'); a=ap.parse_args()
checks=[]
for name in ['chromium','google-chrome','microsoft-edge','wkhtmltopdf','weasyprint']:
 checks.append({'name':name,'available':bool(shutil.which(name)),'path':shutil.which(name)})
try:
 import playwright; checks.append({'name':'playwright-python','available':True,'path':sys.executable})
except ImportError: checks.append({'name':'playwright-python','available':False,'path':sys.executable})
print(json.dumps({'mode':'install' if a.install else 'detect','checks':checks},ensure_ascii=False,indent=2))
if not a.install: sys.exit(0)
print('INSTALL PLAN: create project-local environment and install playwright package; browser binary installation requires explicit follow-up.')
print('No global installation performed by this script.')
