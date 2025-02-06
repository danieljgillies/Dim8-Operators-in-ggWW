import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '..')

from plot_funcs import round_to_5, array_for_plot

bins=round_to_5(np.logspace(np.log10(200), np.log10(4000), 17))
print(bins)
bin_widths=bins[1:17]-bins[0:16]
bin_widths18=np.array([41.1817, 41.1817, 49.6614, 59.8871, 72.2183, 87.0887, 105.021, 126.6458, 152.7232, 184.1698, 222.093, 267.823, 322.97, 389.473, 469.668, 566.377, 682.999, 682.999])


"""
#MATRIX
#Old
#nnllnnlo_centre=2*3000*np.array([11.566163, 11.566163, 7.685741, 4.7633813, 2.7397298, 1.491574, 0.77753524, 0.39711564, 0.19630997, 0.093249664, 0.042387383, 0.018042554, 0.0071327232, 0.0025387694, 0.00080482328, 0.00021758338, 4.8711221e-05, 4.8711221e-05])
#nnllnnlo_min=2*3000*np.array([11.343429, 11.343429, 7.530978, 4.661844, 2.6812585, 1.4592339, 0.76150776, 0.38794496, 0.19129912, 0.090619762, 0.04103044, 0.017403648, 0.006852311, 0.002429927, 0.00076511136, 0.00020600008, 4.6145095e-05, 4.6145095e-05])
#nnllnnlo_max=2*3000*np.array([11.995234, 11.995234, 8.0066247, 4.9861359, 2.8809368, 1.5757553, 0.82449863, 0.42277543, 0.20970162, 0.099909291, 0.045548061, 0.019427594, 0.0076955351, 0.0027415644, 0.00087056858, 0.00023542745, 5.247156e-05, 5.247156e-05])

#nnlo_centre=2*3000*np.array([11.565615, 11.565615, 7.6852724, 4.7661742, 2.7336293, 1.4857702, 0.76946636, 0.39182155, 0.19277728, 0.091149158, 0.041341975, 0.017522463, 0.0069185061, 0.0024535291, 0.00078029884, 0.00021029352, 4.5666504e-05, 4.5666504e-05])
#nnlo_min=2*3000*np.array([11.497911, 11.497911, 7.6390091, 4.7372814, 2.7156889, 1.4762808, 0.76194574, 0.38779326, 0.19031895, 0.089729459, 0.040658972, 0.017181122, 0.0067605729, 0.0023851099, 0.00076000637, 0.00020377673, 4.3434792e-05, 4.3434792e-05])
#nnlo_max=2*3000*np.array([11.657624, 11.657624, 7.7486201, 4.8058818, 2.7600963, 1.5010859, 0.78025171, 0.39797751, 0.19641569, 0.093174725, 0.042347779, 0.018010537, 0.0071342819, 0.0025410513, 0.00080743862, 0.00021849945, 4.8218253e-05, 4.8218253e-05])

#nnll_centre=2*3000*np.array([11.115009, 11.115009, 7.3623271, 4.5406057, 2.6157002, 1.423193, 0.74991066, 0.38488458, 0.19149548, 0.09153185, 0.041651886, 0.017821831, 0.0070461195, 0.0025227433, 0.00079631587, 0.00021568982, 4.995235e-05, 4.995235e-05])
#nnll_min=2*3000*np.array([10.794048, 10.794048, 7.1489289, 4.4093573, 2.5412217, 1.3837402, 0.72732746, 0.37179259, 0.18418938, 0.08764244, 0.039689767, 0.016895488, 0.006642561, 0.0023639926, 0.00074156793, 0.00019965427, 4.6035399e-05, 4.6035399e-05])
#nnll_max=2*3000*np.array([11.749972, 11.749972, 7.8239497, 4.8506664, 2.8084769, 1.535066, 0.81222861, 0.41844839, 0.20889307, 0.1001355, 0.045675847, 0.019579438, 0.0077511429, 0.0027770101, 0.00087658308, 0.00023732547, 5.49401e-05, 5.49401e-05])
#Old ENd

nnllnnlo_centre=2*3000*np.array([11.566163, 11.566163, 7.685741, 4.7633813, 2.7397298, 1.491574, 0.77753524, 0.39711564, 0.19630997, 0.093249664, 0.042387383, 0.018042554, 0.0071327232, 0.0025387694, 0.00080482328, 0.00021758338, 5.0093331e-05, 5.0093331e-05])
nnllnnlo_min=2*3000*np.array([11.343429, 11.343429, 7.530978, 4.661844, 2.6812585, 1.4592339, 0.76150776, 0.38794496, 0.19129912, 0.090619762, 0.04103044, 0.017403648, 0.006852311, 0.002429927, 0.00076511136, 0.00020600008, 4.7301851e-05, 4.7301851e-05])
nnllnnlo_max=2*3000*np.array([11.995234, 11.995234, 8.0066247, 4.9861359, 2.8809368, 1.5757553, 0.82449863, 0.42277543, 0.20970162, 0.099909291, 0.045548061, 0.019427594, 0.0076955351, 0.0027415644, 0.00087056858, 0.00023542745, 5.4177057e-05, 5.4177057e-05])
nnlo_centre=2*3000*np.array([11.565615, 11.565615, 7.6852724, 4.7661742, 2.7336293, 1.4857702, 0.76946636, 0.39182155, 0.19277728, 0.091149158, 0.041341975, 0.017522463, 0.0069185061, 0.0024535291, 0.00078029884, 0.00021029352, 4.7950355e-05, 4.7950355e-05])
#nnlo_min=2*3000*np.array([11.497911, 11.497911, 7.6390091, 4.7372814, 2.7156889, 1.4762808, 0.76194574, 0.38779326, 0.19031895, 0.089729459, 0.040658972, 0.017181122, 0.0067605729, 0.0023851099, 0.00076000637, 0.00020377673, 4.612155e-05, 4.612155e-05])
#nnlo_max=2*3000*np.array([11.657624, 11.657624, 7.7486201, 4.8058818, 2.7600963, 1.5010859, 0.78025171, 0.39797751, 0.19641569, 0.093174725, 0.042347779, 0.018010537, 0.0071342819, 0.0025410513, 0.00080743862, 0.00021849945, 5.0178131e-05, 5.0178131e-05])
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


gglo_centre=bin_widths18*2*3000*np.array([1.26734e-02, 1.26734e-02, 6.51672e-03, 3.21223e-03, 1.47259e-03, 6.19455e-04, 2.41934e-04, 8.74549e-05, 2.96087e-05, 9.30379e-06, 2.71946e-06, 7.30760e-07, 1.81641e-07, 4.12819e-08, 7.95592e-09, 1.36223e-09, 1.87800e-10, 1.87800e-10])
gglo_min=bin_widths18*2*3000*np.array([1.02503e-02, 1.02503e-02, 5.22883e-03, 2.56007e-03, 1.16561e-03, 4.87075e-04, 1.88706e-04, 6.77802e-05, 2.28442e-05, 7.10102e-06, 2.07397e-06, 5.53029e-07, 1.36147e-07, 3.07377e-08, 5.90257e-09, 1.00963e-09, 1.34663e-10, 1.34663e-10])
gglo_max=bin_widths18*2*3000*np.array([1.58875e-02, 1.58875e-02, 8.24098e-03, 4.09774e-03, 1.89183e-03, 8.02629e-04, 3.15717e-04, 1.15084e-04, 3.92605e-05, 1.24067e-05, 3.66317e-06, 9.86425e-07, 2.47132e-07, 5.69607e-08, 1.10466e-08, 1.92877e-09, 2.60394e-10, 2.60394e-10])

logg_050_050=bin_widths18*2*3000*np.array([1.26734e-02, 1.26734e-02, 6.51672e-03, 3.21223e-03, 1.47259e-03, 6.19455e-04, 2.41934e-04, 8.74549e-05, 2.96087e-05, 9.30379e-06, 2.71946e-06, 7.30760e-07, 1.81641e-07, 4.12819e-08, 7.95592e-09, 1.36223e-09, 1.87800e-10, 1.87800e-10])
logg_025_025=bin_widths18*2*3000*np.array([1.58875e-02, 1.58875e-02, 8.24098e-03, 4.09774e-03, 1.89183e-03, 8.02629e-04, 3.15717e-04, 1.15084e-04, 3.92605e-05, 1.24067e-05, 3.66317e-06, 9.86425e-07, 2.47132e-07, 5.69607e-08, 1.10466e-08, 1.92877e-09, 2.60394e-10, 2.60394e-10])
logg_025_050=bin_widths18*2*3000*np.array([1.56012e-02, 1.56012e-02, 7.98134e-03, 3.91806e-03, 1.78818e-03, 7.49127e-04, 2.90886e-04, 1.04808e-04, 3.53847e-05, 1.10487e-05, 3.23288e-06, 8.63918e-07, 2.13426e-07, 4.85242e-08, 9.28585e-09, 1.58722e-09, 2.14542e-10, 2.14542e-10])
logg_050_025=bin_widths18*2*3000*np.array([1.29095e-02, 1.29095e-02, 6.72850e-03, 3.36053e-03, 1.55841e-03, 6.64207e-04, 2.62179e-04, 9.59271e-05, 3.29172e-05, 1.04162e-05, 3.08957e-06, 8.35024e-07, 2.09916e-07, 4.81687e-08, 9.69241e-09, 1.66101e-09, 2.24881e-10, 2.24881e-10])
logg_050_100=bin_widths18*2*3000*np.array([1.23607e-02, 1.23607e-02, 6.28102e-03, 3.06425e-03, 1.38981e-03, 5.79001e-04, 2.23203e-04, 8.01353e-05, 2.68570e-05, 8.31448e-06, 2.42857e-06, 6.39549e-07, 1.58446e-07, 3.56380e-08, 6.86714e-09, 1.14965e-09, 1.53773e-10, 1.53773e-10])
logg_100_050=bin_widths18*2*3000*np.array([1.05096e-02, 1.05096e-02, 5.42571e-03, 2.68417e-03, 1.23493e-03, 5.21104e-04, 2.04321e-04, 7.40782e-05, 2.51907e-05, 7.93016e-06, 2.32975e-06, 6.28961e-07, 1.55893e-07, 3.57670e-08, 6.87201e-09, 1.18523e-09, 1.61603e-10, 1.61603e-10])
logg_100_100=bin_widths18*2*3000*np.array([1.02503e-02, 1.02503e-02, 5.22883e-03, 2.56007e-03, 1.16561e-03, 4.87075e-04, 1.88706e-04, 6.77802e-05, 2.28442e-05, 7.10102e-06, 2.07397e-06, 5.53029e-07, 1.36147e-07, 3.07377e-08, 5.90257e-09, 1.00963e-09, 1.34663e-10, 1.34663e-10])






ggnll_centre=bin_widths18*2*3000*np.array([6.45544e-03, 6.45544e-03, 3.07100e-03, 1.40140e-03, 5.90418e-04, 2.27091e-04, 8.05973e-05, 2.63558e-05, 8.09415e-06, 2.27812e-06, 5.99358e-07, 1.44374e-07, 3.21025e-08, 6.41989e-09, 1.17816e-09, 1.85236e-10, 2.29779e-11, 2.29779e-11])
ggnll_min=bin_widths18*2*3000*np.array([5.48801e-03, 5.48801e-03, 2.59680e-03, 1.17376e-03, 4.90662e-04, 1.87089e-04, 6.57041e-05, 2.13273e-05, 6.46158e-06, 1.80141e-06, 4.67080e-07, 1.11173e-07, 2.44243e-08, 4.80111e-09, 8.72933e-10, 1.32022e-10, 1.59206e-11, 1.59206e-11])
ggnll_max=bin_widths18*2*3000*np.array([7.80447e-03, 7.80447e-03, 3.68548e-03, 1.68809e-03, 7.21053e-04, 2.81473e-04, 1.01219e-04, 3.38626e-05, 1.04788e-05, 3.02858e-06, 8.09445e-07, 1.99010e-07, 4.47757e-08, 9.19993e-09, 1.76740e-09, 2.74790e-10, 3.72237e-11, 3.72237e-11])

ggnll_050050050=bin_widths18*2*3000*np.array([6.45544e-03, 6.45544e-03, 3.07100e-03, 1.40140e-03, 5.90418e-04, 2.27091e-04, 8.05973e-05, 2.63558e-05, 8.09415e-06, 2.27812e-06, 5.99358e-07, 1.44374e-07, 3.21025e-08, 6.41989e-09, 1.17816e-09, 1.85236e-10, 2.29779e-11, 2.29779e-11])
ggnll_050050025=bin_widths18*2*3000*np.array([7.69860e-03, 7.69860e-03, 3.63274e-03, 1.63955e-03, 6.83733e-04, 2.60289e-04, 9.11968e-05, 2.94857e-05, 8.92076e-06, 2.48392e-06, 6.41026e-07, 1.52984e-07, 3.30940e-08, 6.58106e-09, 1.18220e-09, 1.78093e-10, 2.15456e-11, 2.15456e-11])
ggnll_050050100=bin_widths18*2*3000*np.array([6.86841e-03, 6.86841e-03, 3.33433e-03, 1.54048e-03, 6.57648e-04, 2.56413e-04, 9.28084e-05, 3.08854e-05, 9.54617e-06, 2.82411e-06, 8.09445e-07, 1.86222e-07, 4.09492e-08, 8.96161e-09, 1.60058e-09, 2.51474e-10, 3.70995e-11, 3.70995e-11])
ggnll_025025050=bin_widths18*2*3000*np.array([7.59995e-03, 7.59995e-03, 3.65937e-03, 1.68809e-03, 7.21053e-04, 2.81473e-04, 1.01219e-04, 3.38626e-05, 1.04788e-05, 3.02858e-06, 8.05588e-07, 1.99010e-07, 4.47757e-08, 9.19993e-09, 1.76740e-09, 2.74790e-10, 3.72237e-11, 3.72237e-11])
ggnll_025050050=bin_widths18*2*3000*np.array([7.80447e-03, 7.80447e-03, 3.68548e-03, 1.66873e-03, 6.97816e-04, 2.66678e-04, 9.39193e-05, 3.04925e-05, 9.27850e-06, 2.59614e-06, 6.76043e-07, 1.61675e-07, 3.57428e-08, 7.08296e-09, 1.29198e-09, 2.01124e-10, 2.47067e-11, 2.47067e-11])
ggnll_050025050=bin_widths18*2*3000*np.array([6.28935e-03, 6.28935e-03, 3.05154e-03, 1.41993e-03, 6.10339e-04, 2.39609e-04, 8.71017e-05, 2.91820e-05, 9.13828e-06, 2.65651e-06, 7.14206e-07, 1.76607e-07, 4.02455e-08, 8.39720e-09, 1.58206e-09, 2.58328e-10, 3.36677e-11, 3.36677e-11])
ggnll_050100050=bin_widths18*2*3000*np.array([6.46548e-03, 6.46548e-03, 3.03112e-03, 1.35953e-03, 5.63672e-04, 2.13314e-04, 7.42661e-05, 2.38500e-05, 7.17279e-06, 1.97854e-06, 5.08833e-07, 1.20783e-07, 2.58628e-08, 5.16238e-09, 9.25514e-10, 1.38877e-10, 1.67378e-11, 1.67378e-11])
ggnll_100050050=bin_widths18*2*3000*np.array([5.48801e-03, 5.48801e-03, 2.63624e-03, 1.21283e-03, 5.13861e-04, 1.99346e-04, 7.12471e-05, 2.35256e-05, 7.28787e-06, 2.07030e-06, 5.47813e-07, 1.34830e-07, 2.97420e-08, 6.08524e-09, 1.12387e-09, 1.73717e-10, 2.23835e-11, 2.23835e-11])
ggnll_100100050=bin_widths18*2*3000*np.array([5.49776e-03, 5.49776e-03, 2.59680e-03, 1.17376e-03, 4.90662e-04, 1.87089e-04, 6.57041e-05, 2.13273e-05, 6.46158e-06, 1.80141e-06, 4.67080e-07, 1.11173e-07, 2.44243e-08, 4.80111e-09, 8.72933e-10, 1.32022e-10, 1.59206e-11, 1.59206e-11])



nloew_1=2*3000*np.array([11.511081, 11.511081, 7.7478559, 4.8803813, 2.8699538, 1.5934634, 0.84729179, 0.43744109, 0.21696504, 0.10358812, 0.046169964, 0.019171835, 0.007251576, 0.0024461489, 0.00072137817, 0.00018109279, 3.9797881e-05, 3.9797881e-05])
nloew_05=2*3000*np.array([11.101848, 11.101848, 7.5527253, 4.8098925, 2.8600202, 1.6055313, 0.86302901, 0.45040619, 0.22576909, 0.10893574, 0.049066372, 0.020592195, 0.0078722222, 0.002683551, 0.00079926396, 0.00020222444, 4.4614433e-05, 4.4614433e-05])
nloew_2=2*3000*np.array([11.829411, 11.829411, 7.8898836, 4.9233561, 2.867654, 1.5770128, 0.83060556, 0.42475281, 0.20869729, 0.098700565, 0.043576399, 0.01792186, 0.0067137125, 0.002243168, 0.00065556629, 0.00016339969, 3.5779929e-05, 3.5779929e-05])

 

nlophoton_1=2*3000*np.array([0.19810551, 0.19810551, 0.1538622, 0.11262551, 0.077749794, 0.050374167, 0.030672802, 0.017651956, 0.0096082426, 0.0049169342, 0.002365917, 0.0010634943, 0.00044148895, 0.00016755527, 5.7198414e-05, 1.7122486e-05, 4.3313385e-06, 4.3313385e-06])
nlophoton_05=2*3000*np.array([0.2001651, 0.2001651, 0.15559145, 0.11393307, 0.078686114, 0.051000369, 0.031083826, 0.017906348, 0.0097590383, 0.0050017041, 0.0024113818, 0.0010863463, 0.00045210895, 0.00017206034, 5.8892686e-05, 1.7673038e-05, 4.479545e-06, 4.479545e-06])
nlophoton_2=2*3000*np.array([0.19506661, 0.19506661, 0.15158336, 0.11106255, 0.076730494, 0.049748421, 0.030292895, 0.017432152, 0.009484954, 0.0048507582, 0.0023316198, 0.0010467087, 0.00043386039, 0.00016438463, 5.6035729e-05, 1.6756966e-05, 4.2374953e-06, 4.2374953e-06])



lo_1=2*3000*np.array([12.295819, 12.295819, 8.3663669, 5.3392747, 3.1931267, 1.810972, 0.988312, 0.52545869, 0.26945906, 0.13331015, 0.062001067, 0.027009104, 0.010798608, 0.0038856795, 0.0012330404, 0.00033741612, 8.1084759e-05, 8.1084759e-05])
lo_05=2*3000*np.array([11.867498, 11.867498, 8.1618383, 5.2663418, 3.1847893, 1.8263814, 1.0076935, 0.54162471, 0.28072487, 0.14036726, 0.065978877, 0.029051824, 0.011741567, 0.0042706711, 0.0013692046, 0.00037790356, 9.129745e-05, 9.129745e-05])
lo_2=2*3000*np.array([12.626357, 12.626357, 8.5132186, 5.3819802, 3.1878335, 1.7906044, 0.96785689, 0.50965411, 0.25888112, 0.12685941, 0.058438534, 0.025211081, 0.0099813008, 0.0035565022, 0.0011180083, 0.00030354372, 7.2586503e-05, 7.2586503e-05])

nloew_centre=2*3000*np.array([11.511081, 11.511081, 7.7478559, 4.8803813, 2.8699538, 1.5934634, 0.84729179, 0.43744109, 0.21696504, 0.10358812, 0.046169964, 0.019171835, 0.007251576, 0.0024461489, 0.00072137817, 0.00018109279, 3.9797881e-05, 3.9797881e-05])
nloew_min=2*3000*np.array([11.101848, 11.101848, 7.5527253, 4.8098925, 2.8600202, 1.5770128, 0.83060556, 0.42475281, 0.20869729, 0.098700565, 0.043576399, 0.01792186, 0.0067137125, 0.002243168, 0.00065556629, 0.00016339969, 3.5779929e-05, 3.5779929e-05])
nloew_max=2*3000*np.array([11.829411, 11.829411, 7.8898836, 4.9233561, 2.8699538, 1.6055313, 0.86302901, 0.45040619, 0.22576909, 0.10893574, 0.049066372, 0.020592195, 0.0078722222, 0.002683551, 0.00079926396, 0.00020222444, 4.4614433e-05, 4.4614433e-05])

nlophoton_centre=2*3000*np.array([0.19810551, 0.19810551, 0.1538622, 0.11262551, 0.077749794, 0.050374167, 0.030672802, 0.017651956, 0.0096082426, 0.0049169342, 0.002365917, 0.0010634943, 0.00044148895, 0.00016755527, 5.7198414e-05, 1.7122486e-05, 4.3313385e-06, 4.3313385e-06])
nlophoton_min=2*3000*np.array([0.19506661, 0.19506661, 0.15158336, 0.11106255, 0.076730494, 0.049748421, 0.030292895, 0.017432152, 0.009484954, 0.0048507582, 0.0023316198, 0.0010467087, 0.00043386039, 0.00016438463, 5.6035729e-05, 1.6756966e-05, 4.2374953e-06, 4.2374953e-06])
nlophoton_max=2*3000*np.array([0.2001651, 0.2001651, 0.15559145, 0.11393307, 0.078686114, 0.051000369, 0.031083826, 0.017906348, 0.0097590383, 0.0050017041, 0.0024113818, 0.0010863463, 0.00045210895, 0.00017206034, 5.8892686e-05, 1.7673038e-05, 4.479545e-06, 4.479545e-06])

lo_centre=2*3000*np.array([12.295819, 12.295819, 8.3663669, 5.3392747, 3.1931267, 1.810972, 0.988312, 0.52545869, 0.26945906, 0.13331015, 0.062001067, 0.027009104, 0.010798608, 0.0038856795, 0.0012330404, 0.00033741612, 8.1084759e-05, 8.1084759e-05])
lo_min=2*3000*np.array([11.867498, 11.867498, 8.1618383, 5.2663418, 3.1847893, 1.7906044, 0.96785689, 0.50965411, 0.25888112, 0.12685941, 0.058438534, 0.025211081, 0.0099813008, 0.0035565022, 0.0011180083, 0.00030354372, 7.2586503e-05, 7.2586503e-05])
lo_max=2*3000*np.array([12.626357, 12.626357, 8.5132186, 5.3819802, 3.1931267, 1.8263814, 1.0076935, 0.54162471, 0.28072487, 0.14036726, 0.065978877, 0.029051824, 0.011741567, 0.0042706711, 0.0013692046, 0.00037790356, 9.129745e-05, 9.129745e-05])


del_nloew_1=nloew_1/lo_1


nnllnnlonloew_centre=nnllnnlo_centre*del_nloew_1
nnllnnlonloew_min=nnllnnlo_min*del_nloew_1
nnllnnlonloew_max=nnllnnlo_max*del_nloew_1


bin_centres=(bins[0:16] + bins[1:17])/2
bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))




plt.figure()


plt.step(bin_centres, nnllnnlo_centre/nnlo_centre -1 , color='k', where='mid')

plt.fill_between(bin_centres, nnllnnlo_min/nnlo_centre -1, nnllnnlo_max/nnlo_centre -1,
                     color='k', alpha=0.5, step='mid')

plt.step(bin_centres, nnllnnlonloew_centre/nnlo_centre -1, color='b', where='mid')

plt.fill_between(bin_centres, nnllnnlonloew_min/nnlo_centre -1, nnllnnlonloew_max/nnlo_centre -1,
                     color='b', alpha=0.5, step='mid')

plt.semilogx()



plt.xlim(200,4000)              
plt.tight_layout()
plt.savefig("nnllnnloewcheck_2.pdf", bbox_inches='tight')





bin_centres=(bins[0:16] + bins[1:17])/2
bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))



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


sm=nnllnnlonloew_centre+ggphoton_nll_050050050
sm_min=sm-err_sm
sm_max=sm+err_sm

print("fi")
print(nnllnnlonloew_centre/6000)
print(nnllnnlonloew_max/6000)
print(nnllnnlonloew_min/6000)
print(sm/6000)
print(sm_max/6000)
print(sm_min/6000)

"""
nnllnnlonloew_centre=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_centre.npy"))
nnllnnlonloew_min=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_min.npy"))
nnllnnlonloew_max=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_cross_nlo_ew_max.npy"))

print("se")
print(nnllnnlonloew_centre/6000)
print(nnllnnlonloew_max/6000)
print(nnllnnlonloew_min/6000)

nlophoton_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gammagamma_nlo_centre.npy"))
nlophoton_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gammagamma_nlo_min.npy"))
nlophoton_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gammagamma_nlo_max.npy"))


print(nlophoton_centre/6000)
print(nlophoton_max/6000)
print(nlophoton_min/6000)

ggnll_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_centre.npy"))
ggnll_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_min.npy"))
ggnll_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_max.npy"))




ggnll_050050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
ggnll_050050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=0.25MWW.npy"))
ggnll_050050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.5MWW__muresum=1.0MWW.npy"))
ggnll_025025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
ggnll_025050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.25MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
ggnll_050025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=0.25MWW__muresum=0.5MWW.npy"))
ggnll_050100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=0.5MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))
ggnll_100050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=0.5MWW__muresum=0.5MWW.npy"))
ggnll_100100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_gg_nll_qcd_murenorm=1.0MWW_mufac=1.0MWW__muresum=0.5MWW.npy"))

print(ggnll_050050050/(6000*bin_widths18))

sm=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_centre.npy"))
sm_min=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_min.npy"))
sm_max=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_veto35_sm_max.npy"))

print(sm/6000)
print(sm_max/6000)
print(sm_min/6000)

err_sm=(sm_max-sm_min)/2





plt.figure(figsize=(16, 12),dpi=1000)
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
#axs[0].set_title(r"Subleading Processes SM ATLAS 14TeV",\
#               fontsize=18,color="black")
axs[1].set_xlabel(r"$M_{e\mu}$ [GeV]",\
               fontsize=16,color="black")
axs[0].set_ylabel(r"$\frac{d\sigma}{M_{e\mu}}$ $\left[\frac{\mathrm{fb}}{\mathrm{GeV}}\right]$ ",\
               fontsize=20,color="black")
axs[1].set_ylabel(r"$\%$ Contribution",\
               fontsize=16,color="black")
#axs[0].xaxis.set_visible(False)
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
axs[0].annotate(r'$\sqrt{s} = 14$TeV, $\, p p\, \to\, e^{\pm}\nu\mu^{\mp}\nu$,  $p_{T, \mathrm{veto}}=35 \mathrm{GeV}$' , 
            xy=(205,  2*0.7*10**2), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
axs[0].annotate(r'NNPDF31_nnlo_as_0118_luxqed_nf_4', 
            xy=(205, 2*0.49*10**1), 
            fontsize=13,
            alpha=0.5,
            color="k",
            ha='left', 
            va='top',
            multialignment='left')
bin_centres=(bins[0:16] + bins[1:17])/2

bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))

axs[0].step(bin_centres, sm/(bin_widths18*3000), color='k', where='mid', linewidth=0.7)
axs[0].step(bin_centres, -sm/(bin_widths18*3000), color='k', where='mid', label=r'$qq$+$gg$+$\gamma\gamma$')

axs[0].fill_between(bin_centres, sm_min/(bin_widths18*3000), sm_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')

axs[0].step(bin_centres, nnllnnlonloew_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', linewidth=0.7)
axs[0].step(bin_centres, -nnllnnlonloew_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', label=r'$qq$-only (NNLO+NNLL$_{\mathrm{QCD}}\times$NLO$_{\mathrm{EW}}$) ')

axs[0].fill_between(bin_centres, nnllnnlonloew_min/(bin_widths18*3000), nnllnnlonloew_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')


axs[0].step(bin_centres, nlophoton_centre/(bin_widths18*3000), color='y', where='mid', linewidth=0.7)
axs[0].step(bin_centres, -nlophoton_centre/(bin_widths18*3000), color='y', where='mid', label=r'$\gamma\gamma $-only (NLO)')


axs[0].fill_between(bin_centres, nlophoton_min/(bin_widths18*3000), nlophoton_max/(bin_widths18*3000),
                     color='y', alpha=0.3, step='mid')


#axs[0].step(bin_centres, gglo_centre/(bin_widths18*3000), color='b', where='mid', linewidth=0.7)
#axs[0].step(bin_centres, -gglo_centre/(bin_widths18*3000), color='b', where='mid', label=r'$gg$-only (LO)')

#axs[0].fill_between(bin_centres, gglo_min/(bin_widths18*3000), gglo_max/(bin_widths18*3000),
#                     color='b', alpha=0.3, step='mid')

axs[0].step(bin_centres, ggnll_centre/(bin_widths18*3000), color='r', where='mid', linewidth=0.7)
axs[0].step(bin_centres, -ggnll_centre/(bin_widths18*3000), color='r', where='mid', label=r'$gg$-only (NLL)')


axs[0].fill_between(bin_centres, ggnll_min/(bin_widths18*3000), ggnll_max/(bin_widths18*3000),
                     color='r', alpha=0.3, step='mid')



axs[0].legend(loc="lower left", fontsize=11, frameon=False)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(5*10**-12, 4*10**3)


#err_gg=(gglo_max-gglo_min)/2




#err=(gglo_centre/sm)*((err_gg/gglo_centre)**2 + (err_sm/sm)**2)**0.5


#axs[1].step(bin_centres, 100*(gglo_centre/sm), color='b', where='mid', linewidth=0.7)
#axs[1].fill_between(bin_centres, 100*((gglo_centre/sm)-err), 100*((gglo_centre/sm)+err),
#                     color='b', alpha=0.5, step='mid')



err_gg=(ggnll_max-ggnll_min)/2


err=(ggnll_centre/sm)*((err_gg/ggnll_centre)**2 + (err_sm/sm)**2)**0.5


axs[1].step(bin_centres, 100*(ggnll_centre/sm), color='r', where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, 100*((ggnll_centre/sm)-err), 100*((ggnll_centre/sm)+err),
                     color='r', alpha=0.5, step='mid')



err_photon=(nlophoton_max-nlophoton_min)/2




err=(nlophoton_centre/sm)*((err_photon/nlophoton_centre)**2 + (err_sm/sm)**2)**0.5


axs[1].step(bin_centres, 100*(nlophoton_centre/sm), color='y', where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, 100*((nlophoton_centre/sm)-err), 100*((nlophoton_centre/sm)+err),
                     color='y', alpha=0.5, step='mid')



err_nnllnnlonloew=(nnllnnlonloew_max-nnllnnlonloew_min)/2

err=(nnllnnlonloew_centre/sm)*((err_nnllnnlonloew/nnllnnlonloew_centre)**2 + (err_sm/sm)**2)**0.5



axs[1].step(bin_centres, 100*(nnllnnlonloew_centre/sm), color='k', where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, 100*((nnllnnlonloew_centre/sm)-err), 100*((nnllnnlonloew_centre/sm)+err),
                     color='k', alpha=0.5, step='mid')


axs[1].loglog()

axs[1].set_ylim(10**-2, 120)
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)
axs[1].set_yticks([10**-2, 10**-1, 1, 10, 100])
axs[1].set_yticklabels(["0.01", "0.1", "1", "10", "100"])
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
#plt.tight_layout()
plt.savefig("figure_5a.pdf", bbox_inches='tight')

