#!/usr/bin/env python3
"""Run the unchanged scientific suites and current repository checks.

Strict mode requires canonical report byte identity. Explicit portability mode
retains finite numerical differences for review; it changes no scientific test.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'archive/consolidation-2026-10-09'
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'scripts'))
import build_reading

def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(root:Path=ROOT)->dict:
 result={}
 for f in sorted(root.rglob('*')):
  rel=f.relative_to(root)
  if '.git' in rel.parts or '.venv' in rel.parts:continue
  if f.is_symlink():raise ValueError('Source symlink: '+str(rel))
  if f.is_file():result[rel.as_posix()]=digest(f)
 return result

def member(base:Path,name:str)->Path:
 p=PurePosixPath(name)
 if p.is_absolute() or '..' in p.parts or '\\' in name:raise ValueError('Unsafe archive path')
 f=base/p
 if f.is_symlink() or not f.resolve().is_relative_to(base.resolve()):raise ValueError('Escaping archive path')
 return f

def check_archive()->dict:
 spec=json.loads((ROOT/'provenance/IMPORT.json').read_text())
 if digest(ARCHIVE/'MANIFEST.json')!=spec['archive_manifest_sha256']:raise ValueError('Root manifest changed')
 expected=set(json.loads((ARCHIVE/'MANIFEST.json').read_text()))|{'MANIFEST.json'}
 if set(inventory(ARCHIVE))!=expected:raise ValueError('Archive membership changed')
 manifests=[]
 for m in sorted(ARCHIVE.rglob('MANIFEST.json')):
  entries=json.loads(m.read_text())
  for name,v in entries.items():
   f=member(m.parent,name)
   if f.stat().st_size!=v['bytes'] or digest(f)!=v['sha256']:raise ValueError('Archived bytes changed: '+name)
  manifests.append({'path':str(m.relative_to(ARCHIVE)),'members':len(entries)})
 if len(expected)!=spec['file_count'] or len(manifests)!=spec['manifests']:raise ValueError('Archive counts differ')
 if digest(ROOT/'LICENSE')!=spec['license_sha256']:raise ValueError('Owner license changed')
 return {'files':len(expected),'manifests':manifests,'license_unchanged':True}

def check_reading()->int:
 for name,data in build_reading.expected().items():
  if (ROOT/name).read_bytes()!=data:raise ValueError('Generated page differs: '+name)
 return 3

def check_links()->int:
 count=0
 for f in sorted(ROOT.rglob('*')):
  if not f.is_file() or f.suffix not in ('.md','.txt'):continue
  if any(x in f.relative_to(ROOT).parts for x in ('archive','.git','.venv')):continue
  for raw in re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)',f.read_text()):
   target=raw.split('#',1)[0]
   if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
   resolved=(f.parent/target).resolve()
   if not resolved.is_relative_to(ROOT) or not resolved.exists():raise ValueError(f'Broken local link: {f}: {target}')
   count+=1
 return count

def new_output(raw:str)->Path:
 p=Path(raw).expanduser()
 if not p.is_absolute():raise ValueError('Use an absolute output directory')
 p=p.resolve()
 if p.exists() or p==ROOT or ROOT in p.parents:raise ValueError('Use a new directory outside the repository')
 return p

def numeric_only(rows:list)->bool:
 return all(e.get('kind')=='numeric' and type(e.get('reference')) is type(e.get('run'))
            and type(e.get('reference')) in (float,int)
            and math.isfinite(e['reference']) and math.isfinite(e['run']) for e in rows)

def git_value(*args):
 p=subprocess.run(['git','-C',str(ROOT),*args],text=True,capture_output=True)
 return p.stdout.strip() if p.returncode==0 else None

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--output-dir',required=True)
 ap.add_argument('--allow-numeric-report-differences',action='store_true')
 args=ap.parse_args();out=new_output(args.output_dir)
 before=inventory();archive=check_archive();pages=check_reading();links=check_links()
 out.mkdir(parents=True)
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
 with (out/'infrastructure.log').open('xb') as log:
  infra=subprocess.run([sys.executable,str(ROOT/'scripts/check_repository.py'),'--output',str(out/'infrastructure.json')],
                       cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=120)
 with (out/'scientific.log').open('xb') as log:
  result=subprocess.run([sys.executable,str(ARCHIVE/'verify.py'),'--output-dir',str(out/'scientific')],
                        cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=600)
 p=out/'scientific/receipt.json';science=json.loads(p.read_text()) if p.exists() else {}
 infra_data=json.loads((out/'infrastructure.json').read_text())
 differences=[]
 for suite in science.get('suites',[]):
  differences.extend(dict(e,suite=suite['suite']) for e in suite.get('differences',[]))
 assertions=(science.get('scientific_assertions_pass') is True and science.get('groups')==15
             and len(science.get('suites',[]))==3 and science.get('source_unchanged') is True)
 identical=science.get('canonical_reports_byte_identical') is True
 unchanged=inventory()==before
 reviewable=bool(differences) and numeric_only(differences)
 passed=(infra.returncode==0 and assertions and unchanged and
         (identical or (args.allow_numeric_report_differences and reviewable)))
 status='PASS' if passed and identical else ('PASS_REQUIRES_NUMERIC_REVIEW' if passed else 'FAIL')
 receipt={'status':status,'repository':'GoGoKo699/Quantum-Pump-State-Crossover',
          'commit':git_value('rev-parse','HEAD'),'tree':git_value('rev-parse','HEAD^{tree}'),
          'index_tree':git_value('write-tree'),'source_sha256':before,'source_files':len(before),
          'source_unchanged':unchanged,'archive':archive,'reading_pages':pages,'local_links':links,
          'infrastructure_tests':infra_data.get('tests_run'),'infrastructure_pass':infra.returncode==0,
          'scientific_groups':science.get('groups'),'scientific_assertions_pass':assertions,
          'canonical_reports_byte_identical':identical,'original_wrapper_returncode':result.returncode,
          'numeric_review_required':not identical,'allow_numeric_report_differences':args.allow_numeric_report_differences,
          'report_differences':differences,'maximum_numeric_absolute_difference':max((e.get('absolute_difference',0) for e in differences),default=0)}
 with (out/'verification.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
 print(json.dumps({k:v for k,v in receipt.items() if k not in ('source_sha256',)},indent=2))
 raise SystemExit(0 if passed else 1)
if __name__=='__main__':main()
