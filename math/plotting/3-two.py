#!/usr/bin/env python3
"""Module that plots two line graph using one input x"""
import numpy as np
import matplotlib.pyplot as plt


def two():
    """this is documentation to plots two line graph using one input x"""
    x = np.arange(0, 21000, 1000)
    # This represents a decay rate at 50%
    # log convert it into rate of -0.693
    r = np.log(0.5)
    # over time decay, and these are decay speed
    t1 = 5730
    t2 = 1600
    # continuous decay formula, give the fraction remaining at time x
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    # set size of the graph
    plt.figure(figsize=(6.4, 4.8))

    # my code is here
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.title("Exponential Decay of C-14")
    plt.xlim(0, 20000)
    plt.ylim(0, 1)
    plt.plot(x, y1, 'r-', label='C-14')
    plt.plot(x, y2, 'g-', label='Ra-226')
    plt.legend(loc='upper right')
    plt.show()
