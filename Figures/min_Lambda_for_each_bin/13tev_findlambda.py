import matplotlib.pyplot as plt
import numpy as np


bins15 = [0, 55, 75, 85, 95, 110, 125, 140, 160, 185, 220, 280, 380, 600, 1500]
bin_centres = [65, 80, 90, 102.5, 117.5, 132.5, 150, 172.5, 202.5, 250, 330, 490, 1050]


mcfm_nll_k32=np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_O3sq_nll_qcd_centre.npy")
mcfm_nll_kg2=np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_13TeV_veto35_bsm_gg_OGHsq_nll_qcd_centre.npy")


#ratio between dim6 and dim8 contributions at 2TeV.
nll_ratio=mcfm_nll_k32/mcfm_nll_kg2


plt.figure()
plt.plot(bin_centres, nll_ratio)
plt.loglog()
plt.savefig("ratio_13tev.pdf")
plt.figure()



#Formula (2.23) from the paper gives the minimum value of Lambda where O3^2 is significantly smaller than OGH^2 for each bin.
#plt.plot(bin_centres, 2000*((1*nll_ratio)**0.25), 'r', label="empirical from resummed")

plt.plot(bin_centres, 2000*((nll_ratio)**0.25), 'r', label=r"Empirical (NLL) assuming  $\sigma_6^2 > \sigma_8^2$")


print("saving... 13TeV_veto35")
print("\n\n")
print("saving... 13TeV_veto35 d-6^2 > d-8^2")
print(2*((4*nll_ratio)**0.25))
np.save( "lambda_min_empirical_13TeV_veto35_025", 2*((4*nll_ratio)**0.25))
print("\n")
print("saving... 13TeV_veto35 d-6^2 > 2 * d-8^2")
print(2*((2*nll_ratio)**0.25))
np.save( "lambda_min_empirical_13TeV_veto35", 2*((2*nll_ratio)**0.25))
print("\n")
print("saving... 13TeV_veto35 d-6^2 > 4 * d-8^2")
print(2*((1*nll_ratio)**0.25))
np.save( "lambda_min_empirical_13TeV_veto35_1", 2*((1*nll_ratio)**0.25))
print("\n")
print("\n")
print(2*((0.25*nll_ratio)**0.25))
np.save( "lambda_min_empirical_13TeV_veto35_old", 2*((0.25*nll_ratio)**0.25))

a=np.linspace(0,14000)
nll=np.polyfit(x=np.log(bin_centres[len(bin_centres)-2:len(bin_centres)]), y=np.log((2000*((nll_ratio[len(bin_centres)-2:len(bin_centres)])**0.25))), deg=1)
nll=np.poly1d(nll)
b=np.linspace(800,14000)
plt.plot(b, np.exp(nll(np.log(b))), 'r--')


#If we assume that mll takes around half the energy of the mWW pair then Lambda min must be 2root(2) times bigger than Memu.
#plt.plot(a, a*2, label=r'$\Lambda_{\mathrm{min}}\ \ \mathrm{assuming} \ \ M_{e\mu} = \frac{M_{WW}}{2}$')

#If we assume that mll takes around half the energy of the mWW pair then Lambda min must be 2root(2) times bigger than Memu.
#plt.plot(a, a*2*np.sqrt(2), label=r'$\Lambda_{\mathrm{min}}\ \ \mathrm{assuming} \ \ M_{e\mu} = \frac{M_{WW}}{2}$')

#If we assume that mll takes all the energy of the mWW pair then Lambda min must be root(2) times bigger than Memu
#plt.plot(a, a*np.sqrt(2), "--", label=r'$\Lambda_{\mathrm{min}}\ \ \mathrm{assuming} \ \ M_{e\mu} = M_{WW}$')

plt.plot(a, a*2, label=r'$\Lambda_{\mathrm{min}} <\,2\times M_{e\mu}\ \ \,\mathrm{assuming} \ \ M_{e\mu} \approx \frac{M_{WW}}{2}$')

#If we assume that mll takes all the energy of the mWW pair then Lambda min must be root(2) times bigger than Memu
plt.plot(a, a, label=r'$\Lambda_{\mathrm{min}} <\,M_{e\mu}\ \ \ \ \ \ \ \ \mathrm{assuming} \ \ M_{e\mu} \approx M_{WW}$')




plt.loglog()
plt.xlabel(r"$M_{e\mu}\ \left[\mathrm{TeV}\right]$",\
               fontsize=16,color="black")
plt.ylabel(r"$\Lambda_{\mathrm{Min}}\ \left[\mathrm{TeV}\right]$",\
               fontsize=16,color="black")
plt.xticks([200, 1000, 10000, 14000], labels=[r"$0.2$", r"$1$", r"$10$", r"$14$"])
plt.yticks([1000, 10000], labels=[r"$1$", r"$10$"])
plt.legend()
plt.savefig("mass_scale_13.pdf")