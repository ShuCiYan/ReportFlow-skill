#!/usr/bin/env python3
import argparse,glob,os,math
from PIL import Image,ImageDraw
ap=argparse.ArgumentParser(); ap.add_argument('indir'); ap.add_argument('--out',required=True); a=ap.parse_args()
files=sorted(glob.glob(os.path.join(a.indir,'*.png'))); thumbs=[]
for f in files:
 im=Image.open(f).convert('RGB'); im.thumbnail((220,310)); thumbs.append((f,im.copy()))
cols=4; rows=max(1,math.ceil(len(thumbs)/cols)); sheet=Image.new('RGB',(cols*240,rows*340),'white'); d=ImageDraw.Draw(sheet)
for i,(f,im) in enumerate(thumbs):
 x=(i%cols)*240+10; y=(i//cols)*340+10; sheet.paste(im,(x,y)); d.text((x,y+315),os.path.basename(f),fill='black')
sheet.save(a.out); print(f'CONTACT_SHEET={a.out} PAGES={len(files)}')
