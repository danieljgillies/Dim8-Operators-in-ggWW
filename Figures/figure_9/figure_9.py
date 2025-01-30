
import numpy as np
import matplotlib.pyplot as plt
from math import log10, floor
import matplotlib as mpl
import matplotlib.ticker as ticker

def array_for_plot(a):
    return np.concatenate((np.array([a[0]]), a, np.array([a[len(a)-1]])))


def round_to_5(x):
    rounded=[]
    for i in range(len(x)):
        rounded.append(np.round(x[i], 6-int(floor(log10(abs(x[i]))))))
    return np.array(rounded)


bins=round_to_5(np.logspace(np.log10(200), np.log10(4000), 17))
print(bins)
bin_widths=bins[1:17]-bins[0:16]
bin_widths18=np.array([41.1817, 41.1817, 49.6614, 59.8871, 72.2183, 87.0887, 105.021, 126.6458, 152.7232, 184.1698, 222.093, 267.823, 322.97, 389.473, 469.668, 566.377, 682.999, 682.999])


k1nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_centre.npy"))
k1nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_min.npy"))
k1nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_max.npy"))
k1nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k1nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k1nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k1nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k1nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k1nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k1nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k1nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k1nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))


k2nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_centre.npy"))
k2nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_min.npy"))
k2nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_max.npy"))
k2nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k2nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k2nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k2nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k2nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k2nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k2nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k2nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k2nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))


k3nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_centre.npy"))
k3nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_min.npy"))
k3nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_max.npy"))
k3nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k3nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k3nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k3nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k3nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k3nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k3nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k3nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k3nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))


k4nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_centre.npy"))
k4nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_min.npy"))
k4nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_max.npy"))
k4nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k4nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k4nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k4nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k4nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k4nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k4nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k4nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k4nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))


k5nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_centre.npy"))
k5nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_min.npy"))
k5nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_max.npy"))
k5nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k5nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k5nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k5nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k5nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k5nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k5nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k5nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k5nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k6nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_centre.npy"))
k6nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_min.npy"))
k6nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_max.npy"))
k6nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k6nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k6nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k6nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k6nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k6nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k6nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k6nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k6nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6SMint_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k12nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_centre.npy"))
k12nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_min.npy"))
k12nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_max.npy"))
k12nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k12nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k12nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k12nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k12nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k12nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k12nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k12nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k12nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O1sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k22nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_centre.npy"))
k22nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_min.npy"))
k22nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_max.npy"))
k22nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k22nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k22nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k22nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k22nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k22nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k22nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k22nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k22nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O2sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k32nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_centre.npy"))
k32nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_min.npy"))
k32nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_max.npy"))
k32nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k32nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k32nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k32nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k32nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k32nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k32nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k32nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k32nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k42nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_centre.npy"))
k42nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_min.npy"))
k42nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_max.npy"))
k42nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k42nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k42nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k42nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k42nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k42nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k42nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k42nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k42nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k52nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_centre.npy"))
k52nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_min.npy"))
k52nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_max.npy"))
k52nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k52nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k52nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k52nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k52nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k52nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k52nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k52nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k52nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))



k62nll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_centre.npy"))
k62nll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_min.npy"))
k62nll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_max.npy"))
k62nll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k62nll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
k62nll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
k62nll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k62nll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k62nll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
k62nll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
k62nll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
k62nll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))




ggnll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_centre.npy"))
ggnll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_min.npy"))
ggnll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_max.npy"))




ggnll_050050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
ggnll_050050025=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
ggnll_050050100=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
ggnll_025025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
ggnll_025050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
ggnll_050025050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
ggnll_050100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
ggnll_100050050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
ggnll_100100050=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))

print(ggnll_050050050/(6000*bin_widths18))

sm=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_centre.npy"))
sm_min=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_min.npy"))
sm_max=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_max.npy"))

print(sm/6000)
print(sm_max/6000)
print(sm_min/6000)

err_sm=(sm_max-sm_min)/2



mass_scale=2#


k1gg_nll_050050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050050*k12nll_050050050)
k1gg_nll_050050025=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050025*k12nll_050050025)
k1gg_nll_050050100=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050100*k12nll_050050100)
k1gg_nll_025025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025025050*k12nll_025025050)
k1gg_nll_025050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025050050*k12nll_025050050)
k1gg_nll_050025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050025050*k12nll_050025050)
k1gg_nll_050100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050100050*k12nll_050100050)
k1gg_nll_100050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100050050*k12nll_100050050)
k1gg_nll_100100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100100050*k12nll_100100050)


k1gg_nll_min=[]
k1gg_nll_max=[]

for i in range(0, len(k1gg_nll_050050050)):
    values=[k1gg_nll_050050050[i], k1gg_nll_050050025[i], k1gg_nll_050050100[i], k1gg_nll_025025050[i], k1gg_nll_025050050[i], k1gg_nll_050025050[i], k1gg_nll_050100050[i], k1gg_nll_100050050[i], k1gg_nll_100100050[i]]
    k1gg_nll_min.append(np.min(values))
    k1gg_nll_max.append(np.max(values))

k1gg_nll_min=np.array(k1gg_nll_min)
k1gg_nll_max=np.array(k1gg_nll_max)



plt.figure(figsize=(16, 12),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"Operator 1 Comparison to \mathrm{SM} ATLAS 14TeV",\
#               fontsize=18,color="black")
#axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
#               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r"Ratio to SM",\
               fontsize=16,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()
axs[0].annotate(r'$\Lambda=$'+str(mass_scale)+r'TeV', (1800, 0.05),\
               fontsize=18,color="grey")

axs[0].annotate(r'Resummed $p_{T, veto} = 35$GeV', (660, 2*10**-12),\
               fontsize=15,color="grey")

bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].step(bin_centres, sm/(bin_widths18*3000), color='k', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2$', linewidth=0.7)
axs[0].fill_between(bin_centres, sm_min/(bin_widths18*3000), sm_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')


axs[0].step(bin_centres, ggnll_centre/(bin_widths18*3000), color='#FF8C00', where='mid', label=r'$|\mathcal{M}^{(gg)}_{\mathrm{SM}}|^2$', linewidth=0.7)

axs[0].fill_between(bin_centres, ggnll_min/(bin_widths18*3000), ggnll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(k12nll_centre*ggnll_centre)/(bin_widths18*3000), color='#FF8C00', linestyle="--", where='mid', label=r'$2|\mathcal{M}^{(gg)}_{\mathrm{SM}}||\mathcal{M}^{(8)}_1|$', linewidth=0.7)

axs[0].fill_between(bin_centres, k1gg_nll_min/(bin_widths18*3000), k1gg_nll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k1nll_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_1)|\ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k1nll_min)/(bin_widths18*3000), (2000**4)/((mass_scale*1000)**4)*abs(k1nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*k12nll_centre/(bin_widths18*3000), color='b', where='mid', label=r'$|\mathcal{M}^{(8)}_1|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*k12nll_min/(bin_widths18*3000), (2000**8)/((mass_scale*1000)**8)*k12nll_max/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')



axs[0].legend(loc="lower left", fontsize=10, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(0.9*10**-12, 1)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)

ratio_gg_nll=ggnll_centre/sm

err_gg_nll=ratio_gg_nll*((err_sm/sm)**2 + (((ggnll_max-ggnll_min)/2)/ggnll_centre)**2)**0.5

ratio_k1_nll=k1nll_centre/sm

err_k1_nll=ratio_k1_nll*((err_sm/sm)**2 + (((k1nll_max-k1nll_min)/2)/k1nll_centre)**2)**0.5

ratio_k12_nll=k12nll_centre/sm

err_k12_nll=ratio_k12_nll*((err_sm/sm)**2 + (((k12nll_max-k12nll_min)/2)/k12nll_centre)**2)**0.5

ratio_k1gg_nll=np.sqrt(k12nll_centre*ggnll_centre)/sm

err_k1gg_nll=ratio_k1gg_nll*((err_sm/sm)**2 + (((k1gg_nll_max-k1gg_nll_min)/2)/(np.sqrt(k12nll_centre*ggnll_centre)))**2)**0.5



axs[1].loglog()

axs[1].step(bin_centres, ratio_gg_nll, color='#FF8C00', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, ratio_gg_nll-err_gg_nll, ratio_gg_nll+err_gg_nll,
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k12_nll), color='#FF8C00', linestyle="--", where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k12_nll)-err_k1gg_nll), (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k12_nll)+err_k1gg_nll),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(ratio_k1_nll), color='b', linestyle="--", where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k1_nll)-abs(err_k1_nll)), (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k1_nll)+abs(err_k1_nll)),
                     color='b', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*abs(ratio_k12_nll), color='b', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*(ratio_k12_nll-err_k12_nll), (2000**8)/((mass_scale*1000)**8)*(ratio_k12_nll+err_k12_nll),
                     color='b', alpha=0.3, step='mid')
#axs[1].set_ylim(2*10**-4, 2)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].yaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=4))
#plt.tight_layout()
plt.savefig("figure_9a.pdf", bbox_inches='tight')

k2gg_nll_050050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050050*k22nll_050050050)
k2gg_nll_050050025=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050025*k22nll_050050025)
k2gg_nll_050050100=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050100*k22nll_050050100)
k2gg_nll_025025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025025050*k22nll_025025050)
k2gg_nll_025050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025050050*k22nll_025050050)
k2gg_nll_050025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050025050*k22nll_050025050)
k2gg_nll_050100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050100050*k22nll_050100050)
k2gg_nll_100050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100050050*k22nll_100050050)
k2gg_nll_100100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100100050*k22nll_100100050)


k2gg_nll_min=[]
k2gg_nll_max=[]

for i in range(0, len(k2gg_nll_050050050)):
    values=[k2gg_nll_050050050[i], k2gg_nll_050050025[i], k2gg_nll_050050100[i], k2gg_nll_025025050[i], k2gg_nll_025050050[i], k2gg_nll_050025050[i], k2gg_nll_050100050[i], k2gg_nll_100050050[i], k2gg_nll_100100050[i]]
    k2gg_nll_min.append(np.min(values))
    k2gg_nll_max.append(np.max(values))

k2gg_nll_min=np.array(k2gg_nll_min)
k2gg_nll_max=np.array(k2gg_nll_max)



plt.figure(figsize=(16, 12),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"Operator 2 Comparison to \mathrm{SM} ATLAS 14TeV",\
#               fontsize=18,color="black")
#axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
#               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r"Ratio to SM",\
               fontsize=16,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()
axs[0].annotate(r'$\Lambda=$'+str(mass_scale)+r'TeV', (1800, 0.05),\
               fontsize=18,color="grey")

axs[0].annotate(r'Resummed $p_{T, veto} = 35$GeV', (660, 2*10**-12),\
               fontsize=15,color="grey")

bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].step(bin_centres, sm/(bin_widths18*3000), color='k', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2$ ', linewidth=0.7)

axs[0].fill_between(bin_centres, sm_min/(bin_widths18*3000), sm_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')


axs[0].step(bin_centres, ggnll_centre/(bin_widths18*3000), color='#FF8C00', where='mid', label=r'$|\mathcal{M}^{(gg)}_{\mathrm{SM}}|^2$', linewidth=0.7)

axs[0].fill_between(bin_centres, ggnll_min/(bin_widths18*3000), ggnll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(k22nll_centre*ggnll_centre)/(bin_widths18*3000), color='#FF8C00', linestyle="--", where='mid', label=r'$2|\mathcal{M}^{(gg)}_{\mathrm{SM}}||\mathcal{M}^{(8)}_2|$', linewidth=0.7)

axs[0].fill_between(bin_centres, k2gg_nll_min/(bin_widths18*3000), k2gg_nll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k2nll_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_2)|\ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k2nll_min)/(bin_widths18*3000), (2000**4)/((mass_scale*1000)**4)*abs(k2nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*k22nll_centre/(bin_widths18*3000), color='b', where='mid', label=r'$|\mathcal{M}^{(8)}_2|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*k22nll_min/(bin_widths18*3000), (2000**8)/((mass_scale*1000)**8)*k22nll_max/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')


axs[0].legend(loc="lower left", fontsize=10, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(0.9*10**-12, 1)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)


ratio_gg_nll=ggnll_centre/sm

err_gg_nll=ratio_gg_nll*((err_sm/sm)**2 + (((ggnll_max-ggnll_min)/2)/ggnll_centre)**2)**0.5

ratio_k2_nll=k2nll_centre/sm

err_k2_nll=ratio_k2_nll*((err_sm/sm)**2 + (((k2nll_max-k2nll_min)/2)/k2nll_centre)**2)**0.5

ratio_k22_nll=k22nll_centre/sm

err_k22_nll=ratio_k22_nll*((err_sm/sm)**2 + (((k22nll_max-k22nll_min)/2)/k22nll_centre)**2)**0.5

ratio_k2gg_nll=np.sqrt(k22nll_centre*ggnll_centre)/sm

err_k2gg_nll=ratio_k2gg_nll*((err_sm/sm)**2 + (((k2gg_nll_max-k2gg_nll_min)/2)/(np.sqrt(k22nll_centre*ggnll_centre)))**2)**0.5



axs[1].loglog()

axs[1].step(bin_centres, ratio_gg_nll, color='#FF8C00', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, ratio_gg_nll-err_gg_nll, ratio_gg_nll+err_gg_nll,
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k22_nll), color='#FF8C00', linestyle="--", where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k22_nll)-err_k2gg_nll), (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k22_nll)+err_k2gg_nll),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(ratio_k2_nll), color='b', linestyle="--", where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k2_nll)-abs(err_k2_nll)), (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k2_nll)+abs(err_k2_nll)),
                     color='b', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*abs(ratio_k22_nll), color='b', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*(ratio_k22_nll-err_k22_nll), (2000**8)/((mass_scale*1000)**8)*(ratio_k22_nll+err_k22_nll),
                     color='b', alpha=0.3, step='mid')
#axs[1].set_ylim(2*10**-4, 2)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].yaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=4))
#plt.tight_layout()
plt.savefig("figure_9b.pdf", bbox_inches='tight')

k3gg_nll_050050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050050*k32nll_050050050)
k3gg_nll_050050025=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050025*k32nll_050050025)
k3gg_nll_050050100=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050100*k32nll_050050100)
k3gg_nll_025025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025025050*k32nll_025025050)
k3gg_nll_025050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025050050*k32nll_025050050)
k3gg_nll_050025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050025050*k32nll_050025050)
k3gg_nll_050100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050100050*k32nll_050100050)
k3gg_nll_100050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100050050*k32nll_100050050)
k3gg_nll_100100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100100050*k32nll_100100050)


k3gg_nll_min=[]
k3gg_nll_max=[]

for i in range(0, len(k3gg_nll_050050050)):
    values=[k3gg_nll_050050050[i], k3gg_nll_050050025[i], k3gg_nll_050050100[i], k3gg_nll_025025050[i], k3gg_nll_025050050[i], k3gg_nll_050025050[i], k3gg_nll_050100050[i], k3gg_nll_100050050[i], k3gg_nll_100100050[i]]
    k3gg_nll_min.append(np.min(values))
    k3gg_nll_max.append(np.max(values))

k3gg_nll_min=np.array(k3gg_nll_min)
k3gg_nll_max=np.array(k3gg_nll_max)



plt.figure(figsize=(16, 12),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"Operator 3 Comparison to \mathrm{SM} ATLAS 14TeV",\
#               fontsize=18,color="black")
#axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
#               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r"Ratio to SM",\
               fontsize=16,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()
axs[0].annotate(r'$\Lambda=$'+str(mass_scale)+r'TeV', (1800, 0.05),\
               fontsize=18,color="grey")

axs[0].annotate(r'Resummed $p_{T, veto} = 35$GeV', (660, 2*10**-12),\
               fontsize=15,color="grey")
bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].step(bin_centres, sm/(bin_widths18*3000), color='k', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2$ ', linewidth=0.7)

axs[0].fill_between(bin_centres, sm_min/(bin_widths18*3000), sm_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')


axs[0].step(bin_centres, ggnll_centre/(bin_widths18*3000), color='#FF8C00', where='mid', label=r'$|\mathcal{M}^{(gg)}_{\mathrm{SM}}|^2$', linewidth=0.7)

axs[0].fill_between(bin_centres, ggnll_min/(bin_widths18*3000), ggnll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(k32nll_centre*ggnll_centre)/(bin_widths18*3000), color='#FF8C00', linestyle="--", where='mid', label=r'$2|\mathcal{M}^{(gg)}_{\mathrm{SM}}||\mathcal{M}^{(8)}_3|$', linewidth=0.7)

axs[0].fill_between(bin_centres, k3gg_nll_min/(bin_widths18*3000), k3gg_nll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k3nll_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_3)|\ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k3nll_min)/(bin_widths18*3000), (2000**4)/((mass_scale*1000)**4)*abs(k3nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*k32nll_centre/(bin_widths18*3000), color='b', where='mid', label=r'$|\mathcal{M}^{(8)}_3|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*k32nll_min/(bin_widths18*3000), (2000**8)/((mass_scale*1000)**8)*k32nll_max/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')


axs[0].legend(loc="lower left", fontsize=10, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(0.9*10**-12, 1)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)


ratio_gg_nll=ggnll_centre/sm

err_gg_nll=ratio_gg_nll*((err_sm/sm)**2 + (((ggnll_max-ggnll_min)/2)/ggnll_centre)**2)**0.5

ratio_k3_nll=k3nll_centre/sm

err_k3_nll=ratio_k3_nll*((err_sm/sm)**2 + (((k3nll_max-k3nll_min)/2)/k3nll_centre)**2)**0.5

ratio_k32_nll=k32nll_centre/sm

err_k32_nll=ratio_k32_nll*((err_sm/sm)**2 + (((k32nll_max-k32nll_min)/2)/k32nll_centre)**2)**0.5

ratio_k3gg_nll=np.sqrt(k32nll_centre*ggnll_centre)/sm

err_k3gg_nll=ratio_k3gg_nll*((err_sm/sm)**2 + (((k3gg_nll_max-k3gg_nll_min)/2)/(np.sqrt(k32nll_centre*ggnll_centre)))**2)**0.5



axs[1].loglog()

axs[1].step(bin_centres, ratio_gg_nll, color='#FF8C00', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, ratio_gg_nll-err_gg_nll, ratio_gg_nll+err_gg_nll,
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k32_nll), color='#FF8C00', linestyle="--", where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k32_nll)-err_k3gg_nll), (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k32_nll)+err_k3gg_nll),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(ratio_k3_nll), color='b', linestyle="--", where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k3_nll)-abs(err_k3_nll)), (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k3_nll)+abs(err_k3_nll)),
                     color='b', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*abs(ratio_k32_nll), color='b', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*(ratio_k32_nll-err_k32_nll), (2000**8)/((mass_scale*1000)**8)*(ratio_k32_nll+err_k32_nll),
                     color='b', alpha=0.3, step='mid')
#axs[1].set_ylim(2*10**-4, 2)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].yaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=4))
#plt.tight_layout()
plt.savefig("figure_9c.pdf", bbox_inches='tight')

k4gg_nll_050050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050050*k42nll_050050050)
k4gg_nll_050050025=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050025*k42nll_050050025)
k4gg_nll_050050100=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050100*k42nll_050050100)
k4gg_nll_025025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025025050*k42nll_025025050)
k4gg_nll_025050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025050050*k42nll_025050050)
k4gg_nll_050025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050025050*k42nll_050025050)
k4gg_nll_050100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050100050*k42nll_050100050)
k4gg_nll_100050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100050050*k42nll_100050050)
k4gg_nll_100100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100100050*k42nll_100100050)


k4gg_nll_min=[]
k4gg_nll_max=[]

for i in range(0, len(k4gg_nll_050050050)):
    values=[k4gg_nll_050050050[i], k4gg_nll_050050025[i], k4gg_nll_050050100[i], k4gg_nll_025025050[i], k4gg_nll_025050050[i], k4gg_nll_050025050[i], k4gg_nll_050100050[i], k4gg_nll_100050050[i], k4gg_nll_100100050[i]]
    k4gg_nll_min.append(np.min(values))
    k4gg_nll_max.append(np.max(values))

k4gg_nll_min=np.array(k4gg_nll_min)
k4gg_nll_max=np.array(k4gg_nll_max)



plt.figure(figsize=(16, 12),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"Operator 4 Comparison to \mathrm{SM} ATLAS 14TeV",\
#               fontsize=18,color="black")
#axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
#               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r"Ratio to SM",\
               fontsize=16,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()
axs[0].annotate(r'$\Lambda=$'+str(mass_scale)+r'TeV', (1800, 0.05),\
               fontsize=18,color="grey")

axs[0].annotate(r'Resummed $p_{T, veto} = 35$GeV', (660, 2*10**-12),\
               fontsize=15,color="grey")
bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].step(bin_centres, sm/(bin_widths18*3000), color='k', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2$ ', linewidth=0.7)

axs[0].fill_between(bin_centres, sm_min/(bin_widths18*3000), sm_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')


axs[0].step(bin_centres, ggnll_centre/(bin_widths18*3000), color='#FF8C00', where='mid', label=r'$|\mathcal{M}^{(gg)}_{\mathrm{SM}}|^2$', linewidth=0.7)

axs[0].fill_between(bin_centres, ggnll_min/(bin_widths18*3000), ggnll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(k42nll_centre*ggnll_centre)/(bin_widths18*3000), color='#FF8C00', linestyle="--", where='mid', label=r'$2|\mathcal{M}^{(gg)}_{\mathrm{SM}}||\mathcal{M}^{(8)}_4|$', linewidth=0.7)

axs[0].fill_between(bin_centres, k4gg_nll_min/(bin_widths18*3000), k4gg_nll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k4nll_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_4)|\ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k4nll_min)/(bin_widths18*3000), (2000**4)/((mass_scale*1000)**4)*abs(k4nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*k42nll_centre/(bin_widths18*3000), color='b', where='mid', label=r'$|\mathcal{M}^{(8)}_4|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*k42nll_min/(bin_widths18*3000), (2000**8)/((mass_scale*1000)**8)*k42nll_max/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')


axs[0].legend(loc="lower left", fontsize=10, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(0.9*10**-12, 1)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)

#axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
#axs[1].tick_params(which="both", labelsize=13, direction='in', right=True, pad=10)

ratio_gg_nll=ggnll_centre/sm

err_gg_nll=ratio_gg_nll*((err_sm/sm)**2 + (((ggnll_max-ggnll_min)/2)/ggnll_centre)**2)**0.5

ratio_k4_nll=k4nll_centre/sm

err_k4_nll=ratio_k4_nll*((err_sm/sm)**2 + (((k4nll_max-k4nll_min)/2)/k4nll_centre)**2)**0.5

ratio_k42_nll=k42nll_centre/sm

err_k42_nll=ratio_k42_nll*((err_sm/sm)**2 + (((k42nll_max-k42nll_min)/2)/k42nll_centre)**2)**0.5

ratio_k4gg_nll=np.sqrt(k42nll_centre*ggnll_centre)/sm

err_k4gg_nll=ratio_k4gg_nll*((err_sm/sm)**2 + (((k4gg_nll_max-k4gg_nll_min)/2)/(np.sqrt(k42nll_centre*ggnll_centre)))**2)**0.5



axs[1].loglog()

axs[1].step(bin_centres, ratio_gg_nll, color='#FF8C00', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, ratio_gg_nll-err_gg_nll, ratio_gg_nll+err_gg_nll,
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k42_nll), color='#FF8C00', linestyle="--", where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k42_nll)-err_k4gg_nll), (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k42_nll)+err_k4gg_nll),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(ratio_k4_nll), color='b', linestyle="--", where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k4_nll)-abs(err_k4_nll)), (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k4_nll)+abs(err_k4_nll)),
                     color='b', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*abs(ratio_k42_nll), color='b', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*(ratio_k42_nll-err_k42_nll), (2000**8)/((mass_scale*1000)**8)*(ratio_k42_nll+err_k42_nll),
                     color='b', alpha=0.3, step='mid')
#axs[1].set_ylim(2*10**-4, 2)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].yaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=4))
#axs[1].yaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs=[2, 3, 4, 5, 6, 7, 8, 9], numticks=10))
axs[1].minorticks_on()
#plt.tight_layout()
plt.savefig("figure_9d.pdf", bbox_inches='tight')

k5gg_nll_050050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050050*k52nll_050050050)
k5gg_nll_050050025=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050025*k52nll_050050025)
k5gg_nll_050050100=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050100*k52nll_050050100)
k5gg_nll_025025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025025050*k52nll_025025050)
k5gg_nll_025050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025050050*k52nll_025050050)
k5gg_nll_050025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050025050*k52nll_050025050)
k5gg_nll_050100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050100050*k52nll_050100050)
k5gg_nll_100050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100050050*k52nll_100050050)
k5gg_nll_100100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100100050*k52nll_100100050)


k5gg_nll_min=[]
k5gg_nll_max=[]

for i in range(0, len(k5gg_nll_050050050)):
    values=[k5gg_nll_050050050[i], k5gg_nll_050050025[i], k5gg_nll_050050100[i], k5gg_nll_025025050[i], k5gg_nll_025050050[i], k5gg_nll_050025050[i], k5gg_nll_050100050[i], k5gg_nll_100050050[i], k5gg_nll_100100050[i]]
    k5gg_nll_min.append(np.min(values))
    k5gg_nll_max.append(np.max(values))

k5gg_nll_min=np.array(k5gg_nll_min)
k5gg_nll_max=np.array(k5gg_nll_max)



plt.figure(figsize=(16, 12.81),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"Operator 5 Comparison to \mathrm{SM} ATLAS 14TeV",\
#               fontsize=18,color="black")
axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r"Ratio to SM",\
               fontsize=16,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()
axs[0].annotate(r'$\Lambda=$'+str(mass_scale)+r'TeV', (1800, 0.05),\
               fontsize=18,color="grey")

axs[0].annotate(r'Resummed $p_{T, veto} = 35$GeV', (660, 2*10**-12),\
               fontsize=15,color="grey")
bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].step(bin_centres, sm/(bin_widths18*3000), color='k', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2$ ', linewidth=0.7)

axs[0].fill_between(bin_centres, sm_min/(bin_widths18*3000), sm_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')


axs[0].step(bin_centres, ggnll_centre/(bin_widths18*3000), color='#FF8C00', where='mid', label=r'$|\mathcal{M}^{(gg)}_{\mathrm{SM}}|^2$', linewidth=0.7)

axs[0].fill_between(bin_centres, ggnll_min/(bin_widths18*3000), ggnll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(k52nll_centre*ggnll_centre)/(bin_widths18*3000), color='#FF8C00', linestyle="--", where='mid', label=r'$2|\mathcal{M}^{(gg)}_{\mathrm{SM}}||\mathcal{M}^{(8)}_5|$', linewidth=0.7)

axs[0].fill_between(bin_centres, k5gg_nll_min/(bin_widths18*3000), k5gg_nll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k5nll_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_5)|\ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k5nll_min)/(bin_widths18*3000), (2000**4)/((mass_scale*1000)**4)*abs(k5nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*k52nll_centre/(bin_widths18*3000), color='b', where='mid', label=r'$|\mathcal{M}^{(8)}_5|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*k52nll_min/(bin_widths18*3000), (2000**8)/((mass_scale*1000)**8)*k52nll_max/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')


axs[0].legend(loc="lower left", fontsize=10, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(0.9*10**-12, 1)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)


ratio_gg_nll=ggnll_centre/sm

err_gg_nll=ratio_gg_nll*((err_sm/sm)**2 + (((ggnll_max-ggnll_min)/2)/ggnll_centre)**2)**0.5

ratio_k5_nll=k5nll_centre/sm

err_k5_nll=ratio_k5_nll*((err_sm/sm)**2 + (((k5nll_max-k5nll_min)/2)/k5nll_centre)**2)**0.5

ratio_k52_nll=k52nll_centre/sm

err_k52_nll=ratio_k52_nll*((err_sm/sm)**2 + (((k52nll_max-k52nll_min)/2)/k52nll_centre)**2)**0.5

ratio_k5gg_nll=np.sqrt(k52nll_centre*ggnll_centre)/sm

err_k5gg_nll=ratio_k5gg_nll*((err_sm/sm)**2 + (((k5gg_nll_max-k5gg_nll_min)/2)/(np.sqrt(k52nll_centre*ggnll_centre)))**2)**0.5



axs[1].loglog()

axs[1].step(bin_centres, ratio_gg_nll, color='#FF8C00', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, ratio_gg_nll-err_gg_nll, ratio_gg_nll+err_gg_nll,
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k52_nll), color='#FF8C00', linestyle="--", where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k52_nll)-err_k5gg_nll), (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k52_nll)+err_k5gg_nll),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(ratio_k5_nll), color='b', linestyle="--", where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k5_nll)-abs(err_k5_nll)), (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k5_nll)+abs(err_k5_nll)),
                     color='b', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*abs(ratio_k52_nll), color='b', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*(ratio_k52_nll-err_k52_nll), (2000**8)/((mass_scale*1000)**8)*(ratio_k52_nll+err_k52_nll),
                     color='b', alpha=0.3, step='mid')
#axs[1].set_ylim(2*10**-4, 2)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].yaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=4))
#plt.tight_layout()
plt.savefig("figure_9e.pdf", bbox_inches='tight')

k6gg_nll_050050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050050*k62nll_050050050)
k6gg_nll_050050025=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050025*k62nll_050050025)
k6gg_nll_050050100=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050050100*k62nll_050050100)
k6gg_nll_025025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025025050*k62nll_025025050)
k6gg_nll_025050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_025050050*k62nll_025050050)
k6gg_nll_050025050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050025050*k62nll_050025050)
k6gg_nll_050100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_050100050*k62nll_050100050)
k6gg_nll_100050050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100050050*k62nll_100050050)
k6gg_nll_100100050=(2000**4)/((mass_scale*1000)**4)*np.sqrt(ggnll_100100050*k62nll_100100050)


k6gg_nll_min=[]
k6gg_nll_max=[]

for i in range(0, len(k6gg_nll_050050050)):
    values=[k6gg_nll_050050050[i], k6gg_nll_050050025[i], k6gg_nll_050050100[i], k6gg_nll_025025050[i], k6gg_nll_025050050[i], k6gg_nll_050025050[i], k6gg_nll_050100050[i], k6gg_nll_100050050[i], k6gg_nll_100100050[i]]
    k6gg_nll_min.append(np.min(values))
    k6gg_nll_max.append(np.max(values))

k6gg_nll_min=np.array(k6gg_nll_min)
k6gg_nll_max=np.array(k6gg_nll_max)



plt.figure(figsize=(16, 12.81),dpi=100)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"Operator 6 Comparison to \mathrm{SM} ATLAS 14TeV",\
#               fontsize=18,color="black")
axs[1].set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r"Ratio to SM",\
               fontsize=16,color="black")
#axs[0].xaxis.set_visible(False)
axs[0].loglog()
axs[0].annotate(r'$\Lambda=$'+str(mass_scale)+r'TeV', (1800, 0.05),\
               fontsize=18,color="grey")

axs[0].annotate(r'Resummed $p_{T, veto} = 35$GeV', (660, 2*10**-12),\
               fontsize=15,color="grey")
bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].step(bin_centres, sm/(bin_widths18*3000), color='k', where='mid', label=r'$|\mathcal{M}_{\mathrm{SM}}|^2$ ', linewidth=0.7)

axs[0].fill_between(bin_centres, sm_min/(bin_widths18*3000), sm_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')


axs[0].step(bin_centres, ggnll_centre/(bin_widths18*3000), color='#FF8C00', where='mid', label=r'$|\mathcal{M}^{(gg)}_{\mathrm{SM}}|^2$', linewidth=0.7)

axs[0].fill_between(bin_centres, ggnll_min/(bin_widths18*3000), ggnll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(k62nll_centre*ggnll_centre)/(bin_widths18*3000), color='#FF8C00', linestyle="--", where='mid', label=r'$2|\mathcal{M}^{(gg)}_{\mathrm{SM}}||\mathcal{M}^{(8)}_6|$', linewidth=0.7)

axs[0].fill_between(bin_centres, k6gg_nll_min/(bin_widths18*3000), k6gg_nll_max/(bin_widths18*3000),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k6nll_centre)/(bin_widths18*3000), color='b', linestyle="--", where='mid', label=r'$2|\mathrm{Re}(\mathcal{M}^{(gg)}_{\mathrm{SM}}\mathcal{M}^{(8)*}_6)|\ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(k6nll_min)/(bin_widths18*3000), (2000**4)/((mass_scale*1000)**4)*abs(k6nll_max)/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')

axs[0].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*k62nll_centre/(bin_widths18*3000), color='b', where='mid', label=r'$|\mathcal{M}^{(8)}_6|^2\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $', linewidth=0.7)

axs[0].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*k62nll_min/(bin_widths18*3000), (2000**8)/((mass_scale*1000)**8)*k62nll_max/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')


axs[0].legend(loc="lower left", fontsize=10, columnspacing=0.8)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(0.9*10**-12, 1)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)


ratio_gg_nll=ggnll_centre/sm

err_gg_nll=ratio_gg_nll*((err_sm/sm)**2 + (((ggnll_max-ggnll_min)/2)/ggnll_centre)**2)**0.5

ratio_k6_nll=k6nll_centre/sm

err_k6_nll=ratio_k6_nll*((err_sm/sm)**2 + (((k6nll_max-k6nll_min)/2)/k6nll_centre)**2)**0.5

ratio_k62_nll=k62nll_centre/sm

err_k62_nll=ratio_k62_nll*((err_sm/sm)**2 + (((k62nll_max-k62nll_min)/2)/k62nll_centre)**2)**0.5

ratio_k6gg_nll=np.sqrt(k62nll_centre*ggnll_centre)/sm

err_k6gg_nll=ratio_k6gg_nll*((err_sm/sm)**2 + (((k6gg_nll_max-k6gg_nll_min)/2)/(np.sqrt(k62nll_centre*ggnll_centre)))**2)**0.5



axs[1].loglog()

axs[1].step(bin_centres, ratio_gg_nll, color='#FF8C00', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, ratio_gg_nll-err_gg_nll, ratio_gg_nll+err_gg_nll,
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k62_nll), color='#FF8C00', linestyle="--", where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k62_nll)-err_k6gg_nll), (2000**4)/((mass_scale*1000)**4)*(np.sqrt(ratio_gg_nll)*np.sqrt(ratio_k62_nll)+err_k6gg_nll),
                     color='#FF8C00', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**4)/((mass_scale*1000)**4)*abs(ratio_k6_nll), color='b', linestyle="--", where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k6_nll)-abs(err_k6_nll)), (2000**4)/((mass_scale*1000)**4)*(abs(ratio_k6_nll)+abs(err_k6_nll)),
                     color='b', alpha=0.3, step='mid')

axs[1].step(bin_centres, (2000**8)/((mass_scale*1000)**8)*abs(ratio_k62_nll), color='b', where='mid', linewidth=0.7)

axs[1].fill_between(bin_centres, (2000**8)/((mass_scale*1000)**8)*(ratio_k62_nll-err_k62_nll), (2000**8)/((mass_scale*1000)**8)*(ratio_k62_nll+err_k62_nll),
                     color='b', alpha=0.3, step='mid')
#axs[1].set_ylim(2*10**-4, 2)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[1].yaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=4))
#plt.tight_layout()
plt.savefig("figure_9f.pdf", bbox_inches='tight')

