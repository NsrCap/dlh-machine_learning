#!/usr/bin/env python3
"""Module that plots y as a scatter graph"""
import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """use value of x to plot y as a scatter graph"""
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)
    plt.figure(figsize=(6.4, 4.8))

    # my code is here
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.title("Exponential Decay of C-14")
    plt.xlim(0, 28650)
    #  It will only changes how we display the axis, log is for declining axis
    plt.yscale("log")
    plt.plot(x, y)
    plt.show()
