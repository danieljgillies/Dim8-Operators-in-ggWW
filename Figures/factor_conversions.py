import numpy as np

def kg2lam(x):
    return np.sign(x)*np.sqrt((12*np.pi*0.24622**2)/(abs(x)*0.113))

def lam2kg(x):
    return np.sign(x)*(12*np.pi*0.24622**2)/((x**2)*0.113)

def kgtilde2lam(x):
    return np.sign(x)*np.sqrt((8*np.pi*0.24622**2)/(abs(x)*0.113))

def lam2kgtilde(x):
    return np.sign(x)*(8*np.pi*0.24622**2)/((x**2)*0.113)

def fac2lam(x):
    return np.sign(x)*2*(abs(x)**-0.25)

def lam2fac(x):
    return np.sign(x)*(2**4)/(x**4)
