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


def kg_to_max_bin(factor_vals):
    #Take the factor and calculate the relevant mass scale (assuming c=1 and factor is given as kappa)
    mass_vals=kg2lam(factor_vals)
    #Minimum mass scales required to use each bin given in TeV. e.g. 55-75GeV bin requires mass scale of 124GeV (0.12458383TeV) or higher.
    max_mass_scales=np.array([0.12458383, 0.19735961, 0.29153842, 0.34352475, 0.40114594, 0.45812857, 0.50765992, 0.57883101, 0.68620833, 0.82708867, 1.030653, 1.34274721, 1.99743379])
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

def kgtilde_to_max_bin(factor_vals):
    mass_vals=kgtilde2lam(factor_vals)
    max_mass_scales=np.array([0.12458383, 0.19735961, 0.29153842, 0.34352475, 0.40114594, 0.45812857, 0.50765992, 0.57883101, 0.68620833, 0.82708867, 1.030653, 1.34274721, 1.99743379])
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


kg_vals=np.linspace(-10, 10, 2000)
kgtilde_vals=np.linspace(-10, 10, 2000)



points_x, points_y, deltachisqs_all=produce_contours_ATLAS("atlas_kg", kg_vals, kgtilde_vals, atlas, atlas_err, _construct_new_prediction_kgktodd, lam2kg, lam2kgtilde, kg2lam, kgtilde2lam, kg_to_max_bin, kgtilde_to_max_bin, min_bin=3)

np.save("points_x_kg", np.array(points_x))
np.save("points_y_kg", np.array(points_y))
np.save("deltachisqs_all", np.array(deltachisqs_all))

