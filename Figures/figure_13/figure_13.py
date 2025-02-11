import matplotlib.pyplot as plt
import numpy as np
#from Figures
import sys
sys.path.insert(1, '..')

from factor_conversions import kg2lam, kgtilde2lam, lam2kg, lam2kgtilde
from plot_funcs import fmt

points_x_nosyst=np.load("points_x_kg_nosyst.npy")
points_y_nosyst=np.load("points_y_kg_nosyst.npy")
deltachisqs_all_nosyst=np.load("deltachisqs_all_nosyst.npy")

points_x_syst=np.load("points_x_kg_syst.npy")
points_y_syst=np.load("points_y_kg_syst.npy")
deltachisqs_all_syst=np.load("deltachisqs_all_syst.npy")



# Basic contour plot


#Set figure size (rectangular due to different ranges of x and y axes.)
fig, ax = plt.subplots(figsize=(1.1*20, 1.1*(16/18)*20), dpi=900)

secax = ax.secondary_xaxis('top', functions=(kg2lam, lam2kg))
secax.set_xticks([-10, -9, -8, -7, -6, -5, -4, -3, 3, 4, 5, 6, 7, 8, 9, 10])
secax.set_xticklabels([10, "", "", "", "", 5, "", "", "", "", 5, "", "", "", "", 10])
secax.tick_params(which="both", labelsize=22, direction='in')
secax.set_xlabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)

secay = ax.secondary_yaxis('right', functions=(kgtilde2lam, lam2kgtilde))
secay.set_yticks([-6, -5, -4, -3, -2, 3, 4, 5, 6])
secay.set_yticklabels([6, 5, 4, 3, 2, 3, 4, 5, 6])
secay.tick_params(which="both", labelsize=22, direction='in')
secay.set_ylabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)


#Create contour plot.

CS = ax.contour(points_x_syst, points_y_syst, deltachisqs_all_syst, levels=[3.219, 5.991, 13.816], linewidths=3)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=16)
plt.ylabel(r"$\tilde\kappa_g$", fontsize=28)
plt.xlabel(r"$\kappa_g$", fontsize=28)
plt.plot([-0.6/3, 0.4/3], [2/3, 2/3], '--', color="k", label="Projection for HL-LHC Higgs", markersize=14)
plt.plot([-0.6/3, 0.4/3], [-2/3, -2/3], '--', color="k", markersize=14)
plt.plot([-0.6/3, -0.6/3], [-2/3, 2/3], '--', color="k", markersize=14)
plt.plot([0.4/3, 0.4/3], [-2/3, 2/3], '--', color="k", markersize=14)
plt.plot(0, 0, 'x', color="r", label="Standard Model", markersize=10)
plt.xlim(-3, 3)
plt.ylim(-3.5, (2/3)*3)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(fontsize=20, loc="lower right")
plt.tight_layout()
plt.savefig("1_full_contour_plot_syst.pdf")



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
            plt.savefig("2_p=0.05_paths_syst.pdf")






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
            #xs2=np.concatenate((vertices[4200:4600,0], vertices[2350:3170,0], vertices[4000:4700,0], vertices[5600:6450,0]))
            #ys2=np.concatenate((vertices[4200:4600,1], vertices[2350:3170,1], vertices[4000:4700,1], vertices[5600:6450,1]))
            xs2=np.concatenate((vertices[800:1200,0], vertices[1820:2750,0], vertices[3500:4250,0], vertices[4900:5950,0], vertices[6500:6940,0]))
            ys2=np.concatenate((vertices[800:1200,1], vertices[1820:2750,1], vertices[3500:4250,1], vertices[4900:5950,1], vertices[6500:6940,1]))
            
            
            plt.plot(xs2, ys2, "r")
            plt.savefig("3_vertices_syst.pdf")

fig, ax = plt.subplots(figsize=(1.1*20, 1.1*(16/18)*20), dpi=900)

secax = ax.secondary_xaxis('top', functions=(kg2lam, lam2kg))
secax.set_xticks([-10, -9, -8, -7, -6, -5, -4, -3, 3, 4, 5, 6, 7, 8, 9, 10])
secax.set_xticklabels([10, "", "", "", "", 5, "", "", "", "", 5, "", "", "", "", 10])
secax.tick_params(which="both", labelsize=22, direction='in')
secax.set_xlabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)

secay = ax.secondary_yaxis('right', functions=(kgtilde2lam, lam2kgtilde))
secay.set_yticks([-6, -5, -4, -3, -2, 3, 4, 5, 6])
secay.set_yticklabels([6, 5, 4, 3, 2, 3, 4, 5, 6])
secay.tick_params(which="both", labelsize=22, direction='in')
secay.set_ylabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)

CS = ax.contour(points_x_nosyst, points_y_nosyst, deltachisqs_all_nosyst, levels=[3.219, 5.991, 13.816], linewidths=3)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=16)
plt.ylabel(r"$\tilde\kappa_g$", fontsize=28)
plt.xlabel(r"$\kappa_g$", fontsize=28)
plt.plot([-0.6/3, 0.4/3], [2/3, 2/3], '--', color="k", label="Projection for HL-LHC Higgs", markersize=14)
plt.plot([-0.6/3, 0.4/3], [-2/3, -2/3], '--', color="k", markersize=14)
plt.plot([-0.6/3, -0.6/3], [-2/3, 2/3], '--', color="k", markersize=14)
plt.plot([0.4/3, 0.4/3], [-2/3, 2/3], '--', color="k", markersize=14)
plt.plot(0, 0, 'x', color="r", label="Standard Model", markersize=10)
plt.xlim(-3, 3)
plt.ylim(-3.5, (2/3)*3)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(fontsize=20, loc="lower right")
plt.tight_layout()
plt.savefig("1_full_contour_plot_nosyst.pdf")



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
            plt.savefig("2_p=0.05_paths_nosyst.pdf")






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

            #Have to manually vary these ranges to select the correct points.

            #Use all in this case since discontoniuties are minimal.
            #xs1=np.concatenate((vertices[130:440,0], vertices[740:990,0], vertices[1280:1590,0], vertices[1860:2140,0]))
            #ys1=np.concatenate((vertices[130:440,1], vertices[740:990,1], vertices[1280:1590,1], vertices[1860:2140,1]))
            
            
            plt.plot(xs1, ys1, "r")
            plt.savefig("3_vertices_nosyst.pdf")
















fig, ax = plt.subplots(figsize=(1.1*10, 1.1*(8/9)*10), dpi=1000)

secax = ax.secondary_xaxis('top', functions=(kg2lam, lam2kg))
secax.set_xticks([-10, -9, -8, -7, -6, -5, -4, -3, 3, 4, 5, 6, 7, 8, 9, 10])
secax.set_xticklabels([10, "", "", "", "", 5, "", "", "", "", 5, "", "", "", "", 10])
secax.tick_params(which="both", labelsize=22, direction='in')
secax.set_xlabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)

secay = ax.secondary_yaxis('right', functions=(kgtilde2lam, lam2kgtilde))
secay.set_yticks([-6, -5, -4, -3, -2, 3, 4, 5, 6])
secay.set_yticklabels([6, 5, 4, 3, 2, 3, 4, 5, 6])
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
plt.plot(100,100, color='#2E4B7F', label=r"$p=0.05$")



A = np.column_stack((xs1**2, xs1 * ys1, ys1**2, xs1, ys1))
b = np.ones_like(xs1)
x = np.linalg.lstsq(A, b)[0].squeeze()
x_coord = np.linspace(-10,10,300)
y_coord = np.linspace(-10,10,300)
X_coord, Y_coord = np.meshgrid(x_coord, y_coord)
Z_coord = x[0] * X_coord ** 2 + x[1] * X_coord * Y_coord + x[2] * Y_coord**2 + x[3] * X_coord + x[4] * Y_coord

plt.contour(X_coord, Y_coord, Z_coord, levels=[1], colors=('purple'), linestyles="--", linewidths=2)
#To create legend
plt.plot(100,100, color='purple', linestyle="--", label=r"$p=0.05$ no systematic error")

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


plt.ylabel(r"$\tilde\kappa_g$", fontsize=28)
plt.xlabel(r"$\kappa_g$", fontsize=28)
plt.plot([-0.6/3, 0.4/3], [2/3, 2/3], '--', color="k", label="Projection for HL-LHC Higgs", markersize=14)
plt.plot([-0.6/3, 0.4/3], [-2/3, -2/3], '--', color="k", markersize=14)
plt.plot([-0.6/3, -0.6/3], [-2/3, 2/3], '--', color="k", markersize=14)
plt.plot([0.4/3, 0.4/3], [-2/3, 2/3], '--', color="k", markersize=14)
plt.plot(0, 0, 'x', color="r", label="Standard Model", markersize=10)
plt.xlim(-3, 3)
plt.ylim(-3.5, (2/3)*3)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(fontsize=20, loc="lower right")
plt.tight_layout()
plt.savefig("figure_13.pdf")