#!/usr/bin/env python3
import argparse,sys,shutil,subprocess,json,os
ap=argparse.ArgumentParser(); ap.add_argument('html'); ap.add_argument('--out',required=True); ap.add_argument('--preferred',default='weasyprint'); a=ap.parse_args(); attempts=[]
try:
 from weasyprint import HTML; HTML(a.html).write_pdf(a.out); print(json.dumps({'preferred_renderer':a.preferred,'actual_renderer':'weasyprint','fallback_reason':'','success':True})); sys.exit(0)
except Exception as e: attempts.append({'renderer':'weasyprint','error':str(e)})
try:
 from playwright.sync_api import sync_playwright
 with sync_playwright() as p:
  launch_kwargs={'headless':True}
  chrome='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
  if os.path.exists(chrome): launch_kwargs['executable_path']=chrome
  browser=p.chromium.launch(**launch_kwargs); page=browser.new_page(); page.goto('file://'+os.path.abspath(a.html),wait_until='networkidle'); page.pdf(path=a.out,format='A4',print_background=True); browser.close()
 print(json.dumps({'preferred_renderer':a.preferred,'actual_renderer':'playwright-chromium','fallback_reason':'preferred unavailable','success':True})); sys.exit(0)
except Exception as e: attempts.append({'renderer':'playwright-chromium','error':str(e)})
executables=[('chromium',shutil.which('chromium')),('google-chrome',shutil.which('google-chrome')),('microsoft-edge',shutil.which('microsoft-edge')),('google-chrome-app','/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'),('wkhtmltopdf',shutil.which('wkhtmltopdf'))]
for name,exe in executables:
 if exe and not os.path.exists(exe): exe=None
 if not exe: continue
 cmd=[exe,'--headless','--no-sandbox','--disable-gpu','--disable-extensions','--user-data-dir=/tmp/reportflow-chrome-profile',f'--print-to-pdf={a.out}',os.path.abspath(a.html)] if name!='wkhtmltopdf' else [exe,a.html,a.out]
 try:
  p=subprocess.run(cmd,capture_output=True,text=True,timeout=60); ok=p.returncode==0 and os.path.exists(a.out); attempts.append({'renderer':name,'error':p.stderr[-500:] if not ok else ''})
  if ok: print(json.dumps({'preferred_renderer':a.preferred,'actual_renderer':name,'fallback_reason':'preferred unavailable','success':True})); sys.exit(0)
 except Exception as e: attempts.append({'renderer':name,'error':str(e)})
print(json.dumps({'preferred_renderer':a.preferred,'actual_renderer':None,'fallback_reason':'no supported renderer available','success':False,'attempts':attempts},ensure_ascii=False)); sys.exit(2)
