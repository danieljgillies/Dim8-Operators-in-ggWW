import numpy as np

def kg2lam(x):
    return np.sign(x)*np.sqrt((12*np.pi*0.24622**2)/(abs(x)*0.113))

def lam2kg(x):
    return np.sign(x)*(12*np.pi*0.24622**2)/((x**2)*0.113)

def kgtilde2lam(x):
    return np.sign(x)*np.sqrt((8*np.pi*0.24622**2)/(abs(x)*0.113))

def lam2kgtilde(x):
    return np.sign(x)*(8*np.pi*0.24622**2)/((x**2)*0.113)





"""
def kgfactor_to_max_bin_pseudodata(factor_vals):
    
    #This function takes in a set of factors and returns which bin is the maximum bin that can be\
    #constrained with this factor.
    
    #By assuming c=1 convert the factors to Lambda values
    mass_vals=kg2lam(factor_vals)
    #This vector gives minimum value of Lambda for each of the bins. E.g bin1 200-214GeV can only \
    # be used if Lambda is bigger than 750GeV.
    max_mass_scales=np.array([0.7504646, 0.88671293, 1.03336473, 1.18834644, 1.35280008, 1.5310028, 1.73055257, 1.95808899, 2.21780199, 2.51666561, 2.86161449, 3.25420555, 3.70412162, 4.21201279, 4.78111762, 5.40612933])
    
    #Loop breaks when the mass scale is smaller than required for a bin giving the counter as the\
    #  maximum bin for each factor
    which_bin=[]
    for i in range(0, len(mass_vals)):
        counter=0
        for j in range(0, len(max_mass_scales)):
            if abs(mass_vals[i])>max_mass_scales[j]:
                counter+=1
            else:
                break
        which_bin.append(counter)
    return which_bin

def kgtildefactor_to_max_bin_pseudodata(factor_vals):
    mass_vals=kgtilde2lam(factor_vals)
    max_mass_scales=np.array([0.7504646, 0.88671293, 1.03336473, 1.18834644, 1.35280008, 1.5310028, 1.73055257, 1.95808899, 2.21780199, 2.51666561, 2.86161449, 3.25420555, 3.70412162, 4.21201279, 4.78111762, 5.40612933])
    which_bin=[]
    for i in range(0, len(mass_vals)):
        counter=0
        for j in range(0, len(max_mass_scales)):
            if abs(mass_vals[i])>max_mass_scales[j]:
                counter+=1
            else:
                break
        which_bin.append(counter)
    return which_bin

"""