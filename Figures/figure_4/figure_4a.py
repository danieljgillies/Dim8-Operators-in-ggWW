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
"""
nnllnnlo_centre=2*3000*np.array([49.88366, 49.88366, 35.548702, 23.46966, 14.662398, 8.7213963, 4.9908739, 2.7336378, 1.4332547, 0.72271728, 0.3491152, 0.15914543, 0.067571425, 0.027248822, 0.010141837, 0.0032816033, 0.00089527242, 0.00089527242])
nnllnnlo_min=2*3000*np.array([48.723877, 48.723877, 34.82143, 22.987784, 14.334426, 8.5186788, 4.8689836, 2.6648837, 1.3970087, 0.70216417, 0.33794254, 0.15368048, 0.065140109, 0.026183953, 0.009691631, 0.0031212358, 0.00084693901, 0.00084693901])
nnllnnlo_max=2*3000*np.array([50.986438, 50.986438, 36.54135, 24.266466, 15.250325, 9.1230448, 5.251348, 2.8922906, 1.5240861, 0.77222797, 0.37468104, 0.17135992, 0.07282327, 0.029432492, 0.010982673, 0.0035573716, 0.00097114182, 0.00097114182])

nloew_centre=2*3000*np.array([46.44394, 46.44394, 33.750496, 22.670348, 14.395876, 8.7396849, 5.089523, 2.8298894, 1.5082688, 0.77498362, 0.37735184, 0.1732512, 0.073948101, 0.029059399, 0.010219791, 0.0030892209, 0.00076693219, 0.00076693219])
nloew_min=2*3000*np.array([43.083153, 43.083153, 31.817766, 21.696219, 13.973361, 8.5970175, 5.0703203, 2.853503, 1.5386993, 0.79963343, 0.39373411, 0.18279921, 0.078908694, 0.031368133, 0.011162478, 0.0034161022, 0.00085946873, 0.00085946873])
nloew_max=2*3000*np.array([49.308053, 49.308053, 35.353734, 23.449186, 14.713423, 8.8313794, 5.0870432, 2.7989297, 1.4765665, 0.75110032, 0.36208421, 0.16458519, 0.069537759, 0.027042048, 0.0094081841, 0.0028116399, 0.00068941845, 0.00068941845])

nlophoton_centre=2*3000*np.array([0.39709488, 0.39709488, 0.38837147, 0.34048635, 0.27697413, 0.2115976, 0.15261175, 0.10414631, 0.067158633, 0.040657515, 0.022967828, 0.011982403, 0.0057161663, 0.0024727913, 0.00096116876, 0.00033066509, 9.8455517e-05, 9.8455517e-05])
nlophoton_min=2*3000*np.array([0.401336, 0.401336, 0.39241692, 0.34412641, 0.2799621, 0.21402427, 0.1543959, 0.10539341, 0.067974202, 0.041166202, 0.023264784, 0.012152763, 0.0058083733, 0.0025195994, 0.00098286007, 0.00033954966, 0.00010153979, 0.00010153979])
nlophoton_max=2*3000*np.array([0.38740771, 0.38740771, 0.38025332, 0.33418188, 0.27245139, 0.20840392, 0.15052636, 0.10284367, 0.066391459, 0.040222701, 0.022735864, 0.011857782, 0.0056514192, 0.0024404738, 0.00094626439, 0.00032459461, 9.6381926e-05, 9.6381926e-05])


lo_centre=2*3000*np.array([48.227482, 48.227482, 35.463431, 24.036981, 15.425143, 9.4896861, 5.6161858, 3.1868226, 1.741649, 0.9215396, 0.46492786, 0.22261272, 0.099824147, 0.041461113, 0.015518201, 0.0050402516, 0.0013565508, 0.0013565508])
lo_min=2*3000*np.array([44.761098, 44.761098, 33.451331, 23.01854, 14.983184, 9.3424158, 5.6003187, 3.2170218, 1.7791324, 0.95231189, 0.48597514, 0.23536392, 0.10677512, 0.04488064, 0.017006822, 0.005596618, 0.0015280848, 0.0015280848])
lo_max=2*3000*np.array([51.169846, 51.169846, 37.123873, 24.845075, 15.752797, 9.5806568, 5.6076958, 3.1482004, 1.7026786, 0.89171185, 0.44529634, 0.21103033, 0.093640634, 0.038472395, 0.014236852, 0.0045681981, 0.0012131292, 0.0012131292])







del_nloewlo_centre=nloew_centre/lo_centre

#print((nloew_max/lo_max)/(nloew_centre/lo_centre))
#print((nloew_min/lo_min)/(nloew_centre/lo_centre))

nnllnnlonloew_centre=nnllnnlo_centre*del_nloewlo_centre
nnllnnlonloew_min=nnllnnlo_min*del_nloewlo_centre
nnllnnlonloew_max=nnllnnlo_max*del_nloewlo_centre



nnllnnlonloew_err=(nnllnnlonloew_max-nnllnnlonloew_min)/2
nlophoton_err=(nlophoton_max-nlophoton_min)/2

total_err=(nnllnnlonloew_err**2 + nlophoton_err**2)**0.5

print(nnllnnlo_centre/6000)
"""
nnllnnlo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_centre.npy"))
nnllnnlo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_min.npy"))
nnllnnlo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_max.npy"))

#print("fi")
#print(nnllnnlonloew_centre/6000)
#print(nnllnnlonloew_max/6000)
#print(nnllnnlonloew_min/6000)

nnllnnlonloew_centre=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_centre.npy"))
nnllnnlonloew_min=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_min.npy"))
nnllnnlonloew_max=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mWW_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_max.npy"))

print("se")
print(nnllnnlonloew_centre/6000)
print(nnllnnlonloew_max/6000)
print(nnllnnlonloew_min/6000)

nlophoton_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_gammagamma_nlo_centre.npy"))
nlophoton_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_gammagamma_nlo_min.npy"))
nlophoton_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mWW_14TeV_veto35_sm_gammagamma_nlo_max.npy"))


print(nlophoton_centre/6000)
print(nlophoton_max/6000)
print(nlophoton_min/6000)

nnllnnlonloew_err=(nnllnnlonloew_max-nnllnnlonloew_min)/2
nlophoton_err=(nlophoton_max-nlophoton_min)/2

total_err=(nnllnnlonloew_err**2 + nlophoton_err**2)**0.5

plt.figure(figsize=(16, 12),dpi=1000)

fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [2, 1]}, sharex=True)


axs[1].set_xlabel(r"$M_{WW}$ [GeV] ",\
               fontsize=16,color="black")

axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{WW}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r" Ratio$_{\mathrm{QCD}}$ - 1",\
               fontsize=16,color="black")


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
axs[0].annotate(r'$\sqrt{s} = 14$TeV, $\, p p\, \to\, e^{\pm}\nu\mu^{\mp}\nu$', 
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
axs[0].set_xlim(200, 4000)
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
#plt.tight_layout()
plt.savefig("figure_4a.pdf", bbox_inches='tight')

