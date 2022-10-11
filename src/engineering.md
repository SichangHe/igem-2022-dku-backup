<div class="h1-bg">
    <h1 class>Engineering Cycle</h1>
    <img src="https://static.igem.wiki/teams/4161/wiki/wetlab3-for-bg.png" />
</div>

## Introduction

This page will give a detailed explanation about the engineering cycle. To make yeast capable of displaying the target nanobody 20ipaD on the cell surface, 20ipaD gene was inserted behind the yeast membrane-sealed protein *Aga*2; therefore, *Aga*2 would bring the nanobody to the cell surface. The recombinant plasmid pYD1-20ipaD was successfully built, which was supported by PCR amplification data and sequencing data. Apart from yeast, *Lactococcus lactis* and *Escherichia coli* were  also chosen as probiotics for surface displace of nanobodies at the beginning, where 20ipaD/JPS-G3 and control 3xFLAG tags were inserted into pNZ8148 (L. lactis) and pET30a (E. coli) for expression respectively. However, due to failure in transformation and plasmid construction, only yeast was selected as the final product.

## Engineering Cycle

### Yeast

![y-engineering-cycle-high-resolution](https://static.igem.wiki/teams/4161/wiki/y-engineering-cycle-high-resolution.png)

#### Cycle 1

##### Design

We located a single-domain antibody (VHH) named 20ipaD from the database, whose binding ability with the needle tip protein ipaD of *Shigella* type III secretion system has be testified [^Barta,2017] [^Sierocki,2021]. Peptide sequences of 20ipaD from Barta et al (2017). Codon optimization was performed to get DNA sequences. Two flank sequences containing XhoI and ApaI cutting sites as well as C-terminal Flag-tag were added to the ipaD DNA sequence.

##### Build

Designed 20ipaD sequences were chemically de novo synthesized and sent in pUC19. XhoI and ApaI double-digestion enabled us to ligate the 20ipaD DNA sequence into pYD1, a plasmid allowing the surface display of the gene it carries in yeast. The ligation of 20ipaD into pYD1 generates a DNA sequencing coding a recombinant protein of 20ipaD and Aga2, a yeast extracellular membrane protein. pYD1 also contained a replication origin recognized by bacteria and an ampicillin resistance gene. After plasmid ligation, recombinant plasmids were transferred into *E. coli* to get a clone via ampicillin selection. Cloned plasmids were then transferred into yeast cells. Yeast cells containing the plasmid were selected by tryptophane-deficient medium. Expression of the recombinant protein was induced by add galactose.

##### Test

After transformation of recombinant plasmid into *E. coli* and single colony collection, we perform enzyme digestion and gel electrophoresis to check if the ligation and transformation is successful. For expression assay, we incubated induced yeast cells with anti-flag-tag primary antibody. After incubating with FITC conjugated secondary antibody, cells were examined under florescence microscopy and flow cytometry.

##### Learn

Recombinant proteins were observed to express on the cell surfaces on a portion of the cell population. We therefore planned to further testify the effectiveness of our recombinant protein. Though previous modeling through Rosetta suggested that the recombinant Aga2 region as well as the linkers sequences do not undermine the correct folding of the VHH part, we still sought for a experimental support as well as a way to quantify the binding affinity.

#### Cycle 2
##### Design

In this cycle, we aimed to test binding affinity between the recombinant nanobody and the ipaD epitopes. ipaD were retrieved from NCBI database. Codon optimization was also performed to collect the DNA sequence. Similar to 20ipaD, flank regions were inserted into ipaD except the substitution of Flag-tag to HA-tag.

##### Build

Synthesized ipaD sequences were got from the same company. Using the same method, we expressed ipaD recombinant protein of the yeast surface.

#### Cycle 3
##### Design

In this cycle, we aims to improve the expression level of the recombinant protein. Energy flows within the yeast cells would be controlled to concentrate more on protein production rather than other metabolic activities. We started by looking for a strong and continuously expressed promoter to drive the expression of 20ipaD recombinant protein. At the same time, we also tried to reduce other cellular activities.

#### Cycle 4
##### Design

In this cycle, we aims to improve the binding affinity of the recombinant protein with the antigen epitope. We would perform error prone PCRs to introduce mutations into 20ipaD sequences. Concentrations of the nucleotide analogs would be controlled so that only point mutants would be produced. All mutants would be screened to identify binding affinity improvements. To reduce the workload of screening, we would perform a modeling prescreen. In the prescreen, we would predict how single amino acid change influence the binding affinity between 20ipaD and ipaD.

### *Lactococcus lactis*
#### Cycle 1
##### Design

At first, we wanted to obtain the sequence of both 20ipaD and control flag-tag so that we could amplify them via PCR reaction. The 20ipaD is one of the single-VH domain antibodies (VHHs) capable of recognizing distinct epitopes within the antigen IpaD of pathogen Shigella. In this way, we hoped that by fusing 20ipaD and control flag-tag into the *Lactococcus lactis* expression vector pNZ8148, we would achieve the surface display and expression of 20ipaD on *Lactococcus lactis*.

##### Build

To obtain the sequence of 20ipaD, we constructed the plasmid with the 20ipaD sequence surrounded by two different restriction sites of enzymes BamHI and SacI. In this way, through the restrictive digestion of *Bam*HI and *Sac*I, ideally the sequence of 20ipaD would be obtained. The similar construction was also applied with the sequence of control flag-tag, where the enzymes used for restrictive digestion were changed to be NcoI and HindIII.

##### Test

After successfully received the synthesized plasmid sequence for 20ipaD and control flag-tag, we conducted the digestion of BamHI and SacI for the obtain of 20ipaD sequence, and the digestion of *Nco*I and *Hind*III for the obtain of control flag-tag sequence. Gel electrophorese was applied to confirm the size of the sequence. Control flag-tag sequence was successfully obtained. However, according to the gel picture, the band of 20ipaD showed a very different size from that in theory.

##### Learn

We checked the source of error and found that the designed sequence of 20ipaD has been inserted into the pUC19 vector when being synthesized by the company. Unfortunately, pUC19 vector also contained a restriction site for BamHI itself, thus leading to a different enzymatic digestion than what we have expected before.

#### Cycle 2
##### Design

Since pUC19 vector also contained a restriction site for BamHI itself, which would lead to unspecific enzymatic digestion and the failure of getting 20ipaD sequence, we redesigned the experimental steps in order to overcome such a problem.

##### Build

In this try, we would do the PCR amplification of 20ipaD sequence to insert it directly into the pNZ8148 vector first. This would circumvent the enzymatic digestion of pUC19 vector by BamHI that had the insertion of 20ipaD.

##### Learn

From this process we learnt that when the synthesized plasmid went wrong from our expectations, apart from directly asking the company to redo the synthesis, we could also alter the steps of ligation via PCR reaction to solve the problem.

#### Cycle 3

##### Design

We wanted to insert the engineered pNZ8148 vector with 20ipaD into the strain *Lactococcus lactis* NZ9000. According to literature review, electroporation is the commonly used technique to insert vectors into *Lactococcus lactis*.

##### Build

When the OD600 of *Lactococcus lactis* reached 0.3, the bacteria would be subjected to electroporation. The bacteria would be washed with liquid detergent I containing 0.5mol∙L-1 sucrose and 10% glycerol for the insertion of 0.2 μg vector. The pulse of electroporation was delivered by a Gene-Pulser (Scientz) at 25μF and 2.5kV, while the electroporation cuvette (0.2cm in size) was connected in parallel to a 400-Ω resistor (the parameters were searched online and were consulted from technician at Scientz). According to multiple researches done previously, the transformation efficiency would be the highest is the recovery time is 1.5h after electroporation.

##### Test

The process of electroporation was not successful because we failed to insert the vector into *Lactococcus lactis*.

##### Learn

We suspect that the making of electrocompetent cells might be the source of failure. After checking with the team advisor, we found that the type of glycerol used was intended for protein purification, which could cause problems for the electrocompetent cell.

#### Cycle 4
##### Design

To further increase efficiency, after doing more literature reviews we added the pretreatment of *Lactococcus lactis* with lithium acetate (LiAc) and/or dithiothreitol (DTT). We also substituted the type of glycerol used based on the previous error analysis.

##### Build

According to the newly found protocol, the Lactococcus lactis was firstly suspended at room temperature for 30 min in 8ml of 100mM LiAc, 10mM DTT, 0.6M sucrose, and 10mM Tris-HCl (pH=7.5). Following the treatment, *Lactococcus lactis* was pelleted and was resuspended in 1.5ml microcentrifuge tube, and was then washed as previously described. Afterwards, electroporation was conducted as previously described.

### *Escherichia coli*

![E.*coli* Engineering Cycle](https://static.igem.wiki/teams/4161/wiki/e-eng-cyc.png)

#### Cycle 1

##### Design

Initially, we planned to try three different nanobodies (20ipaD, JPS-G3, and JMK-H2) agianst the *Shigella* antigen ipaD from a research paper [^Barta,2017]. We also wanted to try two different surface display systems, beta domain of the E.*coli* outer membrane protein intimin [^Salema,2013] and the E.*coli* curli fiber protein, *csg*B [^Gelfat,2021]. Our target probiotic is E. *coli* Nissle 1917 [^Gelfat,2021]. By inserting the target nanobody sequence behind intimin or *csg*B, reconstructing the plasmid pET30a and transforming the plasmid into E.*coli* Nissle 1917, we expect the protein to be displayed on the surface of E.*coli*, so that it can capture the pathogen via antigen-antibody binding.

##### Build & Test

We designed the following sequences to make the recombinant protein.

- intimin-20ipaD-3xFLAG
  
- csgB-JMK-H2-3xFLAG
  
- JPS-G3-3xFLAG

- ipaD-3xHA

However, due to limitations in budget & time for gene synthesis, we only have JPS-G3-3xFLAG and ipaD-3xHA (inserted into pUC19 plasmids). By plasmid extraction, double digestion (*Bam*HI & *Xho*I) and PCR, we successfully obtained the sequences and verified the accuracy by Sanger sequencing, but we don't have csgB or intimin for surface display.

##### Learn

Complex sequences including potential harmful genes may impact synthesis efficiency.

#### Cycle 2

##### Design

Alternatively, we chose the curli fiber *csg*A [^Gelfat et. al., 2021] sequence for surface display.

##### Build & Test

We designed the following sequences:

- csgA-JPS-G3-3xFLAG

- csgA-ipaD-3xHA (displaying the antigen on the surface of E.*coli* BL21 to mimic *Shigella flexneri*, so that the effectiveness can be evaluated)

*csg*A gene is obtained from the E.*coli* strains (pGEX-4T-1-csgA-shMT) provided by the XJLTU iGEM team via PCR. To connect different parts, we plan to use overlapping PCR.

## Reference

[^Salema,2013]: Salema, V., Marín, E., Martínez-Arteaga, R., Ruano-Gallego, D., Fraile, S., Margolles, Y., Teira, X., Gutierrez, C., Bodelón, G., & Fernández, L. Á. (2013). Selection of Single Domain Antibodies from Immune Libraries Displayed on the Surface of E. coli Cells with Two β-Domains of Opposite Topologies. *PLoS ONE*, 8(9), e75126. <https://doi.org/10.1371/journal.pone.0075126>

[^Gelfat,2021]: Gelfat, I., Aqeel, Y., Tremblay, J. M., Jaskiewicz, J. J., Shrestha, A., Lee, J. N., Hu, S., Qian, X., Magoun, L., Sheoran, A., Bedenice, D., Giem, C., Manjula-Basavanna, A., Osburne, M. S., Tzipori, S., Shoemaker, C. B., Leong, J. M., & Joshi, N. S. (2021). Single domain antibodies against enteric pathogen virulence factors are active as curli fiber fusions on probiotic E. coli Nissle 1917 (p. 2021.06.18.448998). *bioRxiv*. <https://doi.org/10.1101/2021.06.18.448998>

[^Barta,2017]:Barta, M. L., Shearer, J. P., Arizmendi, O., Tremblay, J. M., Mehzabeen, N., Zheng, Q., Battaile, K. P., Lovell, S., Tzipori, S., Picking, W. D., Shoemaker, C. B., & Picking, W. L. (2017). Single-domain antibodies pinpoint potential targets within Shigella invasion plasmid antigen D of the needle tip complex for inhibition of type III secretion. J Biol Chem, 292(40), 16677-16687. <https://doi.org/10.1074/jbc.M117.802231>

[^Sierocki,2021]: Sierocki, R., Jneid, B., Orsini Delgado, M. L., Plaisance, M., Maillere, B., Nozach, H., & Simon, S. (2021). An antibody targeting type III secretion system induces broad protection against Salmonella and Shigella infections. PLoS Negl Trop Dis, 15(3), e0009231. <https://doi.org/10.1371/journal.pntd.0009231>
