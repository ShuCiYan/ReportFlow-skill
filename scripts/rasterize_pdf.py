#!/usr/bin/env python3
import argparse,shutil,subprocess,sys,os
ap=argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('--out-dir',required=True); a=ap.parse_args(); os.makedirs(a.out_dir,exist_ok=True)
exe=shutil.which('pdftoppm')
if not exe: print('RASTERIZE=BLOCKED'); sys.exit(2)
p=subprocess.run([exe,'-png','-r','150',a.pdf,os.path.join(a.out_dir,'page')]); print('RASTERIZE=PASS' if p.returncode==0 else 'RASTERIZE=FAIL'); sys.exit(p.returncode)
