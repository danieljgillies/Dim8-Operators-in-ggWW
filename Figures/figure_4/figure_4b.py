import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '..')

from plot_funcs import round_to_5, array_for_plot


bins=round_to_5(np.logspace(2.1384012462059836, np.log10(4000), 19))
bin_widths=bins[1:]-bins[0:len(bins)-1]
bin_widths18=array_for_plot(bin_widths)

#qq QCD only calculation.
nnllnnlo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_centre.npy"))
nnllnnlo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_min.npy"))
nnllnnlo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_max.npy"))

#qq QCD cross EW calculation.
nnllnnlonloew_centre=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_centre.npy"))
nnllnnlonloew_min=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_min.npy"))
nnllnnlonloew_max=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_max.npy"))

#nlo aa and aq pieces.
nlophoton_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_centre.npy"))
nlophoton_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_min.npy"))
nlophoton_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_max.npy"))


nnllnnlonloew_err=(nnllnnlonloew_max-nnllnnlonloew_min)/2
nlophoton_err=(nlophoton_max-nlophoton_min)/2

#Because MATRIX does not give a break down in terms of $\mu_f$ and $\mu_r$ for the resummed predictions we can only add errors in quadrature.
total_err=(nnllnnlonloew_err**2 + nlophoton_err**2)**0.5

plt.figure(figsize=(16, 12),dpi=1000)

fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [2, 1]}, sharex=True)

axs[1].set_xlabel(r"$M_{e\mu}$ [GeV] ",\
               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r" Ratio$_{\mathrm{QCD}}$ - 1",\
               fontsize=16,color="black")



axs[0].loglog()

axs[0].annotate(r'HL-LHC $\ $(ATLAS Cuts)', 
            xy=(137.5312+3, 10**4), 
            fontsize=15,
            fontweight="bold",
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
axs[0].annotate(r'$\sqrt{s} = 14$TeV, $\, p p\, \to\, e^{\pm}\nu\mu^{\mp}\nu$', 
            xy=(137.5312+3, 0.8*10**3), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
axs[0].annotate(r'NNPDF31_nnlo_as_0118_luxqed_nf_4', 
            xy=(137.5312+3, 0.64*10**2), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')

bin_centres=(bins[0:len(bins)-1] + bins[1:])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].step(bin_centres, nnllnnlo_centre/(bin_widths18*3000), color='k', where='mid', linewidth=0.5)
axs[0].step(bin_centres, -nnllnnlo_centre/(bin_widths18*3000), color='k', where='mid', label=r'NNLL+NNLO$_{\mathrm{QCD}}$')

axs[0].fill_between(bin_centres, nnllnnlo_min/(bin_widths18*3000), nnllnnlo_max/(bin_widths18*3000),
                     color='k', alpha=0.5, step='mid')


axs[0].step(bin_centres, nnllnnlonloew_centre/(bin_widths18*3000), color='b', where='mid', linewidth=0.5)
axs[0].step(bin_centres, -nnllnnlonloew_centre/(bin_widths18*3000), color='b', where='mid', label=r'NNLL+NNLO$_{\mathrm{QCD}}\times$NLO$_{\mathrm{EW}}$')

axs[0].fill_between(bin_centres, nnllnnlonloew_min/(bin_widths18*3000), nnllnnlonloew_max/(bin_widths18*3000),
                     color='b', alpha=0.5, step='mid')



axs[0].step(bin_centres, (nnllnnlonloew_centre+nlophoton_centre)/(bin_widths18*3000), color='orange', where='mid', linewidth=0.5)
axs[0].step(bin_centres, -(nnllnnlonloew_centre+nlophoton_centre)/(bin_widths18*3000), color='orange', where='mid', label=r'NNLL+NNLO$_{\mathrm{QCD}}\times$NLO$_{\mathrm{EW}}$ + NLO $\gamma\gamma$')

axs[0].fill_between(bin_centres, (nnllnnlonloew_centre+nlophoton_centre-total_err)/(bin_widths18*3000), (nnllnnlonloew_centre+nlophoton_centre+total_err)/(bin_widths18*3000),
                     color='orange', alpha=0.5, step='mid')

axs[0].legend(loc="lower left", fontsize=11, frameon=False)
axs[0].set_xlim(137.5312, 4000)
axs[0].set_ylim(10**-8, 2*10**4)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])


ratio_nnllnnlo=nnllnnlo_centre/nnllnnlo_centre
ratio_nnllnnlo_min=nnllnnlo_min/nnllnnlo_centre
ratio_nnllnnlo_max=nnllnnlo_max/nnllnnlo_centre

ratio_nnllnnloew=nnllnnlonloew_centre/nnllnnlo_centre
ratio_nnllnnloew_min=nnllnnlonloew_min/nnllnnlo_centre
ratio_nnllnnloew_max=nnllnnlonloew_max/nnllnnlo_centre


ratio_nnllnnloewwphoton=(nnllnnlonloew_centre+nlophoton_centre)/nnllnnlo_centre
ratio_nnllnnloewwphoton_min=(nnllnnlonloew_centre+nlophoton_centre-total_err)/nnllnnlo_centre
ratio_nnllnnloewwphoton_max=(nnllnnlonloew_centre+nlophoton_centre+total_err)/nnllnnlo_centre

axs[1].step(bin_centres, ratio_nnllnnlo-1, color='k', where='mid')
axs[1].fill_between(bin_centres, ratio_nnllnnlo_min-1, ratio_nnllnnlo_max-1,
                     color='k', alpha=0.5, step='mid')

axs[1].step(bin_centres, ratio_nnllnnloew-1, color='b', where='mid')
axs[1].fill_between(bin_centres, ratio_nnllnnloew_min-1, ratio_nnllnnloew_max-1,
                     color='b', alpha=0.5, step='mid')

axs[1].step(bin_centres, ratio_nnllnnloewwphoton-1, color='orange', where='mid')
axs[1].fill_between(bin_centres, ratio_nnllnnloewwphoton_min-1, ratio_nnllnnloewwphoton_max-1,
                     color='orange', alpha=0.5, step='mid')


axs[1].set_ylim(-0.6, 0.12)
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

plt.savefig("figure_4b.pdf", bbox_inches='tight')

