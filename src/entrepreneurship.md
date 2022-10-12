<div class="h1-bg">
    <h1 class>Entrepreneurship</h1>
    <img src="https://static.igem.wiki/teams/4161/wiki/fig-entre.png" />
</div>

## Introduction

The probiotics market in China is expected to reach a size of USD 13,527.100 million by 2025, growing at a CAGR of 8.81 percent. In 2019, the market was valued at US$8,149.466 million [^1]. Previous research findings has emphasized on the significance of gut microbiome on human health, and this has opened up the marketing of probiotics. Taking advantage of the booming market and the maturation of bioengineering technology, our project aims to guard our guts through bacteria-bacteria interaction, a method that is an alternative to antibiotics. Some probiotic product utilizing bacteria-bacteria cell interaction has already gone through clinical trials and entered the market, such as Lactobacillus reuteri DSM17648 that treats H.pylori infection [^2]. Therefore, it is possible for our product to secure a place in the probiotic market.


The terminal of our designed product is a drug used in people. We understand that animal model testings as well as clinical trials are often involved in the process of drug development. What we have reached so far is only a prototype tested in vitro. After the completion of the in vitro testing we will proceed to in vivo models. To improve our plan we interviewed Jisheng Lin from Sinovac Biotech company, to collected feedbacks and suggestions about how to turn our products into commercial ones as well as cautions on putting our products in a real world situation. Here we provide considerations from various aspects of accessing our products into market and our solutions so far.

## Safety

"Safety is always the first concern," as suggested by Mr. Lin, "even it doesn't work well, at least does no harm." Based on Mr. Lin's suggestions as well as our previous thoughts, several sources of safety concerns are listed as follows: First, the plasmid we used for selection contains a bacterial ampicillin resistance gene. though not expressed in yeast due to different promoter and codon structures, potential horizontal gene transfers still leave risks of spread antibiotic resistent genes to other prokaryotes in the intestine. Second, though our vectors cell linage yeast strain EBY100 has been well studied, the genomic background of our engineered yeast is unknown. Our engineering process may alter the growth and metabolic characteristics. Efforts should be given to test if engineered yeast could harm human bodies. Besides, human intestine is a complicated microenvironment comprises of a microbiota yet not fully understood. It is also important to clarify how long does our engineered yeast can survive in human body, whether it gains competitive advantages over native gut microorganisms, and how it alter the structure of gut microbiome. Third, similar to antibody therapies, allergy may be a question to some people. Therefore, an approach should be developed to pre-test patients' irritability. Fourth, as a commercial product, a standard of quality control during each step of the engineering or the drug production is also needed.

![Entre_image](https://static.igem.wiki/teams/4161/wiki/entre-image.jpg)

## Effectiveness

Effectiveness demonstrates the values of our products. We have shown qualitatively the expression of the antibodies and the binding between the antigen and the antibodies. For a real world application, we need to establish standard to access and quantify these values. Moreover, the success in the simplified in vitro assay does not guarantee the effectiveness of the drug to work in a real scenario. Considering the real world application that our products function in human GI tracts, it requires the engineered yeast be able to settle down, proliferate, and bind to *Shigella* spike proteins. Hence, the growth curve about the engineered yeast in human intestines should also be tested. More importantly, the performance of the drug should also be assessed. Potential questions include whether there is dosage-dependent protection effect, how to assess these effects if they exist, and whether this product focuses on therapy or is precaution oriented.


## Economics

The third aspect related to the economics about our products. Apart from the reagents and consumable usage, stabilities, including plasmid stability and the stability of the phenotype expressions, are important factor influence the cost of production. A passaging lineage stably expression the recombinant antibodies greatly reduce the cost of continuously re-engineering the yeast to harvest antibody expression. Efforts should be devoted to focus on increasing the stability antibody expression during passages.

## Future

We should also seek for further development of our products in the future, such as increasing the valency of our product so that it can target multiple pathogens at the same time.

## Our Solution

As many goals are still far from being achieved, here we proposed our future plan altogether with what we have reached. We used two different approaches to remove the influence of ampicillin resistance gene. In the first approach, we designed a PCR-fusion that jumps the whole ampicillin resistant gene and the bacterial replication origin. The resting plasmid contains around 3200bp including the TRP1 gene that is a suitable size for PCR amplification and enables the selection of transformant yeast cells. The alternative approach used CRISPR-Cas9 to integrate the whole "promoter-Aga2-20ipaD" cassette into yeast genome. The latter also increases phenotype stability as no plasmid is needed to maintain the phenotype. For expression level assessment, we have already established a system employed ELISA to quantify the expression. However, one drawback of this approach is that it does not differentiate surface displayed antibodies from the antibodies no correctly presented on surface. An improved design uses biotins to labeled all surface proteins followed by avidin affinity binding to isolate these proteins from the protein repertoire. Isolated surface protein can be then analyzed via ELISA. To improve expression level, we have listed a set of developed constitutive yeast promoters as candidates. However, we also realized that promoter engineering processes may be required in the future. For the effectiveness test, we have designed a cell invasion test in vitro. Engineered yeast cells together with *Shigella* will be applied to Vero cell cultures. Effectiveness will be measured by proportion of cells being infected.

To remove the influence of cell lines on the result of invasion test, we plan to substitute the Vero cell lines to epithelial cells in the future. After the completion of in vitro assay, further in vivo assay may be applied.

# Conclusion

We realized that what we have built is only a prototype of a *Shigella* infection precaution drug. There is still a long way to go for optimizing the drug in vitro as well as testing the drug in vivo. However, via a series of design processes, we have developed plans to turn it into real world application.

[^1]:China Probiotics Market Size, Share, Opportunities, COVID-19 Impact, And Trends By Ingredient (Bacteria, Yeast), By Form (Liquid, Dry), By Application (Functional Food And Beverages, Dietary Supplements, Animal Feed), And By End-User (Human, Animal) - Forecasts From 2020 To 2025. (2020). <https://www.knowledge-sourcing.com/report/china-probiotics-market#:~:text=China%20probiotics%20market%20is%20estimated,intestinal%20tracts%2C%20and%20bowel%20function>

[^2]:Significant Reduction in Helicobacter pylori Load in Humans with Non-viable Lactobacillus reuteri DSM17648: A Pilot Study. (2015). <https://pubmed.ncbi.nlm.nih.gov/25481036/>