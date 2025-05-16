import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(1, '..')

from plot_funcs import array_for_plot


bins15 = [0, 55, 75, 85, 95, 110, 125, 140, 160, 185, 220, 280, 380, 600, 1500]
bin_sizes15 = np.array([20, 20, 10, 10, 15, 15, 15, 20, 25, 35, 60, 100, 220, 900, 900])


#Load Atlas data
atlas=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas.npy"))
atlas_err= 36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas_err.npy"))

#Load predictions at Lambda=2Tev
nnllnnlonloew_ggphoton_centre=36.1*2*array_for_plot(np.load("../SM_Construction/mll_13TeV_veto35_sm_centre.npy"))
nnllnnlonloew_ggphoton_min=36.1*2*array_for_plot(np.load("../SM_Construction/mll_13TeV_veto35_sm_min.npy"))
nnllnnlonloew_ggphoton_max=36.1*2*array_for_plot(np.load("../SM_Construction/mll_13TeV_veto35_sm_max.npy"))



mcfm_nll_kg2=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_centre.npy"))
mcfm_nll_kg2_min=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_min.npy"))
mcfm_nll_kg2_max=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_max.npy"))


mcfm_nll_kg=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_centre.npy"))
mcfm_nll_kg_min=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_min.npy"))
mcfm_nll_kg_max=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHSMint_nll_qcd_max.npy"))


mcfm_nll_kt2=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OTHsq_nll_qcd_centre.npy"))
mcfm_nll_kt2_min=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OTHsq_nll_qcd_min.npy"))
mcfm_nll_kt2_max=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OTHsq_nll_qcd_max.npy"))


mcfm_nll_kgkt=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHOTHint_nll_qcd_centre.npy"))
mcfm_nll_kgkt_min=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHOTHint_nll_qcd_min.npy"))
mcfm_nll_kgkt_max=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHOTHint_nll_qcd_max.npy"))


mcfm_nll_kt=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OTHSMint_nll_qcd_centre.npy"))
mcfm_nll_kt_min=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OTHSMint_nll_qcd_min.npy"))
mcfm_nll_kt_max=36.1*2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OTHSMint_nll_qcd_max.npy"))


#We want to see how well the current constraints fit with the tails of WW data. To do this we convert the kappa values into \
# mass scales (assuming c=1) and plot the corresponding predictions.

mass_scale_pos=7.291 #(kg=+0.4)
mass_scale_neg=5.953 #(kg=-0.6)
mass_scale_018=14.58 #(kg=-0.18)
mass_scale_002=32.61 #(kg=-0.02)
mass_scale_opt=14.58 #(kg=0.1)
kt_max=0.39
kt_min=-0.19


plt.figure(figsize=(20, 15),dpi=100)
fig, axs = plt.subplots(3, 1, gridspec_kw={'height_ratios': [4, 1, 1]}, sharex=True)
axs[2].set_xlabel(r"$M_{e\mu}$ $[GeV]$ ",\
               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r"$\frac{\mathrm{Models}}{\mathrm{Data}}$",\
               fontsize=12,color="black")
axs[2].set_ylabel(r"$\frac{\mathrm{Models}}{\mathrm{SM}}$",\
               fontsize=12,color="black")



axs[0].loglog()

axs[0].step(bins15, atlas/bin_sizes15, color='grey', where="post", linewidth=1, label="ATLAS Data")
axs[0].fill_between(bins15, (atlas-atlas_err)/bin_sizes15, (atlas+atlas_err)/bin_sizes15, color='grey', alpha=0.3, step="post")

axs[0].step(bins15, nnllnnlonloew_ggphoton_centre/bin_sizes15, color='k', where="post", label=r"Standard Model ($\delta \kappa_t = 0$, $\kappa_g=0$)", linewidth=1)
axs[0].fill_between(bins15, nnllnnlonloew_ggphoton_min/bin_sizes15, nnllnnlonloew_ggphoton_max/bin_sizes15, color='k', alpha=0.3, step="post")


#The four extreme models based on the error bars.
model_1=0.39*mcfm_nll_kt + (0.39**2)*mcfm_nll_kt2 - ((2**2)/(mass_scale_neg**2))*mcfm_nll_kg + ((2**4)/(mass_scale_neg**4))*mcfm_nll_kg2 -0.39*((2**2)/(mass_scale_neg**2))*mcfm_nll_kgkt
model_2=0.39*mcfm_nll_kt + (0.39**2)*mcfm_nll_kt2 - ((2**2)/(mass_scale_018**2))*mcfm_nll_kg + ((2**4)/(mass_scale_018**4))*mcfm_nll_kg2 -0.39*((2**2)/(mass_scale_018**2))*mcfm_nll_kgkt
model_3=-0.19*mcfm_nll_kt + (0.19**2)*mcfm_nll_kt2 - ((2**2)/(mass_scale_002**2))*mcfm_nll_kg + ((2**4)/(mass_scale_002**4))*mcfm_nll_kg2 +0.19*((2**2)/(mass_scale_002**2))*mcfm_nll_kgkt
model_4=-0.19*mcfm_nll_kt + (0.19**2)*mcfm_nll_kt2 + ((2**2)/(mass_scale_pos**2))*mcfm_nll_kg + ((2**4)/(mass_scale_pos**4))*mcfm_nll_kg2 -0.19*((2**2)/(mass_scale_pos**2))*mcfm_nll_kgkt

#The "best fit" model which is not the SM.
model_opt=0.09*mcfm_nll_kt + (0.09**2)*mcfm_nll_kt2 - ((2**2)/(mass_scale_opt**2))*mcfm_nll_kg + ((2**4)/(mass_scale_opt**4))*mcfm_nll_kg2 -0.09*((2**2)/(mass_scale_opt**2))*mcfm_nll_kgkt



axs[0].step(bins15, (nnllnnlonloew_ggphoton_centre + model_opt)/bin_sizes15, where="post", label=r"Best Fit ($\delta \kappa_t = 0.09$, $\kappa_g=-0.1$)", linewidth=1)


axs[0].step(bins15, (nnllnnlonloew_ggphoton_centre + model_1)/bin_sizes15, where="post", label=r"($\delta \kappa_t = 0.39$, $\kappa_g=-0.60$)", linewidth=1)
axs[0].step(bins15, (nnllnnlonloew_ggphoton_centre + model_2)/bin_sizes15, where="post", label=r"($\delta \kappa_t = 0.39$, $\kappa_g=-0.18$)", linewidth=1)
axs[0].step(bins15, (nnllnnlonloew_ggphoton_centre + model_3)/bin_sizes15, where="post", label=r"($\delta \kappa_t = -0.19$, $\kappa_g=-0.02$)", linewidth=1)
axs[0].step(bins15, (nnllnnlonloew_ggphoton_centre + model_4)/bin_sizes15, where="post", label=r"($\delta \kappa_t = -0.19$, $\kappa_g=0.40$)", linewidth=1)

axs[0].legend(loc="lower left", fontsize=9, ncol=1)

axs[0].set_ylim(10**-4, 210)
axs[0].set_xlim(55, 1500)
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True, bottom=False)
axs[2].tick_params(which="both", labelsize=13, direction='in', right=True)

ratio_sm_min=(nnllnnlonloew_ggphoton_min)/(atlas)
ratio_sm_max=(nnllnnlonloew_ggphoton_max)/(atlas)

#We find the ratios.
ratio_1=(nnllnnlonloew_ggphoton_centre + model_1)/(atlas)
ratio_2=(nnllnnlonloew_ggphoton_centre + model_2)/(atlas)
ratio_3=(nnllnnlonloew_ggphoton_centre + model_3)/(atlas)
ratio_4=(nnllnnlonloew_ggphoton_centre + model_4)/(atlas)
ratio_opt=(nnllnnlonloew_ggphoton_centre + model_opt)/(atlas)

axs[1].fill_between(bins15, ratio_sm_min, ratio_sm_max, color='k', alpha=0.3, step="post")


axs[1].step(bins15, atlas/(atlas), color='grey', where="post")
axs[1].fill_between(bins15, (atlas-atlas_err)/(atlas), (atlas+atlas_err)/(atlas), color='grey', alpha=0.3, step="post")

axs[1].step(bins15, ratio_1, where="post", linewidth=1)
axs[1].step(bins15, ratio_2, where="post", linewidth=1)
axs[1].step(bins15, ratio_3, where="post", linewidth=1)
axs[1].step(bins15, ratio_4, where="post", linewidth=1)
axs[1].step(bins15, ratio_opt, where="post", linewidth=1)

axs[2].set_ylim(1-0.01, 1+0.01)

axs[2].step(bins15, (atlas/nnllnnlonloew_ggphoton_centre)*ratio_1, where="post", linewidth=1)
axs[2].step(bins15, (atlas/nnllnnlonloew_ggphoton_centre)*ratio_2, where="post", linewidth=1)
axs[2].step(bins15, (atlas/nnllnnlonloew_ggphoton_centre)*ratio_3, where="post", linewidth=1)
axs[2].step(bins15, (atlas/nnllnnlonloew_ggphoton_centre)*ratio_4, where="post", linewidth=1)
axs[2].step(bins15, (atlas/nnllnnlonloew_ggphoton_centre)*ratio_opt, where="post", linewidth=1)


plt.tight_layout()
plt.savefig("figure_10.pdf")

