import numpy as np
from math import log10, floor

def round_to_5(x):
    rounded=[]
    for i in range(len(x)):
        rounded.append(np.round(x[i], 6-int(floor(log10(abs(x[i]))))))
    return np.array(rounded)


def array_for_plot(a):
    return np.concatenate((np.array([a[0]]), a, np.array([a[len(a)-1]])))


def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    if float(s)==-1.1:
        return r"minimum" if plt.rcParams["text.usetex"] else "minimum"
    if float(s)==3.2:
        return r"p=0.2" if plt.rcParams["text.usetex"] else "p=0.2"
    if float(s)==6:
        return r"p=0.05" if plt.rcParams["text.usetex"] else "p=0.05"
    if float(s)==13.8:
        return r"p=0.001" if plt.rcParams["text.usetex"] else "p=0.001"
