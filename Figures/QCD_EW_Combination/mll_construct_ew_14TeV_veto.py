import numpy as np
import matplotlib.pyplot as plt





nnllnnlo_centre=np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_centre.npy")
nnllnnlo_min=np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_min.npy")
nnllnnlo_max=np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_max.npy")
nloew_centre=np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nlo_ew_centre.npy")
lo_centre=np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_lo_centre.npy")



print(nnllnnlo_centre)
print(nloew_centre)

print(lo_centre)


del_nloew_centre=nloew_centre/lo_centre

#We need to do this because MATRIX does not give us a full breakdown of scale variations only max and min
#This is ok because the EW corrections are approximately the same at each scale 

nnllnnlonloew_centre=nnllnnlo_centre*del_nloew_centre
nnllnnlonloew_min=nnllnnlo_min*del_nloew_centre
nnllnnlonloew_max=nnllnnlo_max*del_nloew_centre

print(nnllnnlonloew_centre)

np.save("mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_centre", nnllnnlonloew_centre)
np.save("mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_min", nnllnnlonloew_min)
np.save("mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_max", nnllnnlonloew_max)









