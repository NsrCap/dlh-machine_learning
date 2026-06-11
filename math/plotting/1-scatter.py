#!/usr/bin/env python3
"""Module that plots y as a scatter graph"""
import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """use value of x to plot y as a scatter graph"""
    # meand of value on x-axis and y-axis
    mean = [69, 0]
    # 15 diagonal represents data points spread
    # while 8 off-diagonat represents relationship btw x & y
    # each array contain x, y values for each data point covariance
    cov = [[15, 8], [8, 15]]
    # make random data points repeatable
    # each time same random data points will be generated
    np.random.seed(5)
    # generate 2000 random data points each point represents x, and y value
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    # shift y by 180 from 0
    y += 180
    plt.figure(figsize=(6.4, 4.8))

    # my code is here
    plt.xlabel("Height (in)")
    plt.ylabel("Weight (lbs)")
    plt.title("Men's Height vs Weight")
    plt.scatter(x, y, color="magenta")
    plt.show()
