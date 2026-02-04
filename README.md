---
title: "Dimension-8 Operators in W^+ W^- production via gluon fusion."
author: "Daniel James Gillies"
date: 06-02-25
---

# Dimension-8 Operators in \( W^+ W^- \) production via gluon fusion.

## Table of Contents

1. [Introduction](#introduction)
2. [Layout of Repo](#layout)



---

## Introduction <a name="introduction"></a>

This GitHub repo is intended to make available the data and tools that were used for the paper "Dimension 8 Operators in WW production via gluon fusion" [arXiv: 2412.16020]. 



## Layout <a name="layout"></a>

- `Figures/`
Contains all scripts, inputs (`.npy`), and outputs (`.pdf`) used to generate the paper’s plots. Each subfolder corresponds to a figure or a specific workflow.

- `Figures/Data_numpy_for_figures`
Contains .npy files with the raw distributions for 13TeV and 14TeV data. This is given for SM
and BSM at some different orders. The BSM gg data from MCFM-RE was originally cross section density
and was multiplied by the bin width to keep it in line with outputs from other programs.

- `Figures/figure_*` 
One folder per figure; typically includes a plotting script (`.py`) and generated pdfs.

   -`Figures/figure_*_1percent`
      These are generated with a combined 1 percent theoretical/systematic error. 
   -`Figures/figure_*_comp*`
      These show constraints with different ways of ensuring EFT validity.

- `Figures/withdata_find_chisq_vals.py`
Builds chi-squared contours from ATLAS data, including bin selection and EFT validity constraints.

- `Figures/withpseudodata_find_chisq_vals.py`
Generates contours from pseudodata with optional systematic errors and sampling.

- `Figures/SM_Construction/`
Stores scripts and arrays for constructing SM predictions at different energies and veto setups.

- `Figures/QCD_EW_Combination/`
Contains data and scripts combining QCD and electroweak corrections used for SM inputs.

- `HelicityAmps/`
Contains Mathematica notebooks showing how the Helicity Amplitudes were calculated for implementation into MCFM-RE. Furthermore the notebook used to generate the FeynRules folder
for the cross check with MadGraph is also shown.


