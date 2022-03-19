# Anticipated results from early modelings
Our early modeling result indicated that the project is theoretically feasible. By using the theory of diffusion (Fick’s Diffusion Law) and parameters from literature review, we modeled the distribution of AMP that is directed to the pathogen by antibodies. For rough estimation, we hypothesize the geometry of probiotics can be simplified as tiny spherical particles with radius R (about 1μm), and the diffusion of AMP in the gastrointestinal tract was modeled as spherically symmetric concentration profiles.

$$
\Delta C=\frac{1}{r^2}\partial_r(r^2\partial_rC)\\\\
$$
($C$: concentration, $r$: the distance from the center of one probiotic sphere)
Stationary situation was the focus, that is
$$
\Delta C=0\\\frac{1}{r^2}\frac{d}{dr}(r^2\frac{dc}{dr})=0
$$
Under boundary conditions: $c=c_0$ at $r=R$， $c=c_1$ far from the particle, the solution is
$$
c=(c_0-c_1)\frac{R}{r}+c_1
$$
The model was built on the fact that transport phenomena could happen under the condition of stationary concentration. The AMP production rate $N$ is expressed by
$$
N=4\pi R^4D(\frac{dc}{dr})_R
$$
($D$:diffusion coefficient)

Having all these equations, the AMP production rate can be finalized as
$$
N=4\pi DR(c_0-c_1)
$$
Form literature review, the diffusion coefficient $D$ of a 2500 Da AMP in intestinal condition is found to be around $0.5×10^{-10}  m^2\cdot s^{-1}$. The AMP production rate $N$ is assumed as about 100 AMP/s.
Therefore, $c_0-c_1$ could be calculated as around $0.7 μg/ml$.