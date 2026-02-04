import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '..')

from plot_funcs import round_to_5, array_for_plot

bins=round_to_5(np.logspace(2.1384012462059836, np.log10(4000), 19))
bin_widths=bins[1:]-bins[0:len(bins)-1]
bin_widths18=array_for_plot(bin_widths)

nnllnnlonloew_centre=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_centre.npy"))
nnllnnlonloew_min=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_min.npy"))
nnllnnlonloew_max=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_max.npy"))


nlophoton_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_centre.npy"))
nlophoton_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_min.npy"))
nlophoton_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gamgam_nlo_max.npy"))


ggnll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_centre.npy"))
ggnll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_min.npy"))
ggnll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_max.npy"))




ggnll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=0.50MWW.npy"))
ggnll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=0.25MWW.npy"))
ggnll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.50MWW_mufac=0.50MWW__muresum=1.00MWW.npy"))
ggnll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.50MWW.npy"))
ggnll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.50MWW__muresum=0.50MWW.npy"))
ggnll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.50MWW_mufac=0.25MWW__muresum=0.50MWW.npy"))
ggnll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.50MWW_mufac=1.00MWW__muresum=0.50MWW.npy"))
ggnll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.00MWW_mufac=0.50MWW__muresum=0.50MWW.npy"))
ggnll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.00MWW_mufac=1.00MWW__muresum=0.50MWW.npy"))


sm=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_centre.npy"))
sm_min=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_min.npy"))
sm_max=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_max.npy"))



err_sm=(sm_max-sm_min)/2





plt.figure(figsize=(16, 12),dpi=1000)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)

axs[1].set_xlabel(r"$M_{e\mu}$ [GeV]",\
               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{M_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r"$\%$ Contribution",\
               fontsize=16,color="black")

axs[0].loglog()


axs[0].annotate(r'HL-LHC $\ $(ATLAS Cuts)', 
            xy=(205,  2*10**3), 
            fontsize=15,
            fontweight="bold",
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
axs[0].annotate(r'$\sqrt{s} = 14$TeV, $\, p p\, \to\, e^{\pm}\nu\mu^{\mp}\nu$,  $p_{T, \mathrm{veto}}=35 \mathrm{GeV}$' , 
            xy=(205,  2*0.7*10**2), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
axs[0].annotate(r'NNPDF31_nnlo_as_0118_luxqed_nf_4', 
            xy=(205,  2*0.49*10**1), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
bin_centres=(bins[0:len(bins)-1] + bins[1:])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].step(bin_centres, nnllnnlonloew_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', linewidth=0.7)
axs[0].step(bin_centres, -nnllnnlonloew_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', label=r'$qq$-only (NNLO+NNLL$_{\mathrm{QCD}}\times$NLO$_{\mathrm{EW}}$) ')

axs[0].fill_between(bin_centres, nnllnnlonloew_min/(bin_widths18*3000), nnllnnlonloew_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')


axs[0].step(bin_centres, ggnll_centre/(bin_widths18*3000), color='r', where='mid', linewidth=0.7)
axs[0].step(bin_centres, -ggnll_centre/(bin_widths18*3000), color='r', where='mid', label=r'$gg$-only (NLL)')


axs[0].fill_between(bin_centres, ggnll_min/(bin_widths18*3000), ggnll_max/(bin_widths18*3000),
                     color='r', alpha=0.3, step='mid')



axs[0].legend(loc="lower left", fontsize=11, frameon=False)
axs[0].set_xlim(137.5312, 4000)
axs[0].set_ylim(2*10**-11, 4*10**3)


#Since we do not have the breakdown in terms of $\mu_r$ and $\mu_f$ we can only add errors in quadrature for ratios.


err_gg=(ggnll_max-ggnll_min)/2


err=(ggnll_centre/sm)*((err_gg/ggnll_centre)**2 + (err_sm/sm)**2)**0.5


axs[1].step(bin_centres, 100*(ggnll_centre/sm), color='r', where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, 100*((ggnll_centre/sm)-err), 100*((ggnll_centre/sm)+err),
                     color='r', alpha=0.5, step='mid')



err_photon=(nlophoton_max-nlophoton_min)/2




err=(nlophoton_centre/sm)*((err_photon/nlophoton_centre)**2 + (err_sm/sm)**2)**0.5


err_nnllnnlonloew=(nnllnnlonloew_max-nnllnnlonloew_min)/2

err=(nnllnnlonloew_centre/sm)*((err_nnllnnlonloew/nnllnnlonloew_centre)**2 + (err_sm/sm)**2)**0.5



axs[1].step(bin_centres, 100*(nnllnnlonloew_centre/sm), color='k', where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, 100*((nnllnnlonloew_centre/sm)-err), 100*((nnllnnlonloew_centre/sm)+err),
                     color='k', alpha=0.5, step='mid')


axs[1].loglog()

axs[1].set_ylim(10**-2, 150)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)
axs[1].set_yticks([10**-2, 10**-1, 1, 10, 100])
axs[1].set_yticklabels(["0.01", "0.1", "1", "10", "100"])
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
plt.savefig("figure_5a_nophoton.pdf", bbox_inches='tight')

