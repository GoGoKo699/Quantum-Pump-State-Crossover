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
import build_reading
class Checks(unittest.TestCase):
 def test_01_archive_and_license(self):
  data=verify.check_archive();self.assertEqual(data['files'],60)
  self.assertEqual([x['members'] for x in data['manifests']],[59,32,12])
  b=(ROOT/'LICENSE').read_bytes()
  self.assertEqual(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'e17a781bf47c4aadf18b68fc593846a1193b86c1')
 def test_02_generated_reading(self):
  self.assertEqual(build_reading.expected(),build_reading.expected());self.assertEqual(verify.check_reading(),3)
  ledger=json.loads((ROOT/'provenance/READING.json').read_text())
  self.assertGreater(sum(x['display_equations'] for x in ledger),30)
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
 def test_06_chat_and_contact(self):
  self.assertIn('continues in the existing Chat',(ROOT/'CURRENT.md').read_text())
  for n in ('README.md','llms.txt'):
   t=(ROOT/n).read_text();self.assertIn('Purpose and contact',t);self.assertIn('mailto:gogoko699@gmail.com',t)
  self.assertIn('convex Gaussian hull',(ROOT/'research/CLAIMS.md').read_text())
 def test_07_read_only_ci(self):
  t=(ROOT/'.github/workflows/verify.yml').read_text()
  for marker in ('contents: read','persist-credentials: false','github.event.pull_request.head.sha || github.sha','if: always()'):self.assertIn(marker,t)
  for bad in ('pull_request_target:','contents: write','git push','GITHUB_TOKEN:'):self.assertNotIn(bad,t)
  uses=re.findall(r'uses: ([^\s#]+)',t);self.assertEqual(len(uses),3)
  self.assertTrue(all(re.fullmatch(r'actions/[a-z-]+@[0-9a-f]{40}',x) for x in uses))
 def test_08_scope_of_import(self):
  d=json.loads((ROOT/'provenance/IMPORT.json').read_text())
  self.assertEqual(d['repository'],'GoGoKo699/Quantum-Pump-State-Crossover')
  self.assertEqual(d['package_sha256'],'944bfc315fe033c3951333638cbdfb229c7c3581b42ca9c49dc85af4b499f802')
  self.assertFalse(list((ROOT/'archive').rglob('*.pdf')))
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
 if out.exists() or out==ROOT or ROOT in out.parents:p.error('Use a new report outside the repository')
 r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
 out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('x') as f:json.dump({'status':'PASS' if r.wasSuccessful() else 'FAIL','tests_run':r.testsRun,'failures':len(r.failures),'errors':len(r.errors)},f,indent=2,sort_keys=True);f.write('\n')
 raise SystemExit(0 if r.wasSuccessful() else 1)
if __name__=='__main__':main()
