#!/usr/bin/env python3
import argparse,shutil,subprocess,sys,os
ap=argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('--out-dir',required=True); a=ap.parse_args(); os.makedirs(a.out_dir,exist_ok=True)
if not os.path.exists(a.pdf): print(f'RASTERIZE=BLOCKED reason=PDF_NOT_FOUND path={a.pdf}'); sys.exit(2)
exe=shutil.which('pdftoppm')
if not exe:
 print('RASTERIZE=BLOCKED reason=PDftoppm_NOT_FOUND; install Poppler (Ubuntu: sudo apt-get install poppler-utils) or provide pdftoppm on PATH')
 sys.exit(2)
p=subprocess.run([exe,'-png','-r','150',a.pdf,os.path.join(a.out_dir,'page')]); print('RASTERIZE=PASS' if p.returncode==0 else 'RASTERIZE=FAIL'); sys.exit(p.returncode)
