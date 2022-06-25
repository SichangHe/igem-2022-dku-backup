## Theoretical estimation of antibody (VHH) effect
In this section, we want to see whether our fusion protein-antibody complex could theoretically function well. To do this, we decide to compare the structure of antibody in complex with its original structure.

Overall, there are 2 steps:

- Protein structure prediction
- Protein structure alignment

### Part 1: Protein structure prediction

Based on the amino acid sequence of the protein,
various algorithms can predict the protein's 3D structure.
These algorithms use machine learning to learn from
databases of known amino acid sequences and structures.

#### Background

Our team designed DNA sequences for four fusion proteins ourselves<!-- todo: from what -->
and these newly designed protein's 3D structures are unknown.
A protein's 3D structure determines its functionality,
which,
in our case,
would be the antibody's docking on the membrane and its binding to the antigen.
<!-- todo: review -->

It would intuitively indicate whether the designs are feasible
by checking their structures.

#### Prediction service

We use Robetta and AlphaFold to predict the structure of the four proteins we designed.

Robetta[^Robetta] is an online public service to predict protein structure.
It is based on the algorithms of Rosetta from the Rosetta Commons.

> Robetta is a protein structure prediction server developed by
the Baker lab at the University of Washington.
At it's core is the Rosetta macromolecular modeling suite developed by
the Rosetta Commons,
a multi-institutional collaborative research and software development group.
Robetta's primary service is to predict the 3-dimensional structure of
a protein given the amino acid sequence.

AlphaFold[^AlphaFoldPaper] is a prediction software that can structure the 3D model of a protein based on its amino acid sequence, using a combination of bioinformatics and physical approaches. We run models on AlphaFold (Phenix version) [^AlphaFoldPh] Colab notebook and it will automatically give the highest-scoring model.
This Colab notebook is derived from ColabFold [^ColabFold] and the DeepMind AlphaFold2 Colab[^AlphaFold2Colab]

Robetta[^Robetta] and AlphaFold Colab notebook[^AlphaFoldPh] both accept single-letter code amino acid sequences
and generate Protein Database (PDB) files,
which contains information about the protein's structure. Robetta produces 5 models of different configuration with same score for each sequence. Alphafold automatically produces the model with highest score.

We view these pdb files in PyMOL[^PyMOL], a powerful tool for 3D structure visualization.

### Part 2: Protein structure alignment

Based on the models we got from Robetta[^Robetta] and AlphaFold Colab notebook[^AlphaFoldPh], we can compare the antibody structure in the model with its original structure by using PyMOL[^PyMOL] alignment. If RMSD (root mean square deviation) value is below 2, we regard two structures similar, which means the antibody in our fusion-antibody complex will theoretically function well.

#### Alignment result
<!-- todo: 2 tables of RMSD value -->
- Alphafold models:\
The pIDDT value shows the model confidence (out of 100) at each position. The higher the better. All pIDDT values are higher than 50. With the exception of group Yeast, the other models scored about 70. RMSD values are all lower than 1, indicating that the structure of the antibody in the complex model was very similar to its original structure.
- Robetta models:\
Except for group Yeast, the antibody structures in other complex models are quite different from their original structures. This may be because we did not provide template to Robetta.

[^Robetta]: Robetta <https://robetta.bakerlab.org>

[^AlphaFoldPaper]: AlphaFold <https://www.nature.com/articles/s41586-021-03819-2>

[^AlphaFoldPh]: AlphaFold(Phenix Version) <https://colab.research.google.com/github/phenix-project/Colabs/blob/main/alphafold2/AlphaFold2.ipynb>

[^ColabFold]: ColabFold <https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb>

[^AlphaFold2Colab]: AlphaFold2 <https://colab.research.google.com/github/deepmind/alphafold/blob/main/notebooks/AlphaFold.ipynb>

[^PyMOL]: PyMOL <https://pymol.org/2/>
