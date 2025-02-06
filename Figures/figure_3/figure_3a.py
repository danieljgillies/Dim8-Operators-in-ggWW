import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '..')

from plot_funcs import round_to_5, array_for_plot

bins=round_to_5(np.logspace(np.log10(200), np.log10(4000), 17))
print(bins)
bin_widths=bins[1:17]-bins[0:16]
bin_widths18=np.array([41.1817, 41.1817, 49.6614, 59.8871, 72.2183, 87.0887, 105.021, 126.6458, 152.7232, 184.1698, 222.093, 267.823, 322.97, 389.473, 469.668, 566.377, 682.999, 682.999])

#MATRIX
nnllnnlo_centre=2*3000*np.array([49.88366, 49.88366, 35.548702, 23.46966, 14.662398, 8.7213963, 4.9908739, 2.7336378, 1.4332547, 0.72271728, 0.3491152, 0.15914543, 0.067571425, 0.027248822, 0.010141837, 0.0032816033, 0.00089527242, 0.00089527242])
nnllnnlo_min=2*3000*np.array([48.723877, 48.723877, 34.82143, 22.987784, 14.334426, 8.5186788, 4.8689836, 2.6648837, 1.3970087, 0.70216417, 0.33794254, 0.15368048, 0.065140109, 0.026183953, 0.009691631, 0.0031212358, 0.00084693901, 0.00084693901])
nnllnnlo_max=2*3000*np.array([50.986438, 50.986438, 36.54135, 24.266466, 15.250325, 9.1230448, 5.251348, 2.8922906, 1.5240861, 0.77222797, 0.37468104, 0.17135992, 0.07282327, 0.029432492, 0.010982673, 0.0035573716, 0.00097114182, 0.00097114182])

nnlo_centre=2*3000*np.array([49.958357, 49.958357, 35.620841, 23.542736, 14.730819, 8.7595365, 5.0188956, 2.7476173, 1.4362314, 0.72218307, 0.3477011, 0.15725656, 0.065513255, 0.026273348, 0.0097856938, 0.0031549028, 0.00085989836, 0.00085989836])
nnlo_min=2*3000*np.array([49.687782, 49.687782, 35.443455, 23.435688, 14.678217, 8.7248164, 4.9952256, 2.7347484, 1.4268275, 0.71620696, 0.34460889, 0.1552657, 0.064267103, 0.025662265, 0.009543065, 0.0030609084, 0.00082773183, 0.00082773183])
nnlo_max=2*3000*np.array([50.316845, 50.316845, 35.862253, 23.693857, 14.817711, 8.816925, 5.0548378, 2.7694196, 1.4510144, 0.73128299, 0.35276266, 0.1602693, 0.067252991, 0.027097544, 0.010112831, 0.0032749302, 0.00089674667, 0.00089674667])

nnll_centre=2*3000*np.array([48.189902, 48.189902, 34.072004, 22.299147, 13.84384, 8.2339296, 4.6975562, 2.5762933, 1.3589625, 0.68863676, 0.33381489, 0.15357043, 0.066687092, 0.027064456, 0.010017716, 0.0032602252, 0.00089378901, 0.00089378901])
nnll_min=2*3000*np.array([46.170887, 46.170887, 32.900587, 21.641987, 13.428335, 7.9827744, 4.552746, 2.4966301, 1.3119178, 0.6615626, 0.31919355, 0.14618531, 0.063189142, 0.025509373, 0.0093849224, 0.0030328885, 0.00082445639, 0.00082445639])
nnll_max=2*3000*np.array([50.108961, 50.108961, 35.60281, 23.46939, 14.671455, 8.7842169, 5.0433297, 2.7824592, 1.4757617, 0.75148374, 0.36578144, 0.1688137, 0.073469536, 0.029866625, 0.011066969, 0.0036036015, 0.00098833498, 0.00098833498])

nnllnnlo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_centre.npy"))
nnllnnlo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/b  _14TeV_veto35_sm_qq_nnllnnlo_qcd_min.npy"))
nnllnnlo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_max.npy"))

print(nnllnnlo_centre/6000)

nnlo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnlo_qcd_centre.npy"))
nnlo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnlo_qcd_min.npy"))
nnlo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnlo_qcd_max.npy"))

nnll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnll_qcd_centre.npy"))
nnll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnll_qcd_min.npy"))
nnll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnll_qcd_max.npy"))





#from matplotlib.ticker import LogLocator
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
plt.figure(figsize=(16, 24),dpi=1000)

fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [2, 1]}, sharex=True)
#axs[0].set_title(r"MATRIX vs ATLAS",\
#               fontsize=18,color="black")
axs[1].set_xlabel(r"$M_{WW}$ [GeV] ",\
               fontsize=16,color="black")
#axs[0].set_ylabel(r"num_events",\
#               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{WW}}$ $\left[\frac{\mathrm{fb}}{\mathrm{\mathrm{GeV}}}\right]$ ",\
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

axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
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

#plt.tight_layout()
plt.savefig("figure_3a.pdf", bbox_inches='tight')

