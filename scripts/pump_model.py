"""Exact-frame diagnostics for a coherent-pump trilinear interaction.

No previous project's source is imported. The finite matrices are diagnostic
truncations; the large-amplitude claim is proved separately by Duhamel bounds.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.special import erfcx, gammaln
from scipy.sparse import diags, kron, csr_matrix
from scipy.sparse.linalg import expm_multiply


def purity_limit(lam: float) -> float:
    if lam < 0: raise ValueError('nonnegative crossover coordinate required')
    if lam == 0: return 1.0
    return float(np.sqrt(np.pi)*erfcx(1/(2*lam))/(2*lam))


def time_gain(alpha: float, lam: float) -> tuple[float,float]:
    if alpha <= 0 or lam < 0: raise ValueError('alpha>0, lambda>=0 required')
    r=float(np.log1p(8*alpha*lam)/2)
    return r,r/alpha


def norm_error_bound(alpha: float, lam: float) -> float:
    r,_=time_gain(alpha,lam)
    def ell(u): return np.expm1(2*u)/(8*alpha)
    def rem(u):
        x=ell(u)
        a=np.sqrt(2+48*x*x+480*x**4)
        b=np.sqrt(1+16*x*x+384*x**4)
        return np.exp(-2*u)*a/(4*alpha)+b/(2*alpha)
    return float(quad(rem,0,r,epsabs=1e-13,epsrel=1e-12)[0])


def depletion_fraction_upper(alpha: float, lam: float) -> float:
    r,_=time_gain(alpha,lam)
    return float(np.exp(r+alpha*alpha*np.expm1(r/(alpha*alpha)))/(4*alpha*alpha))


def operators(npump: int, npair: int):
    if npump<4 or npair<4:raise ValueError('cutoffs at least four')
    c=diags(np.sqrt(np.arange(1,npump)),1,shape=(npump,npump),format='csr')
    kp=diags(np.arange(1,npair,dtype=float),-1,shape=(npair,npair),format='csr')
    km=kp.T.tocsr();q=diags(2*np.arange(npair,dtype=float)+1,format='csr')
    p=c-c.T; t=c+c.T;r=kp+km+q;l=kp+km-q;d=kp-km
    return c,kp,km,q,p,t,r,l,d


def evolve_frame(alpha: float, lam: float, npump=36, npair=80,
                 rtol=2e-10, atol=2e-12) -> dict:
    rf,tau=time_gain(alpha,lam)
    c,kp,km,q,p,t,r,l,d=operators(npump,npair)
    A=kron(p,r,format='csr');B=kron(p,l,format='csr');C=kron(t,d,format='csr')
    initial=np.zeros(npump*npair);initial[0]=1.
    def rhs(u,y):return (np.exp(2*u)*(A@y)+np.exp(-2*u)*(B@y)+2*(C@y))/(4*alpha)
    sol=solve_ivp(rhs,(0,rf),initial,method='DOP853',rtol=rtol,atol=atol)
    if not sol.success:raise RuntimeError(sol.message)
    psi=sol.y[:,-1].reshape(npump,npair)
    rho=psi@psi.T
    nd=float(np.sum(np.arange(npump)*np.diag(rho)))
    cd=float(np.trace(c@rho))
    # Do not subtract two numbers of order alpha**2 to obtain depletion.
    depletion=-(2*alpha*cd+nd)/(alpha*alpha)
    target=expm_multiply(lam*A,initial).reshape(npump,npair)
    return {'alpha':alpha,'lambda':lam,'gain_r':rf,'tau':tau,
            'npump':npump,'npair':npair,'retained_amplitudes':npump*npair,
            'purity':float(np.sum(rho*rho)), 'limit_purity':purity_limit(lam),
            'depletion_fraction':depletion,'depletion_upper':depletion_fraction_upper(alpha,lam),
            'state_norm_error_to_limit_truncation':float(np.linalg.norm(psi-target)),
            'analytic_state_error_bound':norm_error_bound(alpha,lam),
            'norm':float(np.linalg.norm(psi)),
            'last_four_pump_levels':float(np.sum(psi[-4:,:]**2)),
            'last_four_pair_levels':float(np.sum(psi[:,-4:]**2)),
            'function_evaluations':sol.nfev,'rho_p_displaced':rho,'state':psi}


def evolve_number_sectors(alpha: float, tau: float, mmax: int,
                          rtol=2e-11,atol=2e-13) -> dict:
    """Full pair extent in each conserved sector, only initial Poisson tail omitted."""
    ms=np.arange(mmax+1);ks=np.arange(mmax)
    pweight=np.exp(-alpha*alpha+2*ms*np.log(alpha)-gammaln(ms+1))
    initial=np.zeros((mmax+1,mmax+1));initial[:,0]=np.sqrt(pweight)
    couplings=(ks[None,:]+1)*np.sqrt(np.maximum(ms[:,None]-ks[None,:],0))
    def rhs(t,y):
        state=y.reshape(mmax+1,mmax+1);out=np.zeros_like(state)
        out[:,1:]+=couplings*state[:,:-1]
        out[:,:-1]-=couplings*state[:,1:]
        return out.ravel()
    sol=solve_ivp(rhs,(0,tau),initial.ravel(),method='DOP853',rtol=rtol,atol=atol)
    if not sol.success:raise RuntimeError(sol.message)
    v=sol.y[:,-1].reshape(mmax+1,mmax+1)
    psi=np.zeros_like(v)
    for m in range(mmax+1):
        kk=np.arange(m+1);psi[m-kk,kk]=v[m,kk]
    rho=psi@psi.T
    number=float(np.sum(np.arange(mmax+1)*np.sum(psi*psi,axis=0)))
    return {'purity':float(np.sum(rho*rho)),'depletion_fraction':number/(alpha*alpha),
            'retained_probability':float(np.sum(pweight)), 'sector_cutoff':mmax,
            'state':psi,'rho_p':rho,'function_evaluations':sol.nfev}
