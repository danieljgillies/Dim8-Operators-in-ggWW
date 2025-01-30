import numpy as np
import matplotlib.pyplot as plt
from math import log10, floor

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

"""
#MATRIX

##OLD
#nnllnnlo_centre=2*3000*np.array([11.566163, 11.566163, 7.685741, 4.7633813, 2.7397298, 1.491574, 0.77753524, 0.39711564, 0.19630997, 0.093249664, 0.042387383, 0.018042554, 0.0071327232, 0.0025387694, 0.00080482328, 0.00021758338, 4.8711221e-05, 4.8711221e-05])
#nnllnnlo_min=2*3000*np.array([11.343429, 11.343429, 7.530978, 4.661844, 2.6812585, 1.4592339, 0.76150776, 0.38794496, 0.19129912, 0.090619762, 0.04103044, 0.017403648, 0.006852311, 0.002429927, 0.00076511136, 0.00020600008, 4.6145095e-05, 4.6145095e-05])
#nnllnnlo_max=2*3000*np.array([11.995234, 11.995234, 8.0066247, 4.9861359, 2.8809368, 1.5757553, 0.82449863, 0.42277543, 0.20970162, 0.099909291, 0.045548061, 0.019427594, 0.0076955351, 0.0027415644, 0.00087056858, 0.00023542745, 5.247156e-05, 5.247156e-05])

##nnlo_centre=2*3000*np.array([11.565615, 11.565615, 7.6852724, 4.7661742, 2.7336293, 1.4857702, 0.76946636, 0.39182155, 0.19277728, 0.091149158, 0.041341975, 0.017522463, 0.0069185061, 0.0024535291, 0.00078029884, 0.00021029352, 4.5666504e-05, 4.5666504e-05])
##nnlo_min=2*3000*np.array([11.497911, 11.497911, 7.6390091, 4.7372814, 2.7156889, 1.4762808, 0.76194574, 0.38779326, 0.19031895, 0.089729459, 0.040658972, 0.017181122, 0.0067605729, 0.0023851099, 0.00076000637, 0.00020377673, 4.3434792e-05, 4.3434792e-05])
##nnlo_max=2*3000*np.array([11.657624, 11.657624, 7.7486201, 4.8058818, 2.7600963, 1.5010859, 0.78025171, 0.39797751, 0.19641569, 0.093174725, 0.042347779, 0.018010537, 0.0071342819, 0.0025410513, 0.00080743862, 0.00021849945, 4.8218253e-05, 4.8218253e-05])

##nnll_centre=2*3000*np.array([11.115009, 11.115009, 7.3623271, 4.5406057, 2.6157002, 1.423193, 0.74991066, 0.38488458, 0.19149548, 0.09153185, 0.041651886, 0.017821831, 0.0070461195, 0.0025227433, 0.00079631587, 0.00021568982, 4.995235e-05, 4.995235e-05])
##nnll_min=2*3000*np.array([10.794048, 10.794048, 7.1489289, 4.4093573, 2.5412217, 1.3837402, 0.72732746, 0.37179259, 0.18418938, 0.08764244, 0.039689767, 0.016895488, 0.006642561, 0.0023639926, 0.00074156793, 0.00019965427, 4.6035399e-05, 4.6035399e-05])
##nnll_max=2*3000*np.array([11.749972, 11.749972, 7.8239497, 4.8506664, 2.8084769, 1.535066, 0.81222861, 0.41844839, 0.20889307, 0.1001355, 0.045675847, 0.019579438, 0.0077511429, 0.0027770101, 0.00087658308, 0.00023732547, 5.49401e-05, 5.49401e-05])
##OLD End

nnllnnlo_centre=2*3000*np.array([11.566163, 11.566163, 7.685741, 4.7633813, 2.7397298, 1.491574, 0.77753524, 0.39711564, 0.19630997, 0.093249664, 0.042387383, 0.018042554, 0.0071327232, 0.0025387694, 0.00080482328, 0.00021758338, 5.0093331e-05, 5.0093331e-05])
nnllnnlo_min=2*3000*np.array([11.343429, 11.343429, 7.530978, 4.661844, 2.6812585, 1.4592339, 0.76150776, 0.38794496, 0.19129912, 0.090619762, 0.04103044, 0.017403648, 0.006852311, 0.002429927, 0.00076511136, 0.00020600008, 4.7301851e-05, 4.7301851e-05])
nnllnnlo_max=2*3000*np.array([11.995234, 11.995234, 8.0066247, 4.9861359, 2.8809368, 1.5757553, 0.82449863, 0.42277543, 0.20970162, 0.099909291, 0.045548061, 0.019427594, 0.0076955351, 0.0027415644, 0.00087056858, 0.00023542745, 5.4177057e-05, 5.4177057e-05])
nnlo_centre=2*3000*np.array([11.565615, 11.565615, 7.6852724, 4.7661742, 2.7336293, 1.4857702, 0.76946636, 0.39182155, 0.19277728, 0.091149158, 0.041341975, 0.017522463, 0.0069185061, 0.0024535291, 0.00078029884, 0.00021029352, 4.7950355e-05, 4.7950355e-05])
nnlo_min=2*3000*np.array([11.497911, 11.497911, 7.6390091, 4.7372814, 2.7156889, 1.4762808, 0.76194574, 0.38779326, 0.19031895, 0.089729459, 0.040658972, 0.017181122, 0.0067605729, 0.0023851099, 0.00076000637, 0.00020377673, 4.612155e-05, 4.612155e-05])
nnlo_max=2*3000*np.array([11.657624, 11.657624, 7.7486201, 4.8058818, 2.7600963, 1.5010859, 0.78025171, 0.39797751, 0.19641569, 0.093174725, 0.042347779, 0.018010537, 0.0071342819, 0.0025410513, 0.00080743862, 0.00021849945, 5.0178131e-05, 5.0178131e-05])
#nnll_centre=2*3000*np.array([11.115009, 11.115009, 7.3623271, 4.5406057, 2.6157002, 1.423193, 0.74991066, 0.38488458, 0.19149548, 0.09153185, 0.041651886, 0.017821831, 0.0070461195, 0.0025227433, 0.00079631587, 0.00021568982, 5.0030293e-05, 5.0030293e-05])
#nnll_min=2*3000*np.array([10.794048, 10.794048, 7.1489289, 4.4093573, 2.5412217, 1.3837402, 0.72732746, 0.37179259, 0.18418938, 0.08764244, 0.039689767, 0.016895488, 0.006642561, 0.0023639926, 0.00074156793, 0.00019965427, 4.610565e-05, 4.610565e-05])
#nnll_max=2*3000*np.array([11.749972, 11.749972, 7.8239497, 4.8506664, 2.8084769, 1.535066, 0.81222861, 0.41844839, 0.20889307, 0.1001355, 0.045675847, 0.019579438, 0.0077511429, 0.0027770101, 0.00087658308, 0.00023732547, 5.5027099e-05, 5.5027099e-05])



nloew_centre=2*3000*np.array([11.511081, 11.511081, 7.7478559, 4.8803813, 2.8699538, 1.5934634, 0.84729179, 0.43744109, 0.21696504, 0.10358812, 0.046169964, 0.019171835, 0.007251576, 0.0024461489, 0.00072137817, 0.00018109279, 3.9797881e-05, 3.9797881e-05])
nloew_min=2*3000*np.array([11.101848, 11.101848, 7.5527253, 4.8098925, 2.8600202, 1.5770128, 0.83060556, 0.42475281, 0.20869729, 0.098700565, 0.043576399, 0.01792186, 0.0067137125, 0.002243168, 0.00065556629, 0.00016339969, 3.5779929e-05, 3.5779929e-05])
nloew_max=2*3000*np.array([11.829411, 11.829411, 7.8898836, 4.9233561, 2.8699538, 1.6055313, 0.86302901, 0.45040619, 0.22576909, 0.10893574, 0.049066372, 0.020592195, 0.0078722222, 0.002683551, 0.00079926396, 0.00020222444, 4.4614433e-05, 4.4614433e-05])

nlophoton_centre=2*3000*np.array([0.19810551, 0.19810551, 0.1538622, 0.11262551, 0.077749794, 0.050374167, 0.030672802, 0.017651956, 0.0096082426, 0.0049169342, 0.002365917, 0.0010634943, 0.00044148895, 0.00016755527, 5.7198414e-05, 1.7122486e-05, 4.3313385e-06, 4.3313385e-06])
nlophoton_min=2*3000*np.array([0.19506661, 0.19506661, 0.15158336, 0.11106255, 0.076730494, 0.049748421, 0.030292895, 0.017432152, 0.009484954, 0.0048507582, 0.0023316198, 0.0010467087, 0.00043386039, 0.00016438463, 5.6035729e-05, 1.6756966e-05, 4.2374953e-06, 4.2374953e-06])
nlophoton_max=2*3000*np.array([0.2001651, 0.2001651, 0.15559145, 0.11393307, 0.078686114, 0.051000369, 0.031083826, 0.017906348, 0.0097590383, 0.0050017041, 0.0024113818, 0.0010863463, 0.00045210895, 0.00017206034, 5.8892686e-05, 1.7673038e-05, 4.479545e-06, 4.479545e-06])


lo_centre=2*3000*np.array([12.295819, 12.295819, 8.3663669, 5.3392747, 3.1931267, 1.810972, 0.988312, 0.52545869, 0.26945906, 0.13331015, 0.062001067, 0.027009104, 0.010798608, 0.0038856795, 0.0012330404, 0.00033741612, 8.1084759e-05, 8.1084759e-05])
lo_min=2*3000*np.array([11.867498, 11.867498, 8.1618383, 5.2663418, 3.1847893, 1.7906044, 0.96785689, 0.50965411, 0.25888112, 0.12685941, 0.058438534, 0.025211081, 0.0099813008, 0.0035565022, 0.0011180083, 0.00030354372, 7.2586503e-05, 7.2586503e-05])
lo_max=2*3000*np.array([12.626357, 12.626357, 8.5132186, 5.3819802, 3.1931267, 1.8263814, 1.0076935, 0.54162471, 0.28072487, 0.14036726, 0.065978877, 0.029051824, 0.011741567, 0.0042706711, 0.0013692046, 0.00037790356, 9.129745e-05, 9.129745e-05])






del_nloewlo_centre=nloew_centre/lo_centre

diff_nloewlo_centre=nloew_centre-lo_centre
diff_nnlolo_centre=nnlo_centre-lo_centre
diff_nnllnnlolo_centre=nnllnnlo_centre-lo_centre

print(diff_nloewlo_centre)
print(diff_nnlolo_centre)
print(diff_nnllnnlolo_centre)


#print((nloew_max/lo_max)/(nloew_centre/lo_centre))
#print((nloew_min/lo_min)/(nloew_centre/lo_centre))

nnllnnlonloew_centre=nnllnnlo_centre*del_nloewlo_centre
nnllnnlonloew_min=nnllnnlo_min*del_nloewlo_centre
nnllnnlonloew_max=nnllnnlo_max*del_nloewlo_centre


nnllnnlonloew_add_centre=nnllnnlo_centre+diff_nloewlo_centre
nnllnnlonloew_add_min=nnllnnlo_min+diff_nloewlo_centre
nnllnnlonloew_add_max=nnllnnlo_max+diff_nloewlo_centre


print(100*(nnllnnlonloew_centre-nnllnnlonloew_add_centre)/nnllnnlonloew_centre)


nnllnnlonloew_err=(nnllnnlonloew_max-nnllnnlonloew_min)/2
nlophoton_err=(nlophoton_max-nlophoton_min)/2

total_err=(nnllnnlonloew_err**2 + nlophoton_err**2)**0.5
"""
nnllnnlo_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_centre.npy"))
nnllnnlo_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_min.npy"))
nnllnnlo_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_max.npy"))

#print("fi")
#print(nnllnnlonloew_centre/6000)
#print(nnllnnlonloew_max/6000)
#print(nnllnnlonloew_min/6000)

nnllnnlonloew_centre=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_centre.npy"))
nnllnnlonloew_min=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_min.npy"))
nnllnnlonloew_max=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_max.npy"))

print("se")
print(nnllnnlonloew_centre/6000)
print(nnllnnlonloew_max/6000)
print(nnllnnlonloew_min/6000)

nlophoton_centre=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gammagamma_nlo_centre.npy"))
nlophoton_min=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gammagamma_nlo_min.npy"))
nlophoton_max=2*3000*array_for_plot(np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gammagamma_nlo_max.npy"))


print(nlophoton_centre/6000)
print(nlophoton_max/6000)
print(nlophoton_min/6000)

nnllnnlonloew_err=(nnllnnlonloew_max-nnllnnlonloew_min)/2
nlophoton_err=(nlophoton_max-nlophoton_min)/2

total_err=(nnllnnlonloew_err**2 + nlophoton_err**2)**0.5

plt.figure(figsize=(16, 12),dpi=1000)

fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [2, 1]}, sharex=True)

#axs[0].set_title(r"MATRIX vs ATLAS",\
#               fontsize=18,color="black")
axs[1].set_xlabel(r"$M_{e\mu}$ [GeV] ",\
               fontsize=16,color="black")
#axs[0].set_ylabel(r"num_events",\
#               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r" Ratio$_{\mathrm{QCD}}$ - 1",\
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


#axs[0].step(bin_centres, nnllnnlonloew_add_centre/(bin_widths18*3000), color='g', where='mid', linewidth=0.5)
#axs[0].step(bin_centres, -nnllnnlonloew_add_centre/(bin_widths18*3000), color='g', where='mid', label=r'NNLL+NNLO$_{\mathrm{QCD}}+$NLO$_{\mathrm{EW}}$')

#axs[0].fill_between(bin_centres, nnllnnlonloew_add_min/(bin_widths18*3000), nnllnnlonloew_add_max/(bin_widths18*3000),
#                     color='g', alpha=0.5, step='mid')




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

#ratio_nnllnnloew_add=nnllnnlonloew_add_centre/nnllnnlo_centre
#ratio_nnllnnloew_add_min=nnllnnlonloew_add_min/nnllnnlo_centre
#ratio_nnllnnloew_add_max=nnllnnlonloew_add_max/nnllnnlo_centre



ratio_nnllnnloewwphoton=(nnllnnlonloew_centre+nlophoton_centre)/nnllnnlo_centre
ratio_nnllnnloewwphoton_min=(nnllnnlonloew_centre+nlophoton_centre-total_err)/nnllnnlo_centre
ratio_nnllnnloewwphoton_max=(nnllnnlonloew_centre+nlophoton_centre+total_err)/nnllnnlo_centre

axs[1].step(bin_centres, ratio_nnllnnlo-1, color='k', where='mid')
axs[1].fill_between(bin_centres, ratio_nnllnnlo_min-1, ratio_nnllnnlo_max-1,
                     color='k', alpha=0.5, step='mid')

axs[1].step(bin_centres, ratio_nnllnnloew-1, color='b', where='mid')
axs[1].fill_between(bin_centres, ratio_nnllnnloew_min-1, ratio_nnllnnloew_max-1,
                     color='b', alpha=0.5, step='mid')

#axs[1].step(bin_centres, ratio_nnllnnloew_add-1, color='g', where='mid')
#axs[1].fill_between(bin_centres, ratio_nnllnnloew_add_min-1, ratio_nnllnnloew_add_max-1,
#                     color='g', alpha=0.5, step='mid')

axs[1].step(bin_centres, ratio_nnllnnloewwphoton-1, color='orange', where='mid')
axs[1].fill_between(bin_centres, ratio_nnllnnloewwphoton_min-1, ratio_nnllnnloewwphoton_max-1,
                     color='orange', alpha=0.5, step='mid')

#axs[1].set_ylim(-1, 0.12)
axs[1].set_ylim(-0.6, 0.12)
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
#plt.tight_layout()
#plt.savefig("nnlonnllewaddphoton_add.pdf", bbox_inches='tight')
plt.savefig("figure_4b.pdf", bbox_inches='tight')

