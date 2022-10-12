<div class="h1-bg">
    <h1 class>Model</h1>
    <img src="https://static.igem.wiki/teams/4161/wiki/model-bg.png" />
</div>

Models are powerful tools in terms of imagining reasonable future scenarios. Also,
assumptions and results from the model push us to reflect on the present situation
and make adjustments to our existing plans and experiments, which might also develop
our final goal into a more realistic version.

There are 3 modeling sections in our project:

- **Visualization**\
  This section mainly shows the structure of proteins and their docking results,
  and also tries to provide guides for future experiment design.

- **Description and Prediction of drug efficacy**\
  This section mainly describes the efficiency of protein expression, and tries to
  predict the scenario after a patient
  takes the drug.

- **Hardware**\
  This section shows the 3D model of the micro-capsule where Yeast cells are sealed in.
  The micro-capsule is made of shellac, and the pH-dependent solubility that
  prefers a mild basic environment makes shellac perfect for
  releasing probiotics in intestines.

{{#include protein_structure_prediction.md}}

## Description and Prediction of drug efficacy

### Overview

Wet lab results showed that we have successfully expressed 20ipaD on the surface
of Yeast. Our goal is to describe
efficiency of expression and predict the scenario after the drug is released in the
patient's jejunal.

#### Part 1: Protein expression efficiency

To describe how efficient is Yeast concerning the expression of 20ipaD, we manually
calculated the efficiency by counting the number of Yeast cells that expressed
20ipaD and the total number of Yeast cells (**Figure 1**).Through separated assessments conducted by two individuals, we found that our model has a 31.25% expression rate with a STD of ± 0.75.

<img src="https://static.igem.wiki/teams/4161/wiki/fig1-efficiency-expression.png"/>

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
\frac{\mathrm dL'(t)}{\mathrm dt} = \frac{\mathrm dL(t)}{\mathrm dt} - \beta L(t)D(t)
\\[12pt]
\frac{D(t)}{\mathrm dt} = \gamma L(t)D(t)
$$

$L'(t)$: the log count of the number of shigella in jejunal at time $t$ after drug release;\
$L(t)$: the log count of the number of shigella in jejunal at time $t$ before drug release;\
$\beta$: the binding efficiency between 20ipaD and IpaD;\
$D(t)$: the log count of number of Yeast in jejunal at time $t$ after drug release;\
$\gamma$:survival rate of Yeast in jejunal

**Detail:**\
The natural growth of shigella in jejunal can be described in the form of Gompertz equation[^Shigella_natural]:

$$
L(t) = A + Ce^{-e^{-B(t-M)}}
$$

$L(t)$: the log count of the number of shigella in jejunal at time t before drug release;\
$A$: the asymptotic log count as $t$ decreases indefinitely;\
$C$: the asymptotic amount of growth (log number) that occurs as $t$ increases indefinitely;\
$M$: the time at which the absolute growth rate is maximum;\
$B$: the relative growth rate at $M$.

Parameters $A$, $C$, $M$,and $B$ depend on the environmental conditions: temperature $T$, $pH$, and sodium chloride concentration $c$. \
In our case,
$T$ is defaulted to $37$ degrees;
the $pH$ is about $6.9$ in jejunal and about $7.2$ in ileal[^pH];
$c$ in jejunal is about $112\text{mM}$[^NaCl].

Translate the concentration into the form of percentage:

$$
\frac{x g}{100\text{ml}}\frac{1\text{mol}}{58.44g}\frac{1000\text{ml}}{1\text{L}}=0.012\text{M}
\\[12pt]
x = 0.65
$$

So, the concentration of sodium chloride is about $0.65\%$ in jejunal.

Gompertz equation parameters and calculated growth curve values for Shigella can
be found in the paper: ***Effect of Sodium Chloride, pH and Temperature on Growth
of Shigella flexneri***[^Shigella_natural].
Parameters in our situation do not perfectly fit the calculated ones, but they
do fall in a certain range:

- Lower limit:\
    $T=37°$, $pH=6.5$, $c=0.5\%$,\
    $A=4.53$, $B=0.493$, $C=4.47$, $M=3.68$

    $$
    L(t) = 4.53 + 4.47e^{-e^{-0.493(t-3.68)}}
    \\[12pt]
    \frac{L(t)}{\mathrm dt} = 2.20e^{-e^{-0.493(x-3.68)}-0.493(x-3.68)}
    $$

- Higher limit:\
    $T=37°$, $pH=7.5$, $c=0.5\%$,\
    $A=4.26$, $B=0.435$, $C=5.41$, $M=4.54$

    $$
    L(t) = 4.26 + 5.41e^{-e^{-0.435(t-4.54)}}
    \\[12pt]
    \frac{L(t)}{\mathrm dt} = 2.35e^{-e^{-0.435(x-4.54)}-0.435(x-4.54)}
    $$

Since our situation is in this range, so we can have an upper limit and lower limit
for the growth scenario of Shigella (**Figure 2**).

<img src="https://static.igem.wiki/teams/4161/wiki/fig-model-part2-growth-of-shigella.png"/>

**Figure 2** | Upper limit and lower limit for Shigella's natural growth in jejunal.
The x-axis indicates the time with unit of hour; the y-axis indicates the
log count of number of Shigella.

The survival rate of Yeast cells in jejunal varies with time (**Figure 3**)[^pH].

<img src="https://static.igem.wiki/teams/4161/wiki/fig-model-part-2-yeast-survival-rate.png"/>

**Figure 3** | Survival rate of Yeast cells in jejunal with time of digestion.

The survival rate is highest at $t=2\text{h}$, when $30.8\%$
of intake Yeast cells are viable. Then, the viability decreases with time, finally $13\%$
of intake Yeast cells are viable at $5\text{h}$.

#### Part 3: Medication guidance

Our drug is designed to 'kill' the Shigella before it invades
the surface of jejunal, or more realistically, to decrease the concentration of
floating Shigella so that a mass invasion could be avoided or stopped as soon as possible.
Based on the information from wet-lab and math modeling, we would like to give
a possible conclusion or a medication guidance for the patients and the managers
of the healthcare system, so that our vision could be realized.

For a single micro-capsule, assume it contains at least 10 billion CFU (colony-forming unit)[^CFU],
then it contains at least 10 billion live Yeast cells. Since the expression rate is about 31.25%,
there would be at least 3 billion live Yeast cells that expressed at least one
20ipaD on each of their surfaces. After the capsule reaches jejunal, it will dissolve and start to release
Yeast cells. After 2 hours, there will be about 0.9 billion
Yeast cells (30.8%
of the intake)
 that are viable to display 20ipaD and bind with IpaD.

For Shigella, since the upper limit and lower limit of natural growth are found,
we can calculate the maximum population density in the following form:
$$
\text{Density}_{max} (\log_{10}\text{cfu/ml}) = A + C
$$

So the uppper limit of the max density at $t=5\text{h}$ will be about 5 billion Shigella, and
the lower limit will be about 1 billion Shigella.

Therefore, it is proper to take 5-6 capsules every 5 hours after the patient start to have symptoms,
and distribute 1-5 capsules every 5 hours to the people who might develop symptoms due to
living togethor or common life styles.

### Summary & Future plan

To conclude, we have described the 20ipaD expression efficiency of Yeast cell through wet-lab results
and predicted the post-medication scenario through math modeling.
The expression efficiency is found to be about 31.25%± 0.75,
and the upper limit and lower limit of natural growth of Shigella
could help us to define a range for Shigella to grow naturally in jejunal.
By assuming each capsule contains 10 billion CFU,
we are able to give a medication guidance for symptomatic patient to take 5-6 capsules per 5 hours
and for potential patients to take 1-5 capsules per 5 hours.

In the future, more work can be devoted to deciding the binding efficiency $\beta$ between Yeast-20ipaD and IpaD,
and how much CFU is needed and realistic can a single capsule contain. These work can help us
better understand the change of number of Shigella after medication,
so that a more precise medication guidance is available.

[^Yeast_growth]: Salari R, Salari R.(2017).Investigation of the Best Saccharomyces cerevisiae Growth Condition. Electron Physician.  <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5308499/>

[^Shigella_natural]:Zaika, L. L., Engel, L. S., Kim, A. H., & Palumbo, S. A. (1989). Effect of Sodium Chloride, pH and Temperature on Growth of Shigella flexneri. Journal of food protection, 52(5), 356–359.<https://pubmed.ncbi.nlm.nih.gov/31003269/>

[^pH]: Etienne-Mesmin L, Livrelli V, Privat M, Denis S, Cardot JM, Alric M, Blanquet-Diot S.(2011). Effect of a New Probiotic Saccharomyces cerevisiae Strain on Survival of *Escherichia Coli* O157:H7 in a Dynamic Gastrointestinal Model. Applied and Environmental Microbiology. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3028742/>

[^NaCl]: Fordtran JS, Rector FC Jr, Carter NW.(1968) The mechanisms of sodium absorption in the human small intestine. J Clin Invest. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC297237/>

[^CFU]: Choosing the Best Probiotic: How Many CFUs is Enough?. (2022). Deerland. <https://deerland.com/chew/choosing-best-probiotic-many-cfus-enough/>

{{#include hardware.md}}

