import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(1, '..')

from plot_funcs import round_to_5, array_for_plot


bins=round_to_5(np.logspace(2.1384012462059836, np.log10(4000), 19))
bin_widths=bins[1:]-bins[0:len(bins)-1]
bin_widths18=array_for_plot(bin_widths)



kg2nll_centre=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_centre.npy"))
kg2nll_min=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_min.npy"))
kg2nll_max=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_max.npy"))




k32nll_centre=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_centre.npy"))
k32nll_min=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_min.npy"))
k32nll_max=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_max.npy"))



k42nll_centre=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_centre.npy"))
k42nll_min=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_min.npy"))
k42nll_max=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O4sq_nll_qcd_max.npy"))



k52nll_centre=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_centre.npy"))
k52nll_min=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_min.npy"))
k52nll_max=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O5sq_nll_qcd_max.npy"))


k62nll_centre=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_centre.npy"))
k62nll_min=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_min.npy"))
k62nll_max=2*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O6sq_nll_qcd_max.npy"))










plt.figure(figsize=(16, 16),dpi=100)
fig, axs = plt.subplots(1, 1, gridspec_kw={'height_ratios': [5]}, sharex=True)


axs.set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")

axs.set_xlabel(r"$M_{e\mu}$ $\left[\mathrm{GeV}\right]$ ",\
               fontsize=16,color="black")

axs.loglog()

bin_centres=(bins[0:len(bins)-1] + bins[1:])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))


axs.annotate(r'$\Lambda=2$TeV', (1800, 0.01),\
               fontsize=18,color="#3b3b3b")

#Can add Dimension 6 operators if wanted.
#axs.step(bin_centres, kg2nll_centre/(bin_widths18), color='k', where='mid', label=r'$\frac{c_1}{\Lambda^4}|\mathcal{M}^{(6)}_{GH}|^2$', linewidth=0.9)

#axs.fill_between(bin_centres, kg2nll_min/(bin_widths18), kg2nll_max/(bin_widths18),
#                     color='k', alpha=0.2, step='mid')



#Operator 1 and 4 have the same squared distribution.
axs.step(bin_centres, k42nll_centre/(bin_widths18), color='b', where='mid', label=r'$\frac{c_{1/4}}{\Lambda^8}|\mathcal{M}^{(8)}_{1/4}|^2$', linewidth=0.9)

axs.fill_between(bin_centres, k42nll_min/(bin_widths18), k42nll_max/(bin_widths18),
                     color='b', alpha=0.2, step='mid')


#Operator 2 and 3 have the same squared distribution.
axs.step(bin_centres, k32nll_centre/(bin_widths18), color='g', where='mid', label=r'$\frac{c_{2/3}}{\Lambda^8}|\mathcal{M}^{(8)}_{2/3}|^2$', linewidth=0.9)

axs.fill_between(bin_centres, k32nll_min/(bin_widths18), k32nll_max/(bin_widths18),
                     color='g', alpha=0.2, step='mid')






axs.step(bin_centres, k52nll_centre/(bin_widths18), color='y', where='mid', label=r'$\frac{c_5}{\Lambda^8}|\mathcal{M}^{(8)}_5|^2$', linewidth=0.9)

axs.fill_between(bin_centres, k52nll_min/(bin_widths18), k52nll_max/(bin_widths18),
                     color='y', alpha=0.2, step='mid')



axs.step(bin_centres, k62nll_centre/(bin_widths18), color='r', where='mid', label=r'$\frac{c_6}{\Lambda^8}|\mathcal{M}^{(8)}_6|^2$', linewidth=0.9)

axs.fill_between(bin_centres, k62nll_min/(bin_widths18), k62nll_max/(bin_widths18),
                     color='r', alpha=0.2, step='mid')



axs.annotate(r'NLL $p_{T, veto} = 35$GeV', (1100, 2*10**-8),\
               fontsize=14,color="#3b3b3b")

axs.legend(loc="lower left", fontsize=11, columnspacing=0.8)
axs.set_xlim(137.5312, 4000)
axs.set_ylim(10**-8, 0.03)
axs.tick_params(which="both", labelsize=13, direction='in', right=True, top=True)
axs.set_xticks([200, 1000, 4000])
axs.set_xticklabels([r"$200$", r"$1000$", r"$4000$"])


plt.tight_layout(pad=-0.1)
plt.savefig("figure_8.pdf", bbox_inches='tight')
