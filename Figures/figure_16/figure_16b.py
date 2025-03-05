import matplotlib.pyplot as plt
import numpy as np
#from Figures
import sys
sys.path.insert(1, '..')

from factor_conversions import fac2lam, lam2fac

points_x_nosyst=np.load("points_x_k2_fo_nosyst.npy")
points_y_nosyst=np.load("points_y_k3_fo_nosyst.npy")
deltachisqs_all_nosyst=np.load("deltachisqs_all_fo_nosyst.npy")

points_x_syst=np.load("points_x_k2_fo_syst.npy")
points_y_syst=np.load("points_y_k3_fo_syst.npy")
deltachisqs_all_syst=np.load("deltachisqs_all_fo_syst.npy")

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

     

# Basic contour plot


#Set figure size (rectangular due to different ranges of x and y axes.)
fig = plt.figure(figsize=(11.8, (7/6)*11), dpi=100)
border=0.12
ax = fig.add_axes([0.8/11.8 + border*(11/11.8), border, (11/11.8)*(1-2*border), 1-2*border])


secax = ax.secondary_xaxis('top', functions=(fac2lam, lam2fac))
secax.set_xticks([-6, -5, -4, -3, 3, 4, 5, 6])
secax.set_xticklabels([6, 5, 4, 3, 3, 4, 5, 6])
secax.tick_params(which="both", labelsize=22, direction='in')
secax.set_xlabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)

secay = ax.secondary_yaxis('right', functions=(fac2lam, lam2fac))
secay.set_yticks([-6, -5, -4, -3, 3, 4, 5, 6])
secay.set_yticklabels([6, 5, 4, 3, 3, 4, 5, 6])
secay.tick_params(which="both", labelsize=22, direction='in')
secay.set_ylabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)


#Create contour plot.

CS = ax.contour(points_x_syst, points_y_syst, deltachisqs_all_syst, levels=[3.219, 5.991, 13.816], linewidths=3)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=16)
plt.ylabel(r"$\frac{c_2 \mathrm{(2TeV)}^4}{\Lambda^4}$", fontsize=32)
plt.xlabel(r"$\frac{c_3 \mathrm{(2TeV)}^4}{\Lambda^4}$", fontsize=32)
plt.plot(0, 0, 'x', color="r", label="Standard Model", markersize=10)
#plt.xlim(-0.225/2, 0.225/2)
#plt.ylim(-0.3/2, 0.225/2)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(fontsize=20, loc="lower right")
plt.savefig("1_full_contour_plot_fo_syst.pdf")



#We find from this next section of code that there is only curve at p=0.05 from the CS contour


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            xs2=vertices[:,0]
            ys2=vertices[:,1]
            plt.plot(xs2, ys2)
            plt.savefig("2_p=0.05_paths_fo_syst.pdf")






#We find from this section of code the vertices that should be used to fit the ellipse

for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            plt.plot(xs2, ys2)

            #Have to manually vary these ranges to select the correct points.

            #xs2=np.concatenate((vertices[0:6300,0], vertices[6300:11850,0]))
            #ys2=np.concatenate((vertices[0:6300,1], vertices[6300:11850,1]))
            xs2=vertices[0:6700,0]
            ys2=vertices[0:6700,1]
            
            
            plt.plot(xs2, ys2, "r")
            plt.savefig("3_vertices_fo_syst.pdf")

fig = plt.figure(figsize=(11.8, (7/6)*11), dpi=100)
border=0.12
ax = fig.add_axes([0.8/11.8 + border*(11/11.8), border, (11/11.8)*(1-2*border), 1-2*border])


secax = ax.secondary_xaxis('top', functions=(fac2lam, lam2fac))
secax.set_xticks([-6, -5, -4, -3, 3, 4, 5, 6])
secax.set_xticklabels([6, 5, 4, 3, 3, 4, 5, 6])
secax.tick_params(which="both", labelsize=22, direction='in')
secax.set_xlabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)

secay = ax.secondary_yaxis('right', functions=(fac2lam, lam2fac))
secay.set_yticks([-6, -5, -4, -3, 3, 4, 5, 6])
secay.set_yticklabels([6, 5, 4, 3, 3, 4, 5, 6])
secay.tick_params(which="both", labelsize=22, direction='in')
secay.set_ylabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)

ax.tick_params(which="both", labelsize=13, direction='in')

CS = ax.contour(points_x_nosyst, points_y_nosyst, deltachisqs_all_nosyst, levels=[3.219, 5.991, 13.816], linewidths=3)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=16)
plt.ylabel(r"$\frac{c_2 \mathrm{(2TeV)}^4}{\Lambda^4}$", fontsize=32)
plt.xlabel(r"$\frac{c_3 \mathrm{(2TeV)}^4}{\Lambda^4}$", fontsize=32)
plt.plot(0, 0, 'x', color="r", label="Standard Model", markersize=10)
#plt.xlim(-0.225/2, 0.225/2)
#plt.ylim(-0.3/2, 0.225/2)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(fontsize=20, loc="lower right")
plt.savefig("1_full_contour_plot_fo_nosyst.pdf")



#We find from this next section of code that there is only curve at p=0.05 from the CS contour


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            xs1=vertices[:,0]
            ys1=vertices[:,1]
            plt.plot(xs1, ys1)
            plt.savefig("2_p=0.05_paths_fo_nosyst.pdf")






#We find from this section of code the vertices that should be used to fit the ellipse

for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            plt.plot(xs1, ys1)
            print(len(vertices))
            #Have to manually vary these ranges to select the correct points.

            #Use all in this case since discontoniuties are minimal.
            xs1=np.concatenate((vertices[1000:6200,0], vertices[20900:22140,0]))
            ys1=np.concatenate((vertices[1000:6200,1], vertices[20900:22140,1]))
            
            
            plt.plot(xs1, ys1, "r")
            plt.savefig("3_vertices_fo_nosyst.pdf")
















fig = plt.figure(figsize=(11.8, (25.5/24)*11), dpi=100)
border=0.12
ax = fig.add_axes([0.8/11.8 + border*(11/11.8), border, (11/11.8)*(1-2*border), 1-2*border])


secax = ax.secondary_xaxis('top', functions=(fac2lam, lam2fac))
secax.set_xticks([-3, -2, -1.25, 1.25, 2, 3])
secax.set_xticklabels([3, 2, 1.25, 1.25, 2, 3])
secax.tick_params(which="both", labelsize=22, direction='in')
secax.set_xlabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)

secay = ax.secondary_yaxis('right', functions=(fac2lam, lam2fac))
secay.set_yticks([-3, -2, -1.25, 1.25, 2, 3])
secay.set_yticklabels(["", 2, 1.25, 1.25, 2, 3])
secay.tick_params(which="both", labelsize=22, direction='in')
secay.set_ylabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)

ax.tick_params(which="both", labelsize=13, direction='in')


A = np.column_stack((xs2**2, xs2 * ys2, ys2**2, xs2, ys2))
b = np.ones_like(xs2)
x = np.linalg.lstsq(A, b)[0].squeeze()
x_coord = np.linspace(-10,10,300)
y_coord = np.linspace(-10,10,300)
X_coord, Y_coord = np.meshgrid(x_coord, y_coord)
Z_coord = x[0] * X_coord ** 2 + x[1] * X_coord * Y_coord + x[2] * Y_coord**2 + x[3] * X_coord + x[4] * Y_coord

plt.contour(X_coord, Y_coord, Z_coord, levels=[1], colors=('#2E4B7F'), linewidths=2)
#To create legend
plt.plot(100,100, color='#2E4B7F', label=r"$p=0.05$ no jet-veto")



A = np.column_stack((xs1**2, xs1 * ys1, ys1**2, xs1, ys1))
b = np.ones_like(xs1)
x = np.linalg.lstsq(A, b)[0].squeeze()
x_coord = np.linspace(-2,2,300)
y_coord = np.linspace(-2,2,300)
X_coord, Y_coord = np.meshgrid(x_coord, y_coord)
Z_coord = x[0] * X_coord ** 2 + x[1] * X_coord * Y_coord + x[2] * Y_coord**2 + x[3] * X_coord + x[4] * Y_coord

plt.contour(X_coord, Y_coord, Z_coord, levels=[1], colors=('purple'), linestyles="--", linewidths=2)
#To create legend
plt.plot(100,100, color='purple', linestyle="--", label=r"$p=0.05$ no systematic error, no jet-veto")

"""

This next section of code creates orange and white exclusion stripes.

a=np.linspace(-20,20,100)

for i in range(-20, 20, 3):
    ax.fill_betweenx(a, a+(i), a+(i+1), color="orange", alpha=0.5)


from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
polygon = Polygon(np.column_stack((xs2, ys2)), closed=True, color='white', zorder=1)
ax.add_patch(polygon)
"""




#plt.plot(100, 100, color='#2E4B7F', label=r"$p=0.05$ no jet-veto")
#plt.plot(100, 100, color='purple', linestyle="--", label=r"$p=0.05$ no systematic error, no jet-veto")
plt.ylabel(r"$\frac{c_2 \mathrm{(2TeV)}^4}{\Lambda^4}$", fontsize=32)
plt.xlabel(r"$\frac{c_3 \mathrm{(2TeV)}^4}{\Lambda^4}$", fontsize=32)
plt.plot(0, 0, 'x', color="r", label="Standard Model", markersize=10)
plt.xlim(-12, 12)
plt.ylim(-13.5, 12)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(fontsize=20, loc="lower right")
plt.savefig("figure_16b.pdf")