## Interview with Prof Floyd
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
