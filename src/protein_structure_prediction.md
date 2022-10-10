# Visualization

## Overview:
We used online softwares to help us visualize the 3D protein structures and
modeled
their docking
scenarios,
and then we evaluated their stability by using some common parameters. This
section
aims to visually display the protein structure synthesized in this project and
provide ideas or directions for future experiments or experimental teams

### Part 1: General pattern

Our team designed DNA sequences for fusion protein-nanobody complex
ourselves<!-- todo: from what -->
and these newly designed protein's 3D structures are unknown.
A protein's 3D structure determines its functionality,
which,
in our case,
would be the nanobody's docking on the membrane and its binding to the antigen.
<!-- todo: review -->

#### Protein structure prediction

Based on the amino acid sequence of the protein, various algorithms can predict
the
protein's 3D structure. These algorithms use machine learning to learn from
databases
of known amino acid sequences and structures. It would intuitively indicate
whether
the designs are feasible by checking their structures.

- Prediction service

We use Robetta and AlphaFold to predict the structure of the proteins we
designed.

Robetta[^Robetta] is an online public service to predict protein structure.
It is based on the algorithms of Rosetta from the Rosetta Commons.

> Robetta is a protein structure prediction server developed by
the Baker lab at the University of Washington.
At it's core is the Rosetta macromolecular modeling suite developed by
the Rosetta Commons,
a multi-institutional collaborative research and software development group.
Robetta's primary service is to predict the 3-dimensional structure of
a protein given the amino acid sequence.

> AlphaFold[^AlphaFoldPaper] is a prediction software that can structure the 3D
model
of a protein based on its amino acid sequence, using a combination of
bioinformatics
and physical approaches. We run models on AlphaFold (Phenix version)
[^AlphaFoldPh] Colab
notebook and it will automatically give the highest-scoring model.
This Colab notebook is derived from ColabFold [^ColabFold] and the DeepMind
AlphaFold2
 Colab[^AlphaFold2Colab]

Robetta[^Robetta] and AlphaFold Colab notebook[^AlphaFoldPh] both accept
single-letter
code
amino acid sequences
and generate Protein Database (PDB) files,
which contains information about the protein's structure. Robetta produces 5
models of
different configuration with same score for each sequence. Alphafold
automatically produces
the model with highest score.

We view these pdb files in PyMOL[^PyMOL], a powerful tool for 3D structure
visualization.

#### Protein structure evaluation

Assessment of these resultant structures from Robetta and Alphafold2 is needed
for
deciding which structure is more credible and can be used in future anlysis.
There are
several parameters to consider: ramachandran plot, overall G-factors, atomic
Z-score RMS,
percentage of the amino acids having scored >= 0.2 in the 3D/1D profile,
overall quality factor,
and Z-score. We use online server SAVES v6.0[^SAVES] and ProSA[^ProSA] for the
validation.

- Parameters

1. Ramachandran plot:\
   Ramachandran plot shows the theoretical conformation of amino acid residues
and
   is mainly used to evaluate the model quality after homologous modeling. It
considers
   whether the conformation of amino acids is reasonable. Based on an analysis
of
   118 structures of resolution of at least 2.0 Angstroms and R-factor no
greater than
   20%,
   a good quality model would be expected to have over 90% in the most favoured
regions.[^SAVES]
2. Atomic Z-score RMS:\
Z-score root mean square deviation (Z-score RMS) measures the "average
magnitude of the
volume irregularities in the structure." [^Z-scoreRMS] Z-score RMS for a good
model should
be around 1.0.
3. Percentage of the amino acids having scored >= 0.2 in the 3D/1D profile:\
Indicate whether the atomic model is compatible with its amino acid sequence.
It should
be higher than 80% for a good model. [^SAVES]
4. Overall quality factor:\
An overall score for the model provided by SAVES server[^SAVES], ranging from 0
to 100.
It should be higher than 80 for a good model.[^Standard]
5. Z-score:\
Indicate whether the z-score of the input structure is within the range of
scores typically
found for native proteins of similar size[^ProSA].

All the structures shown later are the highest scoring structures.

#### Protein structure alignment

After the evaluation of models we got from Robetta[^Robetta] and AlphaFold Colab
notebook[^AlphaFoldPh], we can compare the antibody structure in the model with
its original
structure by using PyMOL[^PyMOL] alignment. If RMSD (root mean square
deviation) value
is very low,
we regard two structures similar, which means the nanobody in our
fusion-nanobody complex
will theoretically function well.

### Part 2: Yeast-20ipaD visualization
We have successfully expressed the fusion protein-nanobody complex, which is
Yeast-20ipaD.
Here is the highest-scoring structure of Yeast-20ipaD (**Figure 1**).

<img src="https://static.igem.wiki/teams/4161/wiki/fig1-yeast-20ipad.png"
width="500"/>

**Figure 1** | 3D structure of Yeast-20ipaD complex

Ramachandran plot of the above structure showed that
85.1% of residues are in the most favorite regions,
and 11.9% are in the allowed regions; 1.9% of the residues are in the
generously allowed regions
and 1.1% in the disallowed regions.
The Atomic-Z-score RMS is tested to be 1.536, which is a little bit out of
range. A very good model
would have a value close to 1. The percentage of the amino acids have scored >=
0.2 in the 3D/1D profile is 92.39%.
The overall quality factor is 82.89, which is acceptable.
ProSA calculated Z-score is -8.7, which falls in the range of scores typically
found for
experimentally determined (X-ray, NMR) structure for native proteins of similar
size in
PDB database.
The calculated average energy over 40 residues is always under 0. Overall, the
above structure
can be regarded as a good model of Yeast-20ipaD.

<img src="https://static.igem.wiki/teams/4161/wiki/fig2-alignment.png"
width="500"/>

**Figure 2** | Alignment of 20ipaD between itself in complex and it's original
structure.

The alignment between 20ipaD in the complex
and 20ipaD's original structure shows that our complex can
have good effect theoretically (**Figure 2**). The RMSD value is tested to
be 0.807, which means the complex have little influence on the
structure of 20ipaD.

### Part 3: Docking modeling

Interaction imformation (binding sites) of 20ipaD and ipaD
is found in the paper: ***Single-Domain Antibodies Pinpoint Potential Targets
within Shigella
Invasion Plasmid Antigen D
of the Needle Tip Complex for Inhibition of Type III Secretion*** [^Binding].
Since the alignment shows that the 20ipaD
in complex is almost the same with it's
original structure, we can default the binding sites unchanged. Below is the
binding sites between 20ipaD and ipaD (**Figure 3**).

<img src="https://static.igem.wiki/teams/4161/wiki/fig3-binding-positions.png"
width="500"/>

**Figure 3** | Binding sites between 20ipaD and Ipad

We provided the interaction information for online server HADDOCK [^HADDOCK] to
simulate the docking between the complex and ipaD.
Below is the docking structure
(**Figure 4**).

<img src="https://static.igem.wiki/teams/4161/wiki/fig-4-docking-result.png"
width="500"/>

**Figure 4** | Docking between 20ipaD (in complex) 
and IpaD

Ramachandran plot of the above structure showed that 
85.0% of residues are in the most favorite regions, 
and 12.7% are in the allowed regions; 1.2% of the residues are in the generously allowed regions 
and 1.0% in the disallowed regions. 
The Atomic-Z-score RMS is tested to be 1.441, which is relatively close to 1. 
The percentage of the amino acids have scored >= 0.2 in the 3D/1D profile is 87.61%.
The overall quality factor is 85.53, which is acceptable.
ProSA calculated Z-score is -7.16, which falls in the range of scores typically found for 
experimentally determined (X-ray, NMR) structure for native proteins of similar size in 
PDB database.
The calculated average energy over 40 residues is always under 0.
Overall, the above structure indicates that 20ipaD can bind with IpaD well theoretically.

Below is the alignment between our docking result and the original docking 
between 20ipaD and IpaD. 
RMSD is 0.36, which is very small and acceptable. 

<img src="https://static.igem.wiki/teams/4161/wiki/fig-5-alignment-of-docking-and-original.png"
width="500"/>

**Figure 5** | Alignment between Yeast-20ipaD-IpaD and 20ipaD-IpaD.

All the above shows that our Yeast-20ipaD complex could theoretically work well 
when binding with IpaD.


### Part 4: Other combinations of probiotic-nanobody complex
In this section, we would like to show other possible combinations of fusion
protein-nanobody
complex that might theoretically function well. To do this, we modeled their 3D
structures
and their docking scenarios, and analyzed them. This could be helpful for
future experiment
and future teams.

[^Robetta]: Robetta <https://robetta.bakerlab.org>

[^AlphaFoldPaper]: AlphaFold
<https://www.nature.com/articles/s41586-021-03819-2>

[^AlphaFoldPh]: AlphaFold(Phenix Version)
<https://colab.research.google.com/github/phenix-project/Colabs/blob/main/alphaf
old2/AlphaFold2.ipynb>

[^ColabFold]: ColabFold
<https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFol
d2.ipynb>

[^AlphaFold2Colab]: AlphaFold2
<https://colab.research.google.com/github/deepmind/alphafold/blob/main/notebooks
/AlphaFold.ipynb>

[^PyMOL]: PyMOL <https://pymol.org/2/>

[^SAVES]: SAVES <https://saves.mbi.ucla.edu/>

[^ProSA]: Prosa <https://prosa.services.came.sbg.ac.at/prosa.php>

[^Z-scoreRMS]: Deviations from standard atomic volumes as a quality measure for
protein crystal structures
<https://pubmed.ncbi.nlm.nih.gov/8950272/>

[^HADDOCK]: HADDOCK online server <https://wenmr.science.uu.nl/haddock2.4/>

[^Binding]: Single-Domain Antibodies Pinpoint Potential Targets within Shigella
Invasion Plasmid Antigen D
of the Needle Tip Complex for Inhibition of Type III Secretion.
DOI: 10.1074/jbc.M117.802231
<https://pubmed.ncbi.nlm.nih.gov/28842484/>

[^Standard]:Homology modeling and virtual screening approaches to identify potent inhibitors of VEB-1 β-lactamase.
DOI: 10.1186/1742-4682-10-22
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3668210/>

