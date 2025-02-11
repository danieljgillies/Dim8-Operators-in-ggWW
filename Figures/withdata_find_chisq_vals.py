import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from scipy.optimize import minimize, basinhopping, shgo
from factor_conversions import kg2lam, kgtilde2lam, fac2lam

def _chisq(expected, observed, _delta, min_bin, max_bin):
    """
    This function calculates the modified chi squared given the expected and observed data,\
    the maximum bin that data should be considered up to and _delta which is the combined error \
    of the two datasets.

    -----------

    Inputs:

    expected (np.array (dim(16))): The expected data (SM or BSM prediction).
    
    observed (np.array (dim(16))): The ATLAS data (ATLAS data of 16 bins).

    _delta (np.array (dim(16))): The error of the former two combined in quadrature. Note that \
    the SM and BSM share perfectly correlated SM theoretical errors which should not be double counted.

    min_bin (int): The maximum bin this chi squared should be calculated with.

    max_bin (int): The maximum bin this chi squared should be calculated with (given the EFT \
    considerations).
    
    ------

    Returns:

    (int) : The modified chi squared value calculate.

    """

    if len(observed)==13 and len(expected)==13 and len(_delta)==13:
        chisq=((observed - expected)**2)/(expected+(_delta)**2)
        return np.sum(chisq[min_bin:max_bin])
    else:
        raise("Error unexpected number of bins")


def produce_contours_ATLAS(run_name, factor_operatorA_vals, factor_operatorB_vals, atlas_data, atlas_err, generate_bsm_prediction, operatorAlambda_to_factor, operatorBlambda_to_factor, operatorAfactor_to_lambda, operatorBfactor_to_lambda, operatorAfactor_to_max_bin, operatorBfactor_to_max_bin, min_bin=0):#, SM_pred, Delta (Only needed for pseudodata case)
    """

    This function takes in experimental data, along with SM and BSM predictions which must be given using\
    a function "generate_bsm_prediction" (where SM is recovered by setting the coefficients of operators A\
    and B to zero). This function returns the delta chi squared value for each pair of point specified by\
    the input factor arrays "factor_operatorA_vals, factor_operatorB_vals". In order to stay in\
    the EFT regime the function uses "factor_to_mass_scale" and "mass_scale_to_max_bin" to ensure each\
    factor uses only the bins which are likely to still be within the EFT regime. 

    ----------

    Inputs:

    run_name (string): Name for run to be used in plot outputs.

    factor_operatorA_vals (np.array dim(n)): List of factors to be considered for the operator. This can be given either in ($\frac{c}{\Lambda}$) \
    or in the kappa formalism but the functions factor to Lambda and Lambda to factor must be modified \
    appropriately.

    factor_operatorB_vals (np.array dim(m)): Same as above for operator B.

    atlas_data (np.array): The binned experimental data used to produce the contour plots.

    atlas_err (np.array): The experimental error for the binned data.

    generate_bsm_prediction: Function which takes in two factors for the operators A and B and returns a BSM prediction (with errors).
    
    operatorAlambda_to_factor (func): User defined function which returns  the factor (inputted to the "generate_bsm_prediction") associated with a given mass scale.\
    This is usually done by taking some assumption (i.e wilson |c|=1). "generate_bsm_prediction" could take a value in the kappa formalism or a factor which rescales \
    the contribution relative to another value of Lambda. It is up to the user to ensure consistency. This function should also preserve the sign of lambda to indicate \
    if c is +/- 1.

    operatorBlambda_to_factor (func): Same function as above but for operator B.

    operatorAfactor_to_lambda (func): Inverse of function operatorAlambda_to_factor.

    operatorBfactor_to_lambda (func): Same function as above but for operator B.
    
    operatorAfactor_to_max_bin (func): User defined function which returns the maximum bin which should be used when considering the operator with a given\
    factor. Usually done by taking some assumption (i.e wilson |c|=1) and finding the appropriate Mass scale this then informs (with more assumptions) which \
    bins can be used.

    operatorBfactor_to_max_bin(func): Same function as above but for operator B. 

    min_bin (int, default = 0): Exclude bins up to this value.

    ------- 

    Returns:

    points_x, points_y (np.array dim(n, m)): List of points x and points y for each point in the grid set by operator A and B factor values.
    
    deltachisqs_all (np.array dim(n, m)): The value of delta chi squared at the point in x and y.

    """
    #For reproducibility
    np.random.seed(1)
    

    #Find the maximum bin that can be used to constrain each of the factors given.

    max_bin_operatorA=operatorAfactor_to_max_bin(factor_operatorA_vals)
    max_bin_operatorB=operatorBfactor_to_max_bin(factor_operatorB_vals)

    #We define a function to minimise the chisquared value based on two input coefficients a1[0], a1[1]
    def _chisq_tominimize(a1, s, max_bin):
        prediction=generate_bsm_prediction(a1[0], a1[1])
        err_pred=(prediction[2]-prediction[1])/2
        delta=(err_pred**2 + atlas_err**2)**0.5
        return _chisq(prediction[0], s, delta, min_bin, max_bin)
    
    #For each bin range the minimum chi squared for that number of bins must be evaluated.

    current_chisqs=[]
    max_mass_scales=np.array([0.12458383, 0.19735961, 0.29153842, 0.34352475, 0.40114594, 0.45812857, 0.50765992, 0.57883101, 0.68620833, 0.82708867, 1.030653, 1.34274721, 1.99743379])
    for i in range(0,14):
        if i < min_bin+2:
            #We ignore the first three bins and we need at least two bins to minimise chisq so we start from max_bin=min_bin+2 (As [n:n+2] only returns n and n+1)
            current_chisqs.append(0)
        else:
            max_bin=i
            #minimizer_kwargs = {
            #    "args": (atlas_data, max_bin)
            #}
            #Use the basinhopping method to find the global minimum (global minimum appears to be stable)
            #res=basinhopping(_chisq_tominimize, x0=[0, 0], niter=100,  minimizer_kwargs=minimizer_kwargs)
            #shgo works well and requires bounds on the factor (these can be given by the minimum mass scale)
            res=shgo(_chisq_tominimize, bounds=[(operatorAlambda_to_factor(-max_mass_scales[i-1]), operatorAlambda_to_factor(max_mass_scales[i-1])),(operatorBlambda_to_factor(-max_mass_scales[i-1]), operatorBlambda_to_factor(max_mass_scales[i-1]))],  args=(atlas_data, max_bin))
            #res=minimize(_chisq_tominimize, x0=[5, 5], args=(atlas_data, max_bin))
            current_chisqs.append(res.fun)
    
    

    #Can plot chisq if desired.
    a=np.linspace(1,len(current_chisqs), len(current_chisqs))
    plt.figure()
    plt.plot(current_chisqs)
    #plt.plot(current_chisqs/a)
    plt.savefig("current_chisqs_"+run_name+".pdf")
    

    #Define a list of x and y values that are considered.
    points_x=[]
    points_y=[]
    #Define a list for the corresponding delta chi squared values.
    deltachisqs_all=[]
    l=0 
    for i in tqdm(range(0, len(factor_operatorA_vals))):
        #We create a 2d grid of values 
        temp_points_x=[]
        temp_points_y=[]
        temp_deltachisqs_all=[]

        for j in range(0, len(factor_operatorB_vals)):
            max_bin=min([max_bin_operatorA[i], max_bin_operatorB[j]])


            #Set factors currently being considered
            factor_operatorA=factor_operatorA_vals[i]
            factor_operatorB=factor_operatorB_vals[j]


            if max_bin<min_bin+2 :
                #Cannot constrain with less than two bins
                temp_points_x.append(factor_operatorA)
                temp_points_y.append(factor_operatorB)
                temp_deltachisqs_all.append(0)
                continue


            #Generate prediction
            prediction=generate_bsm_prediction(factor_operatorA, factor_operatorB)
            err_pred=(prediction[2]-prediction[1])/2
            delta=(err_pred**2 + atlas_err**2)**0.5
           
            #Find the chi squared of prediction and subtract best prediction for given number of bins.
            deltachisqs=_chisq(prediction[0], atlas_data, delta, min_bin, max_bin) - current_chisqs[max_bin]
            
            
            #Sanity Check
            
            if deltachisqs > 5.9 and deltachisqs < 6 and l==0:
                plt.figure()
                plt.plot(prediction[0][min_bin:max_bin])
                plt.plot(atlas_data[min_bin:max_bin],
                     color='r')
                plt.plot((atlas_data[min_bin:max_bin]+delta[min_bin:max_bin]),
                     color='r', alpha=0.5)
                plt.plot((atlas_data[min_bin:max_bin]-delta[min_bin:max_bin]),
                     color='r', alpha=0.5)
                plt.savefig("error_"+run_name+".pdf")
                plt.figure()
                plt.plot(prediction[0][min_bin:max_bin]/prediction[0][min_bin:max_bin])
                plt.plot(atlas_data[min_bin:max_bin]/prediction[0][min_bin:max_bin],
                     color='r')
                plt.plot((atlas_data[min_bin:max_bin]+delta[min_bin:max_bin])/prediction[0][min_bin:max_bin],
                     color='r', alpha=0.5)
                plt.plot((atlas_data[min_bin:max_bin]-delta[min_bin:max_bin])/prediction[0][min_bin:max_bin],
                     color='r', alpha=0.5)
                plt.savefig("error_rat_"+run_name+".pdf")
                print("First prediction found at p=0.05.")
                print(prediction[0][min_bin:max_bin])
                print("Atlas data.")
                print(atlas_data[min_bin:max_bin])
                print("Theoretical (+systematic) uncertainty.")
                print(delta[min_bin:max_bin])
                print("Value of first operator A factor at p=0.05.")
                print(factor_operatorA)
                print("... corresponding mass scale.")
                print(operatorAfactor_to_lambda(factor_operatorA))
                print("Value of first operator A factor at p=0.05.")
                print(factor_operatorB)
                print("... corresponding mass scale.")
                print(operatorBfactor_to_lambda(factor_operatorB))
                l+=1

            temp_points_x.append(factor_operatorA)
            temp_points_y.append(factor_operatorB)
            temp_deltachisqs_all.append(deltachisqs)


        points_x.append(temp_points_x)
        points_y.append(temp_points_y)
        deltachisqs_all.append(temp_deltachisqs_all)

    return points_x, points_y, deltachisqs_all