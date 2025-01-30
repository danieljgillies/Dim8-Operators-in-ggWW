import numpy as np
import matplotlib.pyplot as plt
from math import log10, floor


def round_to_5(x):
    rounded=[]
    for i in range(len(x)):
        rounded.append(np.round(x[i], 6-int(floor(log10(abs(x[i]))))))
    return np.array(rounded)

def array_for_plot(a):
    return np.concatenate((np.array([a[0]]), a, np.array([a[len(a)-1]])))

bins=round_to_5(np.logspace(np.log10(200), np.log10(4000), 17))
print(bins)
bin_widths=bins[1:17]-bins[0:16]
bin_widths18=np.array([41.1817, 41.1817, 49.6614, 59.8871, 72.2183, 87.0887, 105.021, 126.6458, 152.7232, 184.1698, 222.093, 267.823, 322.97, 389.473, 469.668, 566.377, 682.999, 682.999])

#MATRIX

nnllnnlo_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_centre.npy"))
nnllnnlo_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_min.npy"))
nnllnnlo_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_max.npy"))

print(nnllnnlo_centre/6000)

nnlo_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnlo_qcd_centre.npy"))
nnlo_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnlo_qcd_min.npy"))
nnlo_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnlo_qcd_max.npy"))

nnll_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnll_qcd_centre.npy"))
nnll_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnll_qcd_min.npy"))
nnll_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnll_qcd_max.npy"))





#from matplotlib.ticker import LogLocator
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
plt.figure(figsize=(16, 24),dpi=1000)

fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [2, 1]}, sharex=True)
#axs[0].set_title(r"MATRIX vs ATLAS",\
#               fontsize=18,color="black")
axs[1].set_xlabel(r"$M_{e\mu}$ [GeV] ",\
               fontsize=16,color="black")
#axs[0].set_ylabel(r"num_events",\
#               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r" Ratio$_{\mathrm{NNLO}}$ - 1",\
               fontsize=16,color="black")
#axs[0].xaxis.set_visible(False)


axs[0].loglog()

axs[0].annotate(r'HL-LHC $\ $(ATLAS Cuts)', 
            xy=(205, 10**4), 
            fontsize=15,
            fontweight="bold",
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
axs[0].annotate(r'$\sqrt{s} = 14$TeV, $\, q\bar{q}\, \to\, e^{\pm}\nu\mu^{\mp}\nu$', 
            xy=(205, 0.8*10**3), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
axs[0].annotate(r'NNPDF31_nnlo_as_0118_luxqed_nf_4', 
            xy=(205, 0.64*10**2), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].step(bin_centres, nnlo_centre/(bin_widths18*3000), color='k', where='mid', linewidth=0.5)
axs[0].step(bin_centres, -nnlo_centre/(bin_widths18*3000), color='k', where='mid', label='NNLO')

axs[0].fill_between(bin_centres, nnlo_min/(bin_widths18*3000), nnlo_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')

axs[0].step(bin_centres, nnllnnlo_centre/(bin_widths18*3000), color='b', where='mid', linewidth=0.5)
axs[0].step(bin_centres, -nnllnnlo_centre/(bin_widths18*3000), color='b', where='mid', label='NNLO+NNLL')

axs[0].fill_between(bin_centres, nnllnnlo_min/(bin_widths18*3000), nnllnnlo_max/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')

axs[0].step(bin_centres, nnll_centre/(bin_widths18*3000), color='r', where='mid', linewidth=0.5)
axs[0].step(bin_centres, -nnll_centre/(bin_widths18*3000), color='r', where='mid', label='NNLL')

axs[0].fill_between(bin_centres, nnll_min/(bin_widths18*3000), nnll_max/(bin_widths18*3000),
                     color='r', alpha=0.3, step='mid')

axs[0].legend(loc="upper right", fontsize=11, frameon=False)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(10**-8, 2*10**4)


axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)


ratio_nnllnnlo=nnllnnlo_centre/nnlo_centre
ratio_nnllnnlo_min=nnllnnlo_min/nnlo_centre
ratio_nnllnnlo_max=nnllnnlo_max/nnlo_centre

ratio_nnlo=nnlo_centre/nnlo_centre
ratio_nnlo_min=nnlo_min/nnlo_centre
ratio_nnlo_max=nnlo_max/nnlo_centre

ratio_nnll=nnll_centre/nnlo_centre
ratio_nnll_min=nnll_min/nnlo_centre
ratio_nnll_max=nnll_max/nnlo_centre

axs[1].step(bin_centres, ratio_nnlo-1, color='k', where='mid')
axs[1].fill_between(bin_centres, ratio_nnlo_min-1, ratio_nnlo_max-1,
                     color='k', alpha=0.5, step='mid')

axs[1].step(bin_centres, ratio_nnllnnlo-1, color='b', where='mid')
axs[1].fill_between(bin_centres, ratio_nnllnnlo_min-1, ratio_nnllnnlo_max-1,
                     color='b', alpha=0.3, step='mid')

axs[1].step(bin_centres, ratio_nnll-1, color='r', where='mid')
axs[1].fill_between(bin_centres, ratio_nnll_min-1, ratio_nnll_max-1,
                     color='r', alpha=0.3, step='mid')

axs[1].set_ylim(-0.1, 0.1)
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

#plt.tight_layout()
plt.savefig("figure_3b.pdf", bbox_inches='tight')

