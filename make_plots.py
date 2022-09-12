import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

import numpy as np

###To make plots

def generic_histogram(x, x_name, output_path, output_name, y_name = None, label=None, range=None, bins=None, in_chain=False):
    fig, ax = plt.subplots()
    alpha=1
    if len(x) > 1:
        alpha=0.6
    ax.hist(x, bins=bins, range=range, label=label, alpha=alpha, histtype='stepfilled')
    ax.set_xlabel(x_name)
    if y_name is not None:
        ax.set_ylabel(y_name)
    ax.legend(loc='best')
    if not in_chain:
        plt.savefig(output_path+'/'+output_name+'.png', format='png', transparent=False)
        plt.close()
        plt.clf()

def generic_2D_plot(x,y,x_range, x_bins, x_name, y_range, y_bins, y_name, label, output_path, output_name, title = None, normalization=False, weights=None, xLog=False, yLog=False, save_plot=True, return_hist=False):

    fig, ax = plt.subplots()
    hh, xedges, yedges, _ = ax.hist2d(x,y, [x_bins, y_bins], [x_range,y_range], density=normalization, weights=weights , label=label)
    fig.colorbar(_, ax=ax)
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    if title is not None:
        plt.title = title
    plt.legend()
    if xLog:
        plt.xscale('log', nonposx='clip')
    if yLog:
        plt.yscale('log', nonposy='clip')
    if save_plot:
        plt.savefig(output_path+'/'+output_name+'.png', format='png', transparent=False)


    if return_hist:
        return hh, xedges, yedges

def generic_3D_plot(x,y,z,strength, x_label, y_label, z_label, strength_label, output_path, output_name):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    p = ax.scatter3D(x, y, z, c=strength, cmap='plasma', s=2)
    ax.set_box_aspect([np.ptp(i) for i in [x,y,z]])
    cbar = fig.colorbar(p, ax=ax)
    cbar.set_label(strength_label)
    plt.savefig(output_path+'/'+output_name+'.png', format='png', transparent=False)