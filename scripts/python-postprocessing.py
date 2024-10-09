#!/usr/bin/env python3

import os

import matplotlib.pyplot as plt
import pandas as pd



def plot_data(file_path, logy= True):
    """
    https://gist.github.com/kastnerp/e76fb8ec1394fe0b0926deb07b9689f1
    """

    export_path = "visualization/plots"
    data_name = file_path.split("/")[-1].rstrip('.dat')

    if not os.path.exists(file_path):
        print("File not found: ", file_path)
        return False

    with open(file_path, 'r') as file:
        lines_starting_with_hash = [line for line in file if line.startswith('#')]

    print("write plot for " +file_path)
    data = pd.read_csv(file_path, skiprows=len(lines_starting_with_hash)-1, delimiter='\s+').iloc[:, 1:].shift(+1,axis=1).drop(["Time"], axis= 1)

    plot = data.plot(logy= logy, figsize=(15,5))
    fig = plot.get_figure()
    ax = plt.gca()
    ax.legend(loc='upper right')
    ax.set_xlabel("Iterations")
    ax.set_ylabel(data_name)
    ax.grid(linestyle="--")

    os.makedirs(export_path, exist_ok=True)
    plt.savefig(os.path.join(export_path, data_name +".png") ,dpi=600)


if __name__ == "__main__":
    plot_data("postProcessing/residuals/0/residuals.dat")
    plot_data("postProcessing/probes/0/p", logy= False)
