import matplotlib.pyplot as plt
import numpy as np
#from Figures
import sys
sys.path.insert(1, '..')

from factor_conversions import kg2lam, kgtilde2lam, lam2kg, lam2kgtilde
from plot_funcs import fmt

points_x_mww=np.load("points_x_kg_mww.npy")
points_y_mww=np.load("points_y_kg_mww.npy")
deltachisqs_all_mww=np.load("deltachisqs_all_mww.npy")

points_x_mww4=np.load("points_x_kg_mww4.npy")
points_y_mww4=np.load("points_y_kg_mww4.npy")
deltachisqs_all_mww4=np.load("deltachisqs_all_mww4.npy")

points_x_1=np.load("points_x_kg_1.npy")
points_y_1=np.load("points_y_kg_1.npy")
deltachisqs_all_1=np.load("deltachisqs_all_1.npy")

points_x_05=np.load("points_x_kg_05.npy")
points_y_05=np.load("points_y_kg_05.npy")
deltachisqs_all_05=np.load("deltachisqs_all_05.npy")


points_x_025=np.load("points_x_kg_025.npy")
points_y_025=np.load("points_y_kg_025.npy")
deltachisqs_all_025=np.load("deltachisqs_all_025.npy")


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

CS = ax.contour(points_x_mww4, points_y_mww4, deltachisqs_all_mww4, levels=[3.219, 5.991, 13.816], linewidths=3)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=16)
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
plt.savefig("1_full_contour_plot_mww4.pdf")


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            xs2_mww4=vertices[:,0]
            ys2_mww4=vertices[:,1]
            plt.plot(xs2_mww4, ys2_mww4)
            plt.savefig("2_p=0.05_paths_mww4.pdf")


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            plt.plot(xs2_mww4, ys2_mww4)
            #Have to manually vary these ranges to select the correct points.
            #xs2_mww4=np.concatenate((vertices[0:300,0], vertices[1100:2250,0], vertices[7540:9000,0]))
            #ys2_mww4=np.concatenate((vertices[0:300,1], vertices[1100:2250,1], vertices[7540:9000,1]))
            
            xs2_mww4=vertices[0:3100,0]
            ys2_mww4=vertices[0:3100,1]
            
            plt.plot(xs2_mww4, ys2_mww4, "r")
            plt.savefig("3_vertices_mww4.pdf")



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

CS = ax.contour(points_x_mww, points_y_mww, deltachisqs_all_mww, levels=[3.219, 5.991, 13.816], linewidths=3)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=16)
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
plt.savefig("1_full_contour_plot_mww.pdf")


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            xs2_mww=vertices[:,0]
            ys2_mww=vertices[:,1]
            plt.plot(xs2_mww, ys2_mww)
            plt.savefig("2_p=0.05_paths_mww.pdf")


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            plt.plot(xs2_mww, ys2_mww)
            #Have to manually vary these ranges to select the correct points.
            #xs2_mww=np.concatenate((vertices[780:1900,0], vertices[2800:4250,0], vertices[5380:6300,0], vertices[7540:9000,0]))
            #ys2_mww=np.concatenate((vertices[780:1900,1], vertices[2800:4250,1], vertices[5380:6300,1], vertices[7540:9000,1]))
            xs2_mww=vertices[0:7000,0]
            ys2_mww=vertices[0:7000,1]
            
            plt.plot(xs2_mww, ys2_mww, "r")
            plt.savefig("3_vertices_mww.pdf")



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

CS = ax.contour(points_x_1, points_y_1, deltachisqs_all_1, levels=[3.219, 5.991, 13.816], linewidths=3)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=16)
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
plt.savefig("1_full_contour_plot_1.pdf")


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            xs2_1=vertices[:,0]
            ys2_1=vertices[:,1]
            plt.plot(xs2_1, ys2_1)
            plt.savefig("2_p=0.05_paths_1.pdf")


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            plt.plot(xs2_1, ys2_1)
            #Have to manually vary these ranges to select the correct points.
            #xs2_1=np.concatenate((vertices[0:5500,0], vertices[6300:8040,0]))
            #ys2_1=np.concatenate((vertices[0:5500,1], vertices[6300:8040,1]))
            xs2_1=vertices[0:7000,0]
            ys2_1=vertices[0:7000,1]
            
            plt.plot(xs2_1, ys2_1, "r")
            plt.savefig("3_vertices_1.pdf")




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

CS = ax.contour(points_x_05, points_y_05, deltachisqs_all_05, levels=[3.219, 5.991, 13.816], linewidths=3)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=16)
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
plt.savefig("1_full_contour_plot_05.pdf")


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            xs2_05=vertices[:,0]
            ys2_05=vertices[:,1]
            plt.plot(xs2_05, ys2_05)
            plt.savefig("2_p=0.05_paths_05.pdf")


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            plt.plot(xs2_05, ys2_05)
            #Have to manually vary these ranges to select the correct points.
            xs2_05=np.concatenate((vertices[1400:2150,0], vertices[3000:4400,0], vertices[5420:7000,0], vertices[7750:9400,0], vertices[10200:,0]))
            ys2_05=np.concatenate((vertices[1400:2150,1], vertices[3000:4400,1], vertices[5420:7000,1], vertices[7750:9400,1], vertices[10200:,1]))
        
            
            plt.plot(xs2_05, ys2_05, "r")
            plt.savefig("3_vertices_05.pdf")




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

CS = ax.contour(points_x_025, points_y_025, deltachisqs_all_025, levels=[3.219, 5.991, 13.816], linewidths=3)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=16)
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
plt.savefig("1_full_contour_plot_025.pdf")


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            xs2_025=vertices[:,0]
            ys2_025=vertices[:,1]
            plt.plot(xs2_025, ys2_025)
            plt.savefig("2_p=0.05_paths_025.pdf")


for i, collection in enumerate(CS.collections):
    paths = collection.get_paths()  # Get all the paths for the contour level
    print(f"Contour level {CS.levels[i]}:")
    #Find the p=0.05 level
    if CS.levels[i]==5.991:
        plt.figure()
        for path in paths:
            vertices = path.vertices  # Extract the vertices of the path
            plt.plot(xs2_025, ys2_025)
            #Have to manually vary these ranges to select the correct points.
            xs2_025=np.concatenate((vertices[0:400,0], vertices[2300:3300,0], vertices[5000:6000,0], vertices[7800:8800,0], vertices[10600:11100,0]))
            ys2_025=np.concatenate((vertices[0:400,1], vertices[2300:3300,1], vertices[5000:6000,1], vertices[7800:8800,1], vertices[10600:11100,1]))
        
            
            plt.plot(xs2_025, ys2_025, "r")
            plt.savefig("3_vertices_025.pdf")



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



A = np.column_stack((xs2_1**2, xs2_1 * ys2_1, ys2_1**2, xs2_1, ys2_1))
b = np.ones_like(xs2_1)
x = np.linalg.lstsq(A, b)[0].squeeze()
x_coord = np.linspace(-10,10,300)
y_coord = np.linspace(-10,10,300)
X_coord, Y_coord = np.meshgrid(x_coord, y_coord)
Z_coord = x[0] * X_coord ** 2 + x[1] * X_coord * Y_coord + x[2] * Y_coord**2 + x[3] * X_coord + x[4] * Y_coord

plt.contour(X_coord, Y_coord, Z_coord, levels=[1], colors=('#3c649f'), linewidths=2)
#To create legend
plt.plot(100,100, color='#3c649f', label=r"$p=0.05$, $\sigma_6^2>\sigma_8^2$")


A = np.column_stack((xs2_05**2, xs2_05 * ys2_05, ys2_05**2, xs2_05, ys2_05))
b = np.ones_like(xs2_05)
x = np.linalg.lstsq(A, b)[0].squeeze()
x_coord = np.linspace(-10,10,300)
y_coord = np.linspace(-10,10,300)
X_coord, Y_coord = np.meshgrid(x_coord, y_coord)
Z_coord = x[0] * X_coord ** 2 + x[1] * X_coord * Y_coord + x[2] * Y_coord**2 + x[3] * X_coord + x[4] * Y_coord

plt.contour(X_coord, Y_coord, Z_coord, levels=[1], colors=('#4779c4'), linewidths=2)
#To create legend
plt.plot(100,100, color='#4779c4', label=r"$p=0.05$, $\sigma_6^2>2\times\sigma_8^2$")
#  #4779c4
#  #2E4B7F


A = np.column_stack((xs2_025**2, xs2_025 * ys2_025, ys2_025**2, xs2_025, ys2_025))
b = np.ones_like(xs2_025)
x = np.linalg.lstsq(A, b)[0].squeeze()
x_coord = np.linspace(-15,15,300)
y_coord = np.linspace(-15,15,300)
X_coord, Y_coord = np.meshgrid(x_coord, y_coord)
Z_coord = x[0] * X_coord ** 2 + x[1] * X_coord * Y_coord + x[2] * Y_coord**2 + x[3] * X_coord + x[4] * Y_coord

plt.contour(X_coord, Y_coord, Z_coord, levels=[1], colors=('#83aff0'), linewidths=2)
#To create legend
plt.plot(100,100, color='#83aff0', label=r"$p=0.05$, $\sigma_6^2>4\times\sigma_8^2$")

A = np.column_stack((xs2_mww4**2, xs2_mww4 * ys2_mww4, ys2_mww4**2, xs2_mww4, ys2_mww4))
b = np.ones_like(xs2_mww4)
x = np.linalg.lstsq(A, b)[0].squeeze()
x_coord = np.linspace(-10,10,300)
y_coord = np.linspace(-10,10,300)
X_coord, Y_coord = np.meshgrid(x_coord, y_coord)
Z_coord = x[0] * X_coord ** 2 + x[1] * X_coord * Y_coord + x[2] * Y_coord**2 + x[3] * X_coord + x[4] * Y_coord

plt.contour(X_coord, Y_coord, Z_coord, levels=[1], colors=('yellow'), linestyles="--", linewidths=2)
#To create legend
plt.plot(100,100, color='yellow', linestyle="--", label=r"$p=0.05$, $\Lambda>4\times M_{e\mu}$")


A = np.column_stack((xs2_mww**2, xs2_mww * ys2_mww, ys2_mww**2, xs2_mww, ys2_mww))
b = np.ones_like(xs2_mww)
x = np.linalg.lstsq(A, b)[0].squeeze()
x_coord = np.linspace(-10,10,300)
y_coord = np.linspace(-10,10,300)
X_coord, Y_coord = np.meshgrid(x_coord, y_coord)
Z_coord = x[0] * X_coord ** 2 + x[1] * X_coord * Y_coord + x[2] * Y_coord**2 + x[3] * X_coord + x[4] * Y_coord

plt.contour(X_coord, Y_coord, Z_coord, levels=[1], colors=('purple'), linestyles="--", linewidths=2)
#To create legend
plt.plot(100,100, color='purple', linestyle="--", label=r"$p=0.05$, $\Lambda>2\times M_{e\mu}$")


plt.ylabel(r"$\tilde\kappa_g$", fontsize=28)
plt.xlabel(r"$\kappa_g$", fontsize=28)
#plt.plot([-0.6, 0.4], [2, 2], '--', color="k", label="On-shell Higgs constraints", markersize=14)
#plt.plot([-0.6, 0.4], [-2, -2], '--', color="k", markersize=14)
#plt.plot([-0.6, -0.6], [-2, 2], '--', color="k", markersize=14)
#plt.plot([0.4, 0.4], [-2, 2], '--', color="k", markersize=14)
plt.plot(0, 0, 'x', color="r", label="Standard Model", markersize=10)
plt.xlim(-1.5*9, 1.5*9)
plt.ylim(-1.5*10, 1.5*(2/3)*9)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(fontsize=18.5, loc="lower right", ncol=2)
plt.tight_layout()
plt.savefig("figure_11_comp.pdf")