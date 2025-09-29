import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from scipy.optimize import minimize, basinhopping, shgo
import sys
sys.path.insert(1, '..')

from factor_conversions import kg2lam, kgtilde2lam, lam2kg, lam2kgtilde
from withdata_find_chisq_vals import _chisq, produce_contours_ATLAS


nnllnnlonloew_ggphoton_centre=36.1*2*np.load("../SM_Construction/mll_13TeV_veto35_sm_centre.npy")
nnllnnlonloew_ggphoton_min=36.1*2*np.load("../SM_Construction/mll_13TeV_veto35_sm_min.npy")
nnllnnlonloew_ggphoton_max=36.1*2*np.load("../SM_Construction/mll_13TeV_veto35_sm_max.npy")


nnllnnlonloew_centre=36.1*2*np.load("../QCD_EW_Combination/mll_13TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_centre.npy")
nnllnnlonloew_min=36.1*2*np.load("../QCD_EW_Combination/mll_13TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_min.npy")
nnllnnlonloew_max=36.1*2*np.load("../QCD_EW_Combination/mll_13TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_max.npy")

err_qq=(nnllnnlonloew_max-nnllnnlonloew_min)/2


atlas=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas.npy")
atlas_err= 36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas_err.npy")


mcfm_nll_gg=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_centre.npy")
mcfm_nll_gg_min=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_min.npy")
mcfm_nll_gg_max=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_max.npy")
ggnll_050050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_050050025=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
ggnll_050050100=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
ggnll_025025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
ggnll_025050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_050025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
ggnll_050100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
ggnll_100050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_100100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")

mcfm_nll_kg=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_centre.npy")
mcfm_nll_kg_min=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_min.npy")
mcfm_nll_kg_max=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_max.npy")
kgnll_050050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kgnll_050050025=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
kgnll_050050100=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
kgnll_025025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
kgnll_025050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kgnll_050025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
kgnll_050100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
kgnll_100050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kgnll_100100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")


mcfm_nll_kg2=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_centre.npy")
mcfm_nll_kg2_min=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_min.npy")
mcfm_nll_kg2_max=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_max.npy")
kg2nll_050050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kg2nll_050050025=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
kg2nll_050050100=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
kg2nll_025025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
kg2nll_025050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kg2nll_050025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
kg2nll_050100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
kg2nll_100050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
kg2nll_100100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")


nlophoton_1=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gamgam_nlo_mufac=0.5MWW.npy")
nlophoton_05=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gamgam_nlo_mufac=0.25MWW.npy")
nlophoton_2=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gamgam_nlo_mufac=1.0MWW.npy")



def _construct_new_prediction_kgktodd(kg, kgtilde):

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
    #Take the factor and calculate the relevant mass scale (assuming c=1 and factor is given as kappa)
    mass_vals=kg2lam(factor_vals)
    which_bin=[]
    for i in range(0, len(mass_vals)):
        #The counter increases for every bin until a bin is encoutered which requires a higher mass scale than the factor represents.
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

"""
kg_vals=np.linspace(-14.5, 14.5, 2000)
kgtilde_vals=np.linspace(-9, 9, 2000)

#max_mass_scales=np.array([0.24916766, 0.39471923, 0.58307685, 0.68704951, 0.80229188, 0.91625714, 1.01531984, 1.15766201, 1.37241666, 1.65417734, 2.061306, 2.68549442, 3.99486759])
max_mass_scales=np.load("../min_Lambda_for_each_bin/lambda_min_empirical_13TeV_veto35_025.npy")
print(max_mass_scales)
points_x, points_y, deltachisqs_all=produce_contours_ATLAS("atlas_kg_025", kg_vals, kgtilde_vals, atlas, atlas_err, _construct_new_prediction_kgktodd, lam2kg, lam2kgtilde, kg2lam, kgtilde2lam, kg_to_max_bin, kgtilde_to_max_bin, max_mass_scales, min_bin=3)

np.save("points_x_kg_025", np.array(points_x))
np.save("points_y_kg_025", np.array(points_y))
np.save("deltachisqs_all_025", np.array(deltachisqs_all))

kg_vals=np.linspace(-10, 10, 2000)
kgtilde_vals=np.linspace(-7, 7, 2000)

#max_mass_scales=np.array([0.20952419, 0.33191798, 0.49030723, 0.57773747, 0.67464437, 0.77047734, 0.85377881, 0.97347384, 1.15406025, 1.39099179, 1.73334483, 2.25822263, 3.35926983])
max_mass_scales=np.load("../min_Lambda_for_each_bin/lambda_min_empirical_13TeV_veto35.npy")
print(max_mass_scales)
points_x, points_y, deltachisqs_all=produce_contours_ATLAS("atlas_kg_05", kg_vals, kgtilde_vals, atlas, atlas_err, _construct_new_prediction_kgktodd, lam2kg, lam2kgtilde, kg2lam, kgtilde2lam, kg_to_max_bin, kgtilde_to_max_bin, max_mass_scales, min_bin=3)

np.save("points_x_kg_05", np.array(points_x))
np.save("points_y_kg_05", np.array(points_y))
np.save("deltachisqs_all_05", np.array(deltachisqs_all))

kg_vals=np.linspace(-9, 9, 2000)
kgtilde_vals=np.linspace(-6, 6, 2000)


max_mass_scales=np.load("../min_Lambda_for_each_bin/lambda_min_empirical_13TeV_veto35_1.npy")
#max_mass_scales=np.array([0.17618814, 0.27910864, 0.41229759, 0.48581737, 0.56730603, 0.64789163, 0.71793954, 0.81859066, 0.97044513, 1.16968001, 1.45756345, 1.89893132, 2.82479796])
print(max_mass_scales)

points_x, points_y, deltachisqs_all=produce_contours_ATLAS("atlas_kg_1", kg_vals, kgtilde_vals, atlas, atlas_err, _construct_new_prediction_kgktodd, lam2kg, lam2kgtilde, kg2lam, kgtilde2lam, kg_to_max_bin, kgtilde_to_max_bin, max_mass_scales, min_bin=3)

np.save("points_x_kg_1", np.array(points_x))
np.save("points_y_kg_1", np.array(points_y))
np.save("deltachisqs_all_1", np.array(deltachisqs_all))

kg_vals=np.linspace(-7, 7, 2000)
kgtilde_vals=np.linspace(-5, 5, 2000)

bins = np.array([55, 75, 85, 95, 110, 125, 140, 160, 185, 220, 280, 380, 600, 1500])
bin_centres=(bins[0:len(bins)-1] + bins[1:])/2
print(bin_centres/1000)
print(2*bin_centres/1000)
max_mass_scales=2*bin_centres/1000

points_x, points_y, deltachisqs_all=produce_contours_ATLAS("atlas_kg_mww", kg_vals, kgtilde_vals, atlas, atlas_err, _construct_new_prediction_kgktodd, lam2kg, lam2kgtilde, kg2lam, kgtilde2lam, kg_to_max_bin, kgtilde_to_max_bin, max_mass_scales, min_bin=3)

np.save("points_x_kg_mww", np.array(points_x))
np.save("points_y_kg_mww", np.array(points_y))
np.save("deltachisqs_all_mww", np.array(deltachisqs_all))
"""
kg_vals=np.linspace(-7, 7, 2000)
kgtilde_vals=np.linspace(-5, 5, 2000)

bins = np.array([55, 75, 85, 95, 110, 125, 140, 160, 185, 220, 280, 380, 600, 1500])
bin_centres=(bins[0:len(bins)-1] + bins[1:])/2
print(bin_centres/1000)
print(2*bin_centres/1000)
max_mass_scales=4*bin_centres/1000

points_x, points_y, deltachisqs_all=produce_contours_ATLAS("atlas_kg_mww4", kg_vals, kgtilde_vals, atlas, atlas_err, _construct_new_prediction_kgktodd, lam2kg, lam2kgtilde, kg2lam, kgtilde2lam, kg_to_max_bin, kgtilde_to_max_bin, max_mass_scales, min_bin=3)

np.save("points_x_kg_mww4", np.array(points_x))
np.save("points_y_kg_mww4", np.array(points_y))
np.save("deltachisqs_all_mww4", np.array(deltachisqs_all))

