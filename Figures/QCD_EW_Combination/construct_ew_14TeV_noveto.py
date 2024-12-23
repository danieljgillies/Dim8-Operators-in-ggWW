import numpy as np
import matplotlib.pyplot as plt





nnllnnlo_centre=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_nnllnnlo_centre.npy")
nnllnnlo_min=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_nnllnnlo_min.npy")
nnllnnlo_max=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_nnllnnlo_max.npy")


nloew_centre=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_nlo_ew_centre.npy")


lo_centre=np.load("../Data/14TeV_HLLHC_veto/mll_14TeV_veto35_sm_qq_lo_centre.npy")


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




sm_050050=nnlonloew_noveto_100100+gglo_050050+nlophoton_noveto_1
sm_025025=nnlonloew_noveto_050050+gglo_025025+nlophoton_noveto_05
sm_025050=nnlonloew_noveto_050100+gglo_025050+nlophoton_noveto_1
sm_050025=nnlonloew_noveto_100050+gglo_050025+nlophoton_noveto_05
sm_050100=nnlonloew_noveto_100200+gglo_050100+nlophoton_noveto_2
sm_100050=nnlonloew_noveto_200100+gglo_100050+nlophoton_noveto_1
sm_100100=nnlonloew_noveto_200200+gglo_100100+nlophoton_noveto_2




np.save("mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_nlo_ew_centre", nnllnnlonloew_centre)
np.save("mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_nlo_ew_min", nnllnnlonloew_min)
np.save("mll_14TeV_veto35_sm_qq_nnllnnlo_qcd_nlo_ew_max", nnllnnlonloew_max)









