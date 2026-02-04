import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from scipy.optimize import minimize, basinhopping, shgo
from math import log10, floor
import sys
sys.path.insert(1, '..')

from factor_conversions import kg2lam, kgtilde2lam, lam2kg, lam2kgtilde
from withpseudodata_find_chisq_vals import _chisq, produce_contours_ATLAS

kg2nll_centre=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_centre.npy")
kg2nll_min=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_min.npy")
kg2nll_max=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_max.npy")
kg2nll_050050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=0.50MWW.npy")
kg2nll_050050025=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=0.25MWW.npy")
kg2nll_050050100=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=1.00MWW.npy")
kg2nll_025025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.50MWW.npy")
kg2nll_025050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.25MWW_mufac=0.50MWW__muresum=0.50MWW.npy")
kg2nll_050025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.50MWW_mufac=0.25MWW__muresum=0.50MWW.npy")
kg2nll_050100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.50MWW_mufac=1.00MWW__muresum=0.50MWW.npy")
kg2nll_100050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=1.00MWW_mufac=0.50MWW__muresum=0.50MWW.npy")
kg2nll_100100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=1.00MWW_mufac=1.00MWW__muresum=0.50MWW.npy")




kgnll_centre=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_centre.npy")
kgnll_min=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_min.npy")
kgnll_max=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_max.npy")
kgnll_050050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=0.50MWW.npy")
kgnll_050050025=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=0.25MWW.npy")
kgnll_050050100=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=1.00MWW.npy")
kgnll_025025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.50MWW.npy")
kgnll_025050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.25MWW_mufac=0.50MWW__muresum=0.50MWW.npy")
kgnll_050025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.50MWW_mufac=0.25MWW__muresum=0.50MWW.npy")
kgnll_050100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.50MWW_mufac=1.00MWW__muresum=0.50MWW.npy")
kgnll_100050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=1.00MWW_mufac=0.50MWW__muresum=0.50MWW.npy")
kgnll_100100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=1.00MWW_mufac=1.00MWW__muresum=0.50MWW.npy")


ggnll_centre=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_centre.npy")
ggnll_min=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_min.npy")
ggnll_max=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_max.npy")

ggnll_050050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=0.50MWW.npy")
ggnll_050050025=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=0.25MWW.npy")
ggnll_050050100=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=1.00MWW.npy")
ggnll_025025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.50MWW.npy")
ggnll_025050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.50MWW__muresum=0.50MWW.npy")
ggnll_050025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.50MWW_mufac=0.25MWW__muresum=0.50MWW.npy")
ggnll_050100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.50MWW_mufac=1.00MWW__muresum=0.50MWW.npy")
ggnll_100050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.00MWW_mufac=0.50MWW__muresum=0.50MWW.npy")
ggnll_100100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.00MWW_mufac=1.00MWW__muresum=0.50MWW.npy")


nlophoton_1=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=0.50MWW.npy")
nlophoton_05=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=0.25MWW.npy")
nlophoton_2=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=1.00MWW.npy")




sm=2*3000*np.load("../SM_Construction/mll_14TeV_veto35_sm_centre.npy")
sm_min=2*3000*np.load("../SM_Construction/mll_14TeV_veto35_sm_min.npy")
sm_max=2*3000*np.load("../SM_Construction/mll_14TeV_veto35_sm_max.npy")

print(sm/6000)
print(sm_max/6000)
print(sm_min/6000)

nnllnnlonloew_centre=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_centre.npy")
nnllnnlonloew_min=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_min.npy")
nnllnnlonloew_max=2*3000*np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_max.npy")

err_qq=(nnllnnlonloew_max-nnllnnlonloew_min)/2



def _construct_new_prediction_kgktodd(kg, kgtilde):

    #convert kappa g values into factors relative to Lambda = 2TeV
    factor_kg=(4*kg*0.113)/(12*np.pi*0.24622**2)
    factor_kgtilde=(4*kgtilde*0.113)/(8*np.pi*0.24622**2)

    bsm_ggphoton_nll_050050050=ggnll_050050050+nlophoton_1+((factor_kgtilde**2 + factor_kg**2)*kg2nll_050050050 + (factor_kg)*kgnll_050050050 )
    bsm_ggphoton_nll_050050025=ggnll_050050025+nlophoton_1+((factor_kgtilde**2 + factor_kg**2)*kg2nll_050050025 + (factor_kg)*kgnll_050050025)
    bsm_ggphoton_nll_050050100=ggnll_050050100+nlophoton_1+((factor_kgtilde**2 + factor_kg**2)*kg2nll_050050100 + (factor_kg)*kgnll_050050100)
    bsm_ggphoton_nll_025025050=ggnll_025025050+nlophoton_05+((factor_kgtilde**2 + factor_kg**2)*kg2nll_025025050 + (factor_kg)*kgnll_025025050)
    bsm_ggphoton_nll_025050050=ggnll_025050050+nlophoton_1+((factor_kgtilde**2 + factor_kg**2)*kg2nll_025050050 + (factor_kg)*kgnll_025050050)
    bsm_ggphoton_nll_050025050=ggnll_050025050+nlophoton_05+((factor_kgtilde**2 + factor_kg**2)*kg2nll_050025050 + (factor_kg)*kgnll_050025050)
    bsm_ggphoton_nll_050100050=ggnll_050100050+nlophoton_2+((factor_kgtilde**2 + factor_kg**2)*kg2nll_050100050 + (factor_kg)*kgnll_050100050)
    bsm_ggphoton_nll_100050050=ggnll_100050050+nlophoton_1+((factor_kgtilde**2 + factor_kg**2)*kg2nll_100050050 + (factor_kg)*kgnll_100050050)
    bsm_ggphoton_nll_100100050=ggnll_100100050+nlophoton_2+((factor_kgtilde**2 + factor_kg**2)*kg2nll_100100050 + (factor_kg)*kgnll_100100050)

    
    bsm_ggphoton_nll_min=[]
    bsm_ggphoton_nll_max=[]

    for i in range(0, len(bsm_ggphoton_nll_050050050)):
        values=[bsm_ggphoton_nll_050050050[i], bsm_ggphoton_nll_050050025[i], bsm_ggphoton_nll_050050100[i], bsm_ggphoton_nll_025025050[i], bsm_ggphoton_nll_025050050[i], bsm_ggphoton_nll_050025050[i], bsm_ggphoton_nll_050100050[i], bsm_ggphoton_nll_100050050[i], bsm_ggphoton_nll_100100050[i]]
        bsm_ggphoton_nll_min.append(np.min(values))
        bsm_ggphoton_nll_max.append(np.max(values))

    bsm_ggphoton_nll_min=np.array(bsm_ggphoton_nll_min)
    bsm_ggphoton_nll_max=np.array(bsm_ggphoton_nll_max)

    bsm_ggphoton_nll_err=(bsm_ggphoton_nll_max-bsm_ggphoton_nll_min)/2

    bsm_err_sm=(err_qq**2 + bsm_ggphoton_nll_err**2)**0.5
    
    bsm_nnllnnlonloew_ggphoton_centre=nnllnnlonloew_centre+bsm_ggphoton_nll_050050050
    bsm_nnllnnlonloew_ggphoton_min=bsm_nnllnnlonloew_ggphoton_centre-bsm_err_sm
    bsm_nnllnnlonloew_ggphoton_max=bsm_nnllnnlonloew_ggphoton_centre+bsm_err_sm

    return [bsm_nnllnnlonloew_ggphoton_centre, bsm_nnllnnlonloew_ggphoton_min, bsm_nnllnnlonloew_ggphoton_max]


def kg_to_max_bin(factor_vals, max_mass_scales):
    """
    This function takes in a set of factors and returns which bin is the maximum bin that can be\
    constrained with this factor.
    """
    #By assuming c=1 convert the factors to Lambda values
    mass_vals=kg2lam(factor_vals)
    print(max_mass_scales)

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

def kgtilde_to_max_bin(factor_vals, max_mass_scales):
    mass_vals=kgtilde2lam(factor_vals)
    print(max_mass_scales)
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



kg_vals=np.linspace(-6, 6, 2000)
kgtilde_vals=np.linspace(-6, 6, 2000)
def round_to_5(x):
    rounded=[]
    for i in range(len(x)):
        rounded.append(np.round(x[i], 6-int(floor(log10(abs(x[i]))))))
    return np.array(rounded)

bins=round_to_5(np.logspace(2.1384012462059836, np.log10(4000), 19))
bin_centres=(bins[0:len(bins)-1] + bins[1:])/2


systematic_error=sm*((4.863706128 + bin_centres*0.019542609)/100)

#This vector gives minimum value of Lambda for each of the bins. E.g bin1 200-214GeV can only \
# be used if Lambda is bigger than 1260GeV.

max_mass_scales=np.load("../min_Lambda_for_each_bin/lambda_min_empirical_14TeV_veto35.npy")
print(max_mass_scales)
points_x, points_y, deltachisqs_all=produce_contours_ATLAS("syst", kg_vals, kgtilde_vals, sm, _construct_new_prediction_kgktodd, lam2kg, lam2kgtilde, kg2lam, kgtilde2lam, kg_to_max_bin, kgtilde_to_max_bin, max_mass_scales, systematic_error=systematic_error)

np.save("points_x_kg_syst", np.array(points_x))
np.save("points_y_kg_syst", np.array(points_y))
np.save("deltachisqs_all_syst", np.array(deltachisqs_all))



kg_vals=np.linspace(-2, 2, 2000)
kgtilde_vals=np.linspace(-2, 2, 2000)

points_x, points_y, deltachisqs_all=produce_contours_ATLAS("nosyst", kg_vals, kgtilde_vals, sm, _construct_new_prediction_kgktodd, lam2kg, lam2kgtilde, kg2lam, kgtilde2lam, kg_to_max_bin, kgtilde_to_max_bin, max_mass_scales)


np.save("points_x_kg_nosyst", np.array(points_x))
np.save("points_y_kg_nosyst", np.array(points_y))
np.save("deltachisqs_all_nosyst", np.array(deltachisqs_all))


