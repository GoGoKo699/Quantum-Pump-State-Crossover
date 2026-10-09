#!/usr/bin/env python3
"""Generate current reading pages from immutable scientific source sections."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'archive/consolidation-2026-10-09'
RULES=[
 ('THEOREM.md','research/THEOREM.md','Correct photon counts, non-Gaussian joint state','## 1. Model, preparation, and order of limits',None),
 ('REVIEW.md','research/REVIEW.md','Contribution assessment','## Central scientific account','## Decision'),
 ('SOURCES.md','research/SOURCES.md','Source comparison and reading record','## [CQ]',None),
]
SUBSTITUTIONS={
 'THEOREM.md':[
  ('This section is a direct consequence of the state theorem, derived in the present consolidation.',
   'This section is a direct consequence of the state theorem.'),
  ('Source details and current reading boundaries are in SOURCES.md and REVIEW.md. Full previous proofs and numerical records remain unchanged under prior/.',
   'See [sources](SOURCES.md), [contribution assessment](REVIEW.md), and the [proof map](PROOF_MAP.md) for the preserved supporting derivations.')],
 'REVIEW.md':[], 'SOURCES.md':[]}
def sha(data:bytes)->str:return hashlib.sha256(data).hexdigest()
def equations(text:str)->list[str]:return re.findall(r'\$\$(.*?)\$\$',text,re.S)
def expected():
 pages={};ledger=[]
 for source,destination,title,start,end in RULES:
  raw=(ARCHIVE/source).read_text();selected=raw[raw.index(start):]
  if end:selected=selected[:selected.index(end)]
  text=selected
  for old,new in SUBSTITUTIONS[source]:
   if text.count(old)!=1:raise ValueError('Nonunique transformation: '+source)
   text=text.replace(old,new)
  if equations(text)!=equations(selected):raise ValueError('Scientific equation changed')
  additional=' · [Analytical review](PROOF_REVIEW.md) · [Additional source comparison](SOURCE_REVIEW.md)' if source=='SOURCES.md' else ''
  footer=f'\n\n---\n\n[Preserved source](../archive/consolidation-2026-10-09/{source}){additional} · [Reproducibility](../REPRODUCIBILITY.md)\n'
  data=('# '+title+'\n\n'+text.rstrip()+footer).encode()
  pages[destination]=data
  ledger.append({'source':source,'destination':destination,'start':start,'end_excluded':end,
                 'literal_substitutions':SUBSTITUTIONS[source],'source_sha256':sha(raw.encode()),
                 'display_equations':len(equations(selected)),
                 'equations_sha256':sha(json.dumps(equations(selected)).encode()),'output_sha256':sha(data)})
 pages['provenance/READING.json']=(json.dumps(ledger,indent=2,sort_keys=True)+'\n').encode()
 return pages
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
 bad=[]
 for name,data in expected().items():
  f=ROOT/name
  if args.check:
   if not f.is_file() or f.read_bytes()!=data:bad.append(name)
  else:f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(data)
 if bad:raise SystemExit('Generated reading mismatch: '+', '.join(bad))
 print('Reading pages and transformation ledger verified.' if args.check else 'Reading pages generated.')
if __name__=='__main__':main()
