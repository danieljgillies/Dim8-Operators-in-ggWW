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


nnlo_noveto_050050=2*3000*np.array([21.720349, 21.720349, 14.74502, 9.3833442, 5.5852519, 3.159148, 1.7028145, 0.88663578, 0.44459695, 0.21262424, 0.096666023, 0.041194055, 0.016240919, 0.0057577927, 0.0018089045, 0.00048596908, 0.00011086188, 0.00011086188])
nnlo_noveto_050100=2*3000*np.array([21.669689, 21.669689, 14.707137, 9.3570139, 5.5646243, 3.1456461, 1.6948478, 0.88195234, 0.44205889, 0.21136415, 0.096049833, 0.040915395, 0.016122713, 0.0057141227, 0.0017939307, 0.00048191416, 0.000109966, 0.000109966])
nnlo_noveto_200100=2*3000*np.array([20.802439, 20.802439, 14.131976, 8.9897874, 5.3504147, 3.0234116, 1.6322338, 0.85047037, 0.42701538, 0.20459602, 0.093151036, 0.039740045, 0.015680392, 0.0055696273, 0.0017466266, 0.00046968473, 0.00010701388, 0.00010701388])
nnlo_noveto_100100=2*3000*np.array([21.234452, 21.234452, 14.418387, 9.1717538, 5.4563811, 3.0834954, 1.6630529, 0.86592471, 0.43439166, 0.20791453, 0.094572654, 0.040315731, 0.015897156, 0.0056408612, 0.0017697532, 0.00047568688, 0.00010844992, 0.00010844992])
nnlo_noveto_100200=2*3000*np.array([21.224782, 21.224782, 14.402372, 9.1549827, 5.4408201, 3.0716677, 1.6554366, 0.86122289, 0.43172404, 0.20652747, 0.093890263, 0.040008659, 0.015769917, 0.0055935678, 0.0017528286, 0.00047063031, 0.00010722665, 0.00010722665])
nnlo_noveto_100050=2*3000*np.array([21.265649, 21.265649, 14.453944, 9.2030625, 5.4826015, 3.1017388, 1.6743234, 0.87255312, 0.43800209, 0.20972354, 0.095446362, 0.040707188, 0.016061285, 0.0057020214, 0.0017902379, 0.00048129752, 0.00010970264, 0.00010970264])
nnlo_noveto_200200=2*3000*np.array([20.802703, 20.802703, 14.116509, 8.9696706, 5.3312392, 3.0086099, 1.6225431, 0.84454125, 0.42366027, 0.20284862, 0.092293428, 0.03935315, 0.015519276, 0.0055089063, 0.0017253018, 0.00046335907, 0.0001054947,  0.0001054947])

nnlo_noveto_centre=2*3000*np.array([21.234452, 21.234452, 14.418387, 9.1717538, 5.4563811, 3.0834954, 1.6630529, 0.86592471, 0.43439166, 0.20791453, 0.094572654, 0.040315731, 0.015897156, 0.0056408612, 0.0017697532, 0.00047568688, 0.00010844992, 0.00010844992])

#nnlo_noveto_centre=2*3000*np.array([21.234452, 21.234452, 14.418387, 9.1717538, 5.4563811, 3.0834954, 1.6630529, 0.86592471, 0.43439166, 0.20791453, 0.094572654, 0.040315731, 0.015897156, 0.0056408612, 0.0017697532, 0.0017697532])


nnlo_noveto_min=[]
nnlo_noveto_max=[]

for i in range(0, len(nnlo_noveto_100100)):
    values=[nnlo_noveto_100100[i], nnlo_noveto_050050[i], nnlo_noveto_050100[i], nnlo_noveto_100050[i], nnlo_noveto_100200[i], nnlo_noveto_200100[i], nnlo_noveto_200200[i]]
    nnlo_noveto_min.append(np.min(values))
    nnlo_noveto_max.append(np.max(values))

nnlo_noveto_min=np.array(nnlo_noveto_min)
nnlo_noveto_max=np.array(nnlo_noveto_max)

nnlo_noveto_err=(nnlo_noveto_max-nnlo_noveto_min)/2



#nnlo_noveto_min=np.array([1.24814634e+05, 1.24814634e+05, 8.46990540e+04, 5.38180236e+04, 3.19874352e+04, 1.80516594e+04, 9.73525860e+03, 5.06724750e+03, 2.54196162e+03, 1.21709172e+03, 5.53760568e+02, 2.36118900e+02, 9.31156560e+01, 3.30534378e+01, 1.03518108e+01, 1.03518108e+01])
#nnlo_noveto_max=np.array([1.30322094e+05, 1.30322094e+05, 8.84701200e+04, 5.63000652e+04, 3.35115114e+04, 1.89548880e+04, 1.02168870e+04, 5.31981468e+03, 2.66758170e+03, 1.27574544e+03, 5.79996138e+02, 2.47164330e+02, 9.74455140e+01, 3.45467562e+01, 1.08534270e+01, 1.08534270e+01])

nloew_noveto_1=2*3000*np.array([11.511113, 11.511113, 7.7479197, 4.8802822, 2.8698695, 1.5934809, 0.84769667, 0.43728521, 0.21710801, 0.10353661, 0.046174803, 0.01915083, 0.0072525568, 0.0024454924, 0.00072092486, 0.00018083208, 3.9823136e-05, 3.9823136e-05])
nloew_noveto_05=2*3000*np.array([11.101887, 11.101887, 7.5527977, 4.8097935, 2.8599337, 1.6055518, 0.86343593, 0.45025436, 0.22591764, 0.10888192, 0.04907148, 0.020569664, 0.0078732798, 0.0026828296, 0.00079875395, 0.00020192778, 4.4642598e-05, 4.4642598e-05])
nloew_noveto_2=2*3000*np.array([11.829437, 11.829437, 7.8899399, 4.9232575, 2.8675719, 1.5770278, 0.83100722, 0.42459427, 0.20883494, 0.098651227, 0.043580997, 0.017902206, 0.006714625, 0.0022425665, 0.00065516012, 0.00016316853, 3.5802733e-05, 3.5802733e-05])
nlophoton_noveto_1=2*3000*np.array([0.55454036, 0.55454036, 0.44683043, 0.33947286, 0.24332704, 0.16433014, 0.104394, 0.062477448, 0.035171124, 0.018604705, 0.0092072904, 0.0042450513, 0.0018040918, 0.00069809119, 0.00024169604, 7.2953713e-05, 1.8520227e-05, 1.8520227e-05])
nlophoton_noveto_05=2*3000*np.array([0.54055495, 0.54055495, 0.4369668, 0.33310582, 0.23958348, 0.16238318, 0.10355534, 0.062226806, 0.035182571, 0.018696082, 0.0092974039, 0.0043085125, 0.0018411507, 0.00071657868, 0.00024962841, 7.5841908e-05, 1.9386948e-05, 1.9386948e-05])
nlophoton_noveto_2=2*3000*np.array([0.56657068, 0.56657068, 0.4553804, 0.34502917, 0.24661565, 0.16604847, 0.10513617, 0.062699387, 0.035160542, 0.018523485, 0.0091274554, 0.0041889941, 0.0017714685, 0.00068189169, 0.00023478752, 7.0457271e-05, 1.7778017e-05, 1.7778017e-05])
lo_noveto_1=2*3000*np.array([12.295819, 12.295819, 8.3663669, 5.3392747, 3.1931267, 1.810972, 0.98869523, 0.52528223, 0.2696097, 0.13325747, 0.062005948, 0.026988797, 0.010799532, 0.0038849941, 0.0012325474, 0.00033714988, 8.1110375e-05, 8.1110375e-05])
lo_noveto_05=2*3000*np.array([11.867498, 11.867498, 8.1618383, 5.2663418, 3.1847893, 1.8263814, 1.0080781, 0.54145167, 0.28088141, 0.1403122, 0.065984027, 0.029030043, 0.011742558, 0.0042699175, 0.0013686496, 0.00037760076, 9.1326002e-05, 9.1326002e-05])
lo_noveto_2=2*3000*np.array([12.626357, 12.626357, 8.5132186, 5.3819802, 3.1878335, 1.7906044, 0.96823745, 0.50947559, 0.25902614, 0.12680894, 0.058443175, 0.025192078, 0.0099821645, 0.0035558745, 0.0011175668, 0.00030330756, 7.2609646e-05, 7.2609646e-05])

nloew_noveto_centre=2*3000*np.array([11.511113, 11.511113, 7.7479197, 4.8802822, 2.8698695, 1.5934809, 0.84769667, 0.43728521, 0.21710801, 0.10353661, 0.046174803, 0.01915083, 0.0072525568, 0.0024454924, 0.00072092486, 0.00018083208, 3.9823136e-05, 3.9823136e-05])
nloew_noveto_min=2*3000*np.array([11.101887, 11.101887, 7.5527977, 4.8097935, 2.8599337, 1.5770278, 0.83100722, 0.42459427, 0.20883494, 0.098651227, 0.043580997, 0.017902206, 0.006714625, 0.0022425665, 0.00065516012, 0.00016316853, 3.5802733e-05, 3.5802733e-05])
nloew_noveto_max=2*3000*np.array([11.829437, 11.829437, 7.8899399, 4.9232575, 2.8698695, 1.6055518, 0.86343593, 0.45025436, 0.22591764, 0.10888192, 0.04907148, 0.020569664, 0.0078732798, 0.0026828296, 0.00079875395, 0.00020192778, 4.4642598e-05, 4.4642598e-05])
nlophoton_noveto_centre=2*3000*np.array([0.55454036, 0.55454036, 0.44683043, 0.33947286, 0.24332704, 0.16433014, 0.104394, 0.062477448, 0.035171124, 0.018604705, 0.0092072904, 0.0042450513, 0.0018040918, 0.00069809119, 0.00024169604, 7.2953713e-05, 1.8520227e-05, 1.8520227e-05])
nlophoton_noveto_min=2*3000*np.array([0.54055495, 0.54055495, 0.4369668, 0.33310582, 0.23958348, 0.16238318, 0.10355534, 0.062226806, 0.035160542, 0.018523485, 0.0091274554, 0.0041889941, 0.0017714685, 0.00068189169, 0.00023478752, 7.0457271e-05, 1.7778017e-05, 1.7778017e-05])
nlophoton_noveto_max=2*3000*np.array([0.56657068, 0.56657068, 0.4553804, 0.34502917, 0.24661565, 0.16604847, 0.10513617, 0.062699387, 0.035182571, 0.018696082, 0.0092974039, 0.0043085125, 0.0018411507, 0.00071657868, 0.00024962841, 7.5841908e-05, 1.9386948e-05, 1.9386948e-05])
lo_noveto_centre=2*3000*np.array([12.295819, 12.295819, 8.3663669, 5.3392747, 3.1931267, 1.810972, 0.98869523, 0.52528223, 0.2696097, 0.13325747, 0.062005948, 0.026988797, 0.010799532, 0.0038849941, 0.0012325474, 0.00033714988, 8.1110375e-05, 8.1110375e-05])
lo_noveto_min=2*3000*np.array([11.867498, 11.867498, 8.1618383, 5.2663418, 3.1847893, 1.7906044, 0.96823745, 0.50947559, 0.25902614, 0.12680894, 0.058443175, 0.025192078, 0.0099821645, 0.0035558745, 0.0011175668, 0.00030330756, 7.2609646e-05, 7.2609646e-05])





gglo_centre=bin_widths18*2*3000*np.array([1.26734e-02, 1.26734e-02, 6.51672e-03, 3.21223e-03, 1.47259e-03, 6.19455e-04, 2.41934e-04, 8.74549e-05, 2.96087e-05, 9.30379e-06, 2.71946e-06, 7.30760e-07, 1.81641e-07, 4.12819e-08, 7.95592e-09, 1.36223e-09, 1.87800e-10, 1.87800e-10])
gglo_min=bin_widths18*2*3000*np.array([1.02503e-02, 1.02503e-02, 5.22883e-03, 2.56007e-03, 1.16561e-03, 4.87075e-04, 1.88706e-04, 6.77802e-05, 2.28442e-05, 7.10102e-06, 2.07397e-06, 5.53029e-07, 1.36147e-07, 3.07377e-08, 5.90257e-09, 1.00963e-09, 1.34663e-10, 1.34663e-10])
gglo_max=bin_widths18*2*3000*np.array([1.58875e-02, 1.58875e-02, 8.24098e-03, 4.09774e-03, 1.89183e-03, 8.02629e-04, 3.15717e-04, 1.15084e-04, 3.92605e-05, 1.24067e-05, 3.66317e-06, 9.86425e-07, 2.47132e-07, 5.69607e-08, 1.10466e-08, 1.92877e-09, 2.60394e-10, 2.60394e-10])

gglo_050050=bin_widths18*2*3000*np.array([1.26734e-02, 1.26734e-02, 6.51672e-03, 3.21223e-03, 1.47259e-03, 6.19455e-04, 2.41934e-04, 8.74549e-05, 2.96087e-05, 9.30379e-06, 2.71946e-06, 7.30760e-07, 1.81641e-07, 4.12819e-08, 7.95592e-09, 1.36223e-09, 1.87800e-10, 1.87800e-10])
gglo_025025=bin_widths18*2*3000*np.array([1.58875e-02, 1.58875e-02, 8.24098e-03, 4.09774e-03, 1.89183e-03, 8.02629e-04, 3.15717e-04, 1.15084e-04, 3.92605e-05, 1.24067e-05, 3.66317e-06, 9.86425e-07, 2.47132e-07, 5.69607e-08, 1.10466e-08, 1.92877e-09, 2.60394e-10, 2.60394e-10])
gglo_025050=bin_widths18*2*3000*np.array([1.56012e-02, 1.56012e-02, 7.98134e-03, 3.91806e-03, 1.78818e-03, 7.49127e-04, 2.90886e-04, 1.04808e-04, 3.53847e-05, 1.10487e-05, 3.23288e-06, 8.63918e-07, 2.13426e-07, 4.85242e-08, 9.28585e-09, 1.58722e-09, 2.14542e-10, 2.14542e-10])
gglo_050025=bin_widths18*2*3000*np.array([1.29095e-02, 1.29095e-02, 6.72850e-03, 3.36053e-03, 1.55841e-03, 6.64207e-04, 2.62179e-04, 9.59271e-05, 3.29172e-05, 1.04162e-05, 3.08957e-06, 8.35024e-07, 2.09916e-07, 4.81687e-08, 9.69241e-09, 1.66101e-09, 2.24881e-10, 2.24881e-10])
gglo_050100=bin_widths18*2*3000*np.array([1.23607e-02, 1.23607e-02, 6.28102e-03, 3.06425e-03, 1.38981e-03, 5.79001e-04, 2.23203e-04, 8.01353e-05, 2.68570e-05, 8.31448e-06, 2.42857e-06, 6.39549e-07, 1.58446e-07, 3.56380e-08, 6.86714e-09, 1.14965e-09, 1.53773e-10, 1.53773e-10])
gglo_100050=bin_widths18*2*3000*np.array([1.05096e-02, 1.05096e-02, 5.42571e-03, 2.68417e-03, 1.23493e-03, 5.21104e-04, 2.04321e-04, 7.40782e-05, 2.51907e-05, 7.93016e-06, 2.32975e-06, 6.28961e-07, 1.55893e-07, 3.57670e-08, 6.87201e-09, 1.18523e-09, 1.61603e-10, 1.61603e-10])
gglo_100100=bin_widths18*2*3000*np.array([1.02503e-02, 1.02503e-02, 5.22883e-03, 2.56007e-03, 1.16561e-03, 4.87075e-04, 1.88706e-04, 6.77802e-05, 2.28442e-05, 7.10102e-06, 2.07397e-06, 5.53029e-07, 1.36147e-07, 3.07377e-08, 5.90257e-09, 1.00963e-09, 1.34663e-10, 1.34663e-10])





del_nloew_noveto_1=nloew_noveto_1/lo_noveto_1
del_nloew_noveto_05=nloew_noveto_05/lo_noveto_05
del_nloew_noveto_2=nloew_noveto_2/lo_noveto_2


nnlonloew_noveto_centre=nnlo_noveto_centre*del_nloew_noveto_1
nnlonloew_noveto_min=nnlo_noveto_min*del_nloew_noveto_1
nnlonloew_noveto_max=nnlo_noveto_max*del_nloew_noveto_1



nnlonloew_noveto_050050=nnlo_noveto_050050*del_nloew_noveto_05
nnlonloew_noveto_050100=nnlo_noveto_050100*del_nloew_noveto_1
nnlonloew_noveto_200100=nnlo_noveto_200100*del_nloew_noveto_1
nnlonloew_noveto_100100=nnlo_noveto_100100*del_nloew_noveto_1
nnlonloew_noveto_100200=nnlo_noveto_100200*del_nloew_noveto_2
nnlonloew_noveto_100050=nnlo_noveto_100050*del_nloew_noveto_05
nnlonloew_noveto_200200=nnlo_noveto_200200*del_nloew_noveto_2



#print(nnlonloew_noveto_100100)
#print(gglo_050050)
#print(nlophoton_noveto_1/6000)



sm_050050=nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_1
sm_025025=nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_05
sm_025050=nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_1
sm_050025=nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_05
sm_050100=nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_2
sm_100050=nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_1
sm_100100=nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_2


sm_min=[]
sm_max=[]

for i in range(0, len(sm_050050)):
    values=[sm_050050[i], sm_025025[i], sm_025050[i], sm_050025[i], sm_050100[i], sm_100050[i], sm_100100[i]]
    sm_min.append(np.min(values))
    sm_max.append(np.max(values))

sm_min_1=np.array(sm_min)
sm_max_1=np.array(sm_max)

sm_1=sm_050050

print(sm_1)
print(sm_min_1)
print(sm_max_1)




qqratsm_050050=nnlonloew_noveto_100100/(nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_1)
qqratsm_025025=nnlonloew_noveto_050050/(nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_05)
qqratsm_025050=nnlonloew_noveto_050100/(nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_1)
qqratsm_050025=nnlonloew_noveto_100050/(nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_05)
qqratsm_050100=nnlonloew_noveto_100200/(nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_2)
qqratsm_100050=nnlonloew_noveto_200100/(nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_1)
qqratsm_100100=nnlonloew_noveto_200200/(nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_2)


qqratsm_min=[]
qqratsm_max=[]

for i in range(0, len(qqratsm_050050)):
    values=[qqratsm_050050[i], qqratsm_025025[i], qqratsm_025050[i], qqratsm_050025[i], qqratsm_050100[i], qqratsm_100050[i], qqratsm_100100[i]]
    qqratsm_min.append(np.min(values))
    qqratsm_max.append(np.max(values))

qqratsm_min_1=np.array(qqratsm_min)
qqratsm_max_1=np.array(qqratsm_max)

qqratsm_1=qqratsm_050050


print(qqratsm_1)
print(qqratsm_min_1)
print(qqratsm_max_1)


ggratsm_050050=gglo_050050/(nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_1)
ggratsm_025025=gglo_050050/(nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_05)
ggratsm_025050=gglo_050050/(nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_1)
ggratsm_050025=gglo_050050/(nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_05)
ggratsm_050100=gglo_050050/(nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_2)
ggratsm_100050=gglo_050050/(nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_1)
ggratsm_100100=gglo_050050/(nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_2)


ggratsm_min=[]
ggratsm_max=[]

for i in range(0, len(ggratsm_050050)):
    values=[ggratsm_050050[i], ggratsm_025025[i], ggratsm_025050[i], ggratsm_050025[i], ggratsm_050100[i], ggratsm_100050[i], ggratsm_100100[i]]
    ggratsm_min.append(np.min(values))
    ggratsm_max.append(np.max(values))

ggratsm_min_1=np.array(ggratsm_min)
ggratsm_max_1=np.array(ggratsm_max)

ggratsm_1=ggratsm_050050

print(ggratsm_1)
print(ggratsm_min_1)
print(ggratsm_max_1)


photonratsm_050050=nlophoton_noveto_1/(nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_1)
photonratsm_025025=nlophoton_noveto_05/(nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_05)
photonratsm_025050=nlophoton_noveto_1/(nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_1)
photonratsm_050025=nlophoton_noveto_05/(nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_05)
photonratsm_050100=nlophoton_noveto_2/(nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_2)
photonratsm_100050=nlophoton_noveto_1/(nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_1)
photonratsm_100100=nlophoton_noveto_2/(nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_2)


photonratsm_min=[]
photonratsm_max=[]

for i in range(0, len(photonratsm_050050)):
    values=[photonratsm_050050[i], photonratsm_025025[i], photonratsm_025050[i], photonratsm_050025[i], photonratsm_050100[i], photonratsm_100050[i], photonratsm_100100[i]]
    photonratsm_min.append(np.min(values))
    photonratsm_max.append(np.max(values))

photonratsm_min_1=np.array(photonratsm_min)
photonratsm_max_1=np.array(photonratsm_max)

photonratsm_1=photonratsm_050050

print(photonratsm_1)
print(photonratsm_min_1)
print(photonratsm_max_1)

bin_centres=(bins[0:16] + bins[1:17])/2
bin_centres=np.concatenate((np.array([0]), bin_centres, np.array([5000])))
print(bin_centres)

'''
plt.figure()


plt.step(bin_centres, nnlo_noveto_centre/nnlo_noveto_centre -1 , color='k', where='mid')

plt.fill_between(bin_centres, nnlo_noveto_min/nnlo_noveto_centre -1, nnlo_noveto_max/nnlo_noveto_centre -1,
                     color='k', alpha=0.5, step='mid')

plt.step(bin_centres, nnlonloew_noveto_centre/nnlo_noveto_centre -1, color='r', where='mid')

plt.fill_between(bin_centres, nnlonloew_noveto_min/nnlo_noveto_centre  -1 , nnlonloew_noveto_max/nnlo_noveto_centre -1,
                     color='r', alpha=0.5, step='mid')
plt.semilogx()



plt.xlim(200,4000)              
plt.tight_layout()
plt.savefig("nnllnnloewcheck_noveto.pdf", bbox_inches='tight')
'''




nnlonloew_noveto_100100=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.5MWW_mufac=0.5MWW.npy"))
nnlonloew_noveto_050050=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.25MWW_mufac=0.25MWW.npy"))
nnlonloew_noveto_050100=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.25MWW_mufac=0.5MWW.npy"))
nnlonloew_noveto_100050=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.5MWW_mufac=0.25MWW.npy",))
nnlonloew_noveto_100200=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=0.5MWW_mufac=1.0MWW.npy"))
nnlonloew_noveto_200100=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=1.0MWW_mufac=0.5MWW.npy"))
nnlonloew_noveto_200200=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_murenorm=1.0MWW_mufac=1.0MWW.npy"))



nlophoton_noveto_1=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=0.5MWW.npy"))
nlophoton_noveto_05=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=0.25MWW.npy"))
nlophoton_noveto_2=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_mufac=1.0MWW.npy"))

nlophoton_noveto_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_centre.npy"))
nlophoton_noveto_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_min.npy"))
nlophoton_noveto_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gamgam_nlo_max.npy"))

gglo_centre=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_centre.npy"))
gglo_max=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_max.npy"))
gglo_min=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_min.npy"))


gglo_050050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.5MWW_mufac=0.5MWW.npy"))
gglo_025025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.25MWW_mufac=0.25MWW.npy"))
gglo_025050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.25MWW_mufac=0.5MWW.npy"))
gglo_050025=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.5MWW_mufac=0.25MWW.npy"))
gglo_050100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=0.5MWW_mufac=1.0MWW.npy"))
gglo_100050=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=1.0MWW_mufac=0.5MWW.npy"))
gglo_100100=2*3000*array_for_plot(np.load("../Data_numpy_for_figures/14TeV_HLLHC_noveto/mll_14TeV_noveto_sm_gg_lo_qcd_murenorm=1.0MWW_mufac=1.0MWW.npy"))

nnlonloew_noveto_centre=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_centre.npy"))
nnlonloew_noveto_min=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_min.npy"))
nnlonloew_noveto_max=2*3000*array_for_plot(np.load("../QCD_EW_Combination/mll_14TeV_noveto_sm_qq_nnlo_qcd_cross_nlo_ew_max.npy"))

#print(nnlonloew_noveto_centre)
#print(nnlonloew_noveto_min)
#print(nnlonloew_noveto_max)

sm=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_centre.npy"))
sm_min=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_min.npy"))
sm_max=2*3000*array_for_plot(np.load("../SM_Construction/mll_14TeV_noveto_sm_max.npy"))
print("test start")
print(sm - sm_1)
print(sm_min - sm_min_1)
print(sm_max - sm_max_1)




qqratsm_050050=nnlonloew_noveto_100100/(nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_1)
qqratsm_025025=nnlonloew_noveto_050050/(nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_05)
qqratsm_025050=nnlonloew_noveto_050100/(nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_1)
qqratsm_050025=nnlonloew_noveto_100050/(nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_05)
qqratsm_050100=nnlonloew_noveto_100200/(nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_2)
qqratsm_100050=nnlonloew_noveto_200100/(nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_1)
qqratsm_100100=nnlonloew_noveto_200200/(nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_2)


qqratsm_min=[]
qqratsm_max=[]

for i in range(0, len(qqratsm_050050)):
    values=[qqratsm_050050[i], qqratsm_025025[i], qqratsm_025050[i], qqratsm_050025[i], qqratsm_050100[i], qqratsm_100050[i], qqratsm_100100[i]]
    qqratsm_min.append(np.min(values))
    qqratsm_max.append(np.max(values))

qqratsm_min=np.array(qqratsm_min)
qqratsm_max=np.array(qqratsm_max)

qqratsm=qqratsm_050050

print(qqratsm - qqratsm_1)
print(qqratsm_min - qqratsm_min_1)
print(qqratsm_max - qqratsm_max_1)

ggratsm_050050=gglo_050050/(nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_1)
ggratsm_025025=gglo_050050/(nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_05)
ggratsm_025050=gglo_050050/(nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_1)
ggratsm_050025=gglo_050050/(nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_05)
ggratsm_050100=gglo_050050/(nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_2)
ggratsm_100050=gglo_050050/(nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_1)
ggratsm_100100=gglo_050050/(nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_2)


ggratsm_min=[]
ggratsm_max=[]

for i in range(0, len(ggratsm_050050)):
    values=[ggratsm_050050[i], ggratsm_025025[i], ggratsm_025050[i], ggratsm_050025[i], ggratsm_050100[i], ggratsm_100050[i], ggratsm_100100[i]]
    ggratsm_min.append(np.min(values))
    ggratsm_max.append(np.max(values))

ggratsm_min=np.array(ggratsm_min)
ggratsm_max=np.array(ggratsm_max)

ggratsm=ggratsm_050050


print(ggratsm - ggratsm_1)
print(ggratsm_min - ggratsm_min_1)
print(ggratsm_max - ggratsm_max_1)


photonratsm_050050=nlophoton_noveto_1/(nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_1)
photonratsm_025025=nlophoton_noveto_05/(nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_05)
photonratsm_025050=nlophoton_noveto_1/(nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_1)
photonratsm_050025=nlophoton_noveto_05/(nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_05)
photonratsm_050100=nlophoton_noveto_2/(nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_2)
photonratsm_100050=nlophoton_noveto_1/(nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_1)
photonratsm_100100=nlophoton_noveto_2/(nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_2)


photonratsm_min=[]
photonratsm_max=[]

for i in range(0, len(photonratsm_050050)):
    values=[photonratsm_050050[i], photonratsm_025025[i], photonratsm_025050[i], photonratsm_050025[i], photonratsm_050100[i], photonratsm_100050[i], photonratsm_100100[i]]
    photonratsm_min.append(np.min(values))
    photonratsm_max.append(np.max(values))

photonratsm_min=np.array(photonratsm_min)
photonratsm_max=np.array(photonratsm_max)

photonratsm=photonratsm_050050

print(photonratsm - photonratsm_1)
print(photonratsm_min - photonratsm_min_1)
print(photonratsm_max - photonratsm_max_1)



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
axs[0].annotate(r'$\sqrt{s} = 14$TeV, $\, p p\, \to\, e^{\pm}\nu\mu^{\mp}\nu, $ No Jet Veto', 
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


axs[0].step(bin_centres, nnlonloew_noveto_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', linewidth=0.7)
axs[0].step(bin_centres, -nnlonloew_noveto_centre/(bin_widths18*3000), color='k', linestyle="--", where='mid', label=r'$qq$-only (NNLO$_{\mathrm{QCD}}\times$NLO$_{\mathrm{EW}}$) ')

axs[0].fill_between(bin_centres, nnlonloew_noveto_min/(bin_widths18*3000), nnlonloew_noveto_max/(bin_widths18*3000),
                     color='k', alpha=0.3, step='mid')

axs[0].step(bin_centres, nlophoton_noveto_centre/(bin_widths18*3000), color='y', where='mid', linewidth=0.7)
axs[0].step(bin_centres, -nlophoton_noveto_centre/(bin_widths18*3000), color='y', where='mid', label=r'$\gamma\gamma $-only (NLO)')

axs[0].fill_between(bin_centres, nlophoton_noveto_min/(bin_widths18*3000), nlophoton_noveto_max/(bin_widths18*3000),
                     color='y', alpha=0.3, step='mid')


axs[0].step(bin_centres, gglo_centre/(bin_widths18*3000), color='b', where='mid', linewidth=0.7)
axs[0].step(bin_centres, -gglo_centre/(bin_widths18*3000), color='b', where='mid', label=r'$gg$-only (LO)')

axs[0].fill_between(bin_centres, gglo_min/(bin_widths18*3000), gglo_max/(bin_widths18*3000),
                     color='b', alpha=0.3, step='mid')





axs[0].legend(loc="lower left", fontsize=11, frameon=False)
axs[0].set_xlim(200, 4000)
axs[0].set_ylim(5*10**-12, 4*10**3)




axs[1].step(bin_centres, 100*ggratsm, color='b', where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, 100*ggratsm_min, 100*ggratsm_max,
                     color='b', alpha=0.5, step='mid')






axs[1].step(bin_centres, 100*photonratsm, color='y', where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, 100*photonratsm_min, 100*photonratsm_max,
                     color='y', alpha=0.5, step='mid')




axs[1].step(bin_centres, 100*qqratsm, color='k', where='mid', linewidth=0.7)
axs[1].fill_between(bin_centres, 100*qqratsm_min, 100*qqratsm_max,
                     color='k', alpha=0.5, step='mid')


axs[1].loglog()
axs[0].set_xticks([200, 1000, 4000])
axs[0].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])
axs[0].tick_params(which="both", labelsize=13, direction='in', right=True, top=True, bottom=False)
axs[1].tick_params(which="both", labelsize=13, direction='in', right=True)
axs[1].set_ylim(10**-2, 120)
axs[1].set_yticks([10**-2, 10**-1, 1, 10, 100])
axs[1].set_yticklabels(["0.01", "0.1", "1", "10", "100"])
axs[1].set_xticks([200, 1000, 4000])
axs[1].set_xticklabels([r"$200$", r"$1000$", r"$4000$"])

#plt.tight_layout()
#plt.savefig("figure_5b.pdf", bbox_inches='tight')

plt.savefig("figure_5b_orig.pdf", bbox_inches='tight')