#!/usr/bin/env python3
import argparse,re,sys
from pathlib import Path
ap=argparse.ArgumentParser(); ap.add_argument('html'); a=ap.parse_args(); t=Path(a.html).read_text(errors='ignore')
checks={'html_entities':not bool(re.search(r'&(?:#x|#\d+)',t)),'has_html':('<html' in t and '</html>' in t),'has_body':('<body' in t and '</body>' in t),'script_balance':t.count('<script')==t.count('</script>')}
for k,v in checks.items(): print(k,'PASS' if v else 'FAIL')
sys.exit(0 if all(checks.values()) else 1)
