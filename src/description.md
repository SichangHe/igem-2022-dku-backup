<div class="h1-bg">
    <h1 class>Project Description</h1>
    <img src="https://static.igem.wiki/teams/4161/wiki/wetlab9-for-bg.png" />
</div>

## Background

The *Shigella* species is listed as one of the eight dangerous drug-resistant bacteria[^Langdon2016], with associated mortalities projected to rise to 10 million globally by 2050, if not properly addressed[^ONeill2014].
In the United States alone, over 77,000 antibiotic-resistant cases were reported annually and 90% of overall *Shigella* cases were found to be resistant to the first choice medication ciprofloxacin[^CDC2015].
*Shigella*, as a highly infective, enteroinvasive and occasionally toxin-releasing[^Carayol2013] [^Gray2015]
bacterial genus, may cause severe infection and bacterial dysentery in the colorectal mucosa even with as low a dose as 10 - 100 organisms[^Garcia2014].
*Shigella*-related infections thereby spread rapidly, particularly in low-resource populations[^Hussen2019] and among vulnerable groups including children in care facilities, the homeless, and returned travelers[^CDC2020] [^Huruy2018] [^Casabonne2016] [^Gray2015].

The use of conventional antibiotics aggravates the multidrug resistance of most *Shigella* strains. Besides aiding in the selection of resistant pathogens, antibiotics reduce intestinal species diversity and population, and disrupt the defensive, metabolic, and trophic functions of interdependent microbes [^Francino2016].
Although antibiotics are able to prevent and treat infections, antibiotic exposure to the intestinal microbiota can lead to loss of colonization resistance, rendering the host more susceptible to future invasion[^Kim2017] [^Shad2021].

Engineered probiotics with cell surface display systems are an especially promising alternative that improves *Shigella* eradication rates without heavy reliance on antibiotics.
Single VH domain (VHH) antibodies displayed on the probiotic surface reduce the virulent activity of *Shigella*[^Roehrich2013] through probiotic-pathogen binding while minimizing toxicity to non-targets[^Barta2017] [^Tremblay2013]. Specifically, these antibodies recognize and target epitopes within the tip complex that is conserved across all pathogens that utilize type III secretion system (T3SS) to translocate effector proteins into the host cells[^Barta2017].
Innovations in VHH-IpaD binding not only offer a solution that preserves the potency of antibiotics and microbial composition of the gut microbiome, but also illuminates targeted approaches to treat related T3SS bacteria like Salmonella and enterohemorrhagic *E. coli*, and other novel opportunities for passive immunization[^Greve2019].

Engineered probiotics with cell surface display systems are an especially promising alternative that improves *Shigella* eradication rates without heavy reliance on antibiotics. Single VH domain (VHH) antibodies displayed on the probiotic surface reduce the virulent activity of *Shigella*[^Roehrich2013] through probiotic-pathogen binding while minimizing toxicity to non-targets[^Barta2017] [^Tremblay2013]. Specifically, these antibodies recognize and target epitopes within the tip complex that is conserved across all pathogens that utilize type III secretion system (T3SS) to translocate effector proteins into the host cells[^Barta2017]. Innovations in VHH-IpaD binding not only offer a solution that preserves the potency of antibiotics and microbial composition of the gut microbiome, but also illuminates targeted approaches to treat related T3SS bacteria like *Salmonella* and enterohemorrhagic *E. coli*, and other novel opportunities for passive immunization[^Greve2019].

## Design

### Yeast

![Y_Design](https://static.igem.wiki/teams/4161/wiki/y-design.png)

#### Idea of probiotics

*Saccharomyces cerevisiae*, or baker's yeast, is widely used in the food industry and scientific research.
Its facultative anaerobic feature enables it to make fluffy bread[^Sicard2011].
Also, its variable metabolism pathways make it a good agent for alcohol fermentation and wine production[^Holt2019].
Last but not least, the already-annotated genome makes it an excellent model organism for molecular biology research[^Piskur2004].
With all these features, yeasts have been considered to be safe by Food and Drug Administration for a long time.
Apart from our treatment strategy, this probiotic has been engineered as new conceptual drugs for other diseases treatment, such as vaginal infections, diarrhea, and irritable bowel syndrome (IBS)[^Gaziano2020] [^Palma2015].
Compared to other prokaryotic probiotics, the eukaryotic yeast could support more complex protein folding, which is favorable for the generation of antibodies of interest.
Moreover, previous works have successfully developed a mature Aga proteins yeast surface display system, which has been put to practical use in vaccine selection and sorting[^Boder1997] [^Chao2006].
This established surface display system largely reduces the engineering difficulty and increases the reliability of our engineering.
Take all the considerations above, we put yeasts into our plan list.

#### Design of pYD1-20ipaD plasmid for therapeutic yeast engineering

One of the most important proteins in the type III secretion system (T3SS) of pathogenic *Shigella* called IpaD is our attack target[^Wagner2020].
Because IpaD is the primary trigger to form translocon pores within the host cell membrane, the inhibition of it would probably inhibit the invasion of *Shigella* and thus treat the infection[^Dickenson2011] [^Epler2009].
Several single-domain antibodies (nanobodies) have been previously reported to target IpaD, the most efficient of which is 20ipaD.
Therefore, 20ipaD was chosen for further engineering.
To have the yeasts displayed 20ipaD on the surface, we adopted the strategy of Aga2 yeast surface display system.
Aga2 is a membrane protein of *S. cerevisiae*, which would be sealed on the membrane by the interaction with Aga16.
By fusing the Aga2 protein with 20ipaD, the nanobody could thus be brought to the membrane, and that was what we designed as shown in the figure.
Additionally, we introduced 3xFLAG tag behind 20ipaD for expression assays like immunofluorescent microscopic imaging, western blot, and FACS.
The whole expression module was designed under the control of GAL1 promotor that can be induced by galactose to control the expression of the proteins of interest.
We used pYD1 vector as the backbone which contains an ampicillin resistance marker, *E. coli* replication origin, and tryptophan deficiency marker.
These features enable us to store the recombinant plasmids in *E. coli*, and easily select the yeasts after transformation.

#### Design of pYD1-IpaD plasmid for efficiency detection

*Shigella* is one of the most infectious pathogens characterized by CDC[^CDC2020].
Considering the health risks that could be risen during the experiments, we replace the real *Shigella* by yeasts anchored with the targeted epitope protein IpaD.
The construction strategy of pYD1-IpaD was the same as the pYD1-20ipaD discussed above except for the replacement of FLAG tag with HA tag.
The yeasts containing pYD1-IpaD could display the antigen IpaD on their surfaces to mimic *Shigella*.
With this pathogen analog, the binding affinity of the engineered therapeutic yeasts between the fake pathogens could be measured by whole-cell ELISA and other binding affinity assays.

#### Design of high production and high binding affinity plasmids for efficiency optimization

After proving the construction and binding capacity of the engineered yeast, optimization would be done to increase the efficiency of the product.
Expression efficiency and binding affinity would be the two main aspects of optimization.
To increase the expression efficiency of the nanobody, previously reported strong promoters, including SSA1 and PGK1, would be introduced to replace GAL1 promoter[^Peng2015].
The expression abundance would be compared, and the optimized promoter would be chosen.
To increase the binding affinity of the nanobody, random mutations would be introduced to the 20ipaD sequence by error-prone PCR.
The library would be screened for the optimization of nanobody targeting.

#### Design of delivery of the engineered therapeutic yeasts by Shellac-based microcapsules

Microbes, especially yeasts, are hard to preserve for a long time under room temperature.
Besides, the acidic and digestive environment inside the gut prevents most organisms from getting to the intestine where *Shigella* locates in.
To preserve the engineered yeasts and deliver them into the intestine with the smallest deficiency, we designed the shellac-cased microcapsules.
Shellac is a natural material that can be used as encapsulating material for microcapsules that can wrap and package molecular matters like drugs and cells[^Huang2020].
The properties of shellac include high intensity, which can protect the encapsulated matters; hydrophobicity, making it easier for storage; only disintegration at the basic solution, which means that the microcapsules would not disintegrate in the acidic environment of the stomach, but only dissolve in basic environment of the small intestine where the target pathogen resides[^Huang2019].
Previous research has proven the efficiency of shellac microcapsules delivery of probiotics[^Mei2018] [^Gately2017] [^Hamad2013].
In light of this, we also designed the capsulation for the engineered yeasts.
By producing the microcapsule powder of yeasts, they can be subsequently packaged into macro capsule entities and be productized.

### Lactococcus

![L_Design](https://static.igem.wiki/teams/4161/wiki/l-design.png)

#### Idea of probiotics

The target probiotics, *Lactococcus lactis (L. lactis)*, is a lactic acid-producing Gram-positive species of bacteria that is used extensively in the food fermentation industry like the production of cheese and yogurt.
Therefore, it is generally considered safe (GRAS) status by the Food and Drug Administration[^Song2017].
Apart from its important function in making food, *L. lactis* is often applied as a genetically modified organism for disease treatment of animals and humans[^Braat2006] [^Moreno2016].
In many parts, it acts as an alternative for the gram-positive to *Bacillus subtilis* and *Lactobacillus plantarum*, while it can also substitute the gram-negative counterpart, *Escherichia coli*[García2012]. The small genome size (2.3 Mbp) that has been fully sequenced, plus the development of successfully compatible tools including cloning and expression systems with customizable options, have turned _L. lactis_into a desirable model for genetic engineering[^Song2017].

#### Design of 20ipaD plasmid

Due to the wide use of antibiotics, various types of bacteria have developed antibiotic resistance, thus providing great challenges to human health and therapy design.
Our team's target pathogen, the *Shigella* spp., is no exception.
To overcome the issue of antibiotic resistance, we would like to engineer probiotics to make them effective tools for treating *Shigella* infections.
Through literature review, it is identified that in the process of shigellosis (also named bacillary dysentery), *Shigella* uses the type III secretion system (T3SS) to invade colonic epithelial cells.
Importantly, one important feature of T3SS is the existence of an extracellular needle with an associated tip complex responsible for the assembly of a pore-forming translocon in the host cell membrane[^Barta2017].
For *Shigella flexneri*, the tip complex contains invasion plasmid antigen D (IpaD) that not only regulates secretion but also provides the physical platform for the translocon pore[^Barta2017] [^Muthuramalingam2021].
To explore the potential therapeutic avenues for managing infections of *Shigella*, researchers have developed single-VH domain antibodies (VHHs) that are capable of recognizing distinct epitopes within the antigen IpaD[^Barta2017], where one of such VHHs is the 20ipaD applied by our team.
In order to have our probiotics *L. lactis* express the 20ipaD, we first constructed the 20ipaD plasmid.
For plasmid design, the Usp45 signal peptide was included for secretion to the growth medium, while AcmA3b was included for surface anchoring of the expressed 20ipaD to *L. lactis*[^Plavec2019].
Flag-tag was added for the convenience of purification.
The sequence of 20ipaD was surrounded by two restriction sites (BamHI and SacI respectively).
The aim for such a design is that ideally, through the digestion of restriction enzymes, 20ipaD sequence could be obtained.

#### Design of control group (3*Flag tag) with Flag-tag sequence

In our future stage, we would fuse the *Lactococcus lactis* expression vector pNZ8148 with control flag-tag*3 to benefit the examination procedures, here the plasmid containing control group (3*Flag tag) with Flag-tag sequence was designed so that we could get the sequence of control flag-tag*3 from the plasmid.
Construction of the plasmid was similar to that of 20ipaD, with Usp45 signal peptide (indicated in yellow) and AcmA3b (indicated in green) included.
The sequence of control 3Xflag-tag is shown in blue. Two restriction sites for the enzyme NcoI (indicated in dark green) and HindIII (indicated in dark blue) were designed so that during enzymatic digestion, the sequence of control 3Xflag-tag would be obtained.

### E. coli

![E_design](https://static.igem.wiki/teams/4161/wiki/e-design.png)

*E. coli* Nissle 1917 [^Gelfat2021][^Gelfat2021,2], as a probiotic first isolated from the GI tract of healthy soldiers in WWI, has been proven to impose positive impacts on the human GI tract by suppression and inhibition of GI tract pathogens.
The current trend in developing Nissle for therapeutics is based on the fact that *E. coli* is one of the most developed model organisms for scientific research.
It has a small genome, stability of expression, and is easy to culture.

The detailed design of the *E. coli* surface display system is as follows. Through the literature review, We have targeted two different display systems.
One is based on *E. coli* curli operon [^Gelfat2021].
Curli fiber is a component of biofilm.
The PATCH system [^Gupta2010] developed from previous studies have been effective in displaying proteins of interest.
Furthermore, the large capacity of the curli fiber presents multivalency, making it possible to display multiple proteins at arbitrarily close distances to bind simultaneously for the drug effect to take place.
The plasmid design referenced the pM1s3ATScsg-Etag plasmid on Addgene (Plasmid #137946) from Neel Joshi Lab with the optimized synthetic curli operon.
The other option is based on intimin.
Intimin in *E. coli* has a trans-outer membrane region and a C-terminal repeat of Ig-like and lectin domains that can be used as a potential fusion site for protein display[^Sadana2017].
In some earlier studies, the researchers successfully inserted a fragment of EHEC intimin into a known plasmid vector with a VHH fusing to it and had it successfully express and display the VHH on the bacteria surface[^Salema2013].
To fully exploit the multivalency advantage of the bacterial surface display system, we plan to display more than one kind of nanobodies, so the probiotic can bind to a larger range of pathogens, or it can bind to different antigens of the pathogen.
It is also important to mention that the target antigen IpaD is highly conservative and exists in all strains of *Shigella*.
Also, previous studies have constructed a library of anti-IpaD VHH including VHH 20ipaD, JMKH2, and JPSG3 are found specifically bind to the epitopes in IpaD protein[^Barta2017] [^Sierocki2017]. The affinity of this antigen-VHH pair is considerable when using 20ipaD and JMKH2[^Sierocki2017].

## References

[^Gelfat2021,2]: Gelfat, I. (2021). Engineering E. coli Nissle 1917 to Advance and Facilitate Its Use in Biomedical Applications [Ph.D., Harvard University]. <https://www.proquest.com/docview/2563494610/abstract/615221E21BBF406CPQ/1>

[^Gelfat2021]: Gelfat, I., Aqeel, Y., Tremblay, J. M., Jaskiewicz, J. J., Shrestha, A., Lee, J. N., Hu, S., Qian, X., Magoun, L., Sheoran, A., Bedenice, D., Giem, C., Manjula-Basavanna, A., Osburne, M. S., Tzipori, S., Shoemaker, C. B., Leong, J. M., & Joshi, N. S. (2021). Single domain antibodies against enteric pathogen virulence factors are active as curli fiber fusions on probiotic E. coli Nissle 1917 (p. 2021.06.18.448998). bioRxiv. <https://doi.org/10.1101/2021.06.18.448998>

[^Gupta2010]: Gupta, A., Joshi, N., Lawrence Zitnick, C., Cohen, M., & Curless, B. (2010, September). Single image deblurring using motion density functions. In European conference on computer vision (pp. 171-184). Springer, Berlin, Heidelberg. Retrieved Oct 12, 2022, from <https://link-springer-com.proxy.lib.duke.edu/chapter/10.1007/978-3-642-15549-9_13>

[^Carayol2013]: Carayol, N. and Guy Nhieu. (2013). The Inside Story of *Shigella* Invasion of Intestinal Epithelial Cells. Cold Spring Harbor Perspectives in Medicine. Retrieved March 28, 2022, from <http://perspectivesinmedicine.cshlp.org/content/3/10/a016717.full>

[^Garcia2014]: Zaidi, M. B., & Estrada-García, T. (2014, June 1). shigella: A highly virulent and elusive pathogen. Current tropical medicine reports. Retrieved March 28, 2022, from <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4126259/>

[^ONeill2014]: O' Neill, J. (2014, December). Antimicrobial resistance: Tackling a crisis for the health and wealth of nations . Retrieved March 28, 2022, from <https://amr-review.org/sites/default/files/AMR%20Review%20Paper%20-%20Tackling%20a%20crisis%20for%20the%20health%20and%20wealth%20of%20nations_1.pdf>

[^Langdon2016]: Langdon, A., Crook, N., & Dantas, G. (2016). The effects of antibiotics on the microbiome throughout development and alternative approaches for therapeutic modulation. Genome Medicine, 8(1). <https://doi.org/10.1186/s13073-016-0294-z>

[^CDC2015]: Centers for Disease Control and Prevention. (2015, April 2). Multidrug-resistant shigellosis spreading in the United States.

[^CDC2020]: Centers for Disease Control and Prevention. (2020, October 8). Antibiotic resistance and *Shigella* infections. Centers for Disease Control and Prevention. Retrieved March 28, 2022, from <https://www.cdc.gov/shigella/treatment/antibiotic-resistance-general.html>

[^Hussen2019]: Hussen, S., Mulatu, G., & Yohannes Kassa, Z. (2019). Prevalence of *Shigella* species and its drug resistance pattern in Ethiopia: A systematic review and meta-analysis. Annals of Clinical Microbiology and Antimicrobials, 18(1). <https://doi.org/10.1186/s12941-019-0321-1>

[^Gray2015]: Gray, M. D., Lacher, D. W., Leonard, S. R., Abbott, J., Zhao, S., Lampel, K. A., Prothery, E., Gouali, M., Weill, F.-X., & Maurelli, A. T. (2015, May 14). Prevalence of shiga toxin-producing *Shigella* species isolated from French travellers returning from the Caribbean: An emerging pathogen with international implications. Clinical Microbiology and Infection. Retrieved March 28, 2022, from <https://www.sciencedirect.com/science/article/pii/S1198743X15004437>

[^Casabonne2016]: Casabonne, C., González, A., Aquili, V., & Balagué, C. (2016, November 22). Prevalence and virulence genes of *Shigella* spp.. isolated from patients with diarrhea in Rosario, Argentina. Japanese Journal of Infectious Diseases. Retrieved March 28, 2022, from <https://www.jstage.jst.go.jp/article/yoken/69/6/69_JJID.2015.459/_article/-char/ja/>
.

[^Kim2017]: Kim, S., Covington, A., & Pamer, E. G. (2017, September). The intestinal microbiota: Antibiotics, colonization resistance, and enteric pathogens. Immunological reviews. Retrieved March 28, 2022, from <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6026851/>

[^Francino2016]: Francino, M. P. (2016, January 1). Antibiotics and the human gut microbiome: Dysbioses and accumulation of resistances. Frontiers. Retrieved March 28, 2022, from <https://www.frontiersin.org/articles/10.3389/fmicb.2015.01543/full>

[^Roehrich2013]: Roehrich, A. D., Guillossou, E., Blocker, A. J., & Martinez-Argudo, I. (2013, February). *Shigella* IpaD has a dual role: Signal transduction from the type III secretion system needle tip and intracellular secretion regulation. Molecular microbiology. Retrieved March 28, 2022, from <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3575693/>

[^Tremblay2013]: Tremblay, J.M., Mukherjee, J., Leysath, C.E., Debatis, M., Ofori, K., Baldwin, K., Boucher, C., Peters, R., Beamer, G., Sheoran, A., Bedenice, D., Tzipori, S., & Shoemaker, C.B. (2013, December). A single VHH-based toxin-neutralizing agent and an effector antibody protect mice against challenge with shiga toxins 1 and 2. Infection and immunity. Retrieved March 28, 2022, from <https://pubmed.ncbi.nlm.nih.gov/24082082/>

[^Greve2019]: De Greve H., Virdi V., Bakshi S., & Depicker A. (2019, December 9). Simplified monomeric VHH-FC antibodies provide new opportunities for passive immunization. Current opinion in biotechnology. Retrieved March 28, 2022, from <https://pubmed.ncbi.nlm.nih.gov/31810049/>

[^Sicard2011]: Sicard, D., Jean Luc, J., Legras, L. (2011). Bread, beer and wine: Yeast domestication in the Saccharomyces sensu stricto complex. Comptes Rendus Biologies, Elsevier, 2011, 229 - 236. ⟨10.1016/j.crvi.2010.12.016⟩. ⟨hal-02653082⟩

[^Holt2019]: Holt, S., Miks, M. H., de Carvalho, B. T., Foulquié-Moreno, M. R., Thevelein, J. M. (2019 May) The molecular biology of fruity and floral aromas in beer and other alcoholic beverages, FEMS Microbiology Reviews, 43(3), 193–222, <https://doi.org/10.1093/femsre/fuy041>

[^Piskur2004]: Piskur, J., Langkjaer, R. B. (2004). Yeast genome sequencing: the power of comparative genomics. Molecular microbiology, 53(2), 381–389. <https://doi.org/10.1111/j.1365-2958.2004.04182.x>

[^Gaziano2020]: Gaziano, R., Sabbatini, S., Roselletti, E., Perito, S., Monari, C. (2020). Saccharomyces cerevisiae-Based Probiotics as Novel Antimicrobial Agents to Prevent and Treat Vaginal Infections. Frontiers in microbiology, 11, 718. <https://doi.org/10.3389/fmicb.2020.00718>

[^Palma2015]: Palma, M. L., Zamith-Miranda, D., Martins, F. S., Bozza, F. A., Nimrichter, L., Montero-Lomeli, M., Marques, E. T., Jr, Douradinha, B. (2015). Probiotic Saccharomyces cerevisiae strains as biotherapeutic tools: is there room for improvement?. Applied microbiology and biotechnology, 99(16), 6563–6570. <https://doi.org/10.1007/s00253-015-6776-x>

[^Boder1997]: Boder, E. T., Wittrup, K. D. (1997). Yeast surface display for screening combinatorial polypeptide libraries. Nature biotechnology, 15(6), 553–557. <https://doi.org/10.1038/nbt0697-553>

[^Chao2006]: Chao, G., Lau, W. L., Hackel, B., Sazinsky, S, L., Lippow, S. M., Wittrup, k. D. (2006). Isolating and engineering human antibodies using yeast surface display. Nature Protocol 1, 755–768, 755-770. <https://doi.org/10.1038/nprot.2006.94>

[^Wagner2020]: Wagner, S.; Galan, J. E. Bacteria Type III Protein Secrete System. Springer Nature Switzerland: 2020.

[^Dickenson2011]: Dickenson, N. E., Zhang, L., Epler, C. R., Adam, P. R., Picking, W. L., Picking, W. D. (2011). Conformational changes in IpaD from *Shigella* flexneri upon binding bile salts provide insight into the second step of type III secretion. Biochemistry, 50(2), 172–180. <https://doi.org/10.1021/bi101365f>

[^Epler2009]: Epler, C. R., Dickenson, N. E., Olive, A. J., Picking, W. L., & Picking, W. D. (2009). Liposomes recruit IpaC to the *Shigella* flexneri type III secretion apparatus needle as a final step in secretion induction. Infection and immunity, 77(7), 2754–2761. <https://doi.org/10.1128/IAI.00190-09>

[^Peng2015]: Peng, B., Williams, T. C., Henry, M., Nielsen, L. K., Vickers, C. E. (2015). Controlling heterologous gene expression in yeast cell factories on different carbon substrates and across the diauxic shift: a comparison of yeast promoter activities. Microbial cell factories, 14, 91. <https://doi.org/10.1186/s12934-015-0278-5>

[^Huang2020]: Huang, X., Gänzle, M., Zhang, H., Zhao, M., Fang, Y., Nishinari, K. (2020). Microencapsulation of probiotic lactobacilli with shellac as moisture barrier and to allow controlled release. Journal of the Science of Food and Agriculture. 101. 10.1002/jsfa.10685.

[^Huang2019]: Huang. X., Zhang, H., Peng, S., Zhao, M., Fang, Y. (2019). Tianrankeshixing Bicaichongjiao zai Gongnengzufenweinanghua zhongde Yingyonngyanjiujinzhan [Recent Progress in the Application Shellac as a Natural Edible Wall Material in the Microencapsulation of Functional Ingredients]. Shipinkexue [Food Science], 40(7), 317-324.

[^Mei2018]: Mei, S., Han, P., Wu, H., Shi, J., Tang, L., Jiang, Z. (2018). One-pot fabrication of chitin-shellac composite microspheres for efficient enzyme immobilization. Journal of biotechnology, 266, 1–8. <https://doi.org/10.1016/j.jbiotec.2017.11.015>

[^Gately2017]: Gately, N. M., Kennedy, J. E. (2017). The Development of a Melt-Extruded Shellac Carrier for the Targeted Delivery of Probiotics to the Colon. Pharmaceutics, 9(4), 38. <https://doi.org/10.3390/pharmaceutics9040038>

[^Hamad2013]: Hamad, S. A., Stoyanov, S. D., Paunov, V. N. (2013). Triggered release kinetics of living cells from composite microcapsules. Physical chemistry chemical physics: PCCP, 15(7), 2337–2344. <https://doi.org/10.1039/c2cp42100c>

[^Braat2006]: Braat, H., Rottiers, P., Hommes, D. W., Huyghebaert, N., Remaut, E., Remon, J. P., . . . Steidler, L. (2006). A phase I trial with transgenic bacteria expressing interleukin-10 in Crohn's disease. Clin Gastroenterol Hepatol, 4(6), 754-759. doi:10.1016/j.cgh.2006.03.028

[^Moreno2016]: de Moreno de LeBlanc, A., Del Carmen, S., Chatel, J. M., Azevedo, V., Langella, P., Bermudez-Humaran, L., & LeBlanc, J. G. (2016). Evaluation of the biosafety of recombinant lactic acid bacteria designed to prevent and treat colitis. J Med Microbiol, 65(9), 1038-1046. doi:10.1099/jmm.0.000323

[^Muthuramalingam2021]: Muthuramalingam, M., Whittier, S. K., Picking, W. L., & Picking, W. D. (2021). The *Shigella* Type III Secretion System: An Overview from Top to Bottom. Microorganisms, 9(2). doi:10.3390/microorganisms9020451

[^Plavec2019]: Plavec, T. V., & Berlec, A. (2019). Surface Anchoring on *Lactococcus lactis* by Covalent Isopeptide Bond. Acta Chim Slov, 66(1), 18-27.

[^Song2017]: Song, A. A.-L., In, L. L. A., Lim, S. H. E., & Rahim, R. A. (2017). A review on *Lactococcus* lactis: from food to factory. Microbial Cell Factories, 16(1), 55. doi:10.1186/s12934-017-0669-x

[^Barta2017]: Barta ML, Shearer JP, Arizmendi O, Tremblay JM, Mehzabeen N, Zheng Q, et al. Single-domain antibodies pinpoint potential targets within *Shigella* invasion plasmid antigen D of the needle tip complex for inhibition of type III secretion. J Biol Chem 2017, 292(40), 16677–87.

[^Sierocki2017]: Sierocki, R.; Jneid, B.; Delgado, M. L. O.; Plaisance, M.; Maillère, B.; Nozach, H.; Simon, S. An antibody targeting type III secretion system induces broad protection against Salmonella and *Shigella* infections. PLOS Neglected Tropical Diseases 2021, 15(3): e0009231

[^Sadana2017]: Sadana, P., Monnich, M., Unverzagt, C. and Scrima, A. Structure of the Y. pseudotuberculosis adhesin InvasinE. Protein Sci
2017, 26: 1182–1195.

[^Salema2013]: Salema, V., Marın, E., Martınez-Arteaga, R., Ruano-Gallego, D., Fraile, S., Margolles, Y., et al. Selection of single domain antibodies from immune libraries displayed on the surface of *E. coli* cells with two b-domains of opposite topologies. PLoS One 2013, 8: e75126.
