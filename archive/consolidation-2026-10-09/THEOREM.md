# Correct photon counts, non-Gaussian joint state

9 October 2026. A self-contained account of the coherent-pump crossover in the closed nondegenerate trilinear model. Sections 1–6 consolidate the two preserved research notes without changing their equations. Section 7 derives a phase-referenced quadrature consequence and a distance bound from every single Gaussian state. These are author-side proofs, not external peer review or a priority determination. No repository was accessed.

## 1. Model, preparation, and order of limits

There are three bosonic modes: pump c, signal a, and idler b. Use

$$
H=i\hbar g(ca^\dagger b^\dagger-c^\dagger ab),\quad g>0,\qquad
|\Psi(0)\rangle=|\alpha\rangle_c|0,0\rangle_{ab},\quad \alpha>0.
$$

Set N=alpha^2, tau=gt, and r=alpha*tau. This Hamiltonian and preparation are the established nondegenerate model in Chinni–Quesada [CQ], not a new physical model. The conserved quantities are n_c+n_a and n_c+n_b; the exact state remains globally pure and satisfies n_a=n_b. The nominal deterministic-pump approximation replaces c by alpha and generates

$$
|{\rm TMSV}_r\rangle=S(r)|00\rangle
=\sum_{k\ge0}s_k|k,k\rangle,\qquad
S(r)=e^{r(a^\dagger b^\dagger-ab)},\quad
s_k=\operatorname{sech}r\,\tanh^k r.
$$

Fix a finite crossover coordinate lambda>=0 and let alpha increase at

$$
r=r_\alpha(\lambda)=\frac12\ln(1+8\alpha\lambda),\qquad
\tau_\alpha(\lambda)=r_\alpha(\lambda)/\alpha. \tag{1}
$$

All uniformity statements below concern lambda in an arbitrary fixed compact interval [0,Lambda]. The target TMSV and some measurement resolutions depend on alpha. There is no claim that the physical output state converges to a single finite-energy state as its mean energy increases. Fixed gain, fixed physical time, and fixed depletion are different limits.

## 2. Two controlled state descriptions

Define a pump displacement and remove nominal signal squeezing:

$$
|\Psi_\alpha(r)\rangle=D_c(\alpha)S(r)|\psi_\alpha(r)\rangle.
$$

Call the displaced pump annihilator d and define

$$
p=d-d^\dagger,\quad T=d+d^\dagger,\quad
Q=1+n_a+n_b,\quad C=a^\dagger b^\dagger+ab,
$$
$$
R=Q+C,\quad L=C-Q,\quad A=a^\dagger b^\dagger-ab.
$$

The complete residual state has the limit

$$
|\chi_\lambda\rangle=e^{\lambda pR}|000\rangle. \tag{2}
$$

Define the explicit bounds

$$
\epsilon_\alpha(\lambda)=
\frac{\sqrt{2+48\lambda^2+480\lambda^4}}{8\alpha}
+\frac{r_\alpha(\lambda)\sqrt{1+16\lambda^2+384\lambda^4}}{2\alpha}, \tag{3}
$$
$$
d_\alpha(\lambda)=
\frac{\sqrt2+e^{-2r_\alpha(\lambda)}\sqrt{2+48\lambda^2+480\lambda^4}}{8\alpha},
\qquad \eta_\alpha=\epsilon_\alpha+d_\alpha. \tag{4}
$$

Then

$$
\|\psi_\alpha(r_\alpha)-\chi_\lambda\|\le\epsilon_\alpha,
\tag{5}
$$

and the normalized physical-frame approximation

$$
|\Phi_{\alpha,r}\rangle
=\sum_{k\ge0}s_k\,|\alpha-k/(2\alpha)\rangle_c|k,k\rangle_{ab}
\tag{6}
$$

obeys

$$
\|\Psi_\alpha(r_\alpha)-\Phi_{\alpha,r_\alpha}\|\le\eta_\alpha
=O_\Lambda(\ln\alpha/\alpha). \tag{7}
$$

Both bounds hold for the exact infinite-dimensional evolution. They can exceed a trivial norm bound at small alpha, without affecting their validity or asymptotic use. Equation (6) is a state approximation, not an exact number-conserving ansatz or a new Hamiltonian. In particular its individual coherent branches are not exact conserved-number sectors.

### 2.1 Proof of the residual-state estimate

The displaced and unsqueezed state obeys the exact anti-Hermitian generator

$$
G_\alpha(u)=\frac{e^{2u}}{4\alpha}pR
+\frac{e^{-2u}}{4\alpha}pL+\frac1{2\alpha}TA. \tag{8}
$$

This follows from S(u)^dagger a S(u)=a cosh(u)+b^dagger sinh(u). No pump term is dropped in (8). The first term integrates to V(u)=exp[ell(u)pR], where ell(u)=(exp(2u)-1)/(8alpha). The exact commutators are

$$
[R,A]=2R,\quad[R,L]=4A,\quad[p,T]=2,
$$
$$
V^\dagger TV=T-2\ell R,\quad
V^\dagger AV=A-2\ell pR,\quad
V^\dagger LV=L-4\ell pA+4\ell^2p^2R.
$$

Their vacuum actions give the finite polynomial norms

$$
\|p(L-4\ell pA+4\ell^2p^2R)|0\rangle\|^2
=2+48\ell^2+480\ell^4,
$$
$$
\|(T-2\ell R)(A-2\ell pR)|0\rangle\|^2
=1+16\ell^2+384\ell^4.
$$

Duhamel's identity therefore bounds the state difference by

$$
\int_0^r\left[
\frac{e^{-2u}}{4\alpha}\sqrt{2+48\ell(u)^2+480\ell(u)^4}
+\frac1{2\alpha}\sqrt{1+16\ell(u)^2+384\ell(u)^4}
\right]du. \tag{9}
$$

The exact propagator to the left of the remainder is unitary. Since 0<=ell(u)<=lambda at (1), integration gives (3). This retains the finite exp(2r)/alpha effect to all orders and does not extrapolate a fixed-degree Taylor polynomial in tau.

### 2.2 Proof of the number-marking approximation

On the equal-pair subspace,

$$
B_\alpha=\frac{S(-r)n_aS(r)}{2\alpha}
=\frac{e^{2r}R-e^{-2r}L-2I}{8\alpha}.
$$

Removing D_c(alpha)S(r) from (6) gives exp(p B_alpha)|000>. At (1),

$$
B_\alpha-\lambda R=\frac{R-e^{-2r}L-2I}{8\alpha}.
$$

Apply Duhamel along exp(s lambda pR), 0<=s<=1. The required norms are the first polynomial above with ell=s lambda, and ||p(R-2I)|0>||=sqrt2. This proves (4) as the additional state distance. The triangle inequality gives (7).

### 2.3 Domains and unbounded quantities

The original Hamiltonian is the self-adjoint direct sum of finite matrices in the simultaneous eigenspaces of n_c+n_a and n_c+n_b. The positive conserved number 2n_c+n_a+n_b is comparable to total occupation. Exact evolution consequently preserves every polynomial occupation-domain norm of the initial coherent/vacuum state. Displacements and finite squeezers preserve the oscillator Schwartz space. In suitable quadrature coordinates the leading evolution multiplies a Gaussian by a cubic phase and also preserves that space at finite lambda. Thus the polynomial actions used in the differentiated interaction frames have finite norms, and the Duhamel identities follow on this common domain by approximation. No uniformly bounded cubic operator or convergent infinite Dyson series is assumed.

Norm and trace-distance estimates control bounded measurements. They do not automatically control photon-number or quadrature moments. The energy conclusion below has a separate argument; the new quadrature result is deliberately formulated as a probability-law and bounded-characteristic-function statement.

## 3. Reduced state: exact counts and a vanishing phase width

Tracing the pump from (6) gives

$$
\sigma_{ab}(\alpha,r)=
\sum_{k,l\ge0}s_ks_l e^{-(k-l)^2/(8N)}|k,k\rangle\langle l,l|,
\qquad \tfrac12\|\rho_{ab}-\sigma_{ab}\|_1\le\eta_\alpha. \tag{10}
$$

Equivalently,

$$
\sigma_{ab}=\mathbb E_\vartheta\left[
 e^{i\vartheta n_a}|{\rm TMSV}_r\rangle\langle{\rm TMSV}_r|e^{-i\vartheta n_a}
\right],\qquad
\vartheta\sim\mathcal N(0,1/(4N)). \tag{11}
$$

This is an exact representation of the approximating reduced state. It is not technical noise added to the pure initial pump, not a Markovian phase-diffusion law, and not an approximation for arbitrary inputs. Typical pair-number differences are O(sqrt(N)); the vanishing phase standard deviation can therefore cause finite coherence damping.

The diagonal of (10) is exactly the nominal geometric distribution

$$
p_k=(1-q)q^k,\qquad q=\tanh^2r.
$$

Contractivity under measurement gives total variation at most eta_alpha between the entire exact pair-count distribution and p_k. Each individual output marginal is number diagonal, so each approaches its nominal thermal state in trace distance too.

On |k,k>, exp(i theta n_a)=exp[i theta(n_a+n_b)/2]. Hence every POVM commuting with total output photon number has identical statistics on sigma_ab and the pure TMSV. The exact state's statistics differ by at most eta_alpha, uniformly over this whole measurement class. Passive processing with vacuum ancillary modes followed by photon counting is one example. A coherent phase reference, active processing, multiple sources, or reuse of the correlated pump is not covered by this invariance argument.

## 4. Energy transfer without assuming moment convergence

In an initial pump Fock sector m the exact amplitudes occupy |m-k,k,k> with off-diagonal coefficients (k+1)sqrt(m-k). Cauchy–Schwarz bounds the mean pair number by

$$
\partial_\tau\bar k_m\le2\sqrt m\sqrt{\bar k_m(\bar k_m+1)},
\qquad \bar k_m\le\sinh^2(\sqrt m\tau).
$$

The comparison at initial value zero follows by positive regularization. The bound remains valid even when the true derivative is negative. For a coherent initial pump, number expectations average these sectors with Poisson weights. Using sqrt(m)<=(m+alpha^2)/(2alpha) and the Poisson generating function gives

$$
\frac{\langle n_a\rangle}{\alpha^2}
\le\frac{1}{4\alpha^2}
\exp\left[r+\alpha^2(e^{r/\alpha^2}-1)\right]. \tag{12}
$$

At (1), its limsup after multiplication by alpha is at most 2lambda. Meanwhile (10) transfers the nominal weak limit k/alpha => 2lambda U, U exponential of mean one, to the exact counts. Expectations of bounded truncations min(k/alpha,M), followed by M increasing, give the matching liminf. For fixed lambda>0,

$$
\boxed{\langle n_a\rangle\sim2\lambda\sqrt N,\qquad
\frac{N-\langle n_c\rangle}{N}\sim\frac{2\lambda}{\sqrt N}.} \tag{13}
$$

The absolute transferred energy grows. Only its fraction vanishes. Agreement of a distribution in total variation would not alone have justified (13).

## 5. Purity and the failure of the pure-state prediction

With quadratures x=(a+a^dagger)/sqrt2 and p=(a-a^dagger)/(i sqrt2), define x_+=(x_a+x_b)/sqrt2 and p_-=(p_a-p_b)/sqrt2. Then R=x_+^2+p_-^2. These commuting vacuum quadratures are independent normal variables of variance 1/2, so R has density e^(-u), u>=0. Equation (2) yields the displaced pump marginal

$$
\omega_{p,\lambda}=\int_0^\infty e^{-u}|-\lambda u\rangle\langle-\lambda u|du.
$$

Its purity is

$$
\mathcal P(\lambda)=\int_0^\infty e^{-z-\lambda^2z^2}dz
=\frac{\sqrt\pi}{2\lambda}e^{1/(4\lambda^2)}
\operatorname{erfc}(1/(2\lambda)),\qquad \mathcal P(0)=1. \tag{14}
$$

The exact pump and signal–idler purities agree and differ from (14) by at most 4epsilon_alpha. Conditioning on the pump momentum in (2), the signal vacuum probability gives

$$
\langle{\rm TMSV}_r|\rho_{ab}|{\rm TMSV}_r\rangle
\longrightarrow\mathcal P(\lambda/\sqrt2). \tag{15}
$$

At lambda=1/2, purity tends to 0.757872156141312..., target fidelity tends to 0.842738458576109..., and trace distance from the pure TMSV has liminf at least 0.157261541423891.... These are squared-overlap fidelities. Pump mixedness certifies entanglement across pump versus both outputs under the globally pure preparation; it does not measure signal–idler entanglement separately.

The pump marginal is a positive coherent-state mixture. The signal approximation (11) is a convex mixture of Gaussian states. Non-Gaussian shape is therefore not a claim of Wigner negativity, nor of a state outside the convex Gaussian hull. Section 7 instead separates the output from every *individual* Gaussian density operator.

## 6. Fixed-purity-loss time

For fixed 0<epsilon<1, let lambda_epsilon be the unique positive solution of P(lambda_epsilon)=1-epsilon. The function P decreases strictly from one to zero. Uniform convergence on a compact interval containing the crossing means that all earlier lambda below lambda_epsilon-delta remain above the threshold and a point above lambda_epsilon+delta lies below it, for sufficiently large alpha. Continuity gives an exact crossing between; no global monotonicity of the exact dynamics is needed. Thus the first crossing satisfies

$$
\tau_\epsilon(\alpha)=
\frac{\ln\alpha+\ln(8\lambda_\epsilon)+o(1)}{2\alpha},\qquad
 gt_\epsilon\sim\frac{\ln N}{4\sqrt N}. \tag{16}
$$

The one-percent lambda is 0.071774448243058..., with offset ln(8lambda)=-0.554785198638437.... The closest same-model eighth-order polynomial [CQ] has leading impurity

$$
\frac29\alpha^4\tau^6+
\left(\frac4{45}\alpha^6-\frac29\alpha^4\right)\tau^8.
$$

It tends to zero at tau=[ln(alpha)+O(1)]/(2alpha), where the exact impurity tends to the specified positive epsilon. Its alpha^(-3/4) root is consequently not uniform in this limit. The fixed-gain expansion of the present dynamics,

$$
1-\mathcal P_\alpha(r)=\frac{[\sinh(2r)-2r]^2}{8\alpha^2}
+o_r(\alpha^{-2}),
$$

reproduces the leading sixth- and eighth-order coefficients in [CQ]. This is a limitation of extrapolation, not a contradiction of those coefficients or a reanalysis of their plotted finite-range data.

## 7. A bounded phase-referenced quadrature signature

This section is a direct consequence of the state theorem, derived in the present consolidation. Let X_-=(x_a-x_b)/sqrt2 be the physically squeezed output quadrature. Define the dimensionless, alpha-dependent record Y_alpha=exp(r_alpha) X_-. Its characteristic function is the expectation of a bounded unitary:

$$
C_\alpha(\xi)=\operatorname{Tr}\rho_{ab}
 e^{i\xi e^{r_\alpha}X_-}.
$$

The deterministic-pump TMSV predicts exp(-xi^2/4) at every alpha. The exact state instead obeys

$$
\boxed{
C_\alpha(\xi)\longrightarrow
\varphi_\lambda(\xi)=\frac{e^{-\xi^2/4}}{\sqrt{1+2\lambda^2\xi^2}},
\qquad
|C_\alpha(\xi)-\varphi_\lambda(\xi)|\le2\epsilon_\alpha.
} \tag{17}
$$

In fact the full rescaled homodyne distribution is within epsilon_alpha in total variation of the fixed distribution described below. The rescaling is known from alpha and the nominal gain; it does not require a quantum inverse squeezer. Ideal homodyne records of x_a and x_b and their classical difference suffice, with appropriately phase-locked external references.

### 7.1 Derivation and complete limiting probability law

Let Z=sqrt2 P_d be the normalized displaced-pump momentum; its vacuum law is standard normal. Conditional on Z=z, (2) acts on the outputs by exp(i lambda z R). Its Heisenberg action is

$$
x_-\mapsto x_--2\lambda z p_-,\qquad
p_+\mapsto p_++2\lambda z x_+.
$$

The squeezed quadrature is therefore conditionally normal with variance 1/2+2lambda^2 z^2. Nominal unsqueezing maps the physical Y_alpha precisely to x_- in the residual frame. Partial trace, measurement contraction, and (5) yield the full-law claim. Gaussian integration gives (17), equivalently

$$
Y\mid Z=z\sim\mathcal N\left(0,\frac12+2\lambda^2z^2\right),
\quad Z\sim\mathcal N(0,1),
$$
$$
p_\lambda(y)=\int_{-\infty}^\infty
\frac{e^{-z^2/2}}{\sqrt{2\pi}}
\frac{\exp[-y^2/(1+4\lambda^2z^2)]}
{\sqrt{\pi(1+4\lambda^2z^2)}}dz. \tag{18}
$$

This is a non-Gaussian scale mixture for every lambda>0. Its moments are well defined, but no convergence of exact unbounded quadrature moments is being inferred from (17) or total variation. The stated observation uses bounded sine/cosine statistics or the probability law.

At lambda=1/2 and xi=1,

$$
C_{\rm TMSV}=0.778800783071405\ldots,\qquad
\varphi_{1/2}(1)=0.635888176601638\ldots.
$$

The cosine-expectation difference tends to 0.142912606469767.... Thus the homodyne distributions have liminf total variation at least half that value, 0.071456303234884.... This is a lower bound supplied by one bounded statistic, not an optimal discrimination probability or an entanglement witness.

### 7.2 Separation from every Gaussian state, not only the nominal pure one

For any Gaussian quadrature law with arbitrary mean mu and variance v,

$$
|C_G(2\xi)|=|C_G(\xi)|^4.
$$

For (17), the gap is

$$
W_\lambda(\xi)=e^{-\xi^2}
\left[\frac1{\sqrt{1+8\lambda^2\xi^2}}
-\frac1{(1+2\lambda^2\xi^2)^2}\right]>0
\quad(\lambda\xi\ne0). \tag{19}
$$

Positivity follows from (1+a)^4>1+4a for a>0. If D is trace distance, each characteristic function changes by at most 2D, and its fourth-power modulus changes by at most 8D. For the set G of all two-mode Gaussian density operators, including mixed states and alpha-dependent choices,

$$
\boxed{
\liminf_{\alpha\to\infty}\inf_{\gamma\in G}D(\rho_{ab},\gamma)
\ge W_\lambda(\xi)/10>0.
} \tag{20}
$$

The finite-alpha lower bound is [W_lambda(xi)/10-epsilon_alpha]_+. At lambda=1/2, xi=1, W=0.048893320535687... and the conservative lower bound is 0.004889332053569.... No claim that this bound is sharp is made. It rules out repairing the asymptotic state error with a single adjusted Gaussian covariance or gain.

At the same time, (11) proves distance to the convex Gaussian hull tends to zero. Equations (19)–(20) must not be advertised as a witness of being outside that hull, a Wigner-negativity result, or a metrological advantage. Characteristic functions distinguishing Gaussian from non-Gaussian laws are elementary; the new content is their exact limiting form and error control for this dynamical crossover.

### 7.3 The resolution and reference assumptions are substantive

For fixed lambda>0 the physical scale is

$$
e^{-r_\alpha}\sim(8\lambda)^{-1/2}N^{-1/4}.
$$

Thus a finite separation in the standardized record is not a fixed absolute quadrature displacement. In an explicit additive readout-noise model with independent Gaussian standard deviation sigma_alpha, the characteristic function gains the factor exp[-sigma_alpha^2 exp(2r_alpha) xi^2/2]. To retain the stated nonzero contrast, sigma_alpha exp(r_alpha) must remain bounded. A fixed positive additive resolution washes out this particular readout as N grows.

This last statement can be made for the whole noisy distribution without an unbounded moment estimate. Equation (18) and convergence make Y_alpha tight, hence X_-=exp(-r_alpha)Y_alpha tends to zero in probability. Convolution with a fixed nonzero Gaussian density then converges in total variation to that density, by bounded translation continuity. Both exact and nominal noisy quadrature laws converge to the same readout-noise law. This is a measurement control, not a loss channel added to the generation theorem.

Likewise, the external reference must have the phase stability and resolution required for the specified quadrature measurement. Keeping and reusing the correlated pump is a different operation and can reverse the original unitary [F18]. The result claims no free phase reference, fixed detector tolerance, or validated experimental operating window.

## 8. Interpretation and contribution boundary

The consolidated conclusion is a controlled separation of validity criteria. At the same growing gain, fractional depletion vanishes, the full number distribution and every total-number-conserving measurement become correct, yet the joint state stays mixed and a phase-referenced rescaled quadrature law stays non-Gaussian. A single Gaussian state cannot approximate it, whereas an explicit Gaussian mixture does.

The model, pump-induced quantum corrections, logarithmic squeezing scales, phase uncertainty affecting squeezed quadratures, Gaussian interaction frames, and energy-sector coherent-amplitude shifts have direct antecedents [CQ,HS,GIF,KFD,HZ]. The candidate contribution is the uniform nondegenerate crossover-state theorem, its measurement-dependent consequences, and fixed-purity first-crossing law. It is not the discovery that pumps are quantum, the first squeezing limit, or the first appearance of non-Gaussianity.

The Hamiltonian is closed, resonant, and three-mode. Increasing N at fixed g need not preserve the approximations behind a particular optical implementation. Keeping g sqrt(N) fixed lengthens the physical crossover time logarithmically, allowing losses to matter. Those implementation questions are not answered by the theorem, and no experimental resource advantage is inferred from it.

Source details and current reading boundaries are in SOURCES.md and REVIEW.md. Full previous proofs and numerical records remain unchanged under prior/.
