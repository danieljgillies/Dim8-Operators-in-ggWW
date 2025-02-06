import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys
sys.path.insert(1, '..')

from plot_funcs import round_to_5, array_for_plot

bins=round_to_5(np.logspace(np.log10(200), np.log10(4000), 17))
print(bins)
bin_widths=bins[1:17]-bins[0:16]
bin_widths18=np.array([41.1817, 41.1817, 49.6614, 59.8871, 72.2183, 87.0887, 105.021, 126.6458, 152.7232, 184.1698, 222.093, 267.823, 322.97, 389.473, 469.668, 566.377, 682.999, 682.999])

kg2nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_centre.npy"))
kg2nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_min.npy"))
kg2nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_max.npy"))
kg2nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
kg2nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
kg2nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
kg2nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
kg2nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
kg2nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
kg2nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
kg2nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
kg2nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))

print(kg2nll_centre/(bin_widths18*6000))

k1nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_centre.npy"))
k1nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_min.npy"))
k1nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_max.npy"))
k1nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k1nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k1nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k1nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k1nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k1nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k1nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k1nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k1nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))


k2nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_centre.npy"))
k2nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_min.npy"))
k2nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_max.npy"))
k2nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k2nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k2nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k2nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k2nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k2nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k2nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k2nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k2nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))


k3nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_centre.npy"))
k3nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_min.npy"))
k3nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_max.npy"))
k3nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k3nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k3nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k3nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k3nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k3nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k3nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k3nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k3nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))


k4nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_centre.npy"))
k4nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_min.npy"))
k4nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_max.npy"))
k4nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k4nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k4nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k4nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k4nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k4nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k4nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k4nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k4nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))


k5nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_centre.npy"))
k5nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_min.npy"))
k5nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_max.npy"))
k5nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k5nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k5nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k5nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k5nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k5nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k5nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k5nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k5nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k6nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_centre.npy"))
k6nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_min.npy"))
k6nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_max.npy"))
k6nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k6nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k6nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k6nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k6nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k6nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k6nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k6nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k6nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k12nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_centre.npy"))
k12nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_min.npy"))
k12nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_max.npy"))
k12nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k12nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k12nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k12nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k12nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k12nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k12nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k12nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k12nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k22nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_centre.npy"))
k22nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_min.npy"))
k22nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_max.npy"))
k22nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k22nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k22nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k22nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k22nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k22nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k22nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k22nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k22nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k32nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_centre.npy"))
k32nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_min.npy"))
k32nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_max.npy"))
k32nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k32nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k32nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k32nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k32nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k32nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k32nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k32nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k32nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k42nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_centre.npy"))
k42nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_min.npy"))
k42nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_max.npy"))
k42nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k42nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k42nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k42nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k42nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k42nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k42nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k42nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k42nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k52nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_centre.npy"))
k52nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_min.npy"))
k52nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_max.npy"))
k52nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k52nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k52nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k52nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k52nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k52nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k52nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k52nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k52nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k62nll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_centre.npy"))
k62nll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_min.npy"))
k62nll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_max.npy"))
k62nll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k62nll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k62nll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k62nll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k62nll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k62nll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k62nll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k62nll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k62nll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))




kg2lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_OGHsq_lo_qcd_centre.npy"))
kg2lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_OGHsq_lo_qcd_min.npy"))
kg2lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_OGHsq_lo_qcd_max.npy"))
kg2lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_OGHsq_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
kg2lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_OGHsq_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
kg2lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_OGHsq_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
kg2lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_OGHsq_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
kg2lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_OGHsq_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
kg2lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_OGHsq_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
kg2lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_OGHsq_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

k1lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_centre.npy"))
k1lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_min.npy"))
k1lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_max.npy"))
k1lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k1lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k1lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k1lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k1lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k1lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k1lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1SMint_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

k2lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2SMint_lo_qcd_centre.npy"))
k2lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2SMint_lo_qcd_min.npy"))
k2lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2SMint_lo_qcd_max.npy"))
k2lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2SMint_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k2lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2SMint_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k2lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2SMint_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k2lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2SMint_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k2lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2SMint_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k2lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2SMint_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k2lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2SMint_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

k3lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3SMint_lo_qcd_centre.npy"))
k3lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3SMint_lo_qcd_min.npy"))
k3lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3SMint_lo_qcd_max.npy"))
k3lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3SMint_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k3lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3SMint_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k3lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3SMint_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k3lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3SMint_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k3lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3SMint_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k3lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3SMint_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k3lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3SMint_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

k4lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_centre.npy"))
k4lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_min.npy"))
k4lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_max.npy"))
k4lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k4lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k4lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k4lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k4lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k4lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k4lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4SMint_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

k5lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5SMint_lo_qcd_centre.npy"))
k5lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5SMint_lo_qcd_min.npy"))
k5lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5SMint_lo_qcd_max.npy"))
k5lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5SMint_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k5lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5SMint_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k5lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5SMint_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k5lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5SMint_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k5lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5SMint_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k5lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5SMint_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k5lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5SMint_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

k6lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6SMint_lo_qcd_centre.npy"))
k6lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6SMint_lo_qcd_min.npy"))
k6lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6SMint_lo_qcd_max.npy"))
k6lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6SMint_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k6lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6SMint_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k6lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6SMint_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k6lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6SMint_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k6lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6SMint_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k6lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6SMint_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k6lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6SMint_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

k12lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_centre.npy"))
k12lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_min.npy"))
k12lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_max.npy"))
k12lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k12lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k12lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k12lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k12lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k12lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k12lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O1sq_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

k22lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2sq_lo_qcd_centre.npy"))
k22lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2sq_lo_qcd_min.npy"))
k22lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2sq_lo_qcd_max.npy"))
k22lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2sq_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k22lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2sq_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k22lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2sq_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k22lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2sq_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k22lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2sq_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k22lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2sq_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k22lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O2sq_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

k32lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3sq_lo_qcd_centre.npy"))
k32lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3sq_lo_qcd_min.npy"))
k32lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3sq_lo_qcd_max.npy"))
k32lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3sq_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k32lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3sq_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k32lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3sq_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k32lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3sq_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k32lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3sq_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k32lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3sq_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k32lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3sq_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

k42lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_centre.npy"))
k42lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_min.npy"))
k42lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_max.npy"))
k42lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k42lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k42lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k42lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k42lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k42lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k42lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O4sq_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

k52lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5sq_lo_qcd_centre.npy"))
k52lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5sq_lo_qcd_min.npy"))
k52lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5sq_lo_qcd_max.npy"))
k52lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5sq_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k52lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5sq_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k52lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5sq_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k52lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5sq_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k52lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5sq_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k52lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5sq_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k52lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O5sq_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))


k62lo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6sq_lo_qcd_centre.npy"))
k62lo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6sq_lo_qcd_min.npy"))
k62lo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6sq_lo_qcd_max.npy"))
k62lo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6sq_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
k62lo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6sq_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
k62lo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6sq_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
k62lo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6sq_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
k62lo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6sq_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
k62lo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6sq_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
k62lo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O6sq_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))



print(kg2lo_centre/(bin_widths18*6000))



mass_scale=6#TeV






ratio_o1_lo_050050=k1lo_050050/k12lo_050050
ratio_o1_lo_025025=k1lo_025025/k12lo_025025
ratio_o1_lo_025050=k1lo_025050/k12lo_025050
ratio_o1_lo_050025=k1lo_050025/k12lo_050025
ratio_o1_lo_050100=k1lo_050100/k12lo_050100
ratio_o1_lo_100050=k1lo_100050/k12lo_100050
ratio_o1_lo_100100=k1lo_100100/k12lo_100100

ratio_o1_lo_min=[]
ratio_o1_lo_max=[]

for i in range(0, len(ratio_o1_lo_050050)):
    values=[ratio_o1_lo_050050[i], ratio_o1_lo_025025[i], ratio_o1_lo_025050[i], ratio_o1_lo_050025[i], ratio_o1_lo_050100[i], ratio_o1_lo_100050[i], ratio_o1_lo_100100[i]]
    ratio_o1_lo_min.append(np.min(values))
    ratio_o1_lo_max.append(np.max(values))

ratio_o1_lo_min=np.array(ratio_o1_lo_min)
ratio_o1_lo_max=np.array(ratio_o1_lo_max)


ratio_kgo1_lo_050050=kg2lo_050050/k12lo_050050
ratio_kgo1_lo_025025=kg2lo_025025/k12lo_025025
ratio_kgo1_lo_025050=kg2lo_025050/k12lo_025050
ratio_kgo1_lo_050025=kg2lo_050025/k12lo_050025
ratio_kgo1_lo_050100=kg2lo_050100/k12lo_050100
ratio_kgo1_lo_100050=kg2lo_100050/k12lo_100050
ratio_kgo1_lo_100100=kg2lo_100100/k12lo_100100

ratio_kgo1_lo_min=[]
ratio_kgo1_lo_max=[]

for i in range(0, len(ratio_kgo1_lo_050050)):
    values=[ratio_kgo1_lo_050050[i], ratio_kgo1_lo_025025[i], ratio_kgo1_lo_025050[i], ratio_kgo1_lo_050025[i], ratio_kgo1_lo_050100[i], ratio_kgo1_lo_100050[i], ratio_kgo1_lo_100100[i]]
    ratio_kgo1_lo_min.append(np.min(values))
    ratio_kgo1_lo_max.append(np.max(values))

ratio_kgo1_lo_min=np.array(ratio_kgo1_lo_min)
ratio_kgo1_lo_max=np.array(ratio_kgo1_lo_max)


ratio_o1_nll_050050050=k1nll_050050050/k12nll_050050050
ratio_o1_nll_050050025=k1nll_050050025/k12nll_050050025
ratio_o1_nll_050050100=k1nll_050050100/k12nll_050050100
ratio_o1_nll_025025050=k1nll_025025050/k12nll_025025050
ratio_o1_nll_025050050=k1nll_025050050/k12nll_025050050
ratio_o1_nll_050025050=k1nll_050025050/k12nll_050025050
ratio_o1_nll_050100050=k1nll_050100050/k12nll_050100050
ratio_o1_nll_100050050=k1nll_100050050/k12nll_100050050
ratio_o1_nll_100100050=k1nll_100100050/k12nll_100100050

ratio_o1_nll_min=[]
ratio_o1_nll_max=[]

for i in range(0, len(ratio_o1_nll_050050050)):
    values=[ratio_o1_nll_050050050[i], ratio_o1_nll_050050025[i], ratio_o1_nll_050050100[i], ratio_o1_nll_025025050[i], ratio_o1_nll_025050050[i], ratio_o1_nll_050025050[i], ratio_o1_nll_050100050[i], ratio_o1_nll_100050050[i], ratio_o1_nll_100100050[i]]
    ratio_o1_nll_min.append(np.min(values))
    ratio_o1_nll_max.append(np.max(values))

ratio_o1_nll_min=np.array(ratio_o1_nll_min)
ratio_o1_nll_max=np.array(ratio_o1_nll_max)


ratio_kgo1_nll_050050050=kg2nll_050050050/k12nll_050050050
ratio_kgo1_nll_050050025=kg2nll_050050025/k12nll_050050025
ratio_kgo1_nll_050050100=kg2nll_050050100/k12nll_050050100
ratio_kgo1_nll_025025050=kg2nll_025025050/k12nll_025025050
ratio_kgo1_nll_025050050=kg2nll_025050050/k12nll_025050050
ratio_kgo1_nll_050025050=kg2nll_050025050/k12nll_050025050
ratio_kgo1_nll_050100050=kg2nll_050100050/k12nll_050100050
ratio_kgo1_nll_100050050=kg2nll_100050050/k12nll_100050050
ratio_kgo1_nll_100100050=kg2nll_100100050/k12nll_100100050

ratio_kgo1_nll_min=[]
ratio_kgo1_nll_max=[]

for i in range(0, len(ratio_kgo1_nll_050050050)):
    values=[ratio_kgo1_nll_050050050[i], ratio_kgo1_nll_050050025[i], ratio_kgo1_nll_050050100[i], ratio_kgo1_nll_025025050[i], ratio_kgo1_nll_025050050[i], ratio_kgo1_nll_050025050[i], ratio_kgo1_nll_050100050[i], ratio_kgo1_nll_100050050[i], ratio_kgo1_nll_100100050[i]]
    ratio_kgo1_nll_min.append(np.min(values))
    ratio_kgo1_nll_max.append(np.max(values))

ratio_kgo1_nll_min=np.array(ratio_kgo1_nll_min)
ratio_kgo1_nll_max=np.array(ratio_kgo1_nll_max)


plt.rcParams["hatch.linewidth"] = 4

plt.figure(figsize=(20, 12),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"$\Lambda = 2TeV",\
#               fontsize=18,color="black")
rec1 = plt.Rectangle((500,10**-11),3500,0.5, facecolor="#d3d3d3", 
                     edgecolor="white", hatch=r"\\", zorder=0)
axs[0].add_patch(rec1)

#axs[0].margins(0.3)
#axs[0].autoscale()


axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")

axs[1].set_ylabel("Ratio to LO \n(No Jet Veto)\n",\
               fontsize=14,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()

bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].annotate(r'$\Lambda=2$TeV', (1800, 0.05),\
               fontsize=18,color="#3b3b3b")
axs[0].annotate(r'NLL $p_{T, veto} = 35$GeV', (1200, 2*10**-11),\
               fontsize=14,color="#3b3b3b")
#axs[0].annotate(r'EFT Breakdown', (510, 10**-7),\
#               fontsize=14,color="#3b3b3b")




axs[0].step(bin_centres, kg2nll_centre/(bin_widths18*3000), color='k', where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, kg2nll_min/(bin_widths18*3000), kg2nll_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k1nll_centre)/(bin_widths18*3000), color='b', where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_1)|$', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k1nll_min)/(bin_widths18*3000), abs(k1nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k12nll_centre/(bin_widths18*3000), color='r', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_1|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, k12nll_min/(bin_widths18*3000), k12nll_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''
axs[0].step(bin_centres, kg2lo_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \,$ LO (No Veto)', linewidth=0.9)


axs[0].fill_between(bin_centres, kg2lo_min/(bin_widths18*3000), kg2lo_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k1lo_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_1)|$ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k1lo_min)/(bin_widths18*3000), abs(k1lo_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k12lo_centre/(bin_widths18*3000), color='r', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_1|^2\ \ \ \ \ \ \ \ \ \ \ \, \ \ \ $ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, k12lo_min/(bin_widths18*3000), k12lo_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''


#axs[0].plot([500, 500], [0, 2], color="grey", linestyle="--")#, label=r'$M_{e\mu}^{\mathrm{Max}} = \frac{\Lambda}{4}$')
axs[0].legend(loc="lower left", fontsize=11, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(10**-11, 0.5)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True, pad=10)


ratio_kg2o1=kg2nll_centre/kg2lo_centre
ratio_k1o1=k1nll_centre/k1lo_centre
ratio_k12o1=k12nll_centre/k12lo_centre

axs[1].semilogx()

axs[1].step(bin_centres, abs(ratio_kg2o1), color='k', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k1o1), color='b', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k12o1), color='r', where='mid', linewidth=1)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
axs[1].minorticks_on()
axs[1].set_ylim(0, 1)
#axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
#               fontsize=16,color="black")

#axs[1].set_ylim(1*10**-4, 10**4)
#axs[1].set_yticks([10**-4, 1, 10**4])
#plt.tight_layout(pad=-0.1)
plt.savefig("figure_7a.pdf", bbox_inches='tight')















ratio_o2_lo_050050=k2lo_050050/k22lo_050050
ratio_o2_lo_025025=k2lo_025025/k22lo_025025
ratio_o2_lo_025050=k2lo_025050/k22lo_025050
ratio_o2_lo_050025=k2lo_050025/k22lo_050025
ratio_o2_lo_050100=k2lo_050100/k22lo_050100
ratio_o2_lo_100050=k2lo_100050/k22lo_100050
ratio_o2_lo_100100=k2lo_100100/k22lo_100100

ratio_o2_lo_min=[]
ratio_o2_lo_max=[]

for i in range(0, len(ratio_o2_lo_050050)):
    values=[ratio_o2_lo_050050[i], ratio_o2_lo_025025[i], ratio_o2_lo_025050[i], ratio_o2_lo_050025[i], ratio_o2_lo_050100[i], ratio_o2_lo_100050[i], ratio_o2_lo_100100[i]]
    ratio_o2_lo_min.append(np.min(values))
    ratio_o2_lo_max.append(np.max(values))

ratio_o2_lo_min=np.array(ratio_o2_lo_min)
ratio_o2_lo_max=np.array(ratio_o2_lo_max)


ratio_kgo2_lo_050050=kg2lo_050050/k22lo_050050
ratio_kgo2_lo_025025=kg2lo_025025/k22lo_025025
ratio_kgo2_lo_025050=kg2lo_025050/k22lo_025050
ratio_kgo2_lo_050025=kg2lo_050025/k22lo_050025
ratio_kgo2_lo_050100=kg2lo_050100/k22lo_050100
ratio_kgo2_lo_100050=kg2lo_100050/k22lo_100050
ratio_kgo2_lo_100100=kg2lo_100100/k22lo_100100

ratio_kgo2_lo_min=[]
ratio_kgo2_lo_max=[]

for i in range(0, len(ratio_kgo2_lo_050050)):
    values=[ratio_kgo2_lo_050050[i], ratio_kgo2_lo_025025[i], ratio_kgo2_lo_025050[i], ratio_kgo2_lo_050025[i], ratio_kgo2_lo_050100[i], ratio_kgo2_lo_100050[i], ratio_kgo2_lo_100100[i]]
    ratio_kgo2_lo_min.append(np.min(values))
    ratio_kgo2_lo_max.append(np.max(values))

ratio_kgo2_lo_min=np.array(ratio_kgo2_lo_min)
ratio_kgo2_lo_max=np.array(ratio_kgo2_lo_max)


ratio_o2_nll_050050050=k2nll_050050050/k22nll_050050050
ratio_o2_nll_050050025=k2nll_050050025/k22nll_050050025
ratio_o2_nll_050050100=k2nll_050050100/k22nll_050050100
ratio_o2_nll_025025050=k2nll_025025050/k22nll_025025050
ratio_o2_nll_025050050=k2nll_025050050/k22nll_025050050
ratio_o2_nll_050025050=k2nll_050025050/k22nll_050025050
ratio_o2_nll_050100050=k2nll_050100050/k22nll_050100050
ratio_o2_nll_100050050=k2nll_100050050/k22nll_100050050
ratio_o2_nll_100100050=k2nll_100100050/k22nll_100100050

ratio_o2_nll_min=[]
ratio_o2_nll_max=[]

for i in range(0, len(ratio_o2_nll_050050050)):
    values=[ratio_o2_nll_050050050[i], ratio_o2_nll_050050025[i], ratio_o2_nll_050050100[i], ratio_o2_nll_025025050[i], ratio_o2_nll_025050050[i], ratio_o2_nll_050025050[i], ratio_o2_nll_050100050[i], ratio_o2_nll_100050050[i], ratio_o2_nll_100100050[i]]
    ratio_o2_nll_min.append(np.min(values))
    ratio_o2_nll_max.append(np.max(values))

ratio_o2_nll_min=np.array(ratio_o2_nll_min)
ratio_o2_nll_max=np.array(ratio_o2_nll_max)


ratio_kgo2_nll_050050050=kg2nll_050050050/k22nll_050050050
ratio_kgo2_nll_050050025=kg2nll_050050025/k22nll_050050025
ratio_kgo2_nll_050050100=kg2nll_050050100/k22nll_050050100
ratio_kgo2_nll_025025050=kg2nll_025025050/k22nll_025025050
ratio_kgo2_nll_025050050=kg2nll_025050050/k22nll_025050050
ratio_kgo2_nll_050025050=kg2nll_050025050/k22nll_050025050
ratio_kgo2_nll_050100050=kg2nll_050100050/k22nll_050100050
ratio_kgo2_nll_100050050=kg2nll_100050050/k22nll_100050050
ratio_kgo2_nll_100100050=kg2nll_100100050/k22nll_100100050

ratio_kgo2_nll_min=[]
ratio_kgo2_nll_max=[]

for i in range(0, len(ratio_kgo2_nll_050050050)):
    values=[ratio_kgo2_nll_050050050[i], ratio_kgo2_nll_050050025[i], ratio_kgo2_nll_050050100[i], ratio_kgo2_nll_025025050[i], ratio_kgo2_nll_025050050[i], ratio_kgo2_nll_050025050[i], ratio_kgo2_nll_050100050[i], ratio_kgo2_nll_100050050[i], ratio_kgo2_nll_100100050[i]]
    ratio_kgo2_nll_min.append(np.min(values))
    ratio_kgo2_nll_max.append(np.max(values))

ratio_kgo2_nll_min=np.array(ratio_kgo2_nll_min)
ratio_kgo2_nll_max=np.array(ratio_kgo2_nll_max)


plt.rcParams["hatch.linewidth"] = 4

plt.figure(figsize=(20, 12),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"$\Lambda = 2TeV",\
#               fontsize=18,color="black")
rec1 = plt.Rectangle((500,10**-11),3500,0.5, facecolor="#d3d3d3", 
                     edgecolor="white", hatch=r"\\", zorder=0)
axs[0].add_patch(rec1)

#axs[0].margins(0.3)
#axs[0].autoscale()


axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")

axs[1].set_ylabel("Ratio to LO \n(No Jet Veto)\n",\
               fontsize=14,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()

bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].annotate(r'$\Lambda=2$TeV', (1800, 0.05),\
               fontsize=18,color="#3b3b3b")
axs[0].annotate(r'NLL $p_{T, veto} = 35$GeV', (1200, 2*10**-11),\
               fontsize=14,color="#3b3b3b")


#axs[0].annotate(r'EFT Breakdown', (510, 10**-7),\
#               fontsize=14,color="#3b3b3b")




axs[0].step(bin_centres, kg2nll_centre/(bin_widths18*3000), color='k', where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, kg2nll_min/(bin_widths18*3000), kg2nll_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k2nll_centre)/(bin_widths18*3000), color='b', where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_2)|$', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k2nll_min)/(bin_widths18*3000), abs(k2nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k22nll_centre/(bin_widths18*3000), color='r', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_2|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, k22nll_min/(bin_widths18*3000), k22nll_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''
axs[0].step(bin_centres, kg2lo_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \,$ LO (No Veto)', linewidth=0.9)


axs[0].fill_between(bin_centres, kg2lo_min/(bin_widths18*3000), kg2lo_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k2lo_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_2)|$ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k2lo_min)/(bin_widths18*3000), abs(k2lo_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k22lo_centre/(bin_widths18*3000), color='r', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_2|^2\ \ \ \ \ \ \ \ \ \ \ \, \ \ \ $ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, k22lo_min/(bin_widths18*3000), k22lo_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''


#axs[0].plot([500, 500], [0, 2], color="grey", linestyle="--")#, label=r'$M_{e\mu}^{\mathrm{Max}} = \frac{\Lambda}{4}$')
axs[0].legend(loc="lower left", fontsize=11, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(10**-11, 0.5)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True, pad=10)


ratio_kg2o2=kg2nll_centre/kg2lo_centre
ratio_k2o2=k2nll_centre/k2lo_centre
ratio_k22o2=k22nll_centre/k22lo_centre

axs[1].semilogx()

axs[1].step(bin_centres, abs(ratio_kg2o2), color='k', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k2o2), color='b', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k22o2), color='r', where='mid', linewidth=1)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
axs[1].minorticks_on()
axs[1].set_ylim(0, 1)
#axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
#               fontsize=16,color="black")

#axs[1].set_ylim(1*10**-4, 10**4)
#axs[1].set_yticks([10**-4, 1, 10**4])
#plt.tight_layout(pad=-0.1)
plt.savefig("figure_7b.pdf", bbox_inches='tight')















ratio_o3_lo_050050=k3lo_050050/k32lo_050050
ratio_o3_lo_025025=k3lo_025025/k32lo_025025
ratio_o3_lo_025050=k3lo_025050/k32lo_025050
ratio_o3_lo_050025=k3lo_050025/k32lo_050025
ratio_o3_lo_050100=k3lo_050100/k32lo_050100
ratio_o3_lo_100050=k3lo_100050/k32lo_100050
ratio_o3_lo_100100=k3lo_100100/k32lo_100100

ratio_o3_lo_min=[]
ratio_o3_lo_max=[]

for i in range(0, len(ratio_o3_lo_050050)):
    values=[ratio_o3_lo_050050[i], ratio_o3_lo_025025[i], ratio_o3_lo_025050[i], ratio_o3_lo_050025[i], ratio_o3_lo_050100[i], ratio_o3_lo_100050[i], ratio_o3_lo_100100[i]]
    ratio_o3_lo_min.append(np.min(values))
    ratio_o3_lo_max.append(np.max(values))

ratio_o3_lo_min=np.array(ratio_o3_lo_min)
ratio_o3_lo_max=np.array(ratio_o3_lo_max)


ratio_kgo3_lo_050050=kg2lo_050050/k32lo_050050
ratio_kgo3_lo_025025=kg2lo_025025/k32lo_025025
ratio_kgo3_lo_025050=kg2lo_025050/k32lo_025050
ratio_kgo3_lo_050025=kg2lo_050025/k32lo_050025
ratio_kgo3_lo_050100=kg2lo_050100/k32lo_050100
ratio_kgo3_lo_100050=kg2lo_100050/k32lo_100050
ratio_kgo3_lo_100100=kg2lo_100100/k32lo_100100

ratio_kgo3_lo_min=[]
ratio_kgo3_lo_max=[]

for i in range(0, len(ratio_kgo3_lo_050050)):
    values=[ratio_kgo3_lo_050050[i], ratio_kgo3_lo_025025[i], ratio_kgo3_lo_025050[i], ratio_kgo3_lo_050025[i], ratio_kgo3_lo_050100[i], ratio_kgo3_lo_100050[i], ratio_kgo3_lo_100100[i]]
    ratio_kgo3_lo_min.append(np.min(values))
    ratio_kgo3_lo_max.append(np.max(values))

ratio_kgo3_lo_min=np.array(ratio_kgo3_lo_min)
ratio_kgo3_lo_max=np.array(ratio_kgo3_lo_max)


ratio_o3_nll_050050050=k3nll_050050050/k32nll_050050050
ratio_o3_nll_050050025=k3nll_050050025/k32nll_050050025
ratio_o3_nll_050050100=k3nll_050050100/k32nll_050050100
ratio_o3_nll_025025050=k3nll_025025050/k32nll_025025050
ratio_o3_nll_025050050=k3nll_025050050/k32nll_025050050
ratio_o3_nll_050025050=k3nll_050025050/k32nll_050025050
ratio_o3_nll_050100050=k3nll_050100050/k32nll_050100050
ratio_o3_nll_100050050=k3nll_100050050/k32nll_100050050
ratio_o3_nll_100100050=k3nll_100100050/k32nll_100100050

ratio_o3_nll_min=[]
ratio_o3_nll_max=[]

for i in range(0, len(ratio_o3_nll_050050050)):
    values=[ratio_o3_nll_050050050[i], ratio_o3_nll_050050025[i], ratio_o3_nll_050050100[i], ratio_o3_nll_025025050[i], ratio_o3_nll_025050050[i], ratio_o3_nll_050025050[i], ratio_o3_nll_050100050[i], ratio_o3_nll_100050050[i], ratio_o3_nll_100100050[i]]
    ratio_o3_nll_min.append(np.min(values))
    ratio_o3_nll_max.append(np.max(values))

ratio_o3_nll_min=np.array(ratio_o3_nll_min)
ratio_o3_nll_max=np.array(ratio_o3_nll_max)


ratio_kgo3_nll_050050050=kg2nll_050050050/k32nll_050050050
ratio_kgo3_nll_050050025=kg2nll_050050025/k32nll_050050025
ratio_kgo3_nll_050050100=kg2nll_050050100/k32nll_050050100
ratio_kgo3_nll_025025050=kg2nll_025025050/k32nll_025025050
ratio_kgo3_nll_025050050=kg2nll_025050050/k32nll_025050050
ratio_kgo3_nll_050025050=kg2nll_050025050/k32nll_050025050
ratio_kgo3_nll_050100050=kg2nll_050100050/k32nll_050100050
ratio_kgo3_nll_100050050=kg2nll_100050050/k32nll_100050050
ratio_kgo3_nll_100100050=kg2nll_100100050/k32nll_100100050

ratio_kgo3_nll_min=[]
ratio_kgo3_nll_max=[]

for i in range(0, len(ratio_kgo3_nll_050050050)):
    values=[ratio_kgo3_nll_050050050[i], ratio_kgo3_nll_050050025[i], ratio_kgo3_nll_050050100[i], ratio_kgo3_nll_025025050[i], ratio_kgo3_nll_025050050[i], ratio_kgo3_nll_050025050[i], ratio_kgo3_nll_050100050[i], ratio_kgo3_nll_100050050[i], ratio_kgo3_nll_100100050[i]]
    ratio_kgo3_nll_min.append(np.min(values))
    ratio_kgo3_nll_max.append(np.max(values))

ratio_kgo3_nll_min=np.array(ratio_kgo3_nll_min)
ratio_kgo3_nll_max=np.array(ratio_kgo3_nll_max)


plt.rcParams["hatch.linewidth"] = 4

plt.figure(figsize=(20, 12),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"$\Lambda = 2TeV",\
#               fontsize=18,color="black")
rec1 = plt.Rectangle((500,10**-11),3500,0.5, facecolor="#d3d3d3", 
                     edgecolor="white", hatch=r"\\", zorder=0)
axs[0].add_patch(rec1)

#axs[0].margins(0.3)
#axs[0].autoscale()


axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")

axs[1].set_ylabel("Ratio to LO \n(No Jet Veto)\n",\
               fontsize=14,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()

bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].annotate(r'$\Lambda=2$TeV', (1800, 0.05),\
               fontsize=18,color="#3b3b3b")
axs[0].annotate(r'NLL $p_{T, veto} = 35$GeV', (1200, 2*10**-11),\
               fontsize=14,color="#3b3b3b")
#axs[0].annotate(r'EFT Breakdown', (510, 10**-7),\
#               fontsize=14,color="#3b3b3b")




axs[0].step(bin_centres, kg2nll_centre/(bin_widths18*3000), color='k', where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, kg2nll_min/(bin_widths18*3000), kg2nll_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k3nll_centre)/(bin_widths18*3000), color='b', where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_3)|$', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k3nll_min)/(bin_widths18*3000), abs(k3nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k32nll_centre/(bin_widths18*3000), color='r', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_3|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, k32nll_min/(bin_widths18*3000), k32nll_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''
axs[0].step(bin_centres, kg2lo_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \,$ LO (No Veto)', linewidth=0.9)


axs[0].fill_between(bin_centres, kg2lo_min/(bin_widths18*3000), kg2lo_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k3lo_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_3)|$ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k3lo_min)/(bin_widths18*3000), abs(k3lo_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k32lo_centre/(bin_widths18*3000), color='r', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_3|^2\ \ \ \ \ \ \ \ \ \ \ \, \ \ \ $ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, k32lo_min/(bin_widths18*3000), k32lo_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''


#axs[0].plot([500, 500], [0, 2], color="grey", linestyle="--")#, label=r'$M_{e\mu}^{\mathrm{Max}} = \frac{\Lambda}{4}$')
axs[0].legend(loc="lower left", fontsize=11, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(10**-11, 0.5)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True, pad=10)


ratio_kg2o3=kg2nll_centre/kg2lo_centre
ratio_k3o3=k3nll_centre/k3lo_centre
ratio_k32o3=k32nll_centre/k32lo_centre

axs[1].semilogx()

axs[1].step(bin_centres, abs(ratio_kg2o3), color='k', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k3o3), color='b', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k32o3), color='r', where='mid', linewidth=1)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
axs[1].minorticks_on()
axs[1].set_ylim(0, 1)
#axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
#               fontsize=16,color="black")

#axs[1].set_ylim(1*10**-4, 10**4)
#axs[1].set_yticks([10**-4, 1, 10**4])
#plt.tight_layout(pad=-0.1)
plt.savefig("figure_7c.pdf", bbox_inches='tight')















ratio_o4_lo_050050=k4lo_050050/k42lo_050050
ratio_o4_lo_025025=k4lo_025025/k42lo_025025
ratio_o4_lo_025050=k4lo_025050/k42lo_025050
ratio_o4_lo_050025=k4lo_050025/k42lo_050025
ratio_o4_lo_050100=k4lo_050100/k42lo_050100
ratio_o4_lo_100050=k4lo_100050/k42lo_100050
ratio_o4_lo_100100=k4lo_100100/k42lo_100100

ratio_o4_lo_min=[]
ratio_o4_lo_max=[]

for i in range(0, len(ratio_o4_lo_050050)):
    values=[ratio_o4_lo_050050[i], ratio_o4_lo_025025[i], ratio_o4_lo_025050[i], ratio_o4_lo_050025[i], ratio_o4_lo_050100[i], ratio_o4_lo_100050[i], ratio_o4_lo_100100[i]]
    ratio_o4_lo_min.append(np.min(values))
    ratio_o4_lo_max.append(np.max(values))

ratio_o4_lo_min=np.array(ratio_o4_lo_min)
ratio_o4_lo_max=np.array(ratio_o4_lo_max)


ratio_kgo4_lo_050050=kg2lo_050050/k42lo_050050
ratio_kgo4_lo_025025=kg2lo_025025/k42lo_025025
ratio_kgo4_lo_025050=kg2lo_025050/k42lo_025050
ratio_kgo4_lo_050025=kg2lo_050025/k42lo_050025
ratio_kgo4_lo_050100=kg2lo_050100/k42lo_050100
ratio_kgo4_lo_100050=kg2lo_100050/k42lo_100050
ratio_kgo4_lo_100100=kg2lo_100100/k42lo_100100

ratio_kgo4_lo_min=[]
ratio_kgo4_lo_max=[]

for i in range(0, len(ratio_kgo4_lo_050050)):
    values=[ratio_kgo4_lo_050050[i], ratio_kgo4_lo_025025[i], ratio_kgo4_lo_025050[i], ratio_kgo4_lo_050025[i], ratio_kgo4_lo_050100[i], ratio_kgo4_lo_100050[i], ratio_kgo4_lo_100100[i]]
    ratio_kgo4_lo_min.append(np.min(values))
    ratio_kgo4_lo_max.append(np.max(values))

ratio_kgo4_lo_min=np.array(ratio_kgo4_lo_min)
ratio_kgo4_lo_max=np.array(ratio_kgo4_lo_max)


ratio_o4_nll_050050050=k4nll_050050050/k42nll_050050050
ratio_o4_nll_050050025=k4nll_050050025/k42nll_050050025
ratio_o4_nll_050050100=k4nll_050050100/k42nll_050050100
ratio_o4_nll_025025050=k4nll_025025050/k42nll_025025050
ratio_o4_nll_025050050=k4nll_025050050/k42nll_025050050
ratio_o4_nll_050025050=k4nll_050025050/k42nll_050025050
ratio_o4_nll_050100050=k4nll_050100050/k42nll_050100050
ratio_o4_nll_100050050=k4nll_100050050/k42nll_100050050
ratio_o4_nll_100100050=k4nll_100100050/k42nll_100100050

ratio_o4_nll_min=[]
ratio_o4_nll_max=[]

for i in range(0, len(ratio_o4_nll_050050050)):
    values=[ratio_o4_nll_050050050[i], ratio_o4_nll_050050025[i], ratio_o4_nll_050050100[i], ratio_o4_nll_025025050[i], ratio_o4_nll_025050050[i], ratio_o4_nll_050025050[i], ratio_o4_nll_050100050[i], ratio_o4_nll_100050050[i], ratio_o4_nll_100100050[i]]
    ratio_o4_nll_min.append(np.min(values))
    ratio_o4_nll_max.append(np.max(values))

ratio_o4_nll_min=np.array(ratio_o4_nll_min)
ratio_o4_nll_max=np.array(ratio_o4_nll_max)


ratio_kgo4_nll_050050050=kg2nll_050050050/k42nll_050050050
ratio_kgo4_nll_050050025=kg2nll_050050025/k42nll_050050025
ratio_kgo4_nll_050050100=kg2nll_050050100/k42nll_050050100
ratio_kgo4_nll_025025050=kg2nll_025025050/k42nll_025025050
ratio_kgo4_nll_025050050=kg2nll_025050050/k42nll_025050050
ratio_kgo4_nll_050025050=kg2nll_050025050/k42nll_050025050
ratio_kgo4_nll_050100050=kg2nll_050100050/k42nll_050100050
ratio_kgo4_nll_100050050=kg2nll_100050050/k42nll_100050050
ratio_kgo4_nll_100100050=kg2nll_100100050/k42nll_100100050

ratio_kgo4_nll_min=[]
ratio_kgo4_nll_max=[]

for i in range(0, len(ratio_kgo4_nll_050050050)):
    values=[ratio_kgo4_nll_050050050[i], ratio_kgo4_nll_050050025[i], ratio_kgo4_nll_050050100[i], ratio_kgo4_nll_025025050[i], ratio_kgo4_nll_025050050[i], ratio_kgo4_nll_050025050[i], ratio_kgo4_nll_050100050[i], ratio_kgo4_nll_100050050[i], ratio_kgo4_nll_100100050[i]]
    ratio_kgo4_nll_min.append(np.min(values))
    ratio_kgo4_nll_max.append(np.max(values))

ratio_kgo4_nll_min=np.array(ratio_kgo4_nll_min)
ratio_kgo4_nll_max=np.array(ratio_kgo4_nll_max)


plt.rcParams["hatch.linewidth"] = 4

plt.figure(figsize=(20, 12),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"$\Lambda = 2TeV",\
#               fontsize=18,color="black")
rec1 = plt.Rectangle((500,10**-11),3500,0.5, facecolor="#d3d3d3", 
                     edgecolor="white", hatch=r"\\", zorder=0)
axs[0].add_patch(rec1)

#axs[0].margins(0.3)
#axs[0].autoscale()


axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")

axs[1].set_ylabel("Ratio to LO \n(No Jet Veto)\n",\
               fontsize=14,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()

bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].annotate(r'$\Lambda=2$TeV', (1800, 0.05),\
               fontsize=18,color="#3b3b3b")
axs[0].annotate(r'NLL $p_{T, veto} = 35$GeV', (1200, 2*10**-11),\
               fontsize=14,color="#3b3b3b")
#axs[0].annotate(r'EFT Breakdown', (510, 10**-7),\
#               fontsize=14,color="#3b3b3b")




axs[0].step(bin_centres, kg2nll_centre/(bin_widths18*3000), color='k', where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, kg2nll_min/(bin_widths18*3000), kg2nll_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k4nll_centre)/(bin_widths18*3000), color='b', where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_4)|$', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k4nll_min)/(bin_widths18*3000), abs(k4nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k42nll_centre/(bin_widths18*3000), color='r', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_4|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, k42nll_min/(bin_widths18*3000), k42nll_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''
axs[0].step(bin_centres, kg2lo_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \,$ LO (No Veto)', linewidth=0.9)


axs[0].fill_between(bin_centres, kg2lo_min/(bin_widths18*3000), kg2lo_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k4lo_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_4)|$ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k4lo_min)/(bin_widths18*3000), abs(k4lo_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k42lo_centre/(bin_widths18*3000), color='r', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_4|^2\ \ \ \ \ \ \ \ \ \ \ \, \ \ \ $ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, k42lo_min/(bin_widths18*3000), k42lo_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''


#axs[0].plot([500, 500], [0, 2], color="grey", linestyle="--")#, label=r'$M_{e\mu}^{\mathrm{Max}} = \frac{\Lambda}{4}$')
axs[0].legend(loc="lower left", fontsize=11, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(10**-11, 0.5)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True, pad=10)


ratio_kg2o4=kg2nll_centre/kg2lo_centre
ratio_k4o4=k4nll_centre/k4lo_centre
ratio_k42o4=k42nll_centre/k42lo_centre

axs[1].semilogx()

axs[1].step(bin_centres, abs(ratio_kg2o4), color='k', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k4o4), color='b', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k42o4), color='r', where='mid', linewidth=1)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
axs[1].minorticks_on()
axs[1].set_ylim(0, 1)
#axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
#               fontsize=16,color="black")

#axs[1].set_ylim(1*10**-4, 10**4)
#axs[1].set_yticks([10**-4, 1, 10**4])
#plt.tight_layout(pad=-0.1)
plt.savefig("figure_7d.pdf", bbox_inches='tight')















ratio_o5_lo_050050=k5lo_050050/k52lo_050050
ratio_o5_lo_025025=k5lo_025025/k52lo_025025
ratio_o5_lo_025050=k5lo_025050/k52lo_025050
ratio_o5_lo_050025=k5lo_050025/k52lo_050025
ratio_o5_lo_050100=k5lo_050100/k52lo_050100
ratio_o5_lo_100050=k5lo_100050/k52lo_100050
ratio_o5_lo_100100=k5lo_100100/k52lo_100100

ratio_o5_lo_min=[]
ratio_o5_lo_max=[]

for i in range(0, len(ratio_o5_lo_050050)):
    values=[ratio_o5_lo_050050[i], ratio_o5_lo_025025[i], ratio_o5_lo_025050[i], ratio_o5_lo_050025[i], ratio_o5_lo_050100[i], ratio_o5_lo_100050[i], ratio_o5_lo_100100[i]]
    ratio_o5_lo_min.append(np.min(values))
    ratio_o5_lo_max.append(np.max(values))

ratio_o5_lo_min=np.array(ratio_o5_lo_min)
ratio_o5_lo_max=np.array(ratio_o5_lo_max)


ratio_kgo5_lo_050050=kg2lo_050050/k52lo_050050
ratio_kgo5_lo_025025=kg2lo_025025/k52lo_025025
ratio_kgo5_lo_025050=kg2lo_025050/k52lo_025050
ratio_kgo5_lo_050025=kg2lo_050025/k52lo_050025
ratio_kgo5_lo_050100=kg2lo_050100/k52lo_050100
ratio_kgo5_lo_100050=kg2lo_100050/k52lo_100050
ratio_kgo5_lo_100100=kg2lo_100100/k52lo_100100

ratio_kgo5_lo_min=[]
ratio_kgo5_lo_max=[]

for i in range(0, len(ratio_kgo5_lo_050050)):
    values=[ratio_kgo5_lo_050050[i], ratio_kgo5_lo_025025[i], ratio_kgo5_lo_025050[i], ratio_kgo5_lo_050025[i], ratio_kgo5_lo_050100[i], ratio_kgo5_lo_100050[i], ratio_kgo5_lo_100100[i]]
    ratio_kgo5_lo_min.append(np.min(values))
    ratio_kgo5_lo_max.append(np.max(values))

ratio_kgo5_lo_min=np.array(ratio_kgo5_lo_min)
ratio_kgo5_lo_max=np.array(ratio_kgo5_lo_max)


ratio_o5_nll_050050050=k5nll_050050050/k52nll_050050050
ratio_o5_nll_050050025=k5nll_050050025/k52nll_050050025
ratio_o5_nll_050050100=k5nll_050050100/k52nll_050050100
ratio_o5_nll_025025050=k5nll_025025050/k52nll_025025050
ratio_o5_nll_025050050=k5nll_025050050/k52nll_025050050
ratio_o5_nll_050025050=k5nll_050025050/k52nll_050025050
ratio_o5_nll_050100050=k5nll_050100050/k52nll_050100050
ratio_o5_nll_100050050=k5nll_100050050/k52nll_100050050
ratio_o5_nll_100100050=k5nll_100100050/k52nll_100100050

ratio_o5_nll_min=[]
ratio_o5_nll_max=[]

for i in range(0, len(ratio_o5_nll_050050050)):
    values=[ratio_o5_nll_050050050[i], ratio_o5_nll_050050025[i], ratio_o5_nll_050050100[i], ratio_o5_nll_025025050[i], ratio_o5_nll_025050050[i], ratio_o5_nll_050025050[i], ratio_o5_nll_050100050[i], ratio_o5_nll_100050050[i], ratio_o5_nll_100100050[i]]
    ratio_o5_nll_min.append(np.min(values))
    ratio_o5_nll_max.append(np.max(values))

ratio_o5_nll_min=np.array(ratio_o5_nll_min)
ratio_o5_nll_max=np.array(ratio_o5_nll_max)


ratio_kgo5_nll_050050050=kg2nll_050050050/k52nll_050050050
ratio_kgo5_nll_050050025=kg2nll_050050025/k52nll_050050025
ratio_kgo5_nll_050050100=kg2nll_050050100/k52nll_050050100
ratio_kgo5_nll_025025050=kg2nll_025025050/k52nll_025025050
ratio_kgo5_nll_025050050=kg2nll_025050050/k52nll_025050050
ratio_kgo5_nll_050025050=kg2nll_050025050/k52nll_050025050
ratio_kgo5_nll_050100050=kg2nll_050100050/k52nll_050100050
ratio_kgo5_nll_100050050=kg2nll_100050050/k52nll_100050050
ratio_kgo5_nll_100100050=kg2nll_100100050/k52nll_100100050

ratio_kgo5_nll_min=[]
ratio_kgo5_nll_max=[]

for i in range(0, len(ratio_kgo5_nll_050050050)):
    values=[ratio_kgo5_nll_050050050[i], ratio_kgo5_nll_050050025[i], ratio_kgo5_nll_050050100[i], ratio_kgo5_nll_025025050[i], ratio_kgo5_nll_025050050[i], ratio_kgo5_nll_050025050[i], ratio_kgo5_nll_050100050[i], ratio_kgo5_nll_100050050[i], ratio_kgo5_nll_100100050[i]]
    ratio_kgo5_nll_min.append(np.min(values))
    ratio_kgo5_nll_max.append(np.max(values))

ratio_kgo5_nll_min=np.array(ratio_kgo5_nll_min)
ratio_kgo5_nll_max=np.array(ratio_kgo5_nll_max)


plt.rcParams["hatch.linewidth"] = 4

plt.figure(figsize=(20, 12.64),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"$\Lambda = 2TeV",\
#               fontsize=18,color="black")
rec1 = plt.Rectangle((500,10**-11),3500,0.5, facecolor="#d3d3d3", 
                     edgecolor="white", hatch=r"\\", zorder=0)
            
axs[0].add_patch(rec1)

#axs[0].margins(0.3)
#axs[0].autoscale()


axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")

axs[1].set_ylabel("Ratio to LO \n(No Jet Veto)\n",\
               fontsize=14,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()

bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].annotate(r'$\Lambda=2$TeV', (1800, 0.05),\
               fontsize=18,color="#3b3b3b")
axs[0].annotate(r'NLL $p_{T, veto} = 35$GeV', (1200, 2*10**-11),\
               fontsize=14,color="#3b3b3b")
#axs[0].annotate(r'EFT Breakdown', (510, 10**-7),\
#               fontsize=14,color="#3b3b3b")




axs[0].step(bin_centres, kg2nll_centre/(bin_widths18*3000), color='k', where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, kg2nll_min/(bin_widths18*3000), kg2nll_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k5nll_centre)/(bin_widths18*3000), color='b', where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_5)|$', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k5nll_min)/(bin_widths18*3000), abs(k5nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k52nll_centre/(bin_widths18*3000), color='r', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_5|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, k52nll_min/(bin_widths18*3000), k52nll_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''
axs[0].step(bin_centres, kg2lo_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \,$ LO (No Veto)', linewidth=0.9)


axs[0].fill_between(bin_centres, kg2lo_min/(bin_widths18*3000), kg2lo_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k5lo_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_5)|$ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k5lo_min)/(bin_widths18*3000), abs(k5lo_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k52lo_centre/(bin_widths18*3000), color='r', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_5|^2\ \ \ \ \ \ \ \ \ \ \ \, \ \ \ $ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, k52lo_min/(bin_widths18*3000), k52lo_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''


#axs[0].plot([500, 500], [0, 2], color="grey", linestyle="--")#, label=r'$M_{e\mu}^{\mathrm{Max}} = \frac{\Lambda}{4}$')
axs[0].legend(loc="lower left", fontsize=11, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(10**-11, 0.5)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True, pad=10)


ratio_kg2o5=kg2nll_centre/kg2lo_centre
ratio_k5o5=k5nll_centre/k5lo_centre
ratio_k52o5=k52nll_centre/k52lo_centre

axs[1].semilogx()

axs[1].step(bin_centres, abs(ratio_kg2o5), color='k', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k5o5), color='b', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k52o5), color='r', where='mid', linewidth=1)

axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
               fontsize=16,color="black")
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].set_ylim(0, 1)
axs[1].yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
axs[1].minorticks_on()
#axs[1].set_ylim(1*10**-4, 10**4)
#axs[1].set_yticks([10**-4, 1, 10**4])
#plt.tight_layout(pad=-0.1)
plt.savefig("figure_7e.pdf", bbox_inches='tight')















ratio_o6_lo_050050=k6lo_050050/k62lo_050050
ratio_o6_lo_025025=k6lo_025025/k62lo_025025
ratio_o6_lo_025050=k6lo_025050/k62lo_025050
ratio_o6_lo_050025=k6lo_050025/k62lo_050025
ratio_o6_lo_050100=k6lo_050100/k62lo_050100
ratio_o6_lo_100050=k6lo_100050/k62lo_100050
ratio_o6_lo_100100=k6lo_100100/k62lo_100100

ratio_o6_lo_min=[]
ratio_o6_lo_max=[]

for i in range(0, len(ratio_o6_lo_050050)):
    values=[ratio_o6_lo_050050[i], ratio_o6_lo_025025[i], ratio_o6_lo_025050[i], ratio_o6_lo_050025[i], ratio_o6_lo_050100[i], ratio_o6_lo_100050[i], ratio_o6_lo_100100[i]]
    ratio_o6_lo_min.append(np.min(values))
    ratio_o6_lo_max.append(np.max(values))

ratio_o6_lo_min=np.array(ratio_o6_lo_min)
ratio_o6_lo_max=np.array(ratio_o6_lo_max)


ratio_kgo6_lo_050050=kg2lo_050050/k62lo_050050
ratio_kgo6_lo_025025=kg2lo_025025/k62lo_025025
ratio_kgo6_lo_025050=kg2lo_025050/k62lo_025050
ratio_kgo6_lo_050025=kg2lo_050025/k62lo_050025
ratio_kgo6_lo_050100=kg2lo_050100/k62lo_050100
ratio_kgo6_lo_100050=kg2lo_100050/k62lo_100050
ratio_kgo6_lo_100100=kg2lo_100100/k62lo_100100

ratio_kgo6_lo_min=[]
ratio_kgo6_lo_max=[]

for i in range(0, len(ratio_kgo6_lo_050050)):
    values=[ratio_kgo6_lo_050050[i], ratio_kgo6_lo_025025[i], ratio_kgo6_lo_025050[i], ratio_kgo6_lo_050025[i], ratio_kgo6_lo_050100[i], ratio_kgo6_lo_100050[i], ratio_kgo6_lo_100100[i]]
    ratio_kgo6_lo_min.append(np.min(values))
    ratio_kgo6_lo_max.append(np.max(values))

ratio_kgo6_lo_min=np.array(ratio_kgo6_lo_min)
ratio_kgo6_lo_max=np.array(ratio_kgo6_lo_max)


ratio_o6_nll_050050050=k6nll_050050050/k62nll_050050050
ratio_o6_nll_050050025=k6nll_050050025/k62nll_050050025
ratio_o6_nll_050050100=k6nll_050050100/k62nll_050050100
ratio_o6_nll_025025050=k6nll_025025050/k62nll_025025050
ratio_o6_nll_025050050=k6nll_025050050/k62nll_025050050
ratio_o6_nll_050025050=k6nll_050025050/k62nll_050025050
ratio_o6_nll_050100050=k6nll_050100050/k62nll_050100050
ratio_o6_nll_100050050=k6nll_100050050/k62nll_100050050
ratio_o6_nll_100100050=k6nll_100100050/k62nll_100100050

ratio_o6_nll_min=[]
ratio_o6_nll_max=[]

for i in range(0, len(ratio_o6_nll_050050050)):
    values=[ratio_o6_nll_050050050[i], ratio_o6_nll_050050025[i], ratio_o6_nll_050050100[i], ratio_o6_nll_025025050[i], ratio_o6_nll_025050050[i], ratio_o6_nll_050025050[i], ratio_o6_nll_050100050[i], ratio_o6_nll_100050050[i], ratio_o6_nll_100100050[i]]
    ratio_o6_nll_min.append(np.min(values))
    ratio_o6_nll_max.append(np.max(values))

ratio_o6_nll_min=np.array(ratio_o6_nll_min)
ratio_o6_nll_max=np.array(ratio_o6_nll_max)


ratio_kgo6_nll_050050050=kg2nll_050050050/k62nll_050050050
ratio_kgo6_nll_050050025=kg2nll_050050025/k62nll_050050025
ratio_kgo6_nll_050050100=kg2nll_050050100/k62nll_050050100
ratio_kgo6_nll_025025050=kg2nll_025025050/k62nll_025025050
ratio_kgo6_nll_025050050=kg2nll_025050050/k62nll_025050050
ratio_kgo6_nll_050025050=kg2nll_050025050/k62nll_050025050
ratio_kgo6_nll_050100050=kg2nll_050100050/k62nll_050100050
ratio_kgo6_nll_100050050=kg2nll_100050050/k62nll_100050050
ratio_kgo6_nll_100100050=kg2nll_100100050/k62nll_100100050

ratio_kgo6_nll_min=[]
ratio_kgo6_nll_max=[]

for i in range(0, len(ratio_kgo6_nll_050050050)):
    values=[ratio_kgo6_nll_050050050[i], ratio_kgo6_nll_050050025[i], ratio_kgo6_nll_050050100[i], ratio_kgo6_nll_025025050[i], ratio_kgo6_nll_025050050[i], ratio_kgo6_nll_050025050[i], ratio_kgo6_nll_050100050[i], ratio_kgo6_nll_100050050[i], ratio_kgo6_nll_100100050[i]]
    ratio_kgo6_nll_min.append(np.min(values))
    ratio_kgo6_nll_max.append(np.max(values))

ratio_kgo6_nll_min=np.array(ratio_kgo6_nll_min)
ratio_kgo6_nll_max=np.array(ratio_kgo6_nll_max)


plt.rcParams["hatch.linewidth"] = 4

plt.figure(figsize=(20, 12.64),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"$\Lambda = 2TeV",\
#               fontsize=18,color="black")
rec1 = plt.Rectangle((500,10**-11),3500,0.5, facecolor="#d3d3d3", 
                     edgecolor="white", hatch=r"\\", zorder=0)
axs[0].add_patch(rec1)

#axs[0].margins(0.3)
#axs[0].autoscale()


axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")

axs[1].set_ylabel("Ratio to LO \n(No Jet Veto)\n",\
               fontsize=14,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()

bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].annotate(r'$\Lambda=2$TeV', (1800, 0.05),\
               fontsize=18,color="#3b3b3b")
axs[0].annotate(r'NLL $p_{T, veto} = 35$GeV', (1200, 2*10**-11),\
               fontsize=14,color="#3b3b3b")
#axs[0].annotate(r'EFT Breakdown', (510, 10**-7),\
#               fontsize=14,color="#3b3b3b")




axs[0].step(bin_centres, kg2nll_centre/(bin_widths18*3000), color='k', where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, kg2nll_min/(bin_widths18*3000), kg2nll_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k6nll_centre)/(bin_widths18*3000), color='b', where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_6)|$', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k6nll_min)/(bin_widths18*3000), abs(k6nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k62nll_centre/(bin_widths18*3000), color='r', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_6|^2$', linewidth=0.9)

axs[0].fill_between(bin_centres, k62nll_min/(bin_widths18*3000), k62nll_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''
axs[0].step(bin_centres, kg2lo_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', label=r'$\frac{c_{GH}}{\Lambda^4}|\overline{\mathcal{M}}^{(6)}_{g}|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \,$ LO (No Veto)', linewidth=0.9)


axs[0].fill_between(bin_centres, kg2lo_min/(bin_widths18*3000), kg2lo_max/(bin_widths18*3000),
                     color='k', alpha=0.2, step='mid')

axs[0].step(bin_centres, abs(k6lo_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^4}2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_6)|$ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, abs(k6lo_min)/(bin_widths18*3000), abs(k6lo_max)/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')

axs[0].step(bin_centres, k62lo_centre/(bin_widths18*3000), color='r', linestyle="--", where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_6|^2\ \ \ \ \ \ \ \ \ \ \ \, \ \ \ $ LO (No Veto)', linewidth=0.9)

axs[0].fill_between(bin_centres, k62lo_min/(bin_widths18*3000), k62lo_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')
'''


#axs[0].plot([500, 500], [0, 2], color="grey", linestyle="--")#, label=r'$M_{e\mu}^{\mathrm{Max}} = \frac{\Lambda}{4}$')
axs[0].legend(loc="lower left", fontsize=11, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(10**-11, 0.5)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True, pad=10)

ratio_kg2o6=kg2nll_centre/kg2lo_centre
ratio_k6o6=k6nll_centre/k6lo_centre
ratio_k62o6=k62nll_centre/k62lo_centre

axs[1].semilogx()

axs[1].step(bin_centres, abs(ratio_kg2o6), color='k', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k6o6), color='b', where='mid', linewidth=1)

axs[1].step(bin_centres, abs(ratio_k62o6), color='r', where='mid', linewidth=1)
axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
               fontsize=16,color="black")
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
axs[1].minorticks_on()
axs[1].set_ylim(0, 1)

#axs[1].set_ylim(1*10**-4, 10**4)
#axs[1].set_yticks([10**-4, 1, 10**4])
#plt.tight_layout(pad=-0.1)
plt.savefig("figure_7f.pdf", bbox_inches='tight')

