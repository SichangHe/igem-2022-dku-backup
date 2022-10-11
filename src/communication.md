<div class="h1-bg">
    <h1 class>Communications</h1>
    <img src="https://static.igem.wiki/teams/4161/wiki/communi-bg.jpg" />
</div>

## Overview

We had science communications during different stages of our project.
Firstly, we designed a socially-oriented questionnaire to find out how much the
 public knows about shigella.
Then,throughout expert interviews, we managed to gain insights of our project feasibility
and possible future directions. Finally,
we participated in on-campus communication to let more people know about shigella
and surface display technology.

## Socially-Oriented Questionnaire

Before the experiment, we designed and published a questionnaire about
antibiotic treatment and dysentery on social network platform, and obtained
more than 500 responses from people of different regions, age groups and
education levels in China. We found that many people, although aware of
dysentery, do not know how it is transmitted or the bacteria that causes it.
This makes us realize the importance of science popularization. Meanwhile,
people have different levels of concern about antibiotic resistance, which
means it is necessary for us to focus on antibiotic therapy replacement.

<img src="https://static.igem.wiki/teams/4161/wiki/fig-wenjuan.png"
width="500"/>

## Interview with Prof. Cao
  
  We interviewed Huansheng Cao,
  Assistant professor of Environmental Science at Duke Kunshan University
  for suggestions on our initial lab plans.

  In the interview, team members Yuxin Wang and Chang Shen presented
  the main design, bacterial surface display, to consult Prof Cao on its feasibility.
  After confirming the rich research foundations of our plan, he encouraged us to add computational elements
  to our lab design.

  As a scientist working in computational biology and bioinformatics, he
  pointed us to Alphafold2 for the enhancing the binding affinity of our nanobody
  and the antigen unit. As a well-trained
  biologist, he also suggested fitting our design to more than one model
  organisms, which shows integration in our drug design.

  The interview was full of enthusiasm, so we were able to come across many other topics.
  We discussed the trends in bioinformatics and biotechnology, including bacteria-based
  bioelectricity, and the relationship between human longevity and gut microbiota.

  This interview was both encouraging and informative, and contributed
  greatly to the first stage of human practice.

<img src="https://static.igem.wiki/teams/4161/wiki/prof-cao-interview1.jpg"
width="500"/>

## Interview with Prof. Beckford
After we successfully predicted the 3d structure of fusion protein-antibody
complex by using Robetta and Alphafold2, the focus shift to how the fusion
protein will influence the binding (docking) between antibody and antigen. We
plan to get some insights about this from computer modeling before the wet lab
begins.

We interviewed Floyd Beckford, Professor of Chemistry at Duke Kunshan University
for suggestions on our protein docking simulation.

At the beginning, team leader Lisa Wu introduced the synthetic biology part of
our project. Modeling team leader Zhenyu Xu introduced the progress of protein
structure prediction and the need for protein docking simulation.

As a scientist working in modern medicine, Prof. Floyd pointed us to some
useful docking software--Autodock, ADFR suite, GOLD, and Maestro. These
software are powerful at predicting the docking scenario and are used by many
researchers, with many online teaching resources accessible.

To improve the speed of computer modeling, Prof. Floyd emphasized the
preprocessing of protein structures. Namely, the antigen structure. He
suggested us delete the floating molecules outside the binding sites and keep
those inside, since we only care about the binding scenario. He also pointed
that virtual screening could help if we want to do more mutations to the
binding sites. Concerning the fusion protein-antibody complex models, since
they are the optimal prediction given by Robetta and Alphafold2, we assume
these models do not need preprocessing anymore.

For docking, he suggested us try rigid docking first, and then flexible docking
if we want to get closer to reality.

<img src="https://static.igem.wiki/teams/4161/wiki/fig-floyd.jpg"
width="500"/>

## Interview with Dr. Neel Joshi

**Introduction**

Dr. Neel Joshi is an expert in bioengineering
with tracks in human disease and new therapies.
In his 2019 and 2021 literature,
he and his team described genetically engineering E. coli Nissle 1917
to treat some gastrointestinal diseases like bowel inflammation,
which provide essential references for our project.
To further understand the logics and advantages of this bioengineered model,
we invited Dr. Joshi for an interview.

![Dr. Joshi interview photo 1](https://static.igem.wiki/teams/4161/wiki/dr-joshi-interview1.png)

**Interview Content**

**Q:**
What stimulated you and your team to develop
the surface-displaced single domain antibodies?
What practical problems do you think this model can solve?

**A:**
Although the nanobodies have great potentials in treating gastrointestinal diseases,
it is somewhat hard to deliver those nanobodies directly to the digestive track.
Therefore,
the probiotics can serve as a scaffold to make the delivery of nanobodies easy.

**Q:**
But why did you choose to display the nanobodies on the surface?
Why not directly make the bacteria synthesize nanobodies and release them?

**A:**
The surface display resolution has the property of multi-valency.
By displaying the nanobodies on the surface,
we would have the potential to space the binding domains together
to bind to a pathogen surface.
It could increase binding affinity and decrease the dissociation constant.
It can also diffusion into different directions and increase the local concentration.

**Q:**
What about the method of drug delivery?
That is to say,
how do you decide to send the engineered probiotics to human gastrointestinal track?
And could you explain why you use that delivery method?

**A:**
We only proposed an approach of micro biological therapy.
But to deliver the bacteria,
I think it can be freeze-dried to produce a freeze-dried product.
Because a large portion of the geographical locations
that suffered from these gut problems are the poor areas,
and those areas do not have the condition
to store the bacteria that require a very low temperature.
The freeze-dried products do not require that strict storage conditions,
so they are more available in those areas.

**Q:**
Why pBbB8k plasmid backbone with kanamycin selection marker?
(what's the difference between pUC19,
which is our choice,
and pBbB8K?)

**A:**
pBbB8k is a rather arbitrary choice,
we simply chose it
because it was used due to antibiotics incompatibility in the previous experiment.
When doing in vivo studies,
we engineered plasmids from the original E. coli Nissle genome,
the pMUT plasmids.
These plasmids are more stable than the pBbB8K.
For pUC19,
I don’t see problems with the expression of pUC19 plasmid.
However,
you do need to consider if your antibiotic resistant marker
in the plasmid is compatible with the shigella testing.
If shigella is killed due to the antibiotic selecting E. coli,
it can be a problem.

**Q:**
What are the setbacks of
the Probiotic-associated therapeutic curli hybrids (PATCH) system?

**A:**
The first is safety concerns of curli fibers.
It has been known that curli fibers induce various types of diseases,
including neurological diseases,
etc.
The other is inherit disadvantages for E. coli to produce curli fibers in vivo.
However,
we have been able to shown effective production of curli fiber in vivo
by measuring the amount of curli fibers coming from the fecal samples.

**Q:**
What if the E. coli went out of control and grow infinitely in the gut,
disrupting the original gastrointestinal microorganism environment?

**A:**
This is a very popular question when it comes to distributing microbes to gut.
Actually,
we could use some of the auxotrophic strains to limit the growth of the bacteria.
And I think there are many “switches”
that can turn on the suicide program of those bacteria.
But in this case,
I think E. coli Nissle 1917 is a very safe bacteria,
it has already been identified as a harmless bacterium,
so there should be less safety issues of this strain.

**Q&A Section**

**Q:**
Is it possible to apply magnetic triggers to shigella infection
and cooperate this into the PATCH system?

**A:**
Magnetic triggers are mostly applied in cancer treatment.
This is because in cancer,
you know the spot of the disease.
In bacterial infection it’s hard to locate.

**Q:**
In Barta et al.,
the authors described the different indexes of the nanobodies,
including binding domains and neutralization effects.
What is your rationale when choosing the nanobodies?

**A:**
It really depends on how you generate the nanobodies.
When different parts of the pathogen are used in Alpaca immunizations,
the nanobodies will vary.
When displaying the nanobodies,
some work and others don’t.
We assume this is because of folding problems,
but we did not figure out the exact reason.  

**Q:**
What do you think about sequence optimization in silica?
Do you have experience working with this?
Do you have any suggestions?

**A:**
I would suggest generating different mutations in the sequence
and do some docking analysis.
Then generate the mutations and do wet labs.  

**Q:**
Our project aims to tackle the antibiotic resistance problem worldwide.
Would the PATCH system generate drug resistance issues?

**A:**
This is possible.
For example,
a mutation in the binding domain of the antigen might cause binding problems.
However,
I would say the selective pressure by the nanobody is smaller
compared to that of the antibiotic.
This is because antibiotic kills the pathogen,
while PATCH only binds to the pathogen,
keeping it from invasive activities.  

**Q:**
We are worried
that the proteins in the GI tract environment would coat the surface of the probiotic,
which would cause dysfunction of the nanobodies.
How did your team encounter this problem?

**A:**
The animal model was effective,
which was sufficient to show
that the GI tract environment did not inhibit the binding activity.
The curli production is continuous in vivo,
which provides adequate chance for the binding to occur.
However,
the proteases in the GI tract is something to consider.

**Summary and Reflection**

Dr. Joshi provided lots of perspectives from a brand-new aspect,
which were extra inspirable for the whole team.
First,
Dr. Joshi elaborated on the practical problems
that this model could potentially resolve.
That the probiotic expression system could
make the delivery of nanobodies easier expanded our understanding of
the model as the delivery problem does not only exist in the step of bacteria delivery,
it starts from the delivery of the essential nanobodies.

Next,
the freeze-dry delivery approach gives
a less stricter storage condition of this drug,
making it more available in poor areas,
which corresponds with our assumed delivery method.
As for the safety problem that the public is most interested in,
Dr. Joshi proposed to use some molecular switches
to eliminate those bacteria in addition to using safe strains like Nissle,
giving important clue and indication for our project design.

In the Q&A section,
questions regarding drug localization,
drug resistance,
choice of nanobodies were mentioned by team members.
Dr. Joshi gave many valuable advices depending on the questions.
Overall,
the interview was successful,
and we were able to arm ourselves with adequate knowledge for the wet lab.

### Interview with SINOVAC

[See Entrepreneurship.](entrepreneurship.md)

## On-Campus Communication

As an undergraduate team, we participated in the 2022's College Student
Innovation and Entrepreneurship Training Program—a national training program
for college students on innovation and entrepreneurship. In this way, we can
better promote the topic of synthetic biology to the DKU community and attract
more fresh blood to participate in innovation. We made posters and participated
in project exhibitions, and were regularly inspected by the jury on campus.

<img src="https://static.igem.wiki/teams/4161/wiki/fig-on-campus-communication.png"
width="500"/>

## Summary

Throughout the project, we never stopped science communication with different
groups. The social questionnaire allowed us to identify the need for the
program; the school publicity has attracted a batch of fresh blood to join the
research and innovation of synthetic biology; the expert interviews enabled us to
reflect on the feasibility and future directions of our lab design.
These science communication helped us be more clear about the direction of the experiment
and the significance of this project.
