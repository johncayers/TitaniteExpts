# TitaniteGrowth
Analysis of Danny Flanagan titanite solubility experiments. Paper published in Contributions to Mineralogy and Petrology in 2022. Code written in RStudio by John C. Ayers. Following is a list of final file versions:
1. Fluorescence test described in Methods: FluorescenceTest.R, input file FluorescenceTestV2.csv
2. Diffusion profile plots: DiffusionProfilePlots.Rmd, input files DiffusionProfilesV3.csv
3. Model fit to our experiments: TitaniteExptsMV4.Rmd, input files TitaniteExptsV3.csv, LEPR_Titanite_ExptsV2.csv
4. Model fit to all experiments (ours + LEPR): AllExptsMV4.Rmd, input files AllExptsV3.csv, LEPR_ExperimentsV2.csv, LEPR_LiquidAnhyV4.csv
5. TitaniteReferences.bib: Bibliography of relevant papers in BibTex format; contains citations in Rmd file.

File types:
Rmd: RStudio notebook files written in markdown language
html: Output files created from Rmd files in hypertext markup language
csv: input files in comma separated text format

Note: AllExptsV3.csv contains silicate glass compositions from
1. titanite growth experiments conducted at Vanderbilt University by graduate student Danny Flanagan.
2. titanite dissolution experiments conducted at RPI by Rick Ryerson and Bruce Watson. 
3. phase equilibrium experiments from the LEPR database (Hirschmann2008) that produced titanite.
LEPR_ExperimentsV2.csv: list of titanite-undersaturated experiments from the LEPR database.
LEPR_LiquidAnhyV4.csv: Glass compositions from titanite-undersaturated melts from the LEPR database.
