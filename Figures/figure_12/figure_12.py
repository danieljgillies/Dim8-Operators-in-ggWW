
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '..')
from plot_funcs import round_to_5, array_for_plot

bins=round_to_5(np.logspace(np.log10(200), np.log10(4000), 17))
bin_widths=bins[1:17]-bins[0:16]
bin_widths18=np.array([41.1817, 41.1817, 49.6614, 59.8871, 72.2183, 87.0887, 105.021, 126.6458, 152.7232, 184.1698, 222.093, 267.823, 322.97, 389.473, 469.668, 566.377, 682.999, 682.999])

bins15 = [0, 55, 75, 85, 95, 110, 125, 140, 160, 185, 220, 280, 380, 600, 1500]
bin_centres_atlas = [65, 80, 90, 102.5, 117.5, 132.5, 150, 172.5, 202.5, 250, 330, 490, 1050]


atlas=array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas.npy"))
atlas_err=array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas_err.npy"))
abs_stat_err=array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas_stat_err.npy"))
abs_syst_err=array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas_syst_err.npy"))

#print(atlas)
#print(abs_stat_err)
#print(atlas_err)

nnllnnlonloew_ggphoton_centre=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_centre.npy"))
nnllnnlonloew_ggphoton_min=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_min.npy"))
nnllnnlonloew_ggphoton_max=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_max.npy"))


nnlonloew_ggphoton_centre=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_centre.npy"))
nnlonloew_ggphoton_min=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_min.npy"))
nnlonloew_ggphoton_max=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_max.npy"))

#Error on resummed prediction
err_sm=(nnllnnlonloew_ggphoton_max-nnllnnlonloew_ggphoton_min)/2

#Error on fixed order prediction (without a jet veto)
fo_err=(nnlonloew_ggphoton_max-nnlonloew_ggphoton_min)/(2)


sm=nnlonloew_ggphoton_centre


a=np.polyfit(bin_centres_atlas, 100*abs_syst_err[1:14]/atlas[1:14], 1)
print(a)
#Print the y-intercept and gradient for systematic error.
#0.019542609	4.863706128
#[0.01954262 4.86370437]


plt.figure(dpi=100)


#Percentage statistical and systematic errors.
atlas_syst_err=100*abs_syst_err/atlas
atlas_stat_err=100*abs_stat_err/atlas


plt.step(bins15[1:], atlas_syst_err[1:], color="red", where="post", label="ATLAS systematic error")
plt.step(bins15[1:], atlas_stat_err[1:], color="blue", where="post", label="ATLAS statistical error")

#Projected systematics up to 4000TeV.
x_vals=np.linspace(10, 4000, 10000)
plt.plot(x_vals, 4.8637+ 0.019543*x_vals, color="grey", label="Systematic error projection")

#The error coming from varying EW combination scheme... not included in this paper.
#ewcross_err=np.array([ 0.43006829, 0.43006829, 0.70694987, 1.13680195, 1.8635062,  2.9229523, 4.51181207, 6.50287359, 9.01543409, 12.32643401, 15.86624691, 20.31554285, 25.13947166, 31.22147136, 37.7384327, 47.5414484, 64.18207759, 64.18207759])



bins18=np.concatenate(([200], bins))

#Poisson error based on current predictions.

plt.step(bins18, 100*(nnllnnlonloew_ggphoton_centre**-0.5), color="green", where="post", label="HL-LHC projected statistical error")
plt.step(bins18, 100*err_sm/nnllnnlonloew_ggphoton_centre, color="black", where="post", label="Current theoretial error")
plt.step(bins18, 100*fo_err/sm, color="black", where="post", linestyle="dashed", label="Current theoretial error, without jet-veto")

plt.annotate(r'HL-LHC (ATLAS cuts)', 
            xy=(7,  9*10**2), 
            fontsize=15,
            fontweight="bold",
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
plt.annotate(r'$\sqrt{s} = 14$TeV, $3$ab$^{-1}$', 
            xy=(7,  5*10**2), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
plt.annotate(r'$\, p p\, \to\, e^{\pm}\nu\mu^{\mp}\nu, $', 
            xy=(7, 3*10**2), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')

plt.annotate(r'$4.8637+ 19.543\times \frac{M_{e\mu}}{TeV}$', (20, 20),\
               fontsize=14,color="grey")
plt.ylabel(r'$\%$ Error', fontsize=16,color="black")
plt.xlabel(r'$M_{e\mu}$ [GeV]', fontsize=16,color="black")
plt.grid(alpha=0.3)
plt.legend(loc="lower left", fontsize=10, frameon=False, labelcolor="k")
plt.loglog()
plt.yticks([10**-1, 1, 10, 100, 1000], labels=["0.1", "1", "10", "100", "1000"])
plt.xlim(5, 5000)
plt.tick_params(which="both", labelsize=13, direction='in', right=True, top=True)
plt.tight_layout()
plt.savefig("figure_12.pdf")
