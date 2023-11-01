#!/usr/bin/env python3

import os

import matplotlib.pyplot as plt
import pandas as pd



def plot_residuals():
    """
    https://gist.github.com/kastnerp/e76fb8ec1394fe0b0926deb07b9689f1
    """

    file_path = "postProcessing/residuals/0/residuals.dat"
    export_path = "doc/exports"

    if not os.path.exists(file_path):
        # print("File not found: ", file_path)
        return False

    print("write residuals plot")
    data = pd.read_csv(file_path, skiprows=1, delimiter='\s+').iloc[:, 1:].shift(+1,axis=1).drop(["Time"], axis= 1)

    plot = data.plot(logy= True, figsize=(15,5))
    fig = plot.get_figure()
    ax = plt.gca()
    ax.legend(loc='upper right')
    ax.set_xlabel("Iterations")
    ax.set_ylabel("Residuals")
    ax.grid(linestyle="--")

    os.makedirs(export_path, exist_ok=True)
    plt.savefig(os.path.join(export_path, "residuals.png") ,dpi=600)


if __name__ == "__main__":
    plot_residuals()
