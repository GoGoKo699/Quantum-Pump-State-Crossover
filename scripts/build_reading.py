#!/usr/bin/env python3
"""Generate the theorem from its immutable scientific source."""
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
]
SUBSTITUTIONS={
 'THEOREM.md':[
  ('This section is a direct consequence of the state theorem, derived in the present consolidation.',
   'This section is a direct consequence of the state theorem.'),
  ('Source details and current reading boundaries are in SOURCES.md and REVIEW.md. Full previous proofs and numerical records remain unchanged under prior/.',
   'See [sources](SOURCES.md) for attribution and the [proof map](PROOF_MAP.md) for the supporting derivations.'),
  ('This Hamiltonian and preparation are the established nondegenerate model in Chinni–Quesada [CQ], not a new physical model.',
   'This Hamiltonian and preparation are the established nondegenerate model in Chinni–Quesada [CQ].'),
  ('the new quadrature result is deliberately formulated', 'the quadrature result is formulated'),
  ('There is no claim that the physical output state converges to a single finite-energy state as its mean energy increases.',
   'The comparison follows a brightness-dependent target whose mean energy increases.'),
  ('Equation (6) is a state approximation, not an exact number-conserving ansatz or a new Hamiltonian. In particular its individual coherent branches are not exact conserved-number sectors.',
   'Equation (6) approximates the state in norm. Its individual coherent branches are not exact conserved-number sectors.'),
  ('This is a lower bound supplied by one bounded statistic, not an optimal discrimination probability or an entanglement witness.',
   'This lower bound is supplied by one bounded statistic.'),
  ('No claim that this bound is sharp is made. ', ''),
  ('The pump marginal is a positive coherent-state mixture.',
   'The limiting displaced pump marginal is a positive coherent-state mixture.'),
  ('At the same time, (11) proves distance to the convex Gaussian hull tends to zero. Equations (19)–(20) must not be advertised as a witness of being outside that hull, a Wigner-negativity result, or a metrological advantage. Characteristic functions distinguishing Gaussian from non-Gaussian laws are elementary; the new content is their exact limiting form and error control for this dynamical crossover.',
   'At the same time, (11) proves distance to the convex Gaussian hull tends to zero. Equations (19)–(20) distinguish individual Gaussian states from their mixtures, with an explicit limiting characteristic function and error bound.'),
  ('Likewise, the external reference must have the phase stability and resolution required for the specified quadrature measurement. Keeping and reusing the correlated pump is a different operation and can reverse the original unitary [F18]. The result claims no free phase reference, fixed detector tolerance, or validated experimental operating window.',
   'The external reference must have the phase stability and resolution required for the specified quadrature measurement. Keeping and reusing the correlated pump is a different operation and can reverse the original unitary [F18].'),
  ('## 8. Interpretation and contribution boundary', '## 8. Interpretation'),
  ('The consolidated conclusion is a controlled separation of validity criteria.',
   'The result is a controlled separation of validity criteria.'),
  ('The model, pump-induced quantum corrections, logarithmic squeezing scales, phase uncertainty affecting squeezed quadratures, Gaussian interaction frames, and energy-sector coherent-amplitude shifts have direct antecedents [CQ,HS,GIF,KFD,HZ]. The candidate contribution is the uniform nondegenerate crossover-state theorem, its measurement-dependent consequences, and fixed-purity first-crossing law. It is not the discovery that pumps are quantum, the first squeezing limit, or the first appearance of non-Gaussianity.',
   'The model, pump-induced quantum corrections, logarithmic squeezing scales, phase uncertainty affecting squeezed quadratures, Gaussian interaction frames, and energy-sector coherent-amplitude shifts have direct antecedents [CQ,HS,GIF,KFD,HZ]. The theorem gives a uniform nondegenerate crossover-state approximation, its measurement-dependent consequences, and a fixed-purity first-crossing law.'),
  ('The Hamiltonian is closed, resonant, and three-mode. Increasing N at fixed g need not preserve the approximations behind a particular optical implementation. Keeping g sqrt(N) fixed lengthens the physical crossover time logarithmically, allowing losses to matter. Those implementation questions are not answered by the theorem, and no experimental resource advantage is inferred from it.',
   'The Hamiltonian is closed, resonant, and three-mode. The physical crossover time depends on the coupling convention: keeping g sqrt(N) fixed makes it grow logarithmically with N.')]
}
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
  footer='\n\n---\n\n[Tutorial bridge](TUTORIAL_BRIDGE.md) · [Validity window](VALIDITY_WINDOW.md) · [Sources](SOURCES.md) · [Reproducibility](../REPRODUCIBILITY.md)\n'
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
