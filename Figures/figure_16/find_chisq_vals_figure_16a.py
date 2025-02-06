import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from scipy.optimize import minimize, basinhopping, shgo
from math import log10, floor
import sys
sys.path.insert(1, '..')

from factor_conversions import fac2lam,lam2fac
from withpseudodata_find_chisq_vals import _chisq, produce_contours_ATLAS

k22nll_centre=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_centre.npy")
k22nll_min=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_min.npy")
k22nll_max=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_max.npy")
k22nll_050050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22nll_050050025=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k22nll_050050100=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k22nll_025025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k22nll_025050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22nll_050025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k22nll_050100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k22nll_100050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22nll_100100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")




k2nll_centre=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_centre.npy")
k2nll_min=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_min.npy")
k2nll_max=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_max.npy")
k2nll_050050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k2nll_050050025=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k2nll_050050100=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k2nll_025025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k2nll_025050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k2nll_050025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k2nll_050100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k2nll_100050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k2nll_100100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")


k32nll_centre=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_centre.npy")
k32nll_min=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_min.npy")
k32nll_max=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_max.npy")
k32nll_050050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k32nll_050050025=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k32nll_050050100=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k32nll_025025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k32nll_025050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k32nll_050025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k32nll_050100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k32nll_100050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k32nll_100100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")




k3nll_centre=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_centre.npy")
k3nll_min=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_min.npy")
k3nll_max=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_max.npy")
k3nll_050050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k3nll_050050025=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k3nll_050050100=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k3nll_025025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k3nll_025050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k3nll_050025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k3nll_050100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k3nll_100050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k3nll_100100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")




k22k32nll_centre=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_centre.npy")
k22k32nll_min=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_min.npy")
k22k32nll_max=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_max.npy")
k22k32nll_050050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22k32nll_050050025=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
k22k32nll_050050100=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
k22k32nll_025025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k22k32nll_025050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22k32nll_050025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
k22k32nll_050100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
k22k32nll_100050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
k22k32nll_100100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2O3int_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")



k22k32intnll_050050050=k22k32nll_050050050 - k22nll_050050050 - k32nll_050050050
k22k32intnll_050050025=k22k32nll_050050025 - k22nll_050050025 - k32nll_050050025
k22k32intnll_050050100=k22k32nll_050050100 - k22nll_050050100 - k32nll_050050100
k22k32intnll_025025050=k22k32nll_025025050 - k22nll_025025050 - k32nll_025025050
k22k32intnll_025050050=k22k32nll_025050050 - k22nll_025050050 - k32nll_025050050
k22k32intnll_050025050=k22k32nll_050025050 - k22nll_050025050 - k32nll_050025050
k22k32intnll_050100050=k22k32nll_050100050 - k22nll_050100050 - k32nll_050100050
k22k32intnll_100050050=k22k32nll_100050050 - k22nll_100050050 - k32nll_100050050
k22k32intnll_100100050=k22k32nll_100100050 - k22nll_100100050 - k32nll_100100050



ggnll_centre=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_centre.npy")
ggnll_min=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_min.npy")
ggnll_max=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_max.npy")

ggnll_050050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_050050025=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy")
ggnll_050050100=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy")
ggnll_025025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
ggnll_025050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_050025050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy")
ggnll_050100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy")
ggnll_100050050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy")
ggnll_100100050=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy")


nlophoton_1=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=0.5MWW.npy")
nlophoton_05=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=0.25MWW.npy")
nlophoton_2=2*3000*np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_mufac=1.0MWW.npy")




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




k2_vals=np.linspace(-3, 3, 2000)
k3_vals=np.linspace(-3, 3, 2000)
def round_to_5(x):
    rounded=[]
    for i in range(len(x)):
        rounded.append(np.round(x[i], 6-int(floor(log10(abs(x[i]))))))
    return np.array(rounded)
bins=round_to_5(np.logspace(np.log10(200), np.log10(4000), 17))
bin_centres=(bins[0:16] + bins[1:17])/2
systematic_error=sm*((4.863706128 + bin_centres*0.019542609)/100)



points_x, points_y, deltachisqs_all=produce_contours_ATLAS(k2_vals, k3_vals, sm, _construct_new_prediction_k2k3, lam2fac, lam2fac, fac_to_max_bin, fac_to_max_bin, systematic_error=systematic_error)

np.save("points_x_k2_resum_syst", np.array(points_x))
np.save("points_y_k3_resum_syst", np.array(points_y))
np.save("deltachisqs_all_syst", np.array(deltachisqs_all))



k2_vals=np.linspace(-1.5, 1.5, 2000)
k3_vals=np.linspace(-1.5, 1.5, 2000)

points_x, points_y, deltachisqs_all=produce_contours_ATLAS(k2_vals, k3_vals, sm, _construct_new_prediction_k2k3, lam2fac, lam2fac, fac_to_max_bin, fac_to_max_bin)


np.save("points_x_k2_resum_nosyst", np.array(points_x))
np.save("points_y_k3_resum_nosyst", np.array(points_y))
np.save("deltachisqs_all_nosyst", np.array(deltachisqs_all))


