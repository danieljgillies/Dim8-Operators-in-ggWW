import numpy as np

#We load the combined qcd and ew corrections for qq as the best qq prediction.
#We use the "cross" combined QCD EW prediction as this gives a best guess for the combined QCDEW contribution.
nnllnnlonloew_centre=np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_centre.npy")
nnllnnlonloew_min=np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_min.npy")
nnllnnlonloew_max=np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_max.npy")

print(nnllnnlonloew_centre)
#We load the nlo photon contribution.
nlophoton_MWWover2=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=0.5MWW.npy")
nlophoton_MWWover4=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=0.25MWW.npy")
nlophoton_MWW=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=1.0MWW.npy")


#We load the nll gluon contribution.
ggnll_050050050=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_050050025=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
ggnll_050050100=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
ggnll_025025050=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
ggnll_025050050=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_050025050=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
ggnll_050100050=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
ggnll_100050050=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_100100050=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")


print(ggnll_050050050)
print(nlophoton_MWWover2)

#We combine for each factorisation and renormalisation scale the photon and gluon contributions.
#We cannot also do this for the qq contribution as MATRIX+Radish does not give us a breakdown by \
#           renormalisation/factorisation/resummation scales only the maximum and minimum. For this \ 
#           reason we add the qq and gg/gammagamma errors in quadrature.
ggphoton_nll_050050050=ggnll_050050050+nlophoton_MWWover2
ggphoton_nll_050050025=ggnll_050050025+nlophoton_MWWover2
ggphoton_nll_050050100=ggnll_050050100+nlophoton_MWWover2
ggphoton_nll_025025050=ggnll_025025050+nlophoton_MWWover4
ggphoton_nll_025050050=ggnll_025050050+nlophoton_MWWover2
ggphoton_nll_050025050=ggnll_050025050+nlophoton_MWWover4
ggphoton_nll_050100050=ggnll_050100050+nlophoton_MWW
ggphoton_nll_100050050=ggnll_100050050+nlophoton_MWWover2
ggphoton_nll_100100050=ggnll_100100050+nlophoton_MWW


ggphoton_nll_min=[]
ggphoton_nll_max=[]

#We find the spread of combined gluon-photon contributions bin by bin.
for i in range(0, len(ggphoton_nll_050050050)):
    values=[ggphoton_nll_050050050[i], ggphoton_nll_050050025[i], ggphoton_nll_050050100[i], ggphoton_nll_025025050[i], ggphoton_nll_025050050[i], ggphoton_nll_050025050[i], ggphoton_nll_050100050[i], ggphoton_nll_100050050[i], ggphoton_nll_100100050[i]]
    ggphoton_nll_min.append(np.min(values))
    ggphoton_nll_max.append(np.max(values))


ggphoton_nll_min=np.array(ggphoton_nll_min)
ggphoton_nll_max=np.array(ggphoton_nll_max)

#We find the average (over + and -) theoretical error of combined gluon-photon contributions bin by bin.
ggphoton_nll_err=(ggphoton_nll_max-ggphoton_nll_min)/2

#We find the average (over + and -) theoretical error of qq contributions bin by bin.
err_qq=(nnllnnlonloew_max-nnllnnlonloew_min)/2

#We combine the errors in quadrature.
err_sm=(err_qq**2 + ggphoton_nll_err**2)**0.5
#print(ggphoton_nll_050050050)
#print(ggnll_050050050)
#print(nlophoton_MWWover2)
#We produce resummed SM predictions with a combined theoretical uncertainty.
sm=nnllnnlonloew_centre+ggphoton_nll_050050050
sm_min=sm-err_sm
sm_max=sm+err_sm

np.save("mll_14TeV_veto35_sm_centre", sm)
np.save("mll_14TeV_veto35_sm_min", sm_min)
np.save("mll_14TeV_veto35_sm_max", sm_max)
