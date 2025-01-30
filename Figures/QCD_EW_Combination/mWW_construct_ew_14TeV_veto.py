import numpy as np
import matplotlib.pyplot as plt





nnllnnlo_centre=np.load("../Data/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_centre.npy")
nnllnnlo_min=np.load("../Data/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_min.npy")
nnllnnlo_max=np.load("../Data/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_max.npy")
nloew_centre=np.load("../Data/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nlo_ew_centre.npy")
lo_centre=np.load("../Data/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_lo_centre.npy")



print(nnllnnlo_centre)
print(nloew_centre)

print(lo_centre)


del_nloew_centre=nloew_centre/lo_centre

#We need to do this because MATRIX does not tell us which scale the different 

nnllnnlonloew_centre=nnllnnlo_centre*del_nloew_centre
nnllnnlonloew_min=nnllnnlo_min*del_nloew_centre
nnllnnlonloew_max=nnllnnlo_max*del_nloew_centre

print(nnllnnlonloew_centre)

np.save("mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_nlo_ew_centre", nnllnnlonloew_centre)
np.save("mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_nlo_ew_min", nnllnnlonloew_min)
np.save("mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_nlo_ew_max", nnllnnlonloew_max)









