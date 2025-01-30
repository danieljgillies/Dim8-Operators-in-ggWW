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










plt.figure(figsize=(16, 16),dpi=100)
fig, axs = plt.subplots(1, 1, gridspec_kw={'height_ratios': [5]}, sharex=True)
#axs[0].set_title(r"$\Lambda = 2TeV",\
#               fontsize=18,color="black")
#rec1 = plt.Rectangle((500,10**-11),3500,0.5, facecolor="#d3d3d3", 
#                     edgecolor="white", hatch=r"\\", zorder=0)
#axs.add_patch(rec1)

#axs.margins(0.3)
#axs.autoscale()


axs.set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")

axs.set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
               fontsize=16,color="black")

axs.loglog()

bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs.annotate(r'$\Lambda=2$TeV', (1800, 0.05),\
               fontsize=18,color="#3b3b3b")

#axs.annotate(r'EFT Breakdown', (510, 10**-7),\
#               fontsize=14,color="#3b3b3b")


#axs.step(bin_centres, k12nll_centre/(bin_widths18*3000), color='r', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_1|^2$', linewidth=0.9)

#axs.fill_between(bin_centres, k12nll_min/(bin_widths18*3000), k12nll_max/(bin_widths18*3000),
#                     color='r', alpha=0.2, step='mid')


#axs.step(bin_centres, k22nll_centre/(bin_widths18*3000), color='r', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_2|^2$', linewidth=0.9)

#axs.fill_between(bin_centres, k22nll_min/(bin_widths18*3000), k22nll_max/(bin_widths18*3000),
#                     color='r', alpha=0.2, step='mid')


axs.step(bin_centres, k42nll_centre/(bin_widths18*3000), color='b', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_{1/4}|^2$', linewidth=0.9)

axs.fill_between(bin_centres, k42nll_min/(bin_widths18*3000), k42nll_max/(bin_widths18*3000),
                     color='b', alpha=0.2, step='mid')


axs.step(bin_centres, k32nll_centre/(bin_widths18*3000), color='g', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_{2/3}|^2$', linewidth=0.9)

axs.fill_between(bin_centres, k32nll_min/(bin_widths18*3000), k32nll_max/(bin_widths18*3000),
                     color='g', alpha=0.2, step='mid')






axs.step(bin_centres, k52nll_centre/(bin_widths18*3000), color='y', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_5|^2$', linewidth=0.9)

axs.fill_between(bin_centres, k52nll_min/(bin_widths18*3000), k52nll_max/(bin_widths18*3000),
                     color='y', alpha=0.2, step='mid')



axs.step(bin_centres, k62nll_centre/(bin_widths18*3000), color='r', where='mid', label=r'$\frac{c_1}{\Lambda^8}|\mathcal{M}^{(8)}_6|^2$', linewidth=0.9)

axs.fill_between(bin_centres, k62nll_min/(bin_widths18*3000), k62nll_max/(bin_widths18*3000),
                     color='r', alpha=0.2, step='mid')

axs.annotate(r'NLL $p_{T, veto} = 35$GeV', (1200, 2*10**-8),\
               fontsize=14,color="#3b3b3b")

#axs.plot([500, 500], [0, 2], color="grey", linestyle="--")#, label=r'$M_{e\mu}^{\mathrm{Max}} = \frac{\Lambda}{4}$')
axs.legend(loc="lower left", fontsize=11, columnspacing=0.8)
axs.set_xlim(200, 4000)
axs.set_ylim(10**-8, 0.03)
axs.tick_params(which="both", labelsize=13, direction='in', right=True, top=True)
axs.set_xticks([200, 1000, 4000])
axs.set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

#axs[1].set_ylim(1*10**-4, 10**4)
#axs[1].set_yticks([10**-4, 1, 10**4])
plt.tight_layout(pad=-0.1)
plt.savefig("figure_8.pdf", bbox_inches='tight')
