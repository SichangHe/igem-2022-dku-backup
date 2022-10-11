## Description and Prediction of drug efficacy

### Overview

Wet lab results showed that we have successfully expressed 20ipaD on the surface
of Yeast. Our goal is to describe
efficiency of expression and predict the scenario after the drug is released in the
patient's jejunal.

#### Part 1: Protein expression efficiency

To describe how efficient is Yeast concerning the expression of 20ipaD, we manually
calculated the efficiency by counting the number of Yeast cells that expressed
20ipaD and the total number of Yeast cells (**Figure 1**).

<img src="https://static.igem.wiki/teams/4161/wiki/fig1-efficiency-expression.png" width="800"/>

**Figure 1** | Fluorescent cells for Yeast cells that obviously expressed 20ipaD.
Dark cells for no or very little expression

#### Part 2: Prediction of post-medication scenario

In this section, we want to predict post-medication scenario by using math modeling.
In detail, we want to see how will the number of floating Shigella change
after the drug release,
this will be depending on natural growth of Shigella, the binding efficiency of
20ipaD and IpaD, the concentration of Yeast cells,
and the survival rate of Yeast cells.

Yeast cells are sealed in micro-capsules made of shellac before
being delivered into bodies.
The pH-dependent solubility that prefers a mild basic environment makes shellac
perfect for releasing probiotics in jejunal.

There are several important assumptions for this model:

- Each floating Yeast cell carries one 20ipaD;
- Each floating Shigella cell carries one IpaD;
- Growth of Shigella cultured in BHI (Brian Heart Infusion) medium is similar with
the growth of Shigella in human's jejunal;
- Each 20ipad binds with one IpaD once;
- Died Yeast cell cannot display 20ipaD and cannot bind with IpaD;
- Yeast  growth is not considered here since a healthy immune system does not
allow overgrowth of the yeast, and the growth of the yeast is very slow in neutral;
or even slightly alkaline conditions[^Yeast_growth].

Based on these assumptions, the following two equations describe the change in
number of shigella and Yeast:
$$
\frac{dL'(t)}{dt} = \frac{dL(t)}{dt} - \beta L(t)D(t)
$$
$$
\frac{D(t)}{dt} = \gamma L(t)D(t)
$$
$L'(t)$: the log count of the number of shigella in jejunal at time $t$ after drug release;\
$L(t)$: the log count of the number of shigella in jejunal at time $t$ before drug release;\
$\beta$: the binding efficiency between 20ipaD and IpaD;\
$D(t)$: the log count of number of Yeast in jejunal at time $t$ after drug release;\
$\gamma$:survival rate of Yeast in jejunal

The natural growth of shigella in jejunal can be described in the form of Gompertz equation[^Shigella_natural]:
$$
L(t) = A + C exp [-exp(-B(t-M)) ]
$$
$L(t)$: the log count of the number of shigella in jejunal at time t before drug release;\
$A$: the asymptotic log count as $t$ decreases indefinitely;\
$C$: the asymptotic amount of growth (log number) that occurs as $t$ increases indefinitely;\
$M$: the time at which the absolute growth rate is maximum;\
$B$: the relative growth rate at $M$

Parameters $A$, $C$, $M$,and $B$ depend on the environmental conditions: temperature $T$, $pH$, and sodium chloride concentration $c$. \
In our case,
$T$ is defaulted to 37 degrees;
the $pH$ is about 6.9 in jejunal and about 7.2 in ileal[^pH];
$c$ in jejunal is about 112$mM$[^NaCl].

Translate the concentration into percentage:\
$$
\frac{x g}{100ml}\frac{1mol}{58.44g}
$$

[^Yeast_growth]: Investigation of the Best Saccharomyces cerevisiae Growth Condition. Electron Physician. DOI: 10.19082/3592 <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5308499/>

[^Shigella_natural]:Effect of Sodium Chloride, pH and Temperature on Growth of Shigella flexneri. Journal of Food Protection. DOI:10.4315/0362-028x-52.5.356 <https://pubmed.ncbi.nlm.nih.gov/31003269/>

[^pH]: Effect of a New Probiotic Saccharomyces cerevisiae Strain on Survival of Escherichia coli O157:H7 in a Dynamic Gastrointestinal Model. Applied and Environmental Microbiology. DOI:10.1128/AEM.02130-10 <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3028742/>

[^NaCl]: The mechanisms of sodium absorption in the human small intestine. The Journal of Clinical Investigation. DOI:10.1172/JCI105781 <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC297237/>
