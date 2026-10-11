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
REPOSITORY='https://github.com/GoGoKo699/Quantum-Pump-State-Crossover'
SCIENTIFIC_SUITES=(
 ('consolidation','scripts/check_consolidation.py','verification/consolidation.json'),
 ('comparison','scripts/check_comparison.py','verification/comparison.json'),
 ('pilot','scripts/check_pilot.py','verification/pilot.json'),
)
PROTECTED_PATHS=frozenset(
 {'LICENSE','research/THEOREM.md','scripts/pump_model.py'}
 | {path for _,script,reference in SCIENTIFIC_SUITES for path in (script,reference)}
)
sys.dont_write_bytecode=True

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
 if p.is_absolute() or '..' in p.parts or '\\' in name:raise ValueError('Unsafe source path')
 f=base/p
 if f.is_symlink() or not f.resolve().is_relative_to(base.resolve()):raise ValueError('Escaping source path')
 return f

def check_integrity(root:Path=ROOT)->dict:
 """Verify the exact protected path set and every recorded source/report hash."""
 manifest=member(root,'verification/integrity.json')
 if not manifest.is_file():raise ValueError('Missing integrity manifest')
 spec=json.loads(manifest.read_text())
 if not isinstance(spec,dict) or spec.get('repository')!=REPOSITORY:
  raise ValueError('Integrity repository identity differs')
 entries=spec.get('files')
 if not isinstance(entries,dict) or set(entries)!=PROTECTED_PATHS:
  raise ValueError('Protected path membership differs')
 for name,expected in sorted(entries.items()):
  if not isinstance(expected,str) or re.fullmatch(r'[0-9a-f]{64}',expected) is None:
   raise ValueError('Invalid protected SHA-256: '+name)
  f=member(root,name)
  if not f.is_file():raise ValueError('Missing protected file: '+name)
  if digest(f)!=expected:raise ValueError('Protected bytes changed: '+name)
 return {'files':len(entries),'manifest':'verification/integrity.json',
         'manifest_sha256':digest(manifest),'protected_paths':sorted(entries)}

def check_links()->int:
 count=0
 for f in sorted(ROOT.rglob('*')):
  if not f.is_file() or f.suffix not in ('.md','.txt'):continue
  if any(x in f.relative_to(ROOT).parts for x in ('.git','.venv')):continue
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

def report_differences(reference, run, path=''):
 """Enumerate every changed value; never silently normalize a reference."""
 rows=[]
 if isinstance(reference,dict) and isinstance(run,dict):
  if reference.keys()!=run.keys():
   rows.append({'path':path,'kind':'keys','reference':list(reference),'run':list(run)})
  for key in sorted(reference.keys() & run.keys()):
   rows.extend(report_differences(reference[key],run[key],path+'/'+str(key)))
 elif isinstance(reference,list) and isinstance(run,list):
  if len(reference)!=len(run):
   rows.append({'path':path,'kind':'length','reference':len(reference),'run':len(run)})
  for i,(x,y) in enumerate(zip(reference,run)):
   rows.extend(report_differences(x,y,path+'/'+str(i)))
 elif reference!=run or type(reference) is not type(run):
  row={'path':path,'reference':reference,'run':run,'kind':'value'}
  if type(reference) in (int,float) and type(run) in (int,float):
   row.update(kind='numeric',absolute_difference=abs(reference-run))
  rows.append(row)
 return rows

def git_value(*args):
 p=subprocess.run(['git','-C',str(ROOT),*args],text=True,capture_output=True)
 return p.stdout.strip() if p.returncode==0 else None

def run_scientific(out:Path,env:dict)->dict:
 """Execute all three five-group suites against unchanged canonical reports."""
 before=inventory();out.mkdir()
 results=[]
 for name,script,canonical in SCIENTIFIC_SUITES:
  output=out/(name+'.json');reference=ROOT/canonical
  with (out/(name+'.log')).open('xb') as log:
   result=subprocess.run([sys.executable,str(ROOT/script),'--output',str(output)],
                         cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=180)
  item={'suite':name,'returncode':result.returncode,'script':script,
        'canonical':canonical,'report':output.name,'byte_identical':False}
  if output.is_file():
   data=json.loads(output.read_text());ref=json.loads(reference.read_text())
   item.update(status=data.get('status'),groups=data.get('groups'),
               byte_identical=output.read_bytes()==reference.read_bytes(),
               differences=report_differences(ref,data))
  else:
   item['differences']=[{'path':'','kind':'missing','reference':canonical,'run':None}]
  results.append(item)
 receipt={'scientific_assertions_pass':all(x['returncode']==0 and x.get('status')=='PASS'
                                         and x.get('groups')==5 for x in results),
          'canonical_reports_byte_identical':all(x['byte_identical'] for x in results),
          'source_unchanged':inventory()==before,
          'groups':sum(x.get('groups',0) for x in results),'source_sha256':before,'suites':results}
 with (out/'receipt.json').open('x') as f:
  json.dump(receipt,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
 return receipt

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--output-dir',required=True)
 ap.add_argument('--allow-numeric-report-differences',action='store_true')
 args=ap.parse_args();out=new_output(args.output_dir)
 before=inventory();integrity=check_integrity();links=check_links()
 out.mkdir(parents=True)
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
 with (out/'infrastructure.log').open('xb') as log:
  infra=subprocess.run([sys.executable,str(ROOT/'scripts/check_repository.py'),'--output',str(out/'infrastructure.json')],
                       cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=120)
 science=run_scientific(out/'scientific',env)
 with (out/'proof_review.log').open('xb') as log:
  review_run=subprocess.run([sys.executable,str(ROOT/'scripts/check_proof_review.py'),
                             '--output',str(out/'proof_review.json')],
                            cwd=ROOT,env=dict(env,PYTHONHASHSEED='0'),stdout=log,stderr=subprocess.STDOUT,timeout=120)
 review_path=out/'proof_review.json'
 review=json.loads(review_path.read_text()) if review_path.exists() else {}
 reference_path=ROOT/'verification/proof-review.json'
 reference=json.loads(reference_path.read_text())
 review_differences=report_differences(reference,review)
 review_identical=review_path.exists() and review_path.read_bytes()==reference_path.read_bytes()
 with (out/'manuscript_basis.log').open('xb') as log:
  manuscript_run=subprocess.run([sys.executable,str(ROOT/'scripts/check_manuscript_basis.py'),
                                 '--output',str(out/'manuscript_basis.json')],
                                cwd=ROOT,env=dict(env,PYTHONHASHSEED='0'),stdout=log,stderr=subprocess.STDOUT,timeout=120)
 manuscript_path=out/'manuscript_basis.json'
 manuscript=json.loads(manuscript_path.read_text()) if manuscript_path.exists() else {}
 manuscript_reference_path=ROOT/'verification/manuscript-basis.json'
 manuscript_reference=json.loads(manuscript_reference_path.read_text())
 manuscript_differences=report_differences(manuscript_reference,manuscript)
 manuscript_identical=(manuscript_path.exists() and
                       manuscript_path.read_bytes()==manuscript_reference_path.read_bytes())
 infra_data=json.loads((out/'infrastructure.json').read_text())
 differences=[]
 for suite in science.get('suites',[]):
  differences.extend(dict(e,suite=suite['suite']) for e in suite.get('differences',[]))
 differences.extend(dict(e,suite='proof_review') for e in review_differences)
 differences.extend(dict(e,suite='manuscript_basis') for e in manuscript_differences)
 assertions=(science.get('scientific_assertions_pass') is True and science.get('groups')==15
             and len(science.get('suites',[]))==3 and science.get('source_unchanged') is True
             and review_run.returncode==0 and review.get('status')=='PASS' and review.get('test_groups')==5
             and manuscript_run.returncode==0 and manuscript.get('status')=='PASS' and manuscript.get('test_groups')==5)
 identical=(science.get('canonical_reports_byte_identical') is True and review_identical
            and manuscript_identical)
 unchanged=inventory()==before
 reviewable=bool(differences) and numeric_only(differences)
 infrastructure_pass=(infra.returncode==0 and infra_data.get('status')=='PASS'
                      and infra_data.get('tests_run')==8)
 passed=(infrastructure_pass and assertions and unchanged and
         (identical or (args.allow_numeric_report_differences and reviewable)))
 status='PASS' if passed and identical else ('PASS_REQUIRES_NUMERIC_REVIEW' if passed else 'FAIL')
 receipt={'status':status,'repository':'GoGoKo699/Quantum-Pump-State-Crossover',
          'commit':git_value('rev-parse','HEAD'),'tree':git_value('rev-parse','HEAD^{tree}'),
          'index_tree':git_value('write-tree'),'source_sha256':before,'source_files':len(before),
          'source_unchanged':unchanged,'integrity':integrity,'local_links':links,
          'infrastructure_tests':infra_data.get('tests_run'),'infrastructure_pass':infrastructure_pass,
          'scientific_groups':science.get('groups',0)+review.get('test_groups',0)+manuscript.get('test_groups',0),
          'manuscript_basis_groups':manuscript.get('test_groups'),'manuscript_basis_returncode':manuscript_run.returncode,
          'manuscript_basis_reference':'verification/manuscript-basis.json',
          'manuscript_basis_byte_identical':manuscript_identical,
          'core_scientific_groups':science.get('groups'),'proof_review_groups':review.get('test_groups'),
          'proof_review_returncode':review_run.returncode,'proof_review_hash_seed':'0','proof_review_reference':'verification/proof-review.json',
          'proof_review_byte_identical':review_identical,'scientific_assertions_pass':assertions,
          'canonical_reports_byte_identical':identical,'scientific_receipt':'scientific/receipt.json',
          'numeric_review_required':not identical,'allow_numeric_report_differences':args.allow_numeric_report_differences,
          'report_differences':differences,'maximum_numeric_absolute_difference':max((e.get('absolute_difference',0) for e in differences),default=0)}
 with (out/'verification.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
 print(json.dumps({k:v for k,v in receipt.items() if k not in ('source_sha256',)},indent=2))
 raise SystemExit(0 if passed else 1)
if __name__=='__main__':main()
