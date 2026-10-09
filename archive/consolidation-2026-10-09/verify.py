#!/usr/bin/env python3
"""Run all 15 scientific check groups and verify the preserved research record.

Use a new absolute output directory outside this package. Numerical assertion
success, unchanged sources, and canonical report identity are separate checks.
No scientific tolerance or reference report is changed by this wrapper.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path,PurePosixPath
import subprocess
import sys
ROOT=Path(__file__).resolve().parent

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def inventory():
    out={}
    for p in sorted(ROOT.rglob('*')):
        if p.is_symlink():raise ValueError('Source symlink: '+str(p))
        if p.is_file():out[str(p.relative_to(ROOT))]=digest(p)
    return out

def differences(a,b,path=''):
    out=[]
    if isinstance(a,dict) and isinstance(b,dict):
        if a.keys()!=b.keys():out.append({'path':path,'kind':'keys','reference':list(a),'run':list(b)})
        for k in sorted(a.keys()&b.keys()):out+=differences(a[k],b[k],path+'/'+str(k))
    elif isinstance(a,list) and isinstance(b,list):
        if len(a)!=len(b):out.append({'path':path,'kind':'length','reference':len(a),'run':len(b)})
        for i,(x,y) in enumerate(zip(a,b)):out+=differences(x,y,path+'/'+str(i))
    elif a!=b or type(a)!=type(b):
        e={'path':path,'kind':'value','reference':a,'run':b}
        if type(a) in(int,float) and type(b) in(int,float):e.update(kind='numeric',absolute_difference=abs(a-b))
        out.append(e)
    return out

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output-dir',type=Path,required=True)
    args=ap.parse_args()
    if not args.output_dir.is_absolute():ap.error('Use an absolute output directory')
    out=args.output_dir.resolve()
    if out.exists() or out==ROOT or ROOT in out.parents:ap.error('Use a new directory outside the package')
    before=inventory();anchor=json.loads((ROOT/'notes/incoming_hashes.json').read_text())
    actual={str(p.relative_to(ROOT/'prior')):digest(p) for p in (ROOT/'prior').rglob('*') if p.is_file()}
    if actual!=anchor:raise ValueError('Preserved source membership or bytes changed')
    checked=[]
    for manifest in sorted((ROOT/'prior').rglob('MANIFEST.json')):
        data=json.loads(manifest.read_text())
        for name,v in data.items():
            path=PurePosixPath(name)
            if path.is_absolute() or '..' in path.parts:raise ValueError('Unsafe manifest member')
            f=manifest.parent/path
            if f.stat().st_size!=v['bytes'] or digest(f)!=v['sha256']:raise ValueError('Changed manifest member: '+str(f))
        checked.append({'path':str(manifest.relative_to(ROOT)),'members':len(data)})
    out.mkdir(parents=True)
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    suites=[('consolidation','check_consolidation.py','evidence/first.json'),
            ('comparison','prior/check_comparison.py','prior/evidence/final.json'),
            ('pilot','prior/prior/check_pilot.py','prior/prior/evidence/first.json')]
    results=[]
    for name,script,canonical in suites:
        output=out/(name+'.json')
        with (out/(name+'.log')).open('xb') as log:
            result=subprocess.run([sys.executable,str(ROOT/script),'--output',str(output)],cwd=ROOT,env=env,
                                  stdout=log,stderr=subprocess.STDOUT,timeout=180)
        item={'suite':name,'returncode':result.returncode,'script':script,'canonical':canonical,'report':output.name}
        if output.exists():
            data=json.loads(output.read_text());ref=json.loads((ROOT/canonical).read_text())
            item.update(status=data.get('status'),groups=data.get('groups'),
                        byte_identical=output.read_bytes()==(ROOT/canonical).read_bytes(),differences=differences(ref,data))
        results.append(item)
    assertions=all(x['returncode']==0 and x.get('status')=='PASS' for x in results)
    identical=all(x.get('byte_identical',False) for x in results)
    unchanged=inventory()==before
    receipt={'scientific_assertions_pass':assertions,'canonical_reports_byte_identical':identical,
             'source_unchanged':unchanged,'groups':sum(x.get('groups',0) for x in results),
             'preserved_incoming_files':len(anchor),'checked_manifests':checked,'source_sha256':before,'suites':results}
    with (out/'receipt.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in('source_sha256','suites')},indent=2))
    raise SystemExit(0 if assertions and identical and unchanged else 1)
if __name__=='__main__':main()
