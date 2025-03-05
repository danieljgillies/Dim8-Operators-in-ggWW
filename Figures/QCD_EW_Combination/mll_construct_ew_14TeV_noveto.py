import numpy as np
import matplotlib.pyplot as plt





nnlo_noveto_centre=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nnlo_qcd_centre.npy")
nnlo_noveto_min=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nnlo_qcd_min.npy")
nnlo_noveto_max=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nnlo_qcd_max.npy")



nnlo_noveto_100100=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nnlo_qcd_murenorm=0.50MWW_mufac=0.50MWW.npy")
nnlo_noveto_050050=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nnlo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy")
nnlo_noveto_050100=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nnlo_qcd_murenorm=0.25MWW_mufac=0.50MWW.npy")
nnlo_noveto_100050=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nnlo_qcd_murenorm=0.50MWW_mufac=0.25MWW.npy")
nnlo_noveto_100200=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nnlo_qcd_murenorm=0.50MWW_mufac=1.00MWW.npy")
nnlo_noveto_200100=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nnlo_qcd_murenorm=1.00MWW_mufac=0.50MWW.npy")
nnlo_noveto_200200=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nnlo_qcd_murenorm=1.00MWW_mufac=1.00MWW.npy")




nloew_centre=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nlo_ew_centre.npy")

nloew_noveto_1=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nlo_ew_mufac=0.50MWW.npy")
nloew_noveto_05=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nlo_ew_mufac=0.25MWW.npy")
nloew_noveto_2=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_nlo_ew_mufac=1.00MWW.npy")



lo_noveto_1=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_lo_mufac=0.50MWW.npy")
lo_noveto_05=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_lo_mufac=0.25MWW.npy")
lo_noveto_2=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_qq_lo_mufac=1.00MWW.npy")

del_nloew_noveto_1=nloew_noveto_1/lo_noveto_1
del_nloew_noveto_05=nloew_noveto_05/lo_noveto_05
del_nloew_noveto_2=nloew_noveto_2/lo_noveto_2




nnlonloew_noveto_050050=nnlo_noveto_050050*del_nloew_noveto_05
nnlonloew_noveto_050100=nnlo_noveto_050100*del_nloew_noveto_1
nnlonloew_noveto_200100=nnlo_noveto_200100*del_nloew_noveto_1
nnlonloew_noveto_100100=nnlo_noveto_100100*del_nloew_noveto_1
nnlonloew_noveto_100200=nnlo_noveto_100200*del_nloew_noveto_2
nnlonloew_noveto_100050=nnlo_noveto_100050*del_nloew_noveto_05
nnlonloew_noveto_200200=nnlo_noveto_200200*del_nloew_noveto_2


nnlonloew_noveto_min=[]
nnlonloew_noveto_max=[]

for i in range(0, len(nnlonloew_noveto_100100)):
    values=[nnlonloew_noveto_100100[i], nnlonloew_noveto_050050[i], nnlonloew_noveto_050100[i], nnlonloew_noveto_100050[i], nnlonloew_noveto_100200[i], nnlonloew_noveto_200100[i], nnlonloew_noveto_200200[i]]
    nnlonloew_noveto_min.append(np.min(values))
    nnlonloew_noveto_max.append(np.max(values))

nnlonloew_noveto_min=np.array(nnlonloew_noveto_min)
nnlonloew_noveto_max=np.array(nnlonloew_noveto_max)

print(nnlonloew_noveto_min)
print(nnlonloew_noveto_max)


np.save("mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_centre", nnlonloew_noveto_100100)
np.save("mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_min", nnlonloew_noveto_min)
np.save("mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_max", nnlonloew_noveto_max)

np.save("mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.50MWW_mufac=0.50MWW.npy", nnlonloew_noveto_100100)
np.save("mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.25MWW_mufac=0.25MWW.npy", nnlonloew_noveto_050050)
np.save("mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.25MWW_mufac=0.50MWW.npy", nnlonloew_noveto_050100)
np.save("mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.50MWW_mufac=0.25MWW.npy",nnlonloew_noveto_100050)
np.save("mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.50MWW_mufac=1.00MWW.npy", nnlonloew_noveto_100200)
np.save("mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=1.00MWW_mufac=0.50MWW.npy", nnlonloew_noveto_200100)
np.save("mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=1.00MWW_mufac=1.00MWW.npy", nnlonloew_noveto_200200)








