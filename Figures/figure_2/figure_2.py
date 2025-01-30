import numpy as np
import matplotlib.pyplot as plt
from math import log10, floor

#Doesn't matter if we multiply by 2 and so on because there is no 

def round_to_5(x):
    rounded=[]
    for i in range(len(x)):
        rounded.append(np.round(x[i], 6-int(floor(log10(abs(x[i]))))))
    return np.array(rounded)


def array_for_plot(a):
    return np.concatenate((np.array([a[0]]), a, np.array([a[len(a)-1]])))

bins=round_to_5(np.logspace(np.log10(200), np.log10(4000), 17))
#print(bins)
bin_widths=bins[1:17]-bins[0:16]
bin_widths18=np.array([41.1817, 41.1817, 49.6614, 59.8871, 72.2183, 87.0887, 105.021, 126.6458, 152.7232, 184.1698, 222.093, 267.823, 322.97, 389.473, 469.668, 566.377, 682.999, 682.999])

bin_centres=(bins[0:16] + bins[1:17])/2
bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))




sm=2*np.load("../SM_Construction/mll_14TeV_veto35_sm_centre.npy")
sm_min=2*np.load("../SM_Construction/mll_14TeV_veto35_sm_min.npy")
sm_max=2*np.load("../SM_Construction/mll_14TeV_veto35_sm_max.npy")

#print(sm)
#print(sm_min)
#print(sm_max)

nnllnnlonloew_centre=2*np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_centre.npy")
nnllnnlonloew_min=2*np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_min.npy")
nnllnnlonloew_max=2*np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_max.npy")


nlophoton_MWWover2=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=0.5MWW.npy")
nlophoton_MWWover4=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=0.25MWW.npy")
nlophoton_MWW=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=1.0MWW.npy")


#We load the nll gluon contribution.
ggnll_050050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_050050025=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
ggnll_050050100=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
ggnll_025025050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
ggnll_025050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_050025050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
ggnll_050100050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
ggnll_100050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_100100050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")

#Load the BSM contributions
kgnll_050050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kgnll_050050025=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
kgnll_050050100=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
kgnll_025025050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
kgnll_025050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kgnll_050025050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
kgnll_050100050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
kgnll_100050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kgnll_100100050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")


kg2nll_050050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kg2nll_050050025=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
kg2nll_050050100=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
kg2nll_025025050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
kg2nll_025050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kg2nll_050025050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
kg2nll_050100050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
kg2nll_100050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kg2nll_100100050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")


k3nll_050050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k3nll_050050025=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k3nll_050050100=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k3nll_025025050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k3nll_025050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k3nll_050025050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k3nll_050100050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k3nll_100050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k3nll_100100050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")


k32nll_050050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k32nll_050050025=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k32nll_050050100=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k32nll_025025050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k32nll_025050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k32nll_050025050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k32nll_050100050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k32nll_100050050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k32nll_100100050=2*np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")

#Set an EFT mass scale to rescale the BSM amplitudes appropriately.
mass_scale=3.7# TeV

#Since the resummation from MATRIX+Radish does not give a breakdown in terms of \
#       fac, renorm, and resumm scales we combine the qq error and the \
#       gg/photon (SM and BSM) error in quadrature. Below is the qq error.
err_qq=(nnllnnlonloew_max-nnllnnlonloew_min)/2


#Combining the gg SM and BSM pieces with the photon piece...
#First example is adding the BSM OGH inteference with SM on top of SM prediction.
kgphoton_nll_050050050=((2000**2)/((mass_scale*1000)**2))*kgnll_050050050+ggnll_050050050+nlophoton_MWWover2
kgphoton_nll_050050025=((2000**2)/((mass_scale*1000)**2))*kgnll_050050025+ggnll_050050025+nlophoton_MWWover2
kgphoton_nll_050050100=((2000**2)/((mass_scale*1000)**2))*kgnll_050050100+ggnll_050050100+nlophoton_MWWover2
kgphoton_nll_025025050=((2000**2)/((mass_scale*1000)**2))*kgnll_025025050+ggnll_025025050+nlophoton_MWWover4
kgphoton_nll_025050050=((2000**2)/((mass_scale*1000)**2))*kgnll_025050050+ggnll_025050050+nlophoton_MWWover2
kgphoton_nll_050025050=((2000**2)/((mass_scale*1000)**2))*kgnll_050025050+ggnll_050025050+nlophoton_MWWover4
kgphoton_nll_050100050=((2000**2)/((mass_scale*1000)**2))*kgnll_050100050+ggnll_050100050+nlophoton_MWW
kgphoton_nll_100050050=((2000**2)/((mass_scale*1000)**2))*kgnll_100050050+ggnll_100050050+nlophoton_MWWover2
kgphoton_nll_100100050=((2000**2)/((mass_scale*1000)**2))*kgnll_100100050+ggnll_100100050+nlophoton_MWW


kgphoton_nll_min=[]
kgphoton_nll_max=[]

#We find the spread of combined SM/BSM gluon-photon contributions bin by bin.
for i in range(0, len(kgphoton_nll_050050050)):
    values=[kgphoton_nll_050050050[i], kgphoton_nll_050050025[i], kgphoton_nll_050050100[i], kgphoton_nll_025025050[i], kgphoton_nll_025050050[i], kgphoton_nll_050025050[i], kgphoton_nll_050100050[i], kgphoton_nll_100050050[i], kgphoton_nll_100100050[i]]
    kgphoton_nll_min.append(np.min(values))
    kgphoton_nll_max.append(np.max(values))

kgphoton_nll_min=np.array(kgphoton_nll_min)
kgphoton_nll_max=np.array(kgphoton_nll_max)

#We find the average (over + and -) theoretical error of combined gluon-photon contributions bin by bin.

kgphoton_nll_err=(kgphoton_nll_max-kgphoton_nll_min)/2


#We add the error in quadrature.
err_sm_kg=(err_qq**2 + kgphoton_nll_err**2)**0.5

#New SM + operator OGH contribution with theoretical errors.
sm_kg=nnllnnlonloew_centre+kgphoton_nll_050050050
sm_kg_min=sm_kg-err_sm_kg
sm_kg_max=sm_kg+err_sm_kg


#Repeat for other pieces...

kg2photon_nll_050050050=((2000**4)/((mass_scale*1000)**4))*kg2nll_050050050+ggnll_050050050+nlophoton_MWWover2
kg2photon_nll_050050025=((2000**4)/((mass_scale*1000)**4))*kg2nll_050050025+ggnll_050050025+nlophoton_MWWover2
kg2photon_nll_050050100=((2000**4)/((mass_scale*1000)**4))*kg2nll_050050100+ggnll_050050100+nlophoton_MWWover2
kg2photon_nll_025025050=((2000**4)/((mass_scale*1000)**4))*kg2nll_025025050+ggnll_025025050+nlophoton_MWWover4
kg2photon_nll_025050050=((2000**4)/((mass_scale*1000)**4))*kg2nll_025050050+ggnll_025050050+nlophoton_MWWover2
kg2photon_nll_050025050=((2000**4)/((mass_scale*1000)**4))*kg2nll_050025050+ggnll_050025050+nlophoton_MWWover4
kg2photon_nll_050100050=((2000**4)/((mass_scale*1000)**4))*kg2nll_050100050+ggnll_050100050+nlophoton_MWW
kg2photon_nll_100050050=((2000**4)/((mass_scale*1000)**4))*kg2nll_100050050+ggnll_100050050+nlophoton_MWWover2
kg2photon_nll_100100050=((2000**4)/((mass_scale*1000)**4))*kg2nll_100100050+ggnll_100100050+nlophoton_MWW


kg2photon_nll_min=[]
kg2photon_nll_max=[]

for i in range(0, len(kg2photon_nll_050050050)):
    values=[kg2photon_nll_050050050[i], kg2photon_nll_050050025[i], kg2photon_nll_050050100[i], kg2photon_nll_025025050[i], kg2photon_nll_025050050[i], kg2photon_nll_050025050[i], kg2photon_nll_050100050[i], kg2photon_nll_100050050[i], kg2photon_nll_100100050[i]]
    kg2photon_nll_min.append(np.min(values))
    kg2photon_nll_max.append(np.max(values))

kg2photon_nll_min=np.array(kg2photon_nll_min)
kg2photon_nll_max=np.array(kg2photon_nll_max)

kg2photon_nll_err=(kg2photon_nll_max-kg2photon_nll_min)/2

err_sm_kg2=(err_qq**2 + kg2photon_nll_err**2)**0.5


sm_kg2=nnllnnlonloew_centre+kg2photon_nll_050050050

sm_kg2_min=sm_kg2-err_sm_kg2
sm_kg2_max=sm_kg2+err_sm_kg2




k3photon_nll_050050050=((2000**4)/((mass_scale*1000)**4))*k3nll_050050050+ggnll_050050050+nlophoton_MWWover2
k3photon_nll_050050025=((2000**4)/((mass_scale*1000)**4))*k3nll_050050025+ggnll_050050025+nlophoton_MWWover2
k3photon_nll_050050100=((2000**4)/((mass_scale*1000)**4))*k3nll_050050100+ggnll_050050100+nlophoton_MWWover2
k3photon_nll_025025050=((2000**4)/((mass_scale*1000)**4))*k3nll_025025050+ggnll_025025050+nlophoton_MWWover4
k3photon_nll_025050050=((2000**4)/((mass_scale*1000)**4))*k3nll_025050050+ggnll_025050050+nlophoton_MWWover2
k3photon_nll_050025050=((2000**4)/((mass_scale*1000)**4))*k3nll_050025050+ggnll_050025050+nlophoton_MWWover4
k3photon_nll_050100050=((2000**4)/((mass_scale*1000)**4))*k3nll_050100050+ggnll_050100050+nlophoton_MWW
k3photon_nll_100050050=((2000**4)/((mass_scale*1000)**4))*k3nll_100050050+ggnll_100050050+nlophoton_MWWover2
k3photon_nll_100100050=((2000**4)/((mass_scale*1000)**4))*k3nll_100100050+ggnll_100100050+nlophoton_MWW


k3photon_nll_min=[]
k3photon_nll_max=[]

for i in range(0, len(k3photon_nll_050050050)):
    values=[k3photon_nll_050050050[i], k3photon_nll_050050025[i], k3photon_nll_050050100[i], k3photon_nll_025025050[i], k3photon_nll_025050050[i], k3photon_nll_050025050[i], k3photon_nll_050100050[i], k3photon_nll_100050050[i], k3photon_nll_100100050[i]]
    k3photon_nll_min.append(np.min(values))
    k3photon_nll_max.append(np.max(values))

k3photon_nll_min=np.array(k3photon_nll_min)
k3photon_nll_max=np.array(k3photon_nll_max)

k3photon_nll_err=(k3photon_nll_max-k3photon_nll_min)/2



err_sm_k3=(err_qq**2 + k3photon_nll_err**2)**0.5


sm_k3=nnllnnlonloew_centre+k3photon_nll_050050050
sm_k3_min=sm_k3-err_sm_k3
sm_k3_max=sm_k3+err_sm_k3



k32photon_nll_050050050=((2000**8)/((mass_scale*1000)**8))*k32nll_050050050+ggnll_050050050+nlophoton_MWWover2
k32photon_nll_050050025=((2000**8)/((mass_scale*1000)**8))*k32nll_050050025+ggnll_050050025+nlophoton_MWWover2
k32photon_nll_050050100=((2000**8)/((mass_scale*1000)**8))*k32nll_050050100+ggnll_050050100+nlophoton_MWWover2
k32photon_nll_025025050=((2000**8)/((mass_scale*1000)**8))*k32nll_025025050+ggnll_025025050+nlophoton_MWWover4
k32photon_nll_025050050=((2000**8)/((mass_scale*1000)**8))*k32nll_025050050+ggnll_025050050+nlophoton_MWWover2
k32photon_nll_050025050=((2000**8)/((mass_scale*1000)**8))*k32nll_050025050+ggnll_050025050+nlophoton_MWWover4
k32photon_nll_050100050=((2000**8)/((mass_scale*1000)**8))*k32nll_050100050+ggnll_050100050+nlophoton_MWW
k32photon_nll_100050050=((2000**8)/((mass_scale*1000)**8))*k32nll_100050050+ggnll_100050050+nlophoton_MWWover2
k32photon_nll_100100050=((2000**8)/((mass_scale*1000)**8))*k32nll_100100050+ggnll_100100050+nlophoton_MWW


k32photon_nll_min=[]
k32photon_nll_max=[]

for i in range(0, len(k32photon_nll_050050050)):
    values=[k32photon_nll_050050050[i], k32photon_nll_050050025[i], k32photon_nll_050050100[i], k32photon_nll_025025050[i], k32photon_nll_025050050[i], k32photon_nll_050025050[i], k32photon_nll_050100050[i], k32photon_nll_100050050[i], k32photon_nll_100100050[i]]
    k32photon_nll_min.append(np.min(values))
    k32photon_nll_max.append(np.max(values))

k32photon_nll_min=np.array(k32photon_nll_min)
k32photon_nll_max=np.array(k32photon_nll_max)

k32photon_nll_err=(k32photon_nll_max-k32photon_nll_min)/2

err_sm_k32=(err_qq**2 + k32photon_nll_err**2)**0.5


sm_k32=nnllnnlonloew_centre+k32photon_nll_050050050

sm_k32_min=sm_k32-err_sm_k32
sm_k32_max=sm_k32+err_sm_k32


#For plotting we repeat first and last bin so the prediction does not get cut-off \
#        at ends when using plt.step()
sm=array_for_plot(sm)
sm_min=array_for_plot(sm_min)
sm_max=array_for_plot(sm_max)
sm_kg=array_for_plot(sm_kg)
sm_kg2=array_for_plot(sm_kg2)
sm_k3=array_for_plot(sm_k3)
sm_k32=array_for_plot(sm_k32)

#Figure
plt.figure(figsize=(20, 15),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)

#This is to make the striped shaded area look nicer.
plt.rcParams["hatch.linewidth"] = 4

rec1 = plt.Rectangle((3700/4,-0.2),4000-3700/4,2.2, facecolor="#d3d3d3", 
                     edgecolor="white", hatch=r"\\", zorder=0)

rec2 = plt.Rectangle((3700/4,-0.2),4000-3700/4,2.2, facecolor="#d3d3d3", 
                     edgecolor="white", hatch=r"\\", zorder=0)


axs[0].add_patch(rec1)
axs[1].add_patch(rec2)
axs[0].annotate(r'$\Lambda=$'+str(mass_scale)+r' TeV', (220, 1.5),\
               fontsize=16,color="#3b3b3b")


axs[0].step(bin_centres, sm/sm, color='k', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2$')
axs[0].fill_between(bin_centres, sm_min/sm, sm_max/sm,
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, sm_kg/sm, color='r', linestyle="--", where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2 + \frac{2c_{GH}}{\Lambda^2}2\mathrm{Re}\left(\mathcal{M}^{(gg)}_{\mathrm{SM}}\overline{\mathcal{M}_{g}}^{(6)\ *}\right)$')
axs[0].step(bin_centres, sm_kg2/sm, color='r', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2 + \frac{c^2_{GH}}{\Lambda^4}|\overline{\mathcal{M}^{(6)}_{g}}|^2$')

axs[0].step(bin_centres, sm_k3/sm, color='b', linestyle="--", where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2 + \frac{2c_3}{\Lambda^4}2\mathrm{Re}\left(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}_3^{(8)\ *}\right)$')
axs[0].step(bin_centres, sm_k32/sm, color='b', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2 + \frac{c^2_3}{\Lambda^8}|\mathcal{M}^{(8)}_3|^2$')

axs[0].semilogx()
axs[0].set_xlim(200,4000) 
axs[0].set_ylim(-0.2,2) 

axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
               fontsize=16,color="black")
axs[0].set_ylabel(r"Ratio to SM",\
               fontsize=16,color="black")


axs[0].legend(loc="lower left", fontsize=9.5, ncol=2)    

axs[0].tick_params(which="both", labelsize=14, direction='in', right=True, top=True, pad=10)




axs[1].step(bin_centres, sm/sm, color='k', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2$')
axs[1].fill_between(bin_centres, sm_min/sm, sm_max/sm,
                     color='k', alpha=0.2, step='mid')

axs[1].step(bin_centres, sm_kg/sm, color='r', linestyle="--", where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2 + \frac{2c_{GH}}{\Lambda^2}2\mathrm{Re}\left(\mathcal{M}^{gg}_{\mathrm{SM}}\overline{\mathcal{M}_{g}}^*\right)$')
axs[1].step(bin_centres, sm_kg2/sm, color='r', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2 + \frac{c^2_{GH}}{\Lambda^4}|\overline{\mathcal{M}_{g}}|^2$')

axs[1].step(bin_centres, sm_k3/sm, color='b', linestyle="--", where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2 + \frac{2c_3}{\Lambda^4}2\mathrm{Re}\left(\mathcal{M}^{gg}_{\mathrm{SM}}\overline{\mathcal{M}_3}^*\right)$')
axs[1].step(bin_centres, sm_k32/sm, color='b', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2 + \frac{c^2_3}{\Lambda^8}|\mathcal{M}_3|^2$')

axs[1].set_ylim(0.9,1.1) 
axs[1].set_xticks([200, 1000, 4000])

axs[1].tick_params(which="both", labelsize=14, direction='in', right=True, top=True, pad=10)
axs[1].set_xticklabels(labels=[r"$200$", r"$1000$", r"$4000$"])


plt.tight_layout()
plt.savefig("figure_2.pdf")
