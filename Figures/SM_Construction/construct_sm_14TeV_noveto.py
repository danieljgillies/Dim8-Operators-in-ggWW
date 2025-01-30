import numpy as np

nnlonloew_noveto_100100=np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.5MWW_mufac=0.5MWW.npy")
nnlonloew_noveto_050050=np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.25MWW_mufac=0.25MWW.npy")
nnlonloew_noveto_050100=np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.25MWW_mufac=0.5MWW.npy")
nnlonloew_noveto_100050=np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.5MWW_mufac=0.25MWW.npy",)
nnlonloew_noveto_100200=np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.5MWW_mufac=1.0MWW.npy")
nnlonloew_noveto_200100=np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=1.0MWW_mufac=0.5MWW.npy")
nnlonloew_noveto_200200=np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=1.0MWW_mufac=1.0MWW.npy")



nlophoton_noveto_MWWover2=np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=0.5MWW.npy")
nlophoton_noveto_MWWover4=np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=0.25MWW.npy")
nlophoton_noveto_MWW=np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=1.0MWW.npy")

gglo_050050=np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy")
gglo_025025=np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy")
gglo_025050=np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy")
gglo_050025=np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy")
gglo_050100=np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy")
gglo_100050=np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy")
gglo_100100=np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy")

sm_050050=nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_MWWover2
sm_025025=nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_MWWover4
sm_025050=nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_MWWover2
sm_050025=nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_MWWover4
sm_050100=nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_MWW
sm_100050=nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_MWWover2
sm_100100=nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_MWW


print(6000*nnlonloew_noveto_100100)
print(6000*gglo_050050)
print(nlophoton_noveto_MWWover2)

sm_min=[]
sm_max=[]

for i in range(0, len(sm_050050)):
    values=[sm_050050[i], sm_025025[i], sm_025050[i], sm_050025[i], sm_050100[i], sm_100050[i], sm_100100[i]]
    sm_min.append(np.min(values))
    sm_max.append(np.max(values))

sm_min=np.array(sm_min)
sm_max=np.array(sm_max)

sm=sm_050050



np.save("mll_14TeV_noveto_sm_centre", sm)
np.save("mll_14TeV_noveto_sm_min", sm_min)
np.save("mll_14TeV_noveto_sm_max", sm_max)


