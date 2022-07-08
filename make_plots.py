import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def generic_2D_plot(x,y,x_range, x_bins, x_name, y_range, y_bins, y_name, label, output_path, output_name, normalization=False, weights=None, xLog=False, yLog=False, save_plot=True, return_hist=False):

    fig, ax = plt.subplots()
    hh, xedges, yedges, _ = ax.hist2d(x,y, [x_bins, y_bins], [x_range,y_range], density=normalization, weights=weights , label=label)
    fig.colorbar(_, ax=ax)
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    plt.legend()
    if xLog:
        plt.xscale('log', nonposx='clip')
    if yLog:
        plt.yscale('log', nonposy='clip')
    if save_plot:
        plt.savefig(output_path+'/'+output_name+'.png', format='png', transparent=False)

    plt.close()
    plt.clf()

    if return_hist:
        return hh, xedges, yedges