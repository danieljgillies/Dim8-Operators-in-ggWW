
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '..')
from plot_funcs import round_to_5, array_for_plot

bins=round_to_5(np.logspace(np.log10(200), np.log10(4000), 17))
print(bins)
bin_widths=bins[1:17]-bins[0:16]
bin_widths18=np.array([41.1817, 41.1817, 49.6614, 59.8871, 72.2183, 87.0887, 105.021, 126.6458, 152.7232, 184.1698, 222.093, 267.823, 322.97, 389.473, 469.668, 566.377, 682.999, 682.999])

bins15 = [0, 55, 75, 85, 95, 110, 125, 140, 160, 185, 220, 280, 380, 600, 1500]




bin_centres_atlas = [65, 80, 90, 102.5, 117.5, 132.5, 150, 172.5, 202.5, 250, 330, 490, 1050]

abs_syst_err=np.array([0.222265607, 0.233038623, 0.238126017, 0.193452837, 0.171330091, 0.157819517, 0.116060329, 0.095010526, 0.067880115, 0.030872966, 0.016419196, 0.003516234, 0.000331964])

abs_stat_err=np.array([0.108, 0.137, 0.131,0.104, 0.088, 0.081, 0.063, 0.049, 0.0333, 0.0182, 0.0091, 0.00286, 0.00027])

atlas = np.array([3.453, 3.767, 3.538, 3.094, 2.228, 1.899, 1.558, 1.145, 0.6746, 0.3516, 0.1407, 0.02837, 0.00127])


nnllnnlonloew_ggphoton_centre=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_centre.npy"))
nnllnnlonloew_ggphoton_min=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_min.npy"))
nnllnnlonloew_ggphoton_max=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_max.npy"))




nnlonloew_ggphoton_centre=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_centre.npy"))
nnlonloew_ggphoton_min=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_min.npy"))
nnlonloew_ggphoton_max=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_max.npy"))

err_sm=(nnllnnlonloew_ggphoton_max-nnllnnlonloew_ggphoton_min)/2

fo_err=(nnlonloew_ggphoton_max-nnlonloew_ggphoton_min)/(2)
sm=nnlonloew_ggphoton_centre
a=np.polyfit(bin_centres_atlas, 100*abs_stat_err/atlas, 1)
print(a)
#0.019542609	4.863706128
#[0.01954262 4.86370437]

x_vals=np.linspace(10, 4000, 10000)
plt.figure(dpi=100)


bins15 = [55, 55, 75, 85, 95, 110, 125, 140, 160, 185, 220, 280, 380, 600, 1500]
#plt.plot(bin_centres_atlas, 100*abs_syst_err/atlas, "rx", label="Atlas Systematics")
atlas_syst_err=[6.43688407, 6.43688407, 6.18631864, 6.7305262, 6.25251574, 7.68986046, 8.3106644, 7.44931508, 8.29786253, 10.06227616, 8.78070705, 11.6696489, 12.3941981, 26.13889764, 26.13889764]
plt.step(bins15, atlas_syst_err, color="red", where="post", label="ATLAS systematic error")
print(100*abs_stat_err/atlas)
atlas_stat_err=[3.12771503, 3.12771503, 3.6368463, 3.70265687, 3.36134454, 3.9497307, 4.26540284, 4.0436457,  4.27947598, 4.93625852, 5.17633675, 6.46766169, 10.08107155, 21.25984252, 21.25984252]
#plt.plot(bin_centres_atlas, 100*abs_stat_err/atlas, "bx")
plt.step(bins15, atlas_stat_err, color="blue", where="post", label="ATLAS statistical error")
plt.plot(x_vals, 4.8637+ 0.019543*x_vals, color="grey", label="Systematic error projection")

#plt.plot(x_vals, (4.8637+ 0.019543*x_vals), color="grey")


ewcross_err=np.array([ 0.43006829, 0.43006829, 0.70694987, 1.13680195, 1.8635062,  2.9229523, 4.51181207, 6.50287359, 9.01543409, 12.32643401, 15.86624691, 20.31554285, 25.13947166, 31.22147136, 37.7384327, 47.5414484, 64.18207759, 64.18207759])

print(np.mean(abs_syst_err/abs_stat_err))

bins18=np.concatenate(([200], bins))
print(bins18)
#plt.step(bin_centres18, 100*(nnllnnlonloew_ggphoton_centre**-0.5), color="green", label="Statistical Error")
plt.step(bins18, 100*(nnllnnlonloew_ggphoton_centre**-0.5), color="green", where="post", label="HL-LHC projected statistical error")

#plt.step(bin_centres18, 2*100*(nnllnnlonloew_ggphoton_centre**-0.5), color="green")

#plt.step(bin_centres18, 100*err_sm/nnllnnlonloew_ggphoton_centre, color="black", label="Theoretial Error")
plt.step(bins18, 100*err_sm/nnllnnlonloew_ggphoton_centre, color="black", where="post", label="Current theoretial error")

#plt.step(bins18, ewcross_err, color="Orange", where="post", label="New Cross Error")


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
#plt.xlim(-20,4020)
plt.legend(loc="lower left", fontsize=10, frameon=False, labelcolor="k")
plt.loglog()
plt.yticks([10**-1, 1, 10, 100, 1000], labels=["0.1", "1", "10", "100", "1000"])
#plt.yticklabels([r"$10^{-2}$", r"$10^{-1}$", "1", "10", "100", "1000"])
plt.xlim(5, 5000)
plt.tick_params(which="both", labelsize=13, direction='in', right=True, top=True)

plt.tight_layout()
plt.savefig("figure_12.pdf")
