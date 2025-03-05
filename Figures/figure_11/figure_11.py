import matplotlib.pyplot as plt
import numpy as np
#from Figures
import sys
sys.path.insert(1, '..')

from factor_conversions import kg2lam, kgtilde2lam, lam2kg, lam2kgtilde
from plot_funcs import fmt

points_x=np.load("points_x_kg_05.npy")
points_y=np.load("points_y_kg_05.npy")
deltachisqs_all=np.load("deltachisqs_all_05.npy")


     

# Basic contour plot


#Set figure size (rectangular due to different ranges of x and y axes.)
fig, ax = plt.subplots(figsize=(1.1*20, 1.1*(16/18)*20), dpi=100)

secax = ax.secondary_xaxis('top', functions=(kg2lam, lam2kg))
secax.set_xticks([-6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
secax.set_xticklabels([6, "", "", "", "", "", 3, "", "", 1.5, 1.5, "", "", 3, "", "", "", "", "", 6])
secax.tick_params(which="both", labelsize=22, direction='in')

secax.set_xlabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)

secay = ax.secondary_yaxis('right', functions=(kgtilde2lam, lam2kgtilde))
secay.set_yticks([-6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
secay.set_yticklabels([6, "", "", "", "", "", 3, "", "", 1.5, "", 1.5, "", "", 3, "", "", "", "", "", 6])
secay.tick_params(which="both", labelsize=22, direction='in')
secay.set_ylabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)


#Create contour plot.

CS = ax.contour(points_x, points_y, deltachisqs_all, levels=[3.219, 5.991, 13.816], linewidths=3)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=16)
plt.ylabel(r"$\tilde\kappa_g$", fontsize=28)
plt.xlabel(r"$\kappa_g$", fontsize=28)
plt.plot([-0.6, 0.4], [2, 2], '--', color="k", label="On-shell Higgs constraints", markersize=14)
plt.plot([-0.6, 0.4], [-2, -2], '--', color="k", markersize=14)
plt.plot([-0.6, -0.6], [-2, 2], '--', color="k", markersize=14)
plt.plot([0.4, 0.4], [-2, 2], '--', color="k", markersize=14)
plt.plot(0, 0, 'x', color="r", label="Standard Model", markersize=10)
plt.xlim(-9, 9)
plt.ylim(-10, (2/3)*9)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(fontsize=20, loc="lower right")
plt.tight_layout()
plt.savefig("1_full_contour_plot.pdf")



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
            plt.savefig("2_p=0.05_paths.pdf")






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
            #xs2=np.concatenate((vertices[0:440,0], vertices[1400:2400,0], vertices[3500:4250,0], vertices[5200:6200,0], vertices[7140:,0]))
            #ys2=np.concatenate((vertices[0:440,1], vertices[1400:2400,1], vertices[3500:4250,1], vertices[5200:6200,1], vertices[7140:,1]))
            xs2=np.concatenate((vertices[1400:2150,0], vertices[3000:4400,0], vertices[5420:7000,0], vertices[7750:9400,0], vertices[10200:,0]))
            ys2=np.concatenate((vertices[1400:2150,1], vertices[3000:4400,1], vertices[5420:7000,1], vertices[7750:9400,1], vertices[10200:,1]))
        

            
            plt.plot(xs2, ys2, "r")
            plt.savefig("3_vertices.pdf")



fig, ax = plt.subplots(figsize=(1.1*10, 1.1*(8/9)*10), dpi=100)

secax = ax.secondary_xaxis('top', functions=(kg2lam, lam2kg))
secax.set_xticks([-6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
secax.set_xticklabels([6, "", "", "", "", "", 3, "", "", 1.5, 1.5, "", "", 3, "", "", "", "", "", 6])
secax.tick_params(which="both", labelsize=22, direction='in')

secax.set_xlabel(r'Equivalent $\Lambda\,$[TeV]', fontsize=28)

secay = ax.secondary_yaxis('right', functions=(kgtilde2lam, lam2kgtilde))
secay.set_yticks([-6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
secay.set_yticklabels([6, "", "", "", "", "", 3, "", "", 1.5, "", 1.5, "", "", 3, "", "", "", "", "", 6])
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
plt.plot([-0.6, 0.4], [2, 2], '--', color="k", label="On-shell Higgs constraints", markersize=14)
plt.plot([-0.6, 0.4], [-2, -2], '--', color="k", markersize=14)
plt.plot([-0.6, -0.6], [-2, 2], '--', color="k", markersize=14)
plt.plot([0.4, 0.4], [-2, 2], '--', color="k", markersize=14)
plt.plot(0, 0, 'x', color="r", label="Standard Model", markersize=10)
plt.xlim(-1.5*9, 1.5*9)
plt.ylim(-1.5*10, 1.5*(2/3)*9)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(fontsize=20, loc="lower right")
plt.tight_layout()
plt.savefig("figure_11.pdf")