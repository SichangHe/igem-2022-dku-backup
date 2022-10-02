#DKU iGEM 2022 Executive Plan

##H. Pylori Detection and Therapeutics
###1. Background
$Helicobacter$ $pylori$ is a gram-negative bacterium that poses threats to public health.
$H.$ $pylori$ infection raises the risks of gastritis, gastroduodenal ulcers, and gastric
cancer. Until 2015, 4.4 billion individuals, more than a half of the global population, were estimated to be $H.$ $pylori$-positive, among which South America, Asia, and Africa had the highest prevalence rates around 70% (Hooi et al., 2017). Before long the discovery of $H.$ $pylori$, antimicrobial therapies involving multiple antibiotics have been developed for the eradication of $H.$ $pylori$ (Graham, 2020). However, rising resistance to antibiotics and not enough antibiotic susceptibility testing reduce therapy effectiveness, elongate therapy duration time, and lead to inappropriate use of antibiotics (Savoldi et al., 2018; Saleem & Howden, 2020). Besides, noncompliance of patients raises another challenge of $H.$ $pylori$ eradication. Around 20% of the patients fail to complete treatment due to the adverse effects (Hafeez et al., 2021). Another challenge of current antimicrobial therapy is its potential harm to the homeostasis of human gut microbiome. Antibiotic or proton inhibitors such as PPI that is used in $H.$ $pylori$ treatment can alter the gut microbial composition (Bhalodi et al., 2019), which is correlated with human health.

####Reference
Alexander, S.M., R.J. Retnakumar, D. Chouhan, T.N.B. Devi, S. Dharmaseelan, K. Devadas, N. Thapa, J.P. Tamang, S.C. Lamtha, and S. Chattopadhyay. 2021. Helicobacter pylori in Human Stomach: The Inconsistencies in Clinical Outcomes and the Probable Causes. Frontiers in Microbiology. 12.

Khalilpour, A., M. Kazemzadeh-Narbat, A. Tamayol, R. Oklu, and A. Khademhosseini. 2016. Biomarkers and diagnostic tools for detection of Helicobacter pylori. Applied microbiology and biotechnology. 100:4723-4734.

Nguyen, P.Q., L.R. Soenksen, N.M. Donghia, N.M. Angenent-Mari, H. de Puig, A. Huang, R. Lee, S. Slomovic, T. Galbersanini, G. Lansberry, H.M. Sallum, E.M. Zhao, J.B. Niemi, and J.J. Collins. 2021. Wearable materials with embedded synthetic biology sensors for biomolecule detection. Nature Biotechnology. 39:1366-1374.

###2. Innovative feature
####Detection:
The rapid urease test (RUT) and PCR diagnosis of 16S rRNA gene serve as two popular existing
methods for the detection of H. pylori.
However, false-negative results and a long result waiting time make these methods less reliable and convenient for patients (Khalilpour et al., 2016). In order to increase test accuracy while allowing patients to perform home tests, our team will propose an innovative portable device that provides in vivo detection of $H.$ $pylori$ in saliva samples. Synthetic biology is involved in the product design process. Due to the small amount of $H.$ $pylori$ in saliva, recombinase polymerase amplification (RPA) is firstly used for amplification. Inspired by the SHERLOCK system, components in RPA are freeze-dried into tablets without damaging bioactivity, and they can be activated by the addition of water and the saliva sample (Nguyen et al., 2021). For color change in detection, it is AuNP-based, depending on aptamer binding with $H.$ $pylori$. The aptamers included are specially designed using SELEX to target key polymorphisms/variants of virulence factor of $H.$ $pylori$ (CagA, VacA, DupA) positively associated with onset of severe gastric diseases (Alexander et al., 2021). This aims to improve the effectiveness of detection, as instead of including asymptomatic infections, our detection method tries to recognize conditions of $H.$ $pylori$ capable of developing aggressive clinical outcomes to further prevent severe gastrointestinal diseases linked to $H.$ $pylori$ (Alexander et al., 2021).

####Therapeutics:
To treat $H.$ $pylori$ infection, we plan to use **nanobody (HCAbs)** (the heavy chain of monoclonal antibodies (mAbs)) targeting the urease activity of $H.$ $pylori$. Urease is an essential enzyme for $H.$ $pylori$ to survive in the stomach, since it converts urea to ammonia, which neutralizes the low-pH environment. If urease activity of $H.$ $pylori$ is blocked by antibody-antigen reaction, $H.$ $pylori$ will no longer tolerate the acidic environment. To find proper HCAbs against urease, we plan to use **nanobody grafting and phagemid display** method. Nanobody grafting matches the heavy chain variable region of a donor mAb against urease to an acceptor HCAb. Then, the HCAbs DNA library created by nanobody grafting are cloned into a phagemid and transferred into an E. coli. With the help of a helper phage M13, a lot of filamentous phages with different HCAbs attached will be produced. After several rounds of washing and eluting, we can find the phage (HCAb) with the highest affinity.

####Reference
Wagner, H.J., Wehrle, S., Weiss, E., Cavallari, M., Weber, W., 2018. A Two-Step Approach for the Design and Generation of Nanobodies. Int J Mol Sci 19, 3444. <https://doi.org/10.3390/ijms19113444>

#Guiding Probiotics to shigella with single-domain antibodies
###1. Background
The Shigella species is listed as one of the eight dangerous drug resistant bacteria (WHO, 2016), with associated mortalities projected to rise to 10 million globally by 2050, if not properly addressed (O’ Neill, 2014). In the United States alone, over 77,000 antibiotic resistant cases were reported annually and 90% of overall Shigella cases were found to be resistant to the first choice medication ciprofloxacin (CDC, 2015). Shigella, as a highly infective,  enteroinvasive and occasionally toxin-releasing (Imported Infectious Diseases, 2014; Carayol and Nhieu, 2013; Gray et al., 2015) bacterial genus, may cause severe infection and bacterial dysentery in the colorectal mucosa even with as low a dose as 10 - 100 organisms (Garcia and Zaidi, 2014).  Shigella-related infections thereby spread rapidly, particularly in low-resource populations (Hussen et al., 2019) and among vulnerable groups including children in care facilities, the homeless, and returned travelers (CDC, 2020; Huruy et al., 2018; Casabonne et al., 2016; Gray et al., 2015).

The use of conventional antibiotics aggravates the multidrug resistance of most Shigella strains. Besides aiding in the selection of resistant pathogens, antibiotics reduce intestinal species diversity and population, and disrupt the defensive, metabolic, and trophic functions of interdependent microbes (Francino, 2016; Ramirez et al., 2020). Although antibiotics are able to prevent and treat infections, antibiotic exposure to the intestinal microbiota can lead to loss of colonization resistance, rendering the host more susceptible to future invasion (Kim et al., 2017; Shah et al., 2021).

Engineered probiotics with cell surface display systems are an especially promising alternative that  improve Shigella eradication rates without heavy reliance on antibiotics. Single VH domain (VHH) antibodies displayed on the probiotic surface reduce virulent activity of Shigella (Roehrich et al., 2013) through probiotic-pathogen binding while minimizing toxicity to non-targets (Barta et al., 2017; Trembley et al., 2013). Specifically, these antibodies recognize and target epitopes within the tip complex that is conserved across all pathogens that utilize type III secretion system (T3SS) to translocate effector proteins into the host cells (Barta et al., 2017). Innovations in VHH-ipaD binding not only offer a solution that preserves the potency of antibiotics and microbial composition of the gut microbiome, but also illuminates targeted approaches to treat related T3SS bacteria like Salmonella and enterohemorrhagic E. coli, and other novel opportunities for passive immunization (Greve et al., 2020).

####Reference
Carayol, N. and Guy Nhieu. (2013). The Inside Story of Shigella Invasion of Intestinal Epithelial Cells. Cold Spring Harbor Perspectives in Medicine. Retrieved March 28, 2022, from <http://perspectivesinmedicine.cshlp.org/content/3/10/a016717.full>

Zaidi, M. B., & Estrada-García, T. (2014, June 1). shigella: A highly virulent and elusive pathogen. Current tropical medicine reports. Retrieved March 28, 2022, from <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4126259/>

O' Neill, J. (2014, December). Antimicrobial resistance: Tackling a crisis for the health and wealth of nations . Retrieved March 28, 2022, from <https://amr-review.org/sites/default/files/AMR%20Review%20Paper%20-%20Tackling%20a%20crisis%20for%20the%20health%20and%20wealth%20of%20nations_1.pdf>

Langdon, A., Crook, N., & Dantas, G. (2016). The effects of antibiotics on the microbiome throughout development and alternative approaches for therapeutic modulation. Genome Medicine, 8(1). <https://doi.org/10.1186/s13073-016-0294-z>

Centers for Disease Control and Prevention. (2015, April 2). Multidrug-resistant shigellosis spreading in the United States.

Centers for Disease Control and Prevention. Retrieved March 28, 2022, from <https://www.cdc.gov/media/releases/2015/p0402-multidrug-resistant-shigellosis.html>

Centers for Disease Control and Prevention. (2020, October 8). Antibiotic resistance and Shigella infections. Centers for Disease Control and Prevention. Retrieved March 28, 2022, from <https://www.cdc.gov/shigella/treatment/antibiotic-resistance-general.html>

Hussen, S., Mulatu, G., & Yohannes Kassa, Z. (2019). Prevalence of shigella species and its drug resistance pattern in Ethiopia: A systematic review and meta-analysis. Annals of Clinical Microbiology and Antimicrobials, 18(1). <https://doi.org/10.1186/s12941-019-0321-1>

Gray, M. D., Lacher, D. W., Leonard, S. R., Abbott, J., Zhao, S., Lampel, K. A., Prothery, E., Gouali, M., Weill, F.-X., & Maurelli, A. T. (2015, May 14). Prevalence of shiga toxin-producing Shigella species isolated from French travellers returning from the Caribbean: An emerging pathogen with international implications. Clinical Microbiology and Infection. Retrieved March 28, 2022, from <https://www.sciencedirect.com/science/article/pii/S1198743X15004437>

Uruy, K., Kassu, A., Mulu, A., Gebretsadik, S., Andargie, G., Tadesse, T., Birhan, W., Worku, N., Ghebreselassie, D., Belyhun, Y., Yifru, S., Adugna, S., & Tiruneh, M. (2008). High Level of Antimicrobial Resistance in Shigella Species Isolated From Diarrhoeal Patients in University of Gondar Teaching Hospital, Gondar, Ethiopia . Retrieved March 28, 2022, from <https://pharmacologyonline.silae.it/files/archives/2008/vol2/29_Huruy.pdf>

Casabonne, C., González, A., Aquili, V., & Balagué, C. (2016, November 22). Prevalence and virulence genes of Shigella spp.. isolated from patients with diarrhea in Rosario, Argentina. Japanese Journal of Infectious Diseases. Retrieved March 28, 2022, from <https://www.jstage.jst.go.jp/article/yoken/69/6/69_JJID.2015.459/_article/-char/ja/>

Shah, T., Baloch, Z., Shah, Z., Cui, X., & Xia, X. (2021, June 20). The intestinal microbiota: Impacts of antibiotics therapy, colonization resistance, and diseases. International journal of molecular sciences. Retrieved March 28, 2022, from <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8235228/>

Kim, S., Covington, A., & Pamer, E. G. (2017, September). The intestinal microbiota: Antibiotics, colonization resistance, and enteric pathogens. Immunological reviews. Retrieved March 28, 2022, from <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6026851/>

Francino, M. P. (2016, January 1). Antibiotics and the human gut microbiome: Dysbioses and accumulation of resistances. Frontiers. Retrieved March 28, 2022, from <https://www.frontiersin.org/articles/10.3389/fmicb.2015.01543/full>

Roehrich, A. D., Guillossou, E., Blocker, A. J., & Martinez-Argudo, I. (2013, February). Shigella IpaD has a dual role: Signal transduction from the type III secretion system needle tip and intracellular secretion regulation. Molecular microbiology. Retrieved March 28, 2022, from <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3575693/>

Barta, M. L., Shearer, J. P., Arizmendi, O., Tremblay, J. M., Mehzabeen, N., Zheng, Q., Battaile, K. P., Lovell, S., Tzipori, S., Picking, W. D., Shoemaker, C. B., & Picking, W. L. (2017, October 6). Single-domain antibodies pinpoint potential targets within shigella invasion plasmid antigen d of the needle tip complex for inhibition of type III secretion. The Journal of biological chemistry. Retrieved March 28, 2022, from <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5633129/>

Tremblay, J.M., Mukherjee, J., Leysath, C.E., Debatis, M., Ofori, K., Baldwin, K., Boucher, C., Peters, R., Beamer, G., Sheoran, A., Bedenice, D., Tzipori, S., & Shoemaker, C.B. (2013, December). A single VHH-based toxin-neutralizing agent and an effector antibody protect mice against challenge with shiga toxins 1 and 2. Infection and immunity. Retrieved March 28, 2022, from <https://pubmed.ncbi.nlm.nih.gov/24082082/>

De Greve H., Virdi V., Bakshi S., & Depicker A. (2019, December 9). Simplified monomeric VHH-FC antibodies provide new opportunities for passive immunization. Current opinion in biotechnology. Retrieved March 28, 2022, from <https://pubmed.ncbi.nlm.nih.gov/31810049/>

###2. Innovative feature
Generally, the innovative idea of our project is to inhibit intestinal bacterial pathogen growth by probiotic-pathogen adhesion. It is achieved by displaying single-domain antibody, or camelid heavy chain-only antibodies (VHH), on the surface of probiotic E. coli Nissle 1917 using bacteria cell surface display system. The E. coli Nissle 1917 has the potential to treat bacteria intestinal infections as a probiotic (1). It can also be used as a vector for transporting drugs into intestines (2). The VHH can be used to inhibit pathogen growth and inhibit intracellular pathogen from invading somatic cells (3). To be specific, IpaD (a protein in bacteria type 3 secrete system (T3SS)) of genus Shigella can trigger the downstream cascade involving IpaB and IpaC to assist the translocon pore formation that initiates the invasion of the host cells(8,9). The important features and roles of IpaD in the cytotoxicity of Shigella indicates that IpaD can be a potential target for bacteria de-toxicity and elimination.

This idea combines the antibacterial properties of probiotic E. coli Nissle 1917, VHH and provides a novel approach for target specific drug delivery in intestines. With these antibacterial properties working together, it may achieve a significant effect on treating bacterial intestinal infections. Also, it provides a potential therapy for antibiotic resistant bacteria intestinal infection with a lower price compared to using extracted monoclonal antibody.

Apart from the general idea, the design for achieving the probiotic-pathogen adhesion target
also contains some innovative thoughts. First, we chose a bacterial surface display system. There are two options. One is based on E. coli protein YiaT (4), as it is able to display large proteins with molecular mass up to 50 kDa, which makes it hopeful to successfully display single-domain antibodies with molecular mass ranging from 12-15 kDa. The other option is based on intimin. Intimin in E. coli has a trans-outer membrane region and a C-terminal repeat of Ig-like and lectin domains that can be used as a potential fusion site for protein display (14). In some earlier studies, the researchers successfully inserted a fragment of EHEC intimin into a known plasmid vector with a VHH fusing to it and had it successfully express and display the VHH on the bacteria surface (15). Currently no research used such a display system to express and display VHH 20ipaD, JMKH2, and JPSG3 on E. coli surface, which provides an innovation point for our project. Second, we plan to display more than on kind of antibody, so the probiotic can bind to a larger range of pathogens, or it can bind different antigens of the pathogen. Third, the antigen IpaD that VHH can bind to, is highly conservative and exists in all strains of shigella. Also, previous studies have constructed a library of anti-IpaD VHH including VHH 20ipaD, JMKH2, and JPSG3 are found specifically bind to the epitopes in IpaD protein (11,12). The affinity of this antigen-VHH pair is considerable when using 20ipaD and JMKH2 (12).

####Reference
(1) Sonnenborn, U. Escherichia Coli Strain Nissle 1917—from Bench to Bedside and Back:
History of a Special Escherichia Coli Strain with Probiotic Properties. FEMS Microbiol. Lett. 2016, 363 (19), fnw212. <https://doi.org/10.1093/femsle/fnw212>.

(2)Geldart, K.; Forkus, B.; McChesney, E.; McCue, M.; Kaznessis, Y. PMPES: A Modular Peptide Expression System for the Delivery of Antimicrobial Peptides to the Site of Gastrointestinal Infections Using Probiotics. Pharmaceuticals 2016, 9 (4), 60. <https://doi.org/10.3390/ph9040060>.

(3)  Marcobal, A.; Liu, X.; Zhang, W.; Dimitrov, A. S.; Jia, L.; Lee, P. P.; Fouts, T. R.; Parks, T. P.; Lagenaur, L. A. Expression of Human Immunodeficiency Virus Type 1 Neutralizing Antibody Fragments Using Human Vaginal Lactobacillus. AIDS Res. Hum. Retroviruses 2016, 32 (10–11), 964–971. <https://doi.org/10.1089/aid.2015.0378>.

(4)  Han, M.-J.; Lee, S. H. An Efficient Bacterial Surface Display System Based on a Novel Outer Membrane Anchoring Element from the Escherichia Coli Protein YiaT. FEMS Microbiol. Lett. 2015, 362 (1), 1–7. <https://doi.org/10.1093/femsle/fnu002>.

(8)  Dickenson, N. E., Zhang, L., Epler, C. R., Adam, P. R., Picking, W. L., Picking, W. D. Conformational changes in IpaD from Shigella flexneri upon binding bile salts provide insight into the second step of type III secretion. Biochemistry 2011, 50, 172–180.

(9)  Epler, C. R., Dickenson, N. E., Olive, A. J., Picking, W. L., and Picking, W. D. Liposomes
recruit IpaC to the Shigella flexneri type III secretion apparatus needle as a final step in secretion induction. Infect. Immun. 2009, 77, 2754–2761.

(11)  Barta ML, Shearer JP, Arizmendi O, Tremblay JM, Mehzabeen N, Zheng Q, et al. Single-domain antibodies pinpoint potential targets within Shigella invasion plasmid antigen D of the needle tip complex for inhibition of type III secretion. J Biol Chem 2017, 292(40), 16677–87.

(12)  Sierocki, R.; Jneid, B.; Delgado, M. L. O.; Plaisance, M.; Maillère, B.; Nozach, H.; Simon, S. An antibody targeting type III secretion system induces broad protection against Salmonella and Shigella infections. PLOS Neglected Tropical Diseases 2021, 15(3): e0009231
(14)  Sadana, P., Monnich, M., Unverzagt, C. and Scrima, A. Structure of the Y. pseudotuberculosis adhesin InvasinE. Protein Sci
2017, 26: 1182–1195.

(15)  Salema, V., Marın, E., Martınez-Arteaga, R., Ruano-Gallego, D., Fraile, S., Margolles, Y., et al. Selection of single domain antibodies from immune libraries displayed on the surface of E. coli cells with two b-domains of opposite topologies. PLoS One 2013, 8: e75126.

###3. Anticipated results from early modelings
Our early modeling result indicated that the project is theoretically feasible.
By using the theory of diffusion (Fick’s Diffusion Law) and parameters from literature review, we modeled the distribution of AMP that is directed to the pathogen by antibodies. For rough estimation, we hypothesize the geometry of probiotics can be simplified as tiny spherical particles with radius R (about $1μm$), and the diffusion of AMP in the gastrointestinal tract was modeled as spherically symmetric concentration profiles.

$$
\Delta C=\frac{1}{r^2}\partial_r(r^2\partial_rC)
$$
($C$: concentration, $r$: the distance from the center of one probiotic sphere)
Stationary situation was the focus, that is
$$
\Delta C=0\\[8pt]
\frac{1}{r^2}\frac{d}{dr}(r^2\frac{dc}{dr})=0
$$
Under boundary conditions: $c=c_0$ at $r=R$， $c=c_1$ far from the particle, the solution is
$$
c=(c_0-c_1)\frac{R}{r}+c_1
$$
The model was built on the fact that transport phenomena could happen under the condition of stationary concentration.
The AMP production rate $N$ is expressed by
$$
N=4\pi R^4D(\frac{dc}{dr})_{r=R}
$$
($D$:diffusion coefficient)

Having all these equations, the AMP production rate can be finalized as
$$
N=4\pi DR(c_0-c_1)
$$
Form literature review, the diffusion coefficient $D$ of a 2500 Da AMP in intestinal condition is found to be around $0.5×10^{-10}  m^2\cdot s^{-1}$.
The AMP production rate $N$ is assumed as about 100 AMP/s.
Therefore, $c_0-c_1$ could be calculated as around $0.7 μg/ml$.
