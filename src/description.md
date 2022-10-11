<div class="h1-bg">
    <h1 class>Project Description</h1>
    <img src="https://static.igem.wiki/teams/4161/wiki/wetlab9-for-bg.png" />
</div>

## Background

The Shigella species is listed as one of the eight dangerous drug resistant bacteria[^CDC,2019], with associated mortalities projected to rise to 10 million globally by 2050. The use of conventional antibiotics aggravates the multidrug resistance of most Shigella strains. Besides aiding in the selection of resistant pathogens, antibiotics reduce intestinal species diversity and population, and disrupt the defensive, metabolic, and trophic functions of interdependent microbes [^Francino,2016]. Engineered probiotics with cell surface display systems are promising in tackling this problem due to a weaker selective pressure and specific binding proteins that are less likely to disrupt the host gut microbiome. Through literature review, E.*coli* Nissle 1917, yeast and L.*lactis* are chosen for expression because their probiotic nature present no known harm to the GI tract and the convenience in lab culturing.

## Design

**Yeast**
![Y_Design](https://static.igem.wiki/teams/4161/wiki/y-design.png)

- Idea of probiotics

Saccharomyces cerevisiae, or baker’s yeast, is widely used in food industry and scientific research. Its facultative anaerobic feature enables it to make fluffy bread1. Also, its variable metabolism pathways make it a good agent for alcohol fermentation and wine production2. Last but not least, the already-annotated genome makes it an excellent model organism for molecular biology research3. With all these features, yeasts have been considered to be safe by Food and Drug Administration for a long time. Apart from our treatment strategy, this probiotic has been engineered as new conceptual drugs for other diseases treatment, such as vaginal infections, diarrhea, and irritable bowel syndrome (IBS)4,5. Compared to other prokaryotic probiotics, the eukaryotic yeast could support more complex protein folding, which is favorable for the generation of antibodies of interest. Moreover, previous works have successfully developed a mature Aga proteins yeast surface display system, which have been put in practical use in vaccine selection and sorting6,7. This established surface display system largely reduces the engineering difficulty and increases the reliability of our engineering. Take all the considerations above, we put yeasts into our plan list.

- Design of pYD1-20ipaD plasmid for therapeutic yeast engineering

One of the most important proteins in type III secretion system (T3SS) of pathogenic Shigella called ipaD is our attack target8. Because ipaD is the primary trigger to form translocon pores within the host cell membrane, the inhibition of it would probably inhibit the invasion of Shigella and thus treat the infection9,10. Several single domain antibodies (nanobodies) have been previously reported to target ipaD, the most efficient of which is 20ipaD11. Therefore, 20ipaD was chosen for further engineering. To have the yeasts displayed 20ipaD on surface, we adopted the strategy of Aga2 yeast surface display system. Aga2 is a membrane protein of S. cerevisiae, which would be sealed on membrane by the interaction with Aga16. By fusing the Aga2 protein with 20ipaD, the nanobody could thus be brought to the membrane, and that was what we designed as shown in the figure. Additionally, we introduced 3xFLAG tag behind 20ipaD for expression assays like immunofluorescent microscopic imaging, western blot, and FACS. The whole expression module was designed under the control of GAL1 promotor that can be induced by galactose to control the expression of the proteins of interest. We used pYD1 vector as the backbone which contains ampicillin resistance marker, E. coli replication origin, and tryptophan deficiency marker. These features enable us to store the recombinant plasmids in E. coli, and easily select the yeasts after transformation.

- Design of pYD1-ipaD plasmid for efficiency detection

Shigella is one of the most infectious pathogens characterized by CDC12. Considering the health risks that could be risen during the experiments, we replace the real Shigella by yeasts anchored with the targeted epitope protein ipaD. The construction strategy of pYD1-ipaD was same as the pYD1-20ipaD discussed above except for the replacement of FLAG tag with HA tag. The yeasts containing pYD1-ipaD could display the antigen ipaD on their surfaces to mimic Shigella. With this pathogen analog, the binding affinity of the engineered therapeutic yeasts between the fake pathogens could be measured by whole cell ELISA and other binding affinity assays.

- Design of high production and high binding affinity plasmids for efficiency optimization

After the proving the construction and binding capacity of the engineered yeast, optimization would be done to increase the efficiency of the product. Expression efficiency and binding affinity would be the two main aspects of optimization. To increase the expression efficiency of the nanobody, previously reported strong promoters, including SSA1 and PGK1, would be introduced to replace GAL1 promoter13. The expression abundancy would be compared, and the optimized promoter would be chosen. To increase the binding affinity of the nanobody, random mutations would be introduced to the 20ipaD sequence by error-prone PCR. The library would be screened for the optimization of nanobody targeting.

- Design of delivery of the engineered therapeutic yeasts by Shellac-based microcapsules

Microbes, especially yeasts, are hard to preserve for a long time under room temperature. Besides, the acidic and digestive environment inside the gut prevents most organisms from getting to the intestine where Shigella locates in. In order to preserve the engineered yeasts and deliver them into the intestine with smallest deficiency, we designed the shellac-cased microcapsules. Shellac is a natural material that can be used as encapsulating material for microcapsules that can wrap and package molecular matters like drugs and cells14. The properties of shellac include high intensity, which can protect the encapsuled matters; hydrophobicity, making it easier for storage; only disintegrate at basic solution, which means that the microcapsules would not disintegrate in the acidic environment of stomach, but only dissolve in basic environment of small intestine where the target pathogen resides 15. Previous research has proven the efficiency of shellac microcapsules delivery of probiotics16,17,18. With the light of this, we also designed the capsulation for the engineered yeasts. By producing the microcapsule powder of yeasts, they can be subsequently packaged into macro capsule entities and be productized.

**References**

1.	Sicard, D., Jean Luc, J., Legras, L. (2011). Bread, beer and wine: Yeast domestication in the Saccharomyces sensu stricto complex. Comptes Rendus Biologies, Elsevier, 2011, 229 - 236. ⟨10.1016/j.crvi.2010.12.016⟩. ⟨hal-02653082⟩

2.	Holt, S., Miks, M. H., de Carvalho, B. T., Foulquié-Moreno, M. R., Thevelein, J. M. (2019 May) The molecular biology of fruity and floral aromas in beer and other alcoholic beverages, FEMS Microbiology Reviews, 43(3), 193–222, https://doi.org/10.1093/femsre/fuy041

3.	Piskur, J., Langkjaer, R. B. (2004). Yeast genome sequencing: the power of comparative genomics. Molecular microbiology, 53(2), 381–389. https://doi.org/10.1111/j.1365-2958.2004.04182.x

4.	Gaziano, R., Sabbatini, S., Roselletti, E., Perito, S., Monari, C. (2020). Saccharomyces cerevisiae-Based Probiotics as Novel Antimicrobial Agents to Prevent and Treat Vaginal Infections. Frontiers in microbiology, 11, 718. https://doi.org/10.3389/fmicb.2020.00718

5.	Palma, M. L., Zamith-Miranda, D., Martins, F. S., Bozza, F. A., Nimrichter, L., Montero-Lomeli, M., Marques, E. T., Jr, Douradinha, B. (2015). Probiotic Saccharomyces cerevisiae strains as biotherapeutic tools: is there room for improvement?. Applied microbiology and biotechnology, 99(16), 6563–6570. https://doi.org/10.1007/s00253-015-6776-x

6.	Boder, E. T., Wittrup, K. D. (1997). Yeast surface display for screening combinatorial polypeptide libraries. Nature biotechnology, 15(6), 553–557. https://doi.org/10.1038/nbt0697-553

7.	Chao, G., Lau, W. L., Hackel, B., Sazinsky, S, L., Lippow, S. M., Wittrup, k. D. (2006). Isolating and engineering human antibodies using yeast surface display. Nature Protocol 1, 755–768, 755-770. https://doi.org/10.1038/nprot.2006.94

8.	Wagner, S.; Galan, J. E. Bacteria Type III Protein Secrete System. Springer Nature Switzerland: 2020.

9.	Dickenson, N. E., Zhang, L., Epler, C. R., Adam, P. R., Picking, W. L., Picking, W. D. (2011). Conformational changes in IpaD from Shigella flexneri upon binding bile salts provide insight into the second step of type III secretion. Biochemistry, 50(2), 172–180. https://doi.org/10.1021/bi101365f

10.	Epler, C. R., Dickenson, N. E., Olive, A. J., Picking, W. L., & Picking, W. D. (2009). Liposomes recruit IpaC to the Shigella flexneri type III secretion apparatus needle as a final step in secretion induction. Infection and immunity, 77(7), 2754–2761. https://doi.org/10.1128/IAI.00190-09

11.	Barta, M. L., Shearer, J. P., Arizmendi, O., Tremblay, J. M., Mehzabeen, N., Zheng, Q., Battaile, K. P., Lovell, S., Tzipori, S., Picking, W. D., Shoemaker, C. B., Picking, W. L. (2017). Single-domain antibodies pinpoint potential targets within Shigella invasion plasmid antigen D of the needle tip complex for inhibition of type III secretion. The Journal of biological chemistry, 292(40), 16677–16687. https://doi.org/10.1074/jbc.M117.802231

12.	Centers for Disease Control and Prevention. (2020). Shigella-Shigellosis. https://www.cdc.gov/shigella/index.html

13.	Peng, B., Williams, T. C., Henry, M., Nielsen, L. K., Vickers, C. E. (2015). Controlling heterologous gene expression in yeast cell factories on different carbon substrates and across the diauxic shift: a comparison of yeast promoter activities. Microbial cell factories, 14, 91. https://doi.org/10.1186/s12934-015-0278-5

14.	Huang, X., Gänzle, M., Zhang, H., Zhao, M., Fang, Y., Nishinari, K. (2020). Microencapsulation of probiotic lactobacilli with shellac as moisture barrier and to allow controlled release. Journal of the Science of Food and Agriculture. 101. 10.1002/jsfa.10685.

15.	Huang. X., Zhang, H., Peng, S., Zhao, M., Fang, Y. (2019). Tianrankeshixing Bicaichongjiao zai Gongnengzufenweinanghua zhongde Yingyonngyanjiujinzhan [Recent Progress in the Application Shellac as a Natural Edible Wall Material in the Microencapsulation of Functional Ingredients]. Shipinkexue [Food Science], 40(7), 317-324.

16.	Mei, S., Han, P., Wu, H., Shi, J., Tang, L., Jiang, Z. (2018). One-pot fabrication of chitin-shellac composite microspheres for efficient enzyme immobilization. Journal of biotechnology, 266, 1–8. https://doi.org/10.1016/j.jbiotec.2017.11.015

17.	Gately, N. M., Kennedy, J. E. (2017). The Development of a Melt-Extruded Shellac Carrier for the Targeted Delivery of Probiotics to the Colon. Pharmaceutics, 9(4), 38. https://doi.org/10.3390/pharmaceutics9040038

18.	Hamad, S. A., Stoyanov, S. D., Paunov, V. N. (2013). Triggered release kinetics of living cells from composite microcapsules. Physical chemistry chemical physics: PCCP, 15(7), 2337–2344. https://doi.org/10.1039/c2cp42100c


**Lactococcus**

![L_Design](https://static.igem.wiki/teams/4161/wiki/l-design.png)

- Idea of probiotics

The target probiotics, _Lactococcus lactis (L. lactis)_, is a lactic acid-producing Gram-positive species of bacteria that is used extensively in the food fermentation industry like the production of cheese and yoghurt. Therefore, it is generally considered as safe (GRAS) status by the Food and Drug Administration (Song, In, Lim, & Rahim, 2017). Apart from its important function in making food, _L. lactis _is often applied as the genetically modified organism for disease treatment of animals and humans (Braat et al., 2006; de Moreno de LeBlanc et al., 2016). In many parts, it acts as an alternative for the gram positive to Bacillus subtilis and Lactobacillus plantarum, while it can also substitute the gram-negative counterpart, Escherichia coli (García-Fruitós, 2012). The small genome size (2.3 Mbp) that has been fully sequenced, plus the development of successfully compatible tools including cloning and expression systems with customizable options, have turned _L. lactis _into a desirable model for genetic engineering (Song et al., 2017). 

- Design of 20ipad plasmid

Due to the wide use of antibiotics, various types of bacteria have developed antibiotic resistance, thus providing great challenge to human health and therapy design. Our team’s target pathogen, the Shigella spp., is no exception. To overcome the issue of antibiotic resistance, we would like to engineer the probiotics to make it an effective tool for the treatment of shigella infections. Through literature review, it is identified that in the process of shigellosis (also named bacillary dysentery), Shigella uses the type III secretion system (T3SS) to invade colonic epithelial cells. Importantly, one important feature of T3SS is the existence of an extracellular needle with an associated tip complex responsible for assembly of a pore-forming translocon in the host cell membrane (Barta et al., 2017). For Shigella flexneri, the tip complex contains invasion plasmid antigen D (IpaD) that not only regulates secretion but also provides the physical platform for the translocon pore (Barta et al., 2017; Muthuramalingam, Whittier, Picking, & Picking, 2021). To explore the potential therapeutic avenues for managing infections of Shigella, researchers have developed single-VH domain antibodies (VHHs) that are capable of recognizing distinct epitopes within the antigen IpaD (Barta et al., 2017), where one of such VHHs is the 20ipaD applied by our team. In order to have our probiotics L. lactis express the 20ipaD, we firstly constructed the 20ipaD plasmid. For plasmid design, the Usp45 signal peptide was included for secretion to the growth medium, while AcmA3b was included for surface anchoring of the expressed 20ipaD to _L. lactis_ (Plavec & Berlec, 2019). Flag-tag was added for the convenience of purification. Sequence of 20ipaD was surrounded by two restriction sites (BamHI and SacI respectively). The aim for such a design is that ideally, through the digestion of restriction enzymes, 20ipaD sequence could be obtained. 

- Design of control group (3*Flag tag) with Flag-tag sequence

In our future stage, we would fuse the _Lactococcus lactis_ expression vector pNZ8148 with control flag-tag*3 to benefit the examination procedures, here the plasmid containing control group (3*Flag tag) with Flag-tag sequence was designed so that we could get the sequence of control flag-tag*3 from the plasmid. Construction of the plasmid was similar to that of 20ipaD, with Usp45 signal peptide (indicated in yellow) and AcmA3b (indicated in green) included. The sequence of control flag-tag*3 is shown in blue. Two restriction sites for the enzyme NcoI (indicated in dark green) and HindIII (indicated in dark blue) were designed so that during enzymatic digestion, sequence of control flag-tag*3 would be obtained. 


References

Barta, M., Shearer, J., Arizmendi, O., Tremblay, J., Mehzabeen, N., Zheng, Q., . . . Picking, W. (2017). Single-domain antibodies pinpoint potential targets within Shigella invasion plasmid antigen D of the needle tip complex for inhibition of type III secretion. Journal of Biological Chemistry, 292, jbc.M117.802231. doi:10.1074/jbc.M117.802231

Braat, H., Rottiers, P., Hommes, D. W., Huyghebaert, N., Remaut, E., Remon, J. P., . . . Steidler, L. (2006). A phase I trial with transgenic bacteria expressing interleukin-10 in Crohn's disease. Clin Gastroenterol Hepatol, 4(6), 754-759. doi:10.1016/j.cgh.2006.03.028

de Moreno de LeBlanc, A., Del Carmen, S., Chatel, J. M., Azevedo, V., Langella, P., Bermudez-Humaran, L., & LeBlanc, J. G. (2016). Evaluation of the biosafety of recombinant lactic acid bacteria designed to prevent and treat colitis. J Med Microbiol, 65(9), 1038-1046. doi:10.1099/jmm.0.000323

García-Fruitós, E. (2012). Lactic acid bacteria: a promising alternative for recombinant protein production. Microbial Cell Factories, 11(1), 157. doi:10.1186/1475-2859-11-157

Muthuramalingam, M., Whittier, S. K., Picking, W. L., & Picking, W. D. (2021). The Shigella Type III Secretion System: An Overview from Top to Bottom. Microorganisms, 9(2). doi:10.3390/microorganisms9020451

Plavec, T. V., & Berlec, A. (2019). Surface Anchoring on Lactococcus lactis by Covalent Isopeptide Bond. Acta Chim Slov, 66(1), 18-27. 

Song, A. A.-L., In, L. L. A., Lim, S. H. E., & Rahim, R. A. (2017). A review on Lactococcus lactis: from food to factory. Microbial Cell Factories, 16(1), 55. doi:10.1186/s12934-017-0669-x




**E. coli**
![E_design](https://static.igem.wiki/teams/4161/wiki/e-design.png)


[^CDC,2019]: Centers for Disease Control and Prevention. (2019). 2019 AR
Threats Report. <https://www.cdc.gov/drugresistance/biggest-threats.html>

[^Francino,2016]: Francino, M. P. (2016, January 1). Antibiotics and the human
gut microbiome: Dysbioses and accumulation of resistances. Frontiers. Retrieved
March 28, 2022, from
<https://www.frontiersin.org/articles/10.3389/fmicb.2015.01543/full>
