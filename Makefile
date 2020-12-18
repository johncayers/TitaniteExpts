### R Make file for titanite solubility project
# John C. Ayers
# Created 12/18/2020
# See Gandrud v. 3 (2020) pp. 114-120
# Set working directory
# setwd("C:/Users/ayersj/OneDrive - Vanderbilt/Papers/SpheneSolubility/DataAnalysis/TitaniteExpts")
RDIR = .
# Feed input files into diffusion analysis, create output (target) file with saturation concentrations
# source(DiffusionAnalysisV3.Rmd)
source_python(DiffusionAnalysis.py)

# Merge diffusion and growth experiment results
# Need to change input file TitaniteExptsV2.csv to growth experiments only
# and input file py_optimized_values.csv
source(TitaniteExptsM.Rmd)
