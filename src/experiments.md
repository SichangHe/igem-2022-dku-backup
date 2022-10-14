<div class="h1-bg">
    <h1 class>Experiments</h1>
    <img src="https://static.igem.wiki/teams/4161/wiki/wetlab5-for-bg.png" />
</div>

## Yeast

### Experiment Overview

**Phases**: 1. Stock vectors preparation and vectors storage; 2. Stock gene preparation and amplification; 3. Gene cloning, plasmid construction, storage, and verification; 4. Yeast transformation, protein display, and detection

**Phase I:** Stock vectors preparation and vectors storage
By the end of this phase, we would get:
One tube of pYD1 vector stock solution
One glycerol stock containing *E. coli* DH5α that were transformed with pYD1 vectors

**Phase II**: Gene cloning, plasmid construction, storage, and verification
By the end of this step, we would get:
One tube of pY20ipaD recombinant stock solution (not pure)
One glycerol stock containing *E. coli* DH5α that were transformed with pYD1 vectors

**Phase IV**: Yeast transformation, protein display, and detection
By the end of this phase, we would get:
Glycerol stock of yeast that were transformed with recombinant plasmids
Induced yeasts (display the nanobody on the surface)

### Lab Notes

[Yeast Lab Notes](https://static.igem.wiki/teams/4161/wiki/saccharomyces-cerevisiae-lab-notebook.pdf).

### Protocols

"One-step Method Competent Cell Preparation Kit" from Beyotime was used for this experiment. The protocol follows the manual of the product[^1].

[*E.coli* Competent Cell Transformation](https://static.igem.wiki/teams/4161/wiki/e-coli-competent-cell-transformation.pdf).

[Plasmid Extraction](https://static.igem.wiki/teams/4161/wiki/plasmid-extraction.pdf).

[Genetic Cloning Enzyme Digestion Ligation](https://static.igem.wiki/teams/4161/wiki/genetic-cloning-enzyme-digestion-ligation.pdf).

"DNA Agarose Gel Recycle Kit" from Beyotime was used for this experiment. The protocol follows the manual of the product.[^2]

[Gel Purification](https://static.igem.wiki/teams/4161/wiki/gel-purification.pdf).

"Frozen-EZ Yeast Transformation II Kit" from Zymo was used for this experiment. The protocol follows the manual of the product.[^3]

[Yeast Induction](https://static.igem.wiki/teams/4161/wiki/yeast-induction.pdf).

[Fluorescence Activated Cell Sorting](https://static.igem.wiki/teams/4161/wiki/florescence-activated-cell-sorting.pdf).

"FLAG Tag Immuno-precipitation Kit (Immunomagnetic Beads Method)" from Beyotime was used for this experiment. The protocol follows the manual of the product[^4].

[Protein Purification](https://static.igem.wiki/teams/4161/wiki/protein-purification.pdf).

"TIANprep Mini Plasmid kit" was used for this experiment. The protocol follows the manual of the product[^5].

[Plasmid Extraction](https://static.igem.wiki/teams/4161/wiki/plasmid-extraction.pdf).

## *Escherichia coli*

### Experiment Overview

[Group E Workflow](https://static.igem.wiki/teams/4161/wiki/group-e-workflow.pdf).

#### 1.1 Express the Protein in *E.coli* BL21 Cytoplasm

3 different VHHs (JPS-G3, JMK-H2, 20ipaD) and 1 antigen (IpaD) are expressed separately in *E.coli* DE3 for protein purification. The DNA sequences of the proteins are bind to different detection tags (VHHs - FLAG-tag, antigen - HA-tag) and inserted into pET41a plasmids for bacterial transformation and protein purification. The pET41a plasmid contains a T7 promoter and a T7 terminator for high-level protein expression in E. *coli* DE3, and a GST tag with a Tb (thrombin) site for protein purification. After transformation, the exogenous proteins will be expressed by the bacteria.

#### 1.2 Protein Purification and Affinity Test

Next, we use the GST tag to purify the recombinant protein. The target proteins will be extracted via GSH-GST interaction, and the remaining GST tag will be cut by thrombin. Then, we can get the purified recombinant proteins (target protein + detection tag).

Lastly, co-IP (immuno-precipitation) followed by Western analysis will be used to test the affinity between VHHs and the antigen. By adding anti-FLAG antibodies and anti-HA antibodies to the samples, we can pull down the recombinant proteins with corresponding tags. If adding either anti-FLAG antibodies or anti-HA antibodies leads to a positive result in 'FLAG-VHH + HA-IpaD', we can say that there is high affinity between the expressed VHHs and the antigen.

#### 2.1 Surface Display via csgA

CsgA, or major curlin subunit, is a component of biofilm. The design was a modified version of the PATCH system from Neel Joshi lab. It is composed of a temperature-controlled promoter, Csg synthetic operon, and the VHH targeting Type III secretion system. The design is predicted to be beneficial in a therapeutic context because biofilm formation effectively inhibits the invasion of *Shigella* into epithelial cells.

#### 2.2 Surface Display via intimin

#### 2.3 Detecting *E.coli* surface display

**Congo red binding assay**\
   We use a quantitative congo-red binding assay to detect the expression of curli fibers. Congo red is a dye that binds to the hydroxyl group of polypeptide chains in amyloid through hydrogen bonds. A control group with no curli expression and a group with curli expression are cultured under the same condition. The 490nm absorbance of both groups are measured to quantify the amount of congo red not in binding with curli fiber [(1)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6898321/)[(2)](https://pubs.acs.org/doi/full/10.1021/acsbiomaterials.6b00437).
**Whole cell filtration ELISA**\
   To detect the expression of curli fibers on the cell surface, we perform whole-cell ELISA. Whole-cell ELISA requires the cells to be seeded to the bottoms of the wells, providing conditions to detect proteins in whole cells [(3)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6898321/)[(4)](https://www.lsbio.com/products/elisakits/cellbased).

#### 2.4 Detecting the Binding Affinity Between *E.coli* Expressing VHHs and the antigen

   **Aggregation Assay using OD600 measurements [(5)](https://doi.org/10.1016/j.cell.2018.06.041)**\
   Ag (antigen)-only *E.coli*, Nb (nanobody, i.e., VHHs)-only *E.coli* and the mixture of the two are cultured separately in LB liquid medium for 24 hours. OD600 of their supernatant are measured immediately/after 24 hours to see whether there is significant difference between the Ag-only group, Nb-only group, and mixture group. A significant low OD600 in the mixture group indicates that the *E.coli* expressing VHHs and antigens bind to each other, form assembly, and sink.

   **Observing the Morphologies using Confocal Microscopy [(5)](https://doi.org/10.1016/j.cell.2018.06.041)**\
   GFP and m*Cherry* genes were expressed respectively in Ag-only *E.coli* and Nb-only *E.coli*. When observing the morphology via a confocal microscope, we should see that most neighbors of a certain bacterium should have opposite colors.

#### Lab Notes

[*E.coli* Lab Notes](https://static.igem.wiki/teams/4161/wiki/igem-e-labnotes.pdf).

#### Protocols

[*E.coli* Protocols](https://static.igem.wiki/teams/4161/wiki/igem-e-protocols.pdf).

## *Lactococcus lactis*

### Experiment Overview

![*L.lactis* Workflow](https://static.igem.wiki/teams/4161/wiki/workflow-of-l-lactis-team.png).

### Lab Notes

Because of financial and logistical reasons, wet lab experiments of group L were halted. We therefore can only present the experimental procedures and protocols designed by our members.

### Protocols

Group L intends to display 20ipaD, a nanobody against *Shigella*, onto *L.lactis*. The plasmid construction is performed in *E.coli* and then transformed into *L.lactis*.

[Electroporation Protocol for *Lactococcus lactis*](https://static.igem.wiki/teams/4161/wiki/electroporation-protocol-for-lactococcus-lactis.pdf).

[Gel Extraction Protocol](https://static.igem.wiki/teams/4161/wiki/gel-extraction-protocol.pdf).

[Plasmid Extraction of *L.lactis* Gram positive bacteria](https://static.igem.wiki/teams/4161/wiki/plasmid-extraction-of-l-lactis-gram-positive-bacteria.pdf).

[Protocol for Activating and Preparing Glycerol Stock](https://static.igem.wiki/teams/4161/wiki/protocol-for-activating-and-preparing-glycerol-stock.pdf).

[Protocol for Extracting DNA from *Lactococcus lactis* NZ9000](https://static.igem.wiki/teams/4161/wiki/protocol-for-extracting-dna-from-lactococcus-lactis-nz9000.pdf).

[Protocol for Ligation](https://static.igem.wiki/teams/4161/wiki/protocol-for-ligation.pdf).

[Protocol for Medium Making](https://static.igem.wiki/teams/4161/wiki/protocol-for-medium-making.pdf).

[Protocol for Restriction Enzyme Digestion](https://static.igem.wiki/teams/4161/wiki/protocol-for-restriction-enzyme-digestion.pdf).

Plasmid extraction and gel purification are the same as Group Y.

[Solarbio Protocol of DNA Extraction](https://static.igem.wiki/teams/4161/wiki/solarbio-protocol-of-dna-extraction.pdf).

[^1]: Beyotime One-step Method Competent Cell Preparation Kit. <https://www.beyotime.com/product/D0301.htm>

[^2]: Beyotime DNA Agarose Gel Recycle Kit. <https://www.beyotime.com/product/D0056.htm>

[^3]:Zymo Frozen-EZ_Yeast_Transformation_II_Kit. <https://files.zymoresearch.com/protocols/_t2001_frozen-ez_yeast_transformation_ii.pdf>

[^4]: Beyotime FLAG Tag Immuno-precipitation Kit (Immunomagnetic Beads Method). <https://m.beyotime.com/Manual/P2181%20Flag%E6%A0%87%E7%AD%BE%E8%9B%8B%E7%99%BD%E5%85%8D%E7%96%AB%E6%B2%89%E6%B7%80%E8%AF%95%E5%89%82%E7%9B%92(%E7%A3%81%E7%8F%A0%E6%B3%95).pdf>

[^5]:TIANprep Mini Plasmid kit. <https://en.tiangen.com/download/manual.html?one=34&two=1085&three=1086&id=4307>
