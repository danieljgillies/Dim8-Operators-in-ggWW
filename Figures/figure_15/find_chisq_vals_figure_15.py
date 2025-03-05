import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from scipy.optimize import minimize, basinhopping, shgo
import sys
sys.path.insert(1, '..')

from factor_conversions import fac2lam, lam2fac
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

mcfm_nll_k2=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_centre.npy")
mcfm_nll_k2_min=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_min.npy")
mcfm_nll_k2_max=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_max.npy")
k2nll_050050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k2nll_050050025=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k2nll_050050100=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k2nll_025025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k2nll_025050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k2nll_050025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k2nll_050100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k2nll_100050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k2nll_100100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")


mcfm_nll_k22=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_centre.npy")
mcfm_nll_k22_min=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_min.npy")
mcfm_nll_k22_max=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_max.npy")
k22nll_050050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22nll_050050025=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k22nll_050050100=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k22nll_025025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k22nll_025050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22nll_050025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k22nll_050100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k22nll_100050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22nll_100100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")


mcfm_nll_k3=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_centre.npy")
mcfm_nll_k3_min=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_min.npy")
mcfm_nll_k3_max=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_max.npy")
k3nll_050050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k3nll_050050025=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k3nll_050050100=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k3nll_025025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k3nll_025050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k3nll_050025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k3nll_050100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k3nll_100050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k3nll_100100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")


mcfm_nll_k32=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_centre.npy")
mcfm_nll_k32_min=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_min.npy")
mcfm_nll_k32_max=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_max.npy")
k32nll_050050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k32nll_050050025=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k32nll_050050100=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k32nll_025025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k32nll_025050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k32nll_050025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k32nll_050100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k32nll_100050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k32nll_100100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")



mcfm_nll_k22k32=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_centre.npy")
mcfm_nll_k22k32_min=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_min.npy")
mcfm_nll_k22k32_max=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_max.npy")
k22k32nll_050050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22k32nll_050050025=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k22k32nll_050050100=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k22k32nll_025025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k22k32nll_025050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22k32nll_050025050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k22k32nll_050100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k22k32nll_100050050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22k32nll_100100050=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")

k22k32intnll_050050050=k22k32nll_050050050 - k22nll_050050050 - k32nll_050050050
k22k32intnll_050050025=k22k32nll_050050025 - k22nll_050050025 - k32nll_050050025
k22k32intnll_050050100=k22k32nll_050050100 - k22nll_050050100 - k32nll_050050100
k22k32intnll_025025050=k22k32nll_025025050 - k22nll_025025050 - k32nll_025025050
k22k32intnll_025050050=k22k32nll_025050050 - k22nll_025050050 - k32nll_025050050
k22k32intnll_050025050=k22k32nll_050025050 - k22nll_050025050 - k32nll_050025050
k22k32intnll_050100050=k22k32nll_050100050 - k22nll_050100050 - k32nll_050100050
k22k32intnll_100050050=k22k32nll_100050050 - k22nll_100050050 - k32nll_100050050
k22k32intnll_100100050=k22k32nll_100100050 - k22nll_100100050 - k32nll_100100050

def array_for_plot(a):
    return np.concatenate((np.array([a[0]]), a, np.array([a[len(a)-1]])))

plt.figure()
bins15 = [0, 55, 75, 85, 95, 110, 125, 140, 160, 185, 220, 280, 380, 600, 1500]
plt.step(bins15, array_for_plot(k22k32nll_050050050), where="post")
plt.step(bins15, array_for_plot(k22nll_050050050 + k32nll_050050050), where="post")
plt.step(bins15, array_for_plot(k22nll_050050050 + k32nll_050050050 - k22k32intnll_050050050), where="post")
plt.loglog()
plt.savefig("interference.pdf")

nlophoton_1=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gamgam_nlo_mufac=0.5MWW.npy")
nlophoton_05=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gamgam_nlo_mufac=0.25MWW.npy")
nlophoton_2=36.1*2*np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_sm_gamgam_nlo_mufac=1.0MWW.npy")


def _construct_new_prediction_k2k3(k2, k3):
    bsm_ggphoton_nll_050050050=ggnll_050050050+nlophoton_1+((k2)*k2nll_050050050 + (k2**2)*k22nll_050050050 + (k3)*k3nll_050050050 + (k3**2)*k32nll_050050050 + (k2*k3)*k22k32intnll_050050050)
    bsm_ggphoton_nll_050050025=ggnll_050050025+nlophoton_1+((k2)*k2nll_050050025 + (k2**2)*k22nll_050050025 + (k3)*k3nll_050050025 + (k3**2)*k32nll_050050025 + (k2*k3)*k22k32intnll_050050025)
    bsm_ggphoton_nll_050050100=ggnll_050050100+nlophoton_1+((k2)*k2nll_050050100 + (k2**2)*k22nll_050050100 + (k3)*k3nll_050050100 + (k3**2)*k32nll_050050100 + (k2*k3)*k22k32intnll_050050100)
    bsm_ggphoton_nll_025025050=ggnll_025025050+nlophoton_05+((k2)*k2nll_025025050 + (k2**2)*k22nll_025025050 + (k3)*k3nll_025025050 + (k3**2)*k32nll_025025050 + (k2*k3)*k22k32intnll_025025050)
    bsm_ggphoton_nll_025050050=ggnll_025050050+nlophoton_1+((k2)*k2nll_025050050 + (k2**2)*k22nll_025050050 + (k3)*k3nll_025050050 + (k3**2)*k32nll_025050050 + (k2*k3)*k22k32intnll_025050050)
    bsm_ggphoton_nll_050025050=ggnll_050025050+nlophoton_05+((k2)*k2nll_050025050 + (k2**2)*k22nll_050025050 + (k3)*k3nll_050025050 + (k3**2)*k32nll_050025050 + (k2*k3)*k22k32intnll_050025050)
    bsm_ggphoton_nll_050100050=ggnll_050100050+nlophoton_2+((k2)*k2nll_050100050 + (k2**2)*k22nll_050100050 + (k3)*k3nll_050100050 + (k3**2)*k32nll_050100050 + (k2*k3)*k22k32intnll_050100050)
    bsm_ggphoton_nll_100050050=ggnll_100050050+nlophoton_1+((k2)*k2nll_100050050 + (k2**2)*k22nll_100050050 + (k3)*k3nll_100050050 + (k3**2)*k32nll_100050050 + (k2*k3)*k22k32intnll_100050050)
    bsm_ggphoton_nll_100100050=ggnll_100100050+nlophoton_2+((k2)*k2nll_100100050 + (k2**2)*k22nll_100100050 + (k3)*k3nll_100100050 + (k3**2)*k32nll_100100050 + (k2*k3)*k22k32intnll_100100050)

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



def fac_to_max_bin(factor_vals, max_mass_scales):
    #Take the factor and calculate the relevant mass scale (assuming c=1 and factor is given as kappa)
    mass_vals=fac2lam(factor_vals)
    print(max_mass_scales)
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

#This vector gives minimum value of Lambda for each of the bins. E.g bin 185-220GeV can only \
# be used if Lambda is bigger than 1150GeV.

max_mass_scales=np.load("../min_Lambda_for_each_bin/lambda_min_empirical_13TeV_veto35.npy")


k2_vals=np.linspace(-25, 25, 2000)
k3_vals=np.linspace(-25, 25, 2000)


points_x, points_y, deltachisqs_all=produce_contours_ATLAS("atlas_o2o3", k2_vals, k3_vals, atlas, atlas_err, _construct_new_prediction_k2k3, lam2fac, lam2fac, fac2lam, fac2lam, fac_to_max_bin, fac_to_max_bin, max_mass_scales, min_bin=3)

np.save("points_x_k2", np.array(points_x))
np.save("points_y_k3", np.array(points_y))
np.save("deltachisqs_all", np.array(deltachisqs_all))

