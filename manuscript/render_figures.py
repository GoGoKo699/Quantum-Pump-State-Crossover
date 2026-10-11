#!/usr/bin/env python3
"""Render two analytical manuscript figures and their data, without simulations.

Run into a new output directory. The SVGs use the default Matplotlib color cycle;
all curves are explicit limiting formulas or evaluations of proven finite bounds.
"""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
import math
import numpy as np
from scipy.special import erfcx
import matplotlib
import matplotlib.pyplot as plt


def P(x):
    v=np.asarray(x,float);out=np.ones_like(v)
    use=v>0
    out[use]=np.sqrt(np.pi)*erfcx(1/(2*v[use]))/(2*v[use])
    return out


def write_csv(path,columns,rows):
    with path.open('x',newline='') as stream:
        w=csv.writer(stream,lineterminator='\n');w.writerow(columns)
        w.writerows([[format(float(x),'.17g') for x in row] for row in rows])


def save_svg(fig, path):
    fig.savefig(path,metadata={'Date':None})
    # Preserve the renderer's vectors and labels; normalize line-end whitespace.
    path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output-dir',type=Path,required=True)
    p.add_argument('--show',action='store_true')
    args=p.parse_args();out=args.output_dir.resolve()
    if out.exists():p.error('Refusing to overwrite figure evidence.')
    out.mkdir(parents=True)
    matplotlib.rcParams['svg.fonttype']='none'
    matplotlib.rcParams['svg.hashsalt']='Quantum-Pump-State-Crossover-manuscript'

    lam=np.linspace(0,3,151);pur=P(lam);fid=P(lam/np.sqrt(2))
    write_csv(out/'crossover.csv',['lambda','limiting_purity','limiting_squared_TMSV_fidelity'],zip(lam,pur,fid))
    fig,ax=plt.subplots(figsize=(7.2,4.6))
    ax.plot(lam,pur,label='Pump / joint-output purity',linewidth=2)
    ax.plot(lam,fid,label='Squared TMSV fidelity',linewidth=2,linestyle='--')
    ax.set(xlabel=r'Crossover coordinate $\lambda$',ylabel='Limiting value',xlim=(0,3),ylim=(0,1.04))
    ax.set_title('Accurate photon counts coexist with loss of joint-state purity')
    ax.legend(frameon=False,loc='upper right');ax.grid(alpha=.2)
    fig.text(.13,.025,'Fixed-crossover large-pump limit; count-distribution error tends to zero.',fontsize=9)
    fig.tight_layout(rect=(0,.055,1,1));save_svg(fig,out/'crossover.svg')
    if args.show:plt.show()
    plt.close(fig)

    logN=np.linspace(8,32,121);alpha=10**(logN/2);lam=alpha**.25
    r=.5*np.log1p(8*alpha*lam)
    eps=np.sqrt(2+48*lam**2+480*lam**4)/(8*alpha)
    eps+=r*np.sqrt(1+16*lam**2+384*lam**4)/(2*alpha)
    d=(np.sqrt(2)+np.exp(-2*r)*np.sqrt(2+48*lam**2+480*lam**4))/(8*alpha)
    pur=P(lam);pure_lower=np.maximum(0,1-np.sqrt(np.minimum(1,pur+4*eps)))
    count_upper=np.minimum(1,eps+d)
    gaussian_lower=np.maximum(0,np.exp(-1/lam**2)/45-eps)
    depletion_upper=np.exp(r+alpha**2*np.expm1(r/alpha**2))/(4*alpha**2)
    write_csv(out/'growing_window.csv',
              ['log10_N','lambda','r','epsilon','eta','all_pure_distance_lower',
               'count_TV_upper','single_Gaussian_distance_lower','fractional_depletion_upper'],
              zip(logN,lam,r,eps,eps+d,pure_lower,count_upper,gaussian_lower,depletion_upper))
    fig,ax=plt.subplots(figsize=(7.2,4.6))
    ax.plot(logN,pure_lower,label='Distance from any pure state: lower bound',linewidth=2)
    ax.plot(logN,count_upper,label='Pair-count error: upper bound',linewidth=2,linestyle='--')
    ax.set(xlabel=r'Initial brightness $\log_{10}N$',ylabel='Trace / total-variation distance',
           xlim=(8,32),ylim=(-.025,1.045))
    ax.set_title(r'Controlled separation along $\lambda=N^{1/8}$')
    ax.legend(frameon=False,loc='center right');ax.grid(alpha=.2)
    fig.text(.13,.025,'Proven-inequality evaluations; no high-photon-number simulation or device model.',fontsize=9)
    fig.tight_layout(rect=(0,.055,1,1));save_svg(fig,out/'growing_window.svg')
    if args.show:plt.show()
    plt.close(fig)
    with (out/'generation.json').open('x') as f:
        json.dump({'calculation':'Explicit formulas only; no dynamical data or curve fitting.',
                   'matplotlib_version':matplotlib.__version__,'numpy_version':np.__version__,
                   'figures':['crossover.svg','growing_window.svg'],
                   'data':['crossover.csv','growing_window.csv'],
                   'source':'research/THEOREM.md and research/VALIDITY_WINDOW.md'},f,indent=2,sort_keys=True)
        f.write('\n')
    print('Created two SVG figures and their numerical data in',out)

if __name__=='__main__':main()
