import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from scipy.optimize import minimize, basinhopping, shgo
from math import log10, floor
import sys
sys.path.insert(1, '..')

from factor_conversions import fac2lam,lam2fac
from withpseudodata_find_chisq_vals import _chisq, produce_contours_ATLAS

nnlonloew_noveto_centre=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_centre.npy")
nnlonloew_noveto_min=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_min.npy")
nnlonloew_noveto_max=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_max.npy")

nnlonloew_noveto_100100=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.5MWW_mufac=0.5MWW.npy")
nnlonloew_noveto_050050=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.25MWW_mufac=0.25MWW.npy")
nnlonloew_noveto_050100=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.25MWW_mufac=0.5MWW.npy")
nnlonloew_noveto_100050=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.5MWW_mufac=0.25MWW.npy",)
nnlonloew_noveto_100200=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.5MWW_mufac=1.0MWW.npy")
nnlonloew_noveto_200100=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=1.0MWW_mufac=0.5MWW.npy")
nnlonloew_noveto_200200=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=1.0MWW_mufac=1.0MWW.npy")

err_qq=(nnlonloew_noveto_max-nnlonloew_noveto_min)/2


nlophoton_noveto_MWWover2=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=0.5MWW.npy")
nlophoton_noveto_MWWover4=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=0.25MWW.npy")
nlophoton_noveto_MWW=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=1.0MWW.npy")

gglo_050050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy")
gglo_025025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy")
gglo_025050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy")
gglo_050025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy")
gglo_050100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy")
gglo_100050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy")
gglo_100100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy")



sm=2*3000*np.load("../SM_Construction/mll_14TeV_noveto_sm_centre.npy")
sm_min=2*3000*np.load("../SM_Construction/mll_14TeV_noveto_sm_min.npy")
sm_max=2*3000*np.load("../SM_Construction/mll_14TeV_noveto_sm_max.npy")


k1lo_050050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy")
k1lo_025025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy")
k1lo_025050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy")
k1lo_050025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy")
k1lo_050100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy")
k1lo_100050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy")
k1lo_100100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy")


k12lo_050050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy")
k12lo_025025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy")
k12lo_025050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy")
k12lo_050025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy")
k12lo_050100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy")
k12lo_100050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy")
k12lo_100100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy")


k4lo_050050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy")
k4lo_025025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy")
k4lo_025050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy")
k4lo_050025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy")
k4lo_050100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy")
k4lo_100050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy")
k4lo_100100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy")


k42lo_050050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy")
k42lo_025025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy")
k42lo_025050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy")
k42lo_050025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy")
k42lo_050100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy")
k42lo_100050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy")
k42lo_100100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy")


k12k42lo_050050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1O4int_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy")
k12k42lo_025025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1O4int_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy")
k12k42lo_025050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1O4int_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy")
k12k42lo_050025=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1O4int_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy")
k12k42lo_050100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1O4int_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy")
k12k42lo_100050=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1O4int_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy")
k12k42lo_100100=2*3000*np.load("../Data/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1O4int_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy")

k12k42intlo_050050=k12k42lo_050050 - k12lo_050050 - k42lo_050050
k12k42intlo_025025=k12k42lo_025025 - k12lo_025025 - k42lo_025025
k12k42intlo_025050=k12k42lo_025050 - k12lo_025050 - k42lo_025050
k12k42intlo_050025=k12k42lo_050025 - k12lo_050025 - k42lo_050025
k12k42intlo_050100=k12k42lo_050100 - k12lo_050100 - k42lo_050100
k12k42intlo_100050=k12k42lo_100050 - k12lo_100050 - k42lo_100050
k12k42intlo_100100=k12k42lo_100100 - k12lo_100100 - k42lo_100100


print(k12k42lo_050050)


print(k12k42intlo_050050)


def _construct_new_prediction_k1k4(k1, k4):
    bsm_050050=nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_MWWover2+((k1)*k1lo_050050 + (k1**2)*k12lo_050050 + (k4)*k4lo_050050 + (k4**2)*k42lo_050050 + (k1*k4)*k12k42intlo_050050)
    bsm_025025=nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_MWWover4+((k1)*k1lo_025025 + (k1**2)*k12lo_025025 + (k4)*k4lo_025025 + (k4**2)*k42lo_025025 + (k1*k4)*k12k42intlo_025025)
    bsm_025050=nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_MWWover2+((k1)*k1lo_025050 + (k1**2)*k12lo_025050 + (k4)*k4lo_025050 + (k4**2)*k42lo_025050 + (k1*k4)*k12k42intlo_025050)
    bsm_050025=nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_MWWover4+((k1)*k1lo_050025 + (k1**2)*k12lo_050025 + (k4)*k4lo_050025 + (k4**2)*k42lo_050025 + (k1*k4)*k12k42intlo_050025)
    bsm_050100=nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_MWW+((k1)*k1lo_050100 + (k1**2)*k12lo_050100 + (k4)*k4lo_050100 + (k4**2)*k42lo_050100 + (k1*k4)*k12k42intlo_050100)
    bsm_100050=nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_MWWover2+((k1)*k1lo_100050 + (k1**2)*k12lo_100050 + (k4)*k4lo_100050 + (k4**2)*k42lo_100050 + (k1*k4)*k12k42intlo_100050)
    bsm_100100=nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_MWW+((k1)*k1lo_100100 + (k1**2)*k12lo_100100 + (k4)*k4lo_100100 + (k4**2)*k42lo_100100 + (k1*k4)*k12k42intlo_100100)

    
    bsm_ggphoton_lo_min=[]
    bsm_ggphoton_lo_max=[]

    for i in range(0, len(bsm_050050)):
        values=[bsm_050050[i], bsm_025025[i], bsm_025050[i], bsm_050025[i], bsm_050100[i], bsm_100050[i], bsm_100100[i]]
        bsm_ggphoton_lo_min.append(np.min(values))
        bsm_ggphoton_lo_max.append(np.max(values))

    bsm_ggphoton_lo_min=np.array(bsm_ggphoton_lo_min)
    bsm_ggphoton_lo_max=np.array(bsm_ggphoton_lo_max)

    return [bsm_050050, bsm_ggphoton_lo_min, bsm_ggphoton_lo_max]


def fac_to_max_bin(factor_vals):
    """
    This function takes in a set of factors and returns which bin is the maximum bin that can be\
    constrained with this factor.
    """
    #By assuming c=1 convert the factors to Lambda values
    mass_vals=fac2lam(factor_vals)
    #This vector gives minimum value of Lambda for each of the bins. E.g bin1 200-214GeV can only \
    # be used if Lambda is bigger than 750GeV.
    max_mass_scales=np.array([0.7504646, 0.88671293, 1.03336473, 1.18834644, 1.35280008, 1.5310028, 1.73055257, 1.95808899, 2.21780199, 2.51666561, 2.86161449, 3.25420555, 3.70412162, 4.21201279, 4.78111762, 5.40612933])
    
    #Loop breaks when the mass scale is smaller than required for a bin giving the counter as the\
    #  maximum bin for each factor
    which_bin=[]
    for i in range(0, len(mass_vals)):
        counter=0
        for j in range(0, len(max_mass_scales)):
            if abs(mass_vals[i])>max_mass_scales[j]:
                counter+=1
            else:
                break
        which_bin.append(counter)
    return which_bin



#k1_vals=np.linspace(-5, 5, 600)
#k4_vals=np.linspace(-5, 5, 600)
k1_vals=np.linspace(-0.66, 0.66, 2000)
k4_vals=np.linspace(-0.66, 0.66, 2000)
def round_to_5(x):
    rounded=[]
    for i in range(len(x)):
        rounded.append(np.round(x[i], 6-int(floor(log10(abs(x[i]))))))
    return np.array(rounded)
bins=round_to_5(np.logspace(np.log10(200), np.log10(4000), 17))
bin_centres=(bins[0:16] + bins[1:17])/2
systematic_error=sm*((4.863706128 + bin_centres*0.019542609)/100)

#Include a contour_name for plots

points_x, points_y, deltachisqs_all=produce_contours_ATLAS("fo_syst", k1_vals, k4_vals, sm, _construct_new_prediction_k1k4, lam2fac, lam2fac, fac2lam, fac2lam, fac_to_max_bin, fac_to_max_bin, systematic_error=systematic_error)

np.save("points_x_k1_fo_syst", np.array(points_x))
np.save("points_y_k4_fo_syst", np.array(points_y))
np.save("deltachisqs_all_fo_syst", np.array(deltachisqs_all))


#k1_vals=np.linspace(-1, 1, 600)
#k4_vals=np.linspace(-1, 1, 600)
k1_vals=np.linspace(-0.125, 0.125, 2000)
k4_vals=np.linspace(-0.125, 0.125, 2000)

points_x, points_y, deltachisqs_all=produce_contours_ATLAS("fo_nosyst", k1_vals, k4_vals, sm, _construct_new_prediction_k1k4, lam2fac, lam2fac, fac2lam, fac2lam, fac_to_max_bin, fac_to_max_bin)


np.save("points_x_k1_fo_nosyst", np.array(points_x))
np.save("points_y_k4_fo_nosyst", np.array(points_y))
np.save("deltachisqs_all_fo_nosyst", np.array(deltachisqs_all))


