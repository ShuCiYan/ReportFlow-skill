#!/usr/bin/env python3
import json,shutil,subprocess,sys,importlib.util,os
def ver(cmd):
 try:return subprocess.run([cmd,'--version'],capture_output=True,text=True,timeout=3).stdout.strip().splitlines()[0]
 except Exception:return ''
items=[]
for name in ['weasyprint','wkhtmltopdf','chromium','chromium-browser','google-chrome','microsoft-edge','firefox','pdftoppm','mutool','magick','google-chrome-app']:
 path=shutil.which(name)
 if name=='google-chrome-app':
  path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' if os.path.exists('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome') else None
 items.append({'name':name,'available':bool(path),'executable':path,'version':ver(path) if path else ''})
for mod in ['weasyprint','playwright']:
 items.append({'name':'python:'+mod,'available':bool(importlib.util.find_spec(mod)),'executable':sys.executable,'version':''})
print(json.dumps({'renderers':items,'preferred':'weasyprint','fallbacks':['chromium','google-chrome','microsoft-edge','wkhtmltopdf'],'rasterizers':['pdftoppm','mutool','magick']},ensure_ascii=False,indent=2))
