import matplotlib.pyplot as plt
import numpy as np
from math import log10, floor
import sys
sys.path.insert(1, '..')
from plot_funcs import round_to_5



bins=round_to_5(np.logspace(2.1384012462059836, np.log10(4000), 19))
print("Bin Edges (GeV)...")
print(bins)
bin_widths=bins[1:]-bins[0:len(bins)-1]
print("\n Bin Widths (GeV)...")
print(bin_widths)

bin_centres=(bins[1:]+bins[0:len(bins)-1])/2
print("\n Bin Centres (GeV)...")
print(bin_centres)


kg2nll_centre=np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_OGHsq_nll_qcd_centre.npy")
k32nll_centre=np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_bsm_gg_O3sq_nll_qcd_centre.npy")
kg2lo_centre=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_OGHsq_lo_qcd_murenorm=0.50MWW_mufac=0.50MWW.npy")
k32lo_centre=np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_bsm_gg_O3sq_lo_qcd_murenorm=0.50MWW_mufac=0.50MWW.npy")



#Ratios between dimension-6 and dimension-8 squared contributions at fixed order (LO) and NLL.
lo_ratio=k32lo_centre/kg2lo_centre
nll_ratio=k32nll_centre/kg2nll_centre




plt.figure()
plt.plot(bin_centres, lo_ratio)
plt.plot(bin_centres, nll_ratio)
plt.plot(bin_centres, nll_ratio[15]*(bin_centres/bin_centres[15])**4)
plt.plot(bin_centres, nll_ratio[15]*(bin_centres/bin_centres[15])**2.8)
plt.loglog()
plt.savefig("ratio_14tev.pdf")




plt.figure()
plt.plot(bin_centres, 2000*((1*lo_ratio)**0.25), 'k', label=r"Empirical (LO)   assuming  $\sigma_6^2 > \sigma_8^2$")
plt.plot(bin_centres, 2000*((1*nll_ratio)**0.25), 'r', label=r"Empirical (NLL) assuming  $\sigma_6^2 > \sigma_8^2$")

print("\n\n\n")
print("saving... 14TeV_noveto")
print("\n")
print("saving... 14TeV_noveto d-6^2 > 4 * d-8^2")
print(2*((4*lo_ratio)**0.25))
np.save("lambda_min_empirical_14TeV_noveto_025", 2*((4*lo_ratio)**0.25))
print("\n")
print("saving... 14TeV_noveto d-6^2 > 2 * d-8^2")
print(2*((2*lo_ratio)**0.25))
np.save("lambda_min_empirical_14TeV_noveto", 2*((2*lo_ratio)**0.25))
print("\n")
print("saving... 14TeV_noveto d-6^2 > d-8^2")
print(2*((1*lo_ratio)**0.25))
np.save("lambda_min_empirical_14TeV_noveto_1", 2*((1*lo_ratio)**0.25))
print("\n\n")
print("saving... 14TeV_veto35")
print("\n")
print("saving... 14TeV_veto35 d-6^2 > 4 * d-8^2")
print(2*((4*nll_ratio)**0.25))
np.save("lambda_min_empirical_14TeV_veto35_025", 2*((4*nll_ratio)**0.25))
print("\n")
print("saving... 14TeV_veto35 d-6^2 > 2 * d-8^2")
print(2*((2*nll_ratio)**0.25))
np.save("lambda_min_empirical_14TeV_veto35", 2*((2*nll_ratio)**0.25))
print("\n")
print("saving... 14TeV_veto35 d-6^2 > d-8^2")
print(2*((1*nll_ratio)**0.25))
np.save("lambda_min_empirical_14TeV_veto35_1", 2*((1*nll_ratio)**0.25))



a=np.linspace(0,14000)



###If we assume that mll takes around half the energy of the mWW pair then Lambda min must be 2root(2) times bigger than Memu.
#plt.plot(a, a*2*np.sqrt(2), label=r'$\Lambda_{\mathrm{min}}\ \ \mathrm{assuming} \ \ M_{e\mu} = \frac{M_{WW}}{2}$')

#If we assume that mll takes all the energy of the mWW pair then Lambda min must be root(2) times bigger than Memu
plt.plot(a, a*2, label=r'$\Lambda_{\mathrm{min}} <\,2\times M_{e\mu}\ \ \,\mathrm{assuming} \ \ M_{e\mu} \approx \frac{M_{WW}}{2}$')

#If we assume that mll takes all the energy of the mWW pair then Lambda min must be root(2) times bigger than Memu
plt.plot(a, a, label=r'$\Lambda_{\mathrm{min}} <\,M_{e\mu}\ \ \ \ \ \ \ \ \mathrm{assuming} \ \ M_{e\mu} \approx M_{WW}$')




b=np.linspace(3600,14000)

lo=np.polyfit(x=np.log(bin_centres[len(bin_centres)-3:len(bin_centres)-1]), y=np.log((2000*((1*lo_ratio[len(bin_centres)-3:len(bin_centres)-1])**0.25))), deg=1)
print(lo)
lo=np.poly1d(lo)

nll=np.polyfit(x=np.log(bin_centres[len(bin_centres)-3:len(bin_centres)-1]), y=np.log((2000*((1*nll_ratio[len(bin_centres)-3:len(bin_centres)-1])**0.25))), deg=1)
nll=np.poly1d(nll)
plt.plot(b, np.exp(lo(np.log(b))), 'k--')
plt.plot(b, np.exp(nll(np.log(b))), 'r--')


plt.loglog()
plt.xlabel(r"$M_{e\mu}\ \left[\mathrm{TeV}\right]$",\
               fontsize=16,color="black")
plt.ylabel(r"$\Lambda_{\min}\ \left[\mathrm{TeV}\right]$",\
               fontsize=16,color="black")

plt.tick_params(labelsize=13)
plt.xticks([200, 1000, 2000, 3000, 4000, 5000, 6000], labels=[r"$0.2$", r"$1$", r"$2$", r"$3$", r"$4$", r"$5$", r"$6$"])
plt.yticks([1000, 10000], labels=[r"$1$", r"$10$"])
plt.tight_layout()
plt.xlim(151.69065, 6000)
plt.legend(fontsize=11, columnspacing=0.8)
plt.savefig("mass_scale_14tev.pdf")