# Results

## Introduction

This page will give a detailed record about the experiment results, future plans & project achievements.  

## Experiment Results

### Yeast

#### Summary of Lab Design
In order to decorate the yeast surface with nanobodies against the pathogen, we designed the vector which contains the nanobody gene behind a membrane-sealed protein. The overall experiment design could be divided into 3 phases. In phase I, the expected vector that could potentially express our designed module would be constructed and stored. In phase II, the expression vector would be transformed into yeast and detected for its expression abundance and location. In phase III, the binding affinity and inhibitory efficiency on pathogen would be tested. Due to the limitation of materials and time under the background of local pandemic situation, the experiments only accomplished Phase I & II.

#### Genes of nanobody and pathogen were harvested
The DNA sequence of nanobody 20ipaD and antigen ipaD were obtained from Sangon in the form of pUC19 plasmid insertions, which were stored inside E. coli. The storage bacteria were amplified, and plasmids containing sequences of interest were extracted with Plasmid mini-prep kit from TIangen. Those plasmids were digested by XhoI and ApaI, and the sequences of interest were recycled by agarose gel recycle kit from Beyotime (**Fig1**).

#### Recombinant plasmids were constructed
The purified ipaD and 20ipaD DNA segments mentioned in the previous section, along with the pYD1 vector digested by XhoI & ApaI, were ligated, and transformed into DH5α cells that were selected by ampicillin. Colony direct PCR was applied to inspect the plasmid condition of the colonies formed. pYD1-forward and pyd1-reverse primers were used to show the size of Aga2-Protein, thus verifying the sequence between the primer pairs (**Table 1**). The size of pYD1-ipaD plasmid primer box should be about 1500bp, while the size of pYD1-20ipaD should be about 1000bp. As shown in **Fig2 a**, sample “2-3”, “2-5” meet the requirement for pYD1-ipaD, so the bacteria in those colonies contain the recombinant plasmid pYD1-ipaD. Additionally, all samples in lane 1~10 met the requirement for pYD1-ipaD, which indicates the bacteria in those colonies contain pYD1-20ipad recombinant plasmids (**Fig2 b**). Those colonies were amplified, and the plasmids were extracted. Sequencing data further supported the successful construction of the recombinant plasmids (**Fig3**).

#### Recombinant plasmids were transformed into yeast EBY100
We performed yeast transformation using constructed pYD1-ipaD and pYD1-20ipaD plasmids. Yeast competent cells were prepared by Frozen-EZ Yeast transformation II kit (Zymo Research, T2001). The yeasts were successfully transformed by chemical method using carrier DNA and PEG/LiAc. The plasmids and competent cells were thawed on ice. 10μL of Carrier DNA and 2μg of plasmid was added into 100μL of competent cells. Then 500μL of PEF/LiAc solution was added. The tube was inverted 6-8 times and incubated at 30°C with an inversion at 10-minute interval. Then, 20μL of DMSO was added to increase the transformation efficiency. Then, the tube was incubated under 42°C with an inversion of 5-minute interval. The cells were centrifuged at 12000rpm for 5 seconds and incubated with YPD medium for 1 hour at 30°C. After incubation, the cells were pelleted and resuspend by 100μL of 0.9% NaCl, 50μL of which were spread onto SDCAA medium, and another 50μL of cells onto YPD medium. The plates were incubated at 30°C for 2 days.

The result of the plates was positive (**Fig4**). SDCAA plates, which are the selective plates lack of tryptophan, has demonstrated fewer colony growth compared to YPD plates, indicating successful transformation. Single colonies were taken and incubated at 30°C in SDCAA liquid medium for amplification.

#### Nanobody and pathogen were expressed and displayed on yeast surface
The yeasts that were transformed with pYD1-ipaD, pYD1-20ipaD, and pYD1 were amplified in SDCAA liquid medium for 36h. The cells were harvested by centrifuge at 5000xg for 5 minutes and diluted in SGCAA liquid containing the induction agent galactose to obtain an OD600=0.5. Four milliliters of each diluted cells were transferred into new culture tubes and induced at 21°C for 24h. An additional prep of EBY100 cells without plasmids were also diluted to OD600=0.5 and induced in SGCAA for 24h.

The induced cells were harvested and washed with PBS. The yeasts containing pYD1-ipaD were inoculated with rabbit anti-HA tag antibodies, while the yeasts containing pYD1-20ipaD, pYD1, or no plasmids were inoculated with rabbit anti-FLAG tag antibodies and BSA. After washed with PBS, the cells were inoculated with FITC-conjugated goat anti-rabbit immunoglobin antibodies and BSA without light. The cells were washed twice with PBS before imaged under UV-light. As **Fig5** shows, the yeasts containing pYD1-ipaD and pYD1-20ipaD emitted green fluorescence, whereas the yeasts containing empty plasmids, or no plasmids did not. This fluorescence pattern proved the yeasts indeed expressed and displayed the nanobody and the antigen on their surfaces, which announced the success of engineering.

![y-fig-1](https://static.igem.wiki/teams/4161/wiki/y-fig-1.png)


![y-fig-2](https://static.igem.wiki/teams/4161/wiki/y-fig-2.png)


![y-fig3](https://static.igem.wiki/teams/4161/wiki/y-fig3.png)


![y-fig4](https://static.igem.wiki/teams/4161/wiki/y-fig4.png)


![y-fig5](https://static.igem.wiki/teams/4161/wiki/y-fig5.png)


### *Lactococcus lactis*

### *Escherichia coli*

#### Summary of Experiment Design
We plan to display the nanobody JPS-G3 agianst the *Shigella* antigen ipaD on the surface of E.*coli* Nissle 1917 via the curli fiber protein *csg*A [^Gelfat,2021]. We expect the engineered E.*coli* Nissle 1917 to be capable of capturing the pathogen *Shigella flexneri* via antigen-antibody specific binding. Please check the detailed experiment design at 'design' part.

#### Plasmid Extraction
pUC19-JPS-G3-3xHA and pUC19-ipaD-3xHA were extracted using the TIANGEN plasmid extraction kit.

#### Target Sequence Amplification
Using following primers (**Table 1**), the JPS-G3-3xHA and ipaD-3xHA sequences were successfully amplified, and the results were verified by gel electrophoresis (**Figure 1**). PCR products were purified for further manipulation.

**Table 1** | PCR Primers Used

| Name | Sequence (5' -> 3') | Endonuclease Site |
| --- | --- | --- |
| ipaD_FW | CGCGGATCCATGAATATTACAACTC | *Bam*HI |
| ipaD_RV | GGCCTCGAGTCAAGCGTAG | *Xho*I |
| JPS-G3_FW | CGCGGATCCGGAAGTACACAAGTACAGCTAG | *Bam*HI |
| JPS-G3_RV | CGCGGATCCGGAAGTACACAAGTACAGCTAG | *Xho*I |

<img src="https://static.igem.wiki/teams/4161/wiki/e-labnote-8-31-1.png" width="500"/>

**Figure 1** | Gel Electrophoresis Result for Target Sequence Amplification

#### Molecular Cloning for Cytoplasmic Protein Expression
In order to construct the recombinant plasmids pET30a-ipaD-3xHA and pET30a-JPS-G3-3xFLAG, the PCR products obtained from the last step were digested by endonucleases *Bam*HI and *Xho*I to create sticky ends. Meanwhile, the pET30a plasmids were transformed into E.*coli* DH5a competent cells for propagation. After transformation and overnight culture, the extracted plasmids were also digested with endonucleases *Bam*HI and *Xho*I to create sticky ends. Afterwards, the digested plasmids and target sequences were ligated and transformed into E.*coli* DH5a competent cells (**Figure 2**).

<img src="https://static.igem.wiki/teams/4161/wiki/e-labnote-9-13-2.jpg" width="500"/>

**Figure 2** | Plates for pET30a-ipaD-3xHA (i-1 & i-2) and pET30a-JPS-G3-3xFLAG (J-1 & J-2).

Single colonies were picked from the plates and the inserted sequence were verified by colony PCR (**Figure 3**) and Sanger sequencing.

<img src="https://static.igem.wiki/teams/4161/wiki/e-labnote-9-14-1.png" width="500"/>

**Figure 3** | Gel Electrophoresis Result for Colony PCR

#### Overlap Extension PCR
In order to construct the recombinant DNA sequences csgA-JPS-G3-3xFLAG and csgA-ipaD-3xHA, the following overlap extension PCR primers are used (**Table 2**).

**Table 2** | Overlap Extension PCR Primers

|Name|Sequence (5' -> 3')|Endonuclease Site|
|---|---|---|
|OvF_csgA-shMT|CCGCGTGGATCCATGAAACTTTTAAAAGTAG|*Bam*HI |
|OvR1_csgA-shMT|TAGCTGTACTTGTGTACTTCCCCGCTGCCGCCGTACTGATGA|/|
|OvR2_csgA-shMT|TAGTCAGAGTTGTAATATTCATCCGCTGCCGCCGTACTGATGA|/|
|OvF_JPS-G3|CATCAGTACGGCGGCAGCGGGGAAGTACACAAGTACAGCTAGC|/|
|OvR_JPS-G3|GAATCTCGAGTTATTTGTCGTCGTCATCC|*Xho*I|
|OvF_ipaD|CATCAGTACGGCGGCAGCGGATGAATATTACAACTCTGACTAAT|/|
|OvR_ipaD|GGCCTCGAGTCAAGCGTAGTCAGGTAC|*Xho*I|

However, due to time limitation, this part has not been successfully implemented.

## Project Achievements & Analysis Summary

(只是举例，请随意更改)

### Successes

- Constructed the recombinant xxx plasmid, and transformed it into xxx strain.

- Expressed xxx protein.

- Effectiveness tested by xxx.

### Failures

- Failed to construct and transform the recombinant plasmids in E.*coli* and L.*lactis*.

### Inspirations

-

## Future Plans

(只是举例，请随意更改)

- Express proteins in well-studied probiotic strains.

- Insert nanobody sequences after other promoters that can ensure proper expression *in vivo*.

- Conduct hemolysis experiments to see the effectiveness of killing *Shigella flexneri*.

- Conduct *in vivo* experiments to test the therapeutic effects in rodent GI system.

## Reference

[^Gelfat,2021]: Gelfat, I., Aqeel, Y., Tremblay, J. M., Jaskiewicz, J. J., Shrestha, A., Lee, J. N., Hu, S., Qian, X., Magoun, L., Sheoran, A., Bedenice, D., Giem, C., Manjula-Basavanna, A., Osburne, M. S., Tzipori, S., Shoemaker, C. B., Leong, J. M., & Joshi, N. S. (2021). Single domain antibodies against enteric pathogen virulence factors are active as curli fiber fusions on probiotic E. coli Nissle 1917 (p. 2021.06.18.448998). *bioRxiv*. <https://doi.org/10.1101/2021.06.18.448998>
