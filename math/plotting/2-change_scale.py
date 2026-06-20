#!/usr/bin/env python3
"""Module that plots y wrt x as aline graph"""
import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    "this is documentation for change scale function."
    x = np.arange(0, 28651, 5730)
    # 0.5 means repeated 50% loss in y value and log convert it into rate
    # and exponential applies that rate continously over time
    # log(0.5) = -0.683 so after every years rather after 5730 years
    # y value will decrease with this rate (-0.683/5730)
    # 5730 year required for y value to be half (50%, or 0.5)
    # what if log(0.4), it means after every 5730 years,
    # remaining y value will be 40%, or 0.4 but in plain language
    # y value loss 60% over 5730 years but not decrease
    # log(0.5) tell 50% of y value remain rather 50% decrease
    # after every 5730 year, y value reduce to half
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
    plt.savefig("2-change_scale.png")
    plt.show()
