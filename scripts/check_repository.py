#!/usr/bin/env python3
"""Infrastructure regressions; original scientific tests remain unchanged."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import verify
class Checks(unittest.TestCase):
 def test_01_integrity_and_license(self):
  data=verify.check_integrity();self.assertEqual(data['files'],9)
  self.assertEqual(set(data['protected_paths']),verify.PROTECTED_PATHS)
  b=(ROOT/'LICENSE').read_bytes()
  self.assertEqual(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'e17a781bf47c4aadf18b68fc593846a1193b86c1')
 def test_02_integrity_rejects_tampering(self):
  with tempfile.TemporaryDirectory() as name:
   root=Path(name);entries={}
   for relative in sorted(verify.PROTECTED_PATHS):
    f=root/relative;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(relative+'\n')
    entries[relative]=verify.digest(f)
   manifest=root/'verification/integrity.json'
   def write_manifest(files=entries,repository=verify.REPOSITORY):
    manifest.write_text(json.dumps({'repository':repository,'files':files}))
   write_manifest();self.assertEqual(verify.check_integrity(root)['files'],9)
   target=root/'scripts/check_pilot.py';saved=target.read_bytes()
   target.write_bytes(saved+b'# changed\n')
   with self.assertRaisesRegex(ValueError,'Protected bytes changed'):verify.check_integrity(root)
   target.unlink()
   with self.assertRaisesRegex(ValueError,'Missing protected file'):verify.check_integrity(root)
   target.write_bytes(saved)
   for files in ({k:v for k,v in entries.items() if k!='LICENSE'},
                 dict(entries,unexpected='0'*64)):
    write_manifest(files)
    with self.assertRaisesRegex(ValueError,'membership'):verify.check_integrity(root)
   write_manifest(dict(entries,LICENSE='not-a-sha256'))
   with self.assertRaisesRegex(ValueError,'Invalid protected SHA-256'):verify.check_integrity(root)
   write_manifest(repository='https://github.com/example/another-project')
   with self.assertRaisesRegex(ValueError,'repository identity'):verify.check_integrity(root)
   manifest.unlink()
   with self.assertRaisesRegex(ValueError,'Missing integrity manifest'):verify.check_integrity(root)
 def test_03_current_links(self):self.assertGreaterEqual(verify.check_links(),25)
 def test_04_preservation_and_paths(self):
  with tempfile.TemporaryDirectory() as name:
   root=Path(name);f=root/'x';f.write_text('before');before=verify.inventory(root)
   f.write_text('after');self.assertNotEqual(before,verify.inventory(root))
   for path in ('../escape','/absolute','a/../../b','a\\b'):
    with self.assertRaises(ValueError):verify.member(root,path)
   (root/'link').symlink_to(f)
   with self.assertRaises(ValueError):verify.inventory(root)
 def test_05_output_and_difference_policy(self):
  for p in (str(ROOT),str(ROOT/'results'),'relative/results'):
   with self.assertRaises(ValueError):verify.new_output(p)
  self.assertTrue(verify.numeric_only([{'kind':'numeric','reference':1.,'run':1.00000001}]))
  for a,b in ((1,1.),(True,False),('1','2'),(float('nan'),1.)):
   self.assertFalse(verify.numeric_only([{'kind':'numeric','reference':a,'run':b}]))
  self.assertFalse(verify.numeric_only([{'kind':'keys'}]))
  rows=verify.report_differences({'a':[1.,2.],'b':{'c':3}},
                                 {'a':[1.1,2.2],'b':{'c':4}})
  self.assertEqual([x['path'] for x in rows],['/a/0','/a/1','/b/c'])
  self.assertTrue(verify.numeric_only(rows))
  self.assertFalse(verify.numeric_only(verify.report_differences({'a':1.},{'a':1.1,'b':2.})))
 def test_06_contact_and_scope(self):
  for n in ('README.md','llms.txt'):
   t=(ROOT/n).read_text();self.assertIn('Purpose and contact',t);self.assertIn('mailto:gogoko699@gmail.com',t)
  self.assertIn('convex Gaussian hull',(ROOT/'research/CLAIMS.md').read_text())
 def test_07_read_only_ci(self):
  t=(ROOT/'.github/workflows/verify.yml').read_text()
  for marker in ('contents: read','persist-credentials: false','github.event.pull_request.head.sha || github.sha','if: always()'):self.assertIn(marker,t)
  for bad in ('pull_request_target:','contents: write','git push','GITHUB_TOKEN:'):self.assertNotIn(bad,t)
  uses=re.findall(r'uses: ([^\s#]+)',t);self.assertEqual(len(uses),3)
  self.assertTrue(all(re.fullmatch(r'actions/[a-z-]+@[0-9a-f]{40}',x) for x in uses))
 def test_08_scientific_suite_inventory(self):
  self.assertEqual([name for name,_,_ in verify.SCIENTIFIC_SUITES],
                   ['consolidation','comparison','pilot'])
  for name,script,canonical in verify.SCIENTIFIC_SUITES:
   self.assertEqual(script,'scripts/check_'+name+'.py')
   self.assertEqual(canonical,'verification/'+name+'.json')
   self.assertIn(script,verify.PROTECTED_PATHS);self.assertIn(canonical,verify.PROTECTED_PATHS)
   data=json.loads((ROOT/canonical).read_text())
   self.assertEqual(data.get('status'),'PASS');self.assertEqual(data.get('groups'),5)
  for filename in ('proof-review.json','manuscript-basis.json'):
   data=json.loads((ROOT/'verification'/filename).read_text())
   self.assertEqual(data.get('status'),'PASS');self.assertEqual(data.get('test_groups'),5)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
 if out.exists() or out==ROOT or ROOT in out.parents:p.error('Use a new report outside the repository')
 r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
 out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('x') as f:json.dump({'status':'PASS' if r.wasSuccessful() else 'FAIL','tests_run':r.testsRun,'failures':len(r.failures),'errors':len(r.errors)},f,indent=2,sort_keys=True);f.write('\n')
 raise SystemExit(0 if r.wasSuccessful() else 1)
if __name__=='__main__':main()
