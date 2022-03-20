#H. Pylori Detection and Therapeutics
##1. Innovation feature
###Detection:
The rapid urease test (RUT) and PCR diagnosis of 16S rRNA gene serve as two popular existing methods for the detection of H. pylori. However, false-negative results and a long result waiting time make these methods less reliable and convenient for patients (Khalilpour et al., 2016). In order to increase test accuracy while allowing patients to perform home tests, our team will propose an innovative portable device that provides in vivo detection of H. pylori in saliva samples. Synthetic biology is involved in the product design process. Due to the small amount of H. pylori in saliva, recombinase polymerase amplification (RPA) is firstly used for amplification. Inspired by the SHERLOCK system, components in RPA are freeze-dried into tablets without damaging bioactivity, and they can be activated by the addition of water and the saliva sample (Nguyen et al., 2021). For color change in detection, it is AuNP-based, depending on aptamer binding with H. pylori. The aptamers included are specially designed using SELEX to target key polymorphisms/variants of virulence factor of H. pylori (CagA, VacA, DupA) positively associated with onset of severe gastric diseases (Alexander et al., 2021). This aims to improve the effectiveness of detection, as instead of including asymptomatic infections, our detection method tries to recognize conditions of H. pylori capable of developing aggressive clinical outcomes to further prevent severe gastrointestinal diseases linked to H. pylori (Alexander et al., 2021).

####Reference
Alexander, S.M., R.J. Retnakumar, D. Chouhan, T.N.B. Devi, S. Dharmaseelan, K. Devadas, N. Thapa, J.P. Tamang, S.C. Lamtha, and S. Chattopadhyay. 2021. Helicobacter pylori in Human Stomach: The Inconsistencies in Clinical Outcomes and the Probable Causes. Frontiers in Microbiology. 12.

Khalilpour, A., M. Kazemzadeh-Narbat, A. Tamayol, R. Oklu, and A. Khademhosseini. 2016. Biomarkers and diagnostic tools for detection of Helicobacter pylori. Applied microbiology and biotechnology. 100:4723-4734.

Nguyen, P.Q., L.R. Soenksen, N.M. Donghia, N.M. Angenent-Mari, H. de Puig, A. Huang, R. Lee, S. Slomovic, T. Galbersanini, G. Lansberry, H.M. Sallum, E.M. Zhao, J.B. Niemi, and J.J. Collins. 2021. Wearable materials with embedded synthetic biology sensors for biomolecule detection. Nature Biotechnology. 39:1366-1374.

###Therapeutics:

To treat H. pylori infection, we plan to use **nanobody (HCAbs)** (the heavy chain of monoclonal antibodies (mAbs)) targeting the urease activity of H. pylori. Urease is an essential enzyme for H. pylori to survive in the stomach, since it converts urea to ammonia, which neutralizes the low-pH environment. If urease activity of H. pylori is blocked by antibody-antigen reaction, H. pylori will no longer tolerate the acidic environment. To find proper HCAbs against urease, we plan to use **nanobody grafting and phagemid display** method. Nanobody grafting matches the heavy chain variable region of a donor mAb against urease to an acceptor HCAb. Then, the HCAbs DNA library created by nanobody grafting are cloned into a phagemid and transferred into an E. coli. With the help of a helper phage M13, a lot of filamentous phages with different HCAbs attached will be produced. After several rounds of washing and eluting, we can find the phage (HCAb) with the highest affinity.

####Reference
Wagner, H.J., Wehrle, S., Weiss, E., Cavallari, M., Weber, W., 2018. A Two-Step Approach for the Design and Generation of Nanobodies. Int J Mol Sci 19, 3444. <https://doi.org/10.3390/ijms19113444>

#Guiding Probiotics to shigella with single-domain antibodies

##1. Innovation feature
Generally, the innovative idea of our project is to inhibit intestinal bacterial pathogen growth by probiotic-pathogen adhesion. It is achieved by displaying single-domain antibody, or camelid heavy chain-only antibodies (VHH), on the surface of probiotic E. coli Nissle 1917 using bacteria cell surface display system. The E. coli Nissle 1917 has the potential to treat bacteria intestinal infections as a probiotic (1). It can also be used as a vector for transporting drugs into intestines (2). The VHH can be used to inhibit pathogen growth and inhibit intracellular pathogen from invading somatic cells (3). To be specific, IpaD (a protein in bacteria type 3 secrete system (T3SS)) of genus Shigella can trigger the downstream cascade involving IpaB and IpaC to assist the translocon pore formation that initiates the invasion of the host cells(8,9). The important features and roles of IpaD in the cytotoxicity of Shigella indicates that IpaD can be a potential target for bacteria de-toxicity and elimination.

This idea combines the antibacterial properties of probiotic E. coli Nissle 1917, VHH and provides a novel approach for target specific drug delivery in intestines. With these antibacterial properties working together, it may achieve a significant effect on treating bacterial intestinal infections. Also, it provides a potential therapy for antibiotic resistant bacteria intestinal infection with a lower price compared to using extracted monoclonal antibody.

Apart from the general idea, the design for achieving the probiotic-pathogen adhesion target also contains some innovative thoughts. First, we chose a bacterial surface display system. There are two options. One is based on E. coli protein YiaT (4), as it is able to display large proteins with molecular mass up to 50 kDa, which makes it hopeful to successfully display single-domain antibodies with molecular mass ranging from 12-15 kDa. The other option is based on intimin. Intimin in E. coli has a trans-outer membrane region and a C-terminal repeat of Ig-like and lectin domains that can be used as a potential fusion site for protein display (14). In some earlier studies, the researchers successfully inserted a fragment of EHEC intimin into a known plasmid vector with a VHH fusing to it and had it successfully express and display the VHH on the bacteria surface (15). Currently no research used such a display system to express and display VHH 20ipaD, JMKH2, and JPSG3 on E. coli surface, which provides an innovation point for our project. Second, we plan to display more than on kind of antibody, so the probiotic can bind to a larger range of pathogens, or it can bind different antigens of the pathogen. Third, the antigen IpaD that VHH can bind to, is highly conservative and exists in all strains of shigella. Also, previous studies have constructed a library of anti-IpaD VHH including VHH 20ipaD, JMKH2, and JPSG3 are found specifically bind to the epitopes in IpaD protein (11,12). The affinity of this antigen-VHH pair is considerable when using 20ipaD and JMKH2 (12).
##Reference:
(1) Sonnenborn, U. Escherichia Coli Strain Nissle 1917—from Bench to Bedside and Back: History of a Special Escherichia Coli Strain with Probiotic Properties. FEMS Microbiol. Lett. 2016, 363 (19), fnw212. <https://doi.org/10.1093/femsle/fnw212>.

(2)Geldart, K.; Forkus, B.; McChesney, E.; McCue, M.; Kaznessis, Y. PMPES: A Modular Peptide Expression System for the Delivery of Antimicrobial Peptides to the Site of Gastrointestinal Infections Using Probiotics. Pharmaceuticals 2016, 9 (4), 60. <https://doi.org/10.3390/ph9040060>.

(3)  Marcobal, A.; Liu, X.; Zhang, W.; Dimitrov, A. S.; Jia, L.; Lee, P. P.; Fouts, T. R.; Parks, T. P.; Lagenaur, L. A. Expression of Human Immunodeficiency Virus Type 1 Neutralizing Antibody Fragments Using Human Vaginal Lactobacillus. AIDS Res. Hum. Retroviruses 2016, 32 (10–11), 964–971. <https://doi.org/10.1089/aid.2015.0378>.

(4)  Han, M.-J.; Lee, S. H. An Efficient Bacterial Surface Display System Based on a Novel Outer Membrane Anchoring Element from the Escherichia Coli Protein YiaT. FEMS Microbiol. Lett. 2015, 362 (1), 1–7. <https://doi.org/10.1093/femsle/fnu002>.

(8)  Dickenson, N. E., Zhang, L., Epler, C. R., Adam, P. R., Picking, W. L., Picking, W. D. Conformational changes in IpaD from Shigella flexneri upon binding bile salts provide insight into the second step of type III secretion. Biochemistry 2011, 50, 172–180.

(9)  Epler, C. R., Dickenson, N. E., Olive, A. J., Picking, W. L., and Picking, W. D. Liposomes recruit IpaC to the Shigella flexneri type III secretion apparatus needle as a final step in secretion induction. Infect. Immun. 2009, 77, 2754–2761.

(11)  Barta ML, Shearer JP, Arizmendi O, Tremblay JM, Mehzabeen N, Zheng Q, et al. Single-domain antibodies pinpoint potential targets within Shigella invasion plasmid antigen D of the needle tip complex for inhibition of type III secretion. J Biol Chem 2017, 292(40), 16677–87.

(12)  Sierocki, R.; Jneid, B.; Delgado, M. L. O.; Plaisance, M.; Maillère, B.; Nozach, H.; Simon, S. An antibody targeting type III secretion system induces broad protection against Salmonella and Shigella infections. PLOS Neglected Tropical Diseases 2021, 15(3): e0009231
(14)  Sadana, P., Monnich, M., Unverzagt, C. and Scrima, A. Structure of the Y. pseudotuberculosis adhesin InvasinE. Protein Sci 2017, 26: 1182–1195.

(15)  Salema, V., Marın, E., Martınez-Arteaga, R., Ruano-Gallego, D., Fraile, S., Margolles, Y., et al. Selection of single domain antibodies from immune libraries displayed on the surface of E. coli cells with two b-domains of opposite topologies. PLoS One 2013, 8: e75126.

##Anticipated results from early modelings
Our early modeling result indicated that the project is theoretically feasible.
By using the theory of diffusion (Fick’s Diffusion Law) and parameters from literature review, we modeled the distribution of AMP that is directed to the pathogen by antibodies. For rough estimation, we hypothesize the geometry of probiotics can be simplified as tiny spherical particles with radius R (about $1μm$), and the diffusion of AMP in the gastrointestinal tract was modeled as spherically symmetric concentration profiles.

$$
\Delta C=\frac{1}{r^2}\partial_r(r^2\partial_rC)
$$
($C$: concentration, $r$: the distance from the center of one probiotic sphere)
Stationary situation was the focus, that is
$$
\Delta C=0\\\\[8pt]
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
