## Protein structure prediction

Based on the amino acid sequence of the protein,
various algorithms can predict the protein's 3D structure.
These algorithms use machine learning to learn from
databases of known amino acid sequences and structures.

### Background

Our team designed DNA sequences for four fusion proteins ourselves<!-- todo: from what -->
and these newly designed protein's 3D structures are unknown.
A protein's 3D structure determines its functionality,
which,
in our case,
would be docking on the membrane and binding to the antigen.
<!-- todo: review -->

It would intuitively indicate whether the designs are feasible
by checking their structures.

### Prediction service

We use Robetta to predict the structure of the four proteins we designed.
Robetta[^Robetta] is an online public service to predict protein structure.
It is based on the algorithms of Rosetta from the Rosetta Commons.

> Robetta is a protein structure prediction server developed by
the Baker lab at the University of Washington.
At it's core is the Rosetta macromolecular modeling suite developed by
the Rosetta Commons,
a multi-institutional collaborative research and software development group.
Robetta's primary service is to predict the 3-dimensional structure of
a protein given the amino acid sequence.

Robetta accepts single-letter code amino acid sequences
and generates Protein Database (PDB) files,
which contains information about the protein's structure.
We view these PDB files with PyMOL[^PyMOL],
a PDB file view.

[^Robetta]: Robetta <https://robetta.bakerlab.org>

[^PyMOL]: PyMOL <https://pymol.org/2/>
