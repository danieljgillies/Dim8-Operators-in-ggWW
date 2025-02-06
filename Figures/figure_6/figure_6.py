import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.insert(1, '..')

from plot_funcs import array_for_plot

bins = [55, 75, 85, 95, 110, 125, 140, 160, 185, 220, 280, 380, 600, 1500]

bin_centres = [65, 80, 90, 102.5, 117.5, 132.5, 150, 172.5, 202.5, 250, 330, 490, 1050]

bins = [65, 80, 90, 102.5, 117.5, 132.5, 150, 172.5, 202.5, 250, 330, 490, 1050]

bin_sizes = np.array([20, 10, 10, 15, 15, 15, 20, 25, 35, 60, 100, 220, 900])


bin_sizes15 = np.array([20, 20, 10, 10, 15, 15, 15, 20, 25, 35, 60, 100, 220, 900, 900])

#atlas = np.array([3.453, 3.767, 3.538, 3.094, 2.228, 1.899, 1.558, 1.145, 0.6746, 0.3516, 0.1407, 0.02837, 0.00127])*bin_sizes
#atlas_err= np.array([0.247115358, 0.270325729, 0.271781162, 0.219636063, 0.192608411, 0.177392221, 0.132056806, 0.106901824, 0.075608201, 0.035838248, 0.01877232, 0.004532494, 0.000427902])*bin_sizes
"""
atlas15 = np.array([3.453, 3.453, 3.767, 3.538, 3.094, 2.228, 1.899, 1.558, 1.145, 0.6746, 0.3516, 0.1407, 0.02837, 0.00127, 0.00127])*bin_sizes15
atlas15_err= np.array([0.247115358, 0.247115358, 0.270325729, 0.271781162, 0.219636063, 0.192608411, 0.177392221, 0.132056806, 0.106901824, 0.075608201, 0.035838248, 0.01877232, 0.004532494, 0.000427902, 0.000427902])*bin_sizes15



#print(atlas/2)
#print(atlas_err/2)

matrix_nnlo_plus_nnll = 2*np.array([27.603294, 27.603294, 15.081798, 14.581068, 19.636623, 16.476035, 13.538172, 14.123358, 12.791331, 11.772087, 10.772255, 6.8853558, 3.2612599, 0.73267258, 0.73267258])
matrix_nnlo_plus_nnll_min = 2*np.array([26.946828, 26.946828, 14.743792, 14.268309, 19.219296, 16.143792, 13.278251, 13.868299, 12.557001, 11.543792, 10.55314, 6.739068, 3.1930373, 0.71416354, 0.71416354])
matrix_nnlo_plus_nnll_max = 2*np.array([28.159048, 28.159048, 15.406034, 14.912714, 20.114192, 16.907486, 13.918219, 14.549298, 13.210522, 12.198224, 11.214221, 7.2144588, 3.4444632, 0.78156333, 0.78156333])

#matrix_nnlo_plus_nnll = 2*np.array([27.636919, 27.636919, 15.095345, 14.597371, 19.65931, 16.490982, 13.557724, 14.139633, 12.798895, 11.781295, 10.784972, 6.8898707, 3.2459466, 0.72248279, 0.72248279])
#matrix_nnlo_plus_nnll_min = 2*np.array([27.449987, 27.449987, 15.007011, 14.524937, 19.546947, 16.395318, 13.492471, 14.064795, 12.718779, 11.721945, 10.732448, 6.8506043, 3.2186815, 0.71331594, 0.71331594])
#matrix_nnlo_plus_nnll_max = 2*np.array([27.859022, 27.859022, 15.214144, 14.703088, 19.806468, 16.614847, 13.649901, 14.241654, 12.897025, 11.865087, 10.862564, 6.9466717, 3.2838753, 0.73549521, 0.73549521])



matrix_nlo_ew = 2*np.array([25.648298, 25.648298, 14.133931, 13.754045, 18.505229, 15.579244, 12.788682, 13.495198, 12.314601, 11.443918, 10.673656, 6.9371232, 3.4235559, 0.79091385, 0.79091385])
matrix_nlo_ew_min = 2*np.array([23.716738, 23.716738, 13.119033, 12.809054, 17.305497, 14.640366, 12.077129, 12.816008, 11.775048, 11.035557, 10.410357, 6.8709977, 3.3784404, 0.7604296, 0.7604296])
matrix_nlo_ew_max = 2*np.array([27.304238, 27.304238, 14.999116, 14.555462, 19.515701, 16.362826, 13.376572, 14.049032, 12.746215, 11.760373, 10.863331, 6.9677772, 3.460759, 0.823469, 0.823469])

matrix_nlo_photon = 2*np.array([0.19479288, 0.19479288, 0.11608064, 0.12409102, 0.18676383, 0.1746192, 0.15662201, 0.17856602, 0.17850965, 0.18474737, 0.19881783, 0.16103781, 0.10624382, 0.033798066, 0.033798066])
matrix_nlo_photon_min = 2*np.array([0.18957236, 0.18957236, 0.11315484, 0.12136751, 0.18306661, 0.17137563, 0.15395121, 0.17566529, 0.1757739, 0.18208559, 0.19617798, 0.15914333, 0.10514653, 0.033447382, 0.033447382])
matrix_nlo_photon_max = 2*np.array([0.19728989, 0.19728989, 0.11752271, 0.12536763, 0.1885088, 0.17622673, 0.1579901, 0.18016443, 0.1801421, 0.18648775, 0.20076665, 0.16266432, 0.10738152, 0.034247574, 0.034247574])

nlophoton_1=2*np.array([0.19479288, 0.19479288, 0.11608064, 0.12409102, 0.18676383, 0.1746192, 0.15662201, 0.17856602, 0.17850965, 0.18474737, 0.19881783, 0.16103781, 0.10624382, 0.033798066, 0.033798066])
nlophoton_05=2*np.array([0.19728989, 0.19728989, 0.11752271, 0.12536763, 0.1885088, 0.17622673, 0.1579901, 0.18016443, 0.1801421, 0.18648775, 0.20076665, 0.16266432, 0.10738152, 0.034247574, 0.034247574])
nlophoton_2=2*np.array([0.18957236, 0.18957236, 0.11315484, 0.12136751, 0.18306661, 0.17137563, 0.15395121, 0.17566529, 0.1757739, 0.18208559, 0.19617798, 0.15914333, 0.10514653, 0.033447382, 0.033447382])




matrix_lo = 2*np.array([26.215602, 26.215602, 14.484436, 14.128136, 19.082919, 16.148051, 13.329621, 14.146151, 12.995492, 12.169272, 11.472213, 7.5948254, 3.8834107, 0.97012323, 0.97012323])
matrix_lo_min = 2*np.array([24.271464, 24.271464, 13.460223, 13.172161, 17.864787, 15.189772, 12.599335, 13.445418, 12.435822, 11.743859, 11.197663, 7.5286175, 3.8283072, 0.93131328, 0.93131328])
matrix_lo_max = 2*np.array([27.873357, 27.873357, 15.352977, 14.93465, 20.103543, 16.943645, 13.929751, 14.714319, 13.440331, 12.496246, 11.667156, 7.6220736, 3.9296634, 1.0116261, 1.0116261])


del_nloewlo=matrix_nlo_ew/matrix_lo


nnllnnlonloew_centre=(del_nloewlo)*matrix_nnlo_plus_nnll
nnllnnlonloew_min=(del_nloewlo)*matrix_nnlo_plus_nnll_min
nnllnnlonloew_max=(del_nloewlo)*matrix_nnlo_plus_nnll_max


mcfm_nll_gg=2*bin_sizes15*np.array([9.23595e-02, 9.23595e-02, 7.66466e-02, 6.63246e-02, 5.49889e-02, 4.20910e-02, 3.12449e-02, 2.18580e-02, 1.39625e-02, 7.85788e-03, 3.53353e-03, 1.11774e-03, 1.84657e-04, 5.48301e-06, 5.48301e-06])
mcfm_nll_gg_min=2*bin_sizes15*np.array([7.58978e-02, 7.58978e-02, 6.33923e-02, 5.48003e-02, 4.57568e-02, 3.50824e-02, 2.59196e-02, 1.83816e-02, 1.17533e-02, 6.67415e-03, 2.94683e-03, 9.23977e-04, 1.50656e-04, 4.56072e-06, 4.56072e-06])
mcfm_nll_gg_max=2*bin_sizes15*np.array([1.16059e-01, 1.16059e-01, 9.56980e-02, 8.23264e-02, 6.79834e-02, 5.18156e-02, 3.83359e-02, 2.68288e-02, 1.69067e-02, 9.58508e-03, 4.24451e-03, 1.36997e-03, 2.30640e-04, 2.03023e-05, 2.03023e-05])

ggnll_050050050=2*bin_sizes15*np.array([9.23595e-02, 9.23595e-02, 7.66466e-02, 6.63246e-02, 5.49889e-02, 4.20910e-02, 3.12449e-02, 2.18580e-02, 1.39625e-02, 7.85788e-03, 3.53353e-03, 1.11774e-03, 1.84657e-04, 5.48301e-06, 5.48301e-06])
ggnll_050050025=2*bin_sizes15*np.array([1.11099e-01, 1.11099e-01, 9.23142e-02, 8.00798e-02, 6.63203e-02, 5.05925e-02, 3.74031e-02, 2.61660e-02, 1.66514e-02, 9.36469e-03, 4.14827e-03, 1.29550e-03, 2.12401e-04, 6.16110e-06, 6.16110e-06])
ggnll_050050100=2*bin_sizes15*np.array([9.24769e-02, 9.24769e-02, 7.71351e-02, 6.74503e-02, 5.65027e-02, 4.32405e-02, 3.20537e-02, 2.28897e-02, 1.47339e-02, 8.33242e-03, 3.77192e-03, 1.24536e-03, 2.08960e-04, 2.03023e-05, 2.03023e-05])
ggnll_025025050=2*bin_sizes15*np.array([1.05127e-01, 1.05127e-01, 8.71411e-02, 7.56721e-02, 6.33612e-02, 4.86565e-02, 3.60614e-02, 2.55328e-02, 1.63131e-02, 9.31544e-03, 4.22714e-03, 1.36997e-03, 2.30640e-04, 7.10832e-06, 7.10832e-06])
ggnll_025050050=2*bin_sizes15*np.array([1.16059e-01, 1.16059e-01, 9.56980e-02, 8.23264e-02, 6.79834e-02, 5.18156e-02, 3.83359e-02, 2.68288e-02, 1.69067e-02, 9.58508e-03, 4.24451e-03, 1.32781e-03, 2.16224e-04, 6.53909e-06, 6.53909e-06])
ggnll_050025050=2*bin_sizes15*np.array([8.33621e-02, 8.33621e-02, 7.01322e-02, 6.14459e-02, 5.09730e-02, 3.92575e-02, 2.93679e-02, 2.08735e-02, 1.33625e-02, 7.64063e-03, 3.51248e-03, 1.14763e-03, 1.97345e-04, 6.16443e-06, 6.16443e-06])
ggnll_050100050=2*bin_sizes15*np.array([9.82133e-02, 9.82133e-02, 8.05333e-02, 6.91299e-02, 5.72014e-02, 4.35789e-02, 3.19839e-02, 2.24118e-02, 1.41317e-02, 7.89820e-03, 3.46793e-03, 1.07045e-03, 1.75424e-04, 4.97997e-06, 4.97997e-06])
ggnll_100050050=2*bin_sizes15*np.array([7.58978e-02, 7.58978e-02, 6.33923e-02, 5.48003e-02, 4.57568e-02, 3.50824e-02, 2.59196e-02, 1.83816e-02, 1.17533e-02, 6.67415e-03, 3.02183e-03, 9.65252e-04, 1.61242e-04, 4.90374e-06, 4.90374e-06])
ggnll_100100050=2*bin_sizes15*np.array([8.09774e-02, 8.09774e-02, 6.67896e-02, 5.74544e-02, 4.72613e-02, 3.63208e-02, 2.66436e-02, 1.87698e-02, 1.18804e-02, 6.69823e-03, 2.94683e-03, 9.23977e-04, 1.50656e-04, 4.56072e-06, 4.56072e-06])



ggphoton_nll_050050050=ggnll_050050050+nlophoton_1
ggphoton_nll_050050025=ggnll_050050025+nlophoton_1
ggphoton_nll_050050100=ggnll_050050100+nlophoton_1
ggphoton_nll_025025050=ggnll_025025050+nlophoton_05
ggphoton_nll_025050050=ggnll_025050050+nlophoton_1
ggphoton_nll_050025050=ggnll_050025050+nlophoton_05
ggphoton_nll_050100050=ggnll_050100050+nlophoton_2
ggphoton_nll_100050050=ggnll_100050050+nlophoton_1
ggphoton_nll_100100050=ggnll_100100050+nlophoton_2





ggphoton_nll_min=[]
ggphoton_nll_max=[]

for i in range(0, len(ggphoton_nll_050050050)):
    values=[ggphoton_nll_050050050[i], ggphoton_nll_050050025[i], ggphoton_nll_050050100[i], ggphoton_nll_025025050[i], ggphoton_nll_025050050[i], ggphoton_nll_050025050[i], ggphoton_nll_050100050[i], ggphoton_nll_100050050[i], ggphoton_nll_100100050[i]]
    ggphoton_nll_min.append(np.min(values))
    ggphoton_nll_max.append(np.max(values))

ggphoton_nll_min=np.array(ggphoton_nll_min)
ggphoton_nll_max=np.array(ggphoton_nll_max)

ggphoton_nll_err=(ggphoton_nll_max-ggphoton_nll_min)/2

err_qq=(nnllnnlonloew_max-nnllnnlonloew_min)/2

err_sm=(err_qq**2 + ggphoton_nll_err**2)**0.5

print("errs")
print(err_qq)
print(ggphoton_nll_err)
print(err_sm)


nnllnnlonloew_ggphoton_centre=nnllnnlonloew_centre+ggphoton_nll_050050050
nnllnnlonloew_ggphoton_max=nnllnnlonloew_ggphoton_centre+err_sm
nnllnnlonloew_ggphoton_min=nnllnnlonloew_ggphoton_centre-err_sm


nnllnnlonloew_ggphoton_centre_old=nnllnnlonloew_centre+mcfm_nll_gg + matrix_nlo_photon
nnllnnlonloew_ggphoton_max_old=nnllnnlonloew_max+mcfm_nll_gg_max + matrix_nlo_photon_max
nnllnnlonloew_ggphoton_min_old=nnllnnlonloew_min+mcfm_nll_gg_min + matrix_nlo_photon_min

print(nnllnnlonloew_ggphoton_max_old/nnllnnlonloew_ggphoton_max)
print(nnllnnlonloew_ggphoton_min_old/nnllnnlonloew_ggphoton_min)

nnllnnlonloew_ggphoton_centre_1=nnllnnlonloew_ggphoton_centre
nnllnnlonloew_ggphoton_min_1=nnllnnlonloew_ggphoton_min
nnllnnlonloew_ggphoton_max_1=nnllnnlonloew_ggphoton_max

print(nnllnnlonloew_ggphoton_centre)
print(nnllnnlonloew_ggphoton_min)
print(nnllnnlonloew_ggphoton_max)

"""
atlas15=2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas.npy"))
atlas15_err=2*array_for_plot(np.load("../Data_numpy_for_figures/13TeV_ATLAS/mll_atlas_err.npy"))


nnllnnlonloew_ggphoton_centre=2*array_for_plot(np.load("../SM_Construction/mll_13TeV_veto35_sm_centre.npy"))
nnllnnlonloew_ggphoton_min=2*array_for_plot(np.load("../SM_Construction/mll_13TeV_veto35_sm_min.npy"))
nnllnnlonloew_ggphoton_max=2*array_for_plot(np.load("../SM_Construction/mll_13TeV_veto35_sm_max.npy"))

print(nnllnnlonloew_ggphoton_centre)
print(nnllnnlonloew_ggphoton_min)
print(nnllnnlonloew_ggphoton_max)

#print(nnllnnlonloew_ggphoton_centre-nnllnnlonloew_ggphoton_centre_1)
#print(nnllnnlonloew_ggphoton_min-nnllnnlonloew_ggphoton_min_1)
#print(nnllnnlonloew_ggphoton_max-nnllnnlonloew_ggphoton_max_1)

bin_centres = [65, 80, 90, 102.5, 117.5, 132.5, 150, 172.5, 202.5, 250, 330, 490, 1050]

bins15 = [0, 55, 75, 85, 95, 110, 125, 140, 160, 185, 220, 280, 380, 600, 1500]
test_data= [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13]

plt.figure(figsize=(16, 12),dpi=100)

fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [2, 1]}, sharex=True)
#axs[0].set_title(r"MATRIX vs ATLAS",\
#               fontsize=18,color="black")
axs[1].set_xlabel(r"$M_{e\mu}$ [GeV] ",\
               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{dM_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r" Theory / Data",\
               fontsize=13,color="black")
#axs[0].xaxis.set_visible(False)

#axs[0].annotate(r'ATLAS', 
#            xy=(56,  1.95*10**2), 
#            fontsize=15,
#            fontweight="bold",
#            alpha=0.5,
#            color="k",
#            ha='left', 
#            va='top',
#            multialignment='left')
axs[0].annotate(r'$\sqrt{s} = 13$TeV, $36.1$fb$^{-1}$', 
            xy=(56,  1.2*4*10**1), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
axs[0].annotate(r'$\, p p\, \to\, e^{\pm}\nu\mu^{\mp}\nu, $', 
            xy=(56, 1.7*10**1), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')

#axs[0].step(bins15, test_data, color='pink', label='ATLAS', where="post", linewidth=0.5)

#axs[0].step(bins15, atlas15/bin_sizes15, color='grey', label='ATLAS Data (10.17182/hepdata.89225.v1/t7)', where="post", linewidth=1)
axs[0].step(bins15, atlas15/bin_sizes15, color='grey', label='ATLAS Data 2019', where="post", linewidth=1)
axs[0].fill_between(bins15, (atlas15-atlas15_err)/bin_sizes15, (atlas15+atlas15_err)/bin_sizes15,
                     color='grey', alpha=0.5, step="post")


print(nnllnnlonloew_ggphoton_centre)
axs[0].step(bins15, nnllnnlonloew_ggphoton_centre/bin_sizes15, color='b', label=r'$qq$ (NNLO+NNLL$_{\mathrm{QCD}}\times$NLO$_{\mathrm{EW}}$), $\gamma\gamma$ (NLO), $gg$ (NLL)', where="post", linewidth=1)
axs[0].fill_between(bins15, nnllnnlonloew_ggphoton_min/bin_sizes15, nnllnnlonloew_ggphoton_max/bin_sizes15,
                     color='b', alpha=0.5, step="post")



axs[0].semilogy()
leg = axs[0].legend(loc="lower left", fontsize=11, frameon=False, labelcolor="k")

for t in leg.texts:
    t.set_alpha(0.6)

axs[0].set_xlim(55, 1500)
#axs[0].set_ylim(0.75*10**-4, 3*10**2)
axs[0].set_ylim(0.75*10**-4, 80)


ratio_matrix_all=(nnllnnlonloew_ggphoton_centre)/(atlas15)
ratio_matrix_all_min=(nnllnnlonloew_ggphoton_min)/(atlas15)
ratio_matrix_all_max=(nnllnnlonloew_ggphoton_max)/(atlas15)


#axs[1].errorbar(bin_centres, (atlas/nnllnnlonloew_ggphoton_centre[1:14]), yerr=atlas_err/nnllnnlonloew_ggphoton_centre[1:14], fmt='x', color='k')
axs[1].step(bins15, atlas15/(atlas15) , color='grey', where="post")
axs[1].fill_between(bins15, (atlas15-atlas15_err)/(atlas15), (atlas15+atlas15_err)/(atlas15), color='grey', alpha=0.3, step="post")

axs[1].step(bins15, ratio_matrix_all, color='b', where="post")

axs[1].fill_between(bins15, ratio_matrix_all_min, ratio_matrix_all_max,
                     color='b', alpha=0.5, step="post")                     
axs[0].set_xlim(55, 1500)
axs[0].loglog()
axs[1].set_ylim(0.6, 1.4)

axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)
#axs[1].grid()
plt.subplots_adjust(hspace=0.1)
#plt.tight_layout()

plt.savefig("figure_6.pdf", bbox_inches='tight')

