import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.insert(1, '..')

from plot_funcs import array_for_plot


bin_sizes15 = np.array([20, 20, 10, 10, 15, 15, 15, 20, 25, 35, 60, 100, 220, 900, 900])
bins15 = [0, 55, 75, 85, 95, 110, 125, 140, 160, 185, 220, 280, 380, 600, 1500]



atlas15=2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas.npy"))
atlas15_err=2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas_err.npy"))


nnllnnlonloew_ggphoton_centre=2*array_for_plot(np.load("../SM_Construction/mll_13TeV_veto35_sm_centre.npy"))
nnllnnlonloew_ggphoton_min=2*array_for_plot(np.load("../SM_Construction/mll_13TeV_veto35_sm_min.npy"))
nnllnnlonloew_ggphoton_max=2*array_for_plot(np.load("../SM_Construction/mll_13TeV_veto35_sm_max.npy"))



plt.figure(figsize=(16, 12),dpi=100)

fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [2, 1]}, sharex=True)

axs[1].set_xlabel(r"$M_{e\mu}$ [GeV] ",\
               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r" Theory / Data",\
               fontsize=13,color="black")

axs[0].annotate(r'$\sqrt{s} = 13$TeV, $36.1$fb$^{-1}$', 
            xy=(56,  1.2*4*10**1), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
axs[0].annotate(r'$\, p p\, \to\, e^{\pm}\nu\mu^{\mp}\nu, $', 
            xy=(56, 1.7*10**1), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')

axs[0].step(bins15, atlas15/bin_sizes15, color='grey', label='ATLAS Data 2019', where="post", linewidth=1)
axs[0].fill_between(bins15, (atlas15-atlas15_err)/bin_sizes15, (atlas15+atlas15_err)/bin_sizes15,
                     color='grey', alpha=0.5, step="post")


axs[0].step(bins15, nnllnnlonloew_ggphoton_centre/bin_sizes15, color='b', label=r'$qq$ (NNLO+NNLL$_{\mathrm{QCD}}\times$NLO$_{\mathrm{EW}}$), $\gamma\gamma$ (NLO), $gg$ (NLL)', where="post", linewidth=1)
axs[0].fill_between(bins15, nnllnnlonloew_ggphoton_min/bin_sizes15, nnllnnlonloew_ggphoton_max/bin_sizes15,
                     color='b', alpha=0.5, step="post")



axs[0].semilogy()
leg = axs[0].legend(loc="lower left", fontsize=11, frameon=False, labelcolor="k")

for t in leg.texts:
    t.set_alpha(0.6)

axs[0].set_xlim(55, 1500)
axs[0].set_ylim(0.75*10**-4, 80)


ratio_matrix_all=(nnllnnlonloew_ggphoton_centre)/(atlas15)
ratio_matrix_all_min=(nnllnnlonloew_ggphoton_min)/(atlas15)
ratio_matrix_all_max=(nnllnnlonloew_ggphoton_max)/(atlas15)


axs[1].step(bins15, atlas15/(atlas15) , color='grey', where="post")
axs[1].fill_between(bins15, (atlas15-atlas15_err)/(atlas15), (atlas15+atlas15_err)/(atlas15), color='grey', alpha=0.3, step="post")

axs[1].step(bins15, ratio_matrix_all, color='b', where="post")

axs[1].fill_between(bins15, ratio_matrix_all_min, ratio_matrix_all_max,
                     color='b', alpha=0.5, step="post")                     
axs[0].set_xlim(55, 1500)
axs[0].loglog()
axs[1].set_ylim(0.6, 1.4)

axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)
plt.subplots_adjust(hspace=0.1)

plt.savefig("figure_6.pdf", bbox_inches='tight')

