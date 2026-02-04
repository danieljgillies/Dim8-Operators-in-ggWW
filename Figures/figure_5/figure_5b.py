import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '..')

from plot_funcs import round_to_5, array_for_plot

bins=round_to_5(np.logspace(2.1384012462059836, np.log10(4000), 19))
bin_widths=bins[1:]-bins[0:len(bins)-1]
bin_widths18=array_for_plot(bin_widths)


nnlonloew_noveto_100100=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.50MWW_mufac=0.50MWW.npy"))
nnlonloew_noveto_050050=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.25MWW_mufac=0.25MWW.npy"))
nnlonloew_noveto_050100=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.25MWW_mufac=0.50MWW.npy"))
nnlonloew_noveto_100050=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.50MWW_mufac=0.25MWW.npy",))
nnlonloew_noveto_100200=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.50MWW_mufac=1.00MWW.npy"))
nnlonloew_noveto_200100=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=1.00MWW_mufac=0.50MWW.npy"))
nnlonloew_noveto_200200=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=1.00MWW_mufac=1.00MWW.npy"))



nlophoton_noveto_1=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=0.50MWW.npy"))
nlophoton_noveto_05=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=0.25MWW.npy"))
nlophoton_noveto_2=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=1.00MWW.npy"))

nlophoton_noveto_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_centre.npy"))
nlophoton_noveto_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_min.npy"))
nlophoton_noveto_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_max.npy"))

gglo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_centre.npy"))
gglo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_max.npy"))
gglo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_min.npy"))


gglo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.50MWW_mufac=0.50MWW.npy"))
gglo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
gglo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.25MWW_mufac=0.50MWW.npy"))
gglo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.50MWW_mufac=0.25MWW.npy"))
gglo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.50MWW_mufac=1.00MWW.npy"))
gglo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=1.00MWW_mufac=0.50MWW.npy"))
gglo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=1.00MWW_mufac=1.00MWW.npy"))

nnlonloew_noveto_centre=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_centre.npy"))
nnlonloew_noveto_min=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_min.npy"))
nnlonloew_noveto_max=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_max.npy"))


sm=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_centre.npy"))
sm_min=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_min.npy"))
sm_max=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_max.npy"))


#To calculate the ratios of the fixed order calculations we find the ratios for every $\mu_r$ and $\mu_f$ and find the maximum and minimum values.

qqratsm_050050=nnlonloew_noveto_100100/(nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_1)
qqratsm_025025=nnlonloew_noveto_050050/(nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_05)
qqratsm_025050=nnlonloew_noveto_050100/(nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_1)
qqratsm_050025=nnlonloew_noveto_100050/(nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_05)
qqratsm_050100=nnlonloew_noveto_100200/(nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_2)
qqratsm_100050=nnlonloew_noveto_200100/(nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_1)
qqratsm_100100=nnlonloew_noveto_200200/(nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_2)


qqratsm_min=[]
qqratsm_max=[]

for i in range(0, len(qqratsm_050050)):
    values=[qqratsm_050050[i], qqratsm_025025[i], qqratsm_025050[i], qqratsm_050025[i], qqratsm_050100[i], qqratsm_100050[i], qqratsm_100100[i]]
    qqratsm_min.append(np.min(values))
    qqratsm_max.append(np.max(values))

qqratsm_min=np.array(qqratsm_min)
qqratsm_max=np.array(qqratsm_max)

qqratsm=qqratsm_050050


ggratsm_050050=gglo_050050/(nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_1)
ggratsm_025025=gglo_050050/(nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_05)
ggratsm_025050=gglo_050050/(nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_1)
ggratsm_050025=gglo_050050/(nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_05)
ggratsm_050100=gglo_050050/(nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_2)
ggratsm_100050=gglo_050050/(nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_1)
ggratsm_100100=gglo_050050/(nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_2)


ggratsm_min=[]
ggratsm_max=[]

for i in range(0, len(ggratsm_050050)):
    values=[ggratsm_050050[i], ggratsm_025025[i], ggratsm_025050[i], ggratsm_050025[i], ggratsm_050100[i], ggratsm_100050[i], ggratsm_100100[i]]
    ggratsm_min.append(np.min(values))
    ggratsm_max.append(np.max(values))

ggratsm_min=np.array(ggratsm_min)
ggratsm_max=np.array(ggratsm_max)

ggratsm=ggratsm_050050



photonratsm_050050=nlophoton_noveto_1/(nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_1)
photonratsm_025025=nlophoton_noveto_05/(nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_05)
photonratsm_025050=nlophoton_noveto_1/(nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_1)
photonratsm_050025=nlophoton_noveto_05/(nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_05)
photonratsm_050100=nlophoton_noveto_2/(nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_2)
photonratsm_100050=nlophoton_noveto_1/(nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_1)
photonratsm_100100=nlophoton_noveto_2/(nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_2)


photonratsm_min=[]
photonratsm_max=[]

for i in range(0, len(photonratsm_050050)):
    values=[photonratsm_050050[i], photonratsm_025025[i], photonratsm_025050[i], photonratsm_050025[i], photonratsm_050100[i], photonratsm_100050[i], photonratsm_100100[i]]
    photonratsm_min.append(np.min(values))
    photonratsm_max.append(np.max(values))

photonratsm_min=np.array(photonratsm_min)
photonratsm_max=np.array(photonratsm_max)

photonratsm=photonratsm_050050




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
axs[0].annotate(r'$\sqrt{s} = 14$TeV, $\, p p\, \to\, e^{\pm}\nu\mu^{\mp}\nu, $ No Jet Veto', 
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

axs[0].step(bin_centres, sm/(bin_widths18*3000), color='k', where='mid', linewidth=0.7)
axs[0].step(bin_centres, -sm/(bin_widths18*3000), color='k', where='mid', label=r'$qq$+$gg$+$\gamma\gamma$')

axs[0].fill_between(bin_centres, sm_min/(bin_widths18*3000), sm_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')


axs[0].step(bin_centres, nnlonloew_noveto_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', linewidth=0.7)
axs[0].step(bin_centres, -nnlonloew_noveto_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', label=r'$qq$-only (NNLO$_{\mathrm{QCD}}\times$NLO$_{\mathrm{EW}}$) ')

axs[0].fill_between(bin_centres, nnlonloew_noveto_min/(bin_widths18*3000), nnlonloew_noveto_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')

axs[0].step(bin_centres, nlophoton_noveto_centre/(bin_widths18*3000), color='y', where='mid', linewidth=0.7)
axs[0].step(bin_centres, -nlophoton_noveto_centre/(bin_widths18*3000), color='y', where='mid', label=r'$\gamma\gamma $-only (NLO)')

axs[0].fill_between(bin_centres, nlophoton_noveto_min/(bin_widths18*3000), nlophoton_noveto_max/(bin_widths18*3000),
                     color='y', alpha=0.3, step='mid')


axs[0].step(bin_centres, gglo_centre/(bin_widths18*3000), color='b', where='mid', linewidth=0.7)
axs[0].step(bin_centres, -gglo_centre/(bin_widths18*3000), color='b', where='mid', label=r'$gg$-only (LO)')

axs[0].fill_between(bin_centres, gglo_min/(bin_widths18*3000), gglo_max/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')





axs[0].legend(loc="lower left", fontsize=11, frameon=False)
axs[0].set_xlim(137.5312, 4000)
axs[0].set_ylim(2*10**-11, 4*10**3)




axs[1].step(bin_centres, 100*ggratsm, color='b', where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, 100*ggratsm_min, 100*ggratsm_max,
                     color='b', alpha=0.5, step='mid')






axs[1].step(bin_centres, 100*photonratsm, color='y', where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, 100*photonratsm_min, 100*photonratsm_max,
                     color='y', alpha=0.5, step='mid')




axs[1].step(bin_centres, 100*qqratsm, color='k', where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, 100*qqratsm_min, 100*qqratsm_max,
                     color='k', alpha=0.5, step='mid')


axs[1].loglog()
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)
axs[1].set_ylim(10**-2, 150)
axs[1].set_yticks([10**-2, 10**-1, 1, 10, 100])
axs[1].set_yticklabels(["0.01", "0.1", "1", "10", "100"])
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

plt.savefig("figure_5b.pdf", bbox_inches='tight')