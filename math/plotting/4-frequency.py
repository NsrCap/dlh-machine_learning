#!/usr/bin/env python3
"""Module that plots two line graph using one input x"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """this is documentation to plots two line graph using one input x"""
    # generate same sequence of random number every time we run the code
    np.random.seed(5)
    # generate 50 random data points with mean 68 and standard deviation 15
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))
    # understood from visual provided in task, rather explicit statement
    intervals = np.arange(0, 101, 10)
    # create x and y axis values auto using hist, with 50 random data points
    # each data point represent student grades
    # hist will auto calculate range of grades (min and max) from 50 random no.
    # lets say mini grade was 50 and maxi was 96 = 46/10bin = 4.6 approx 5
    # from start 50+5=55 so first range is 50-55 and so on
    # this represent value on x-axis
    # Y-axis value, hist auto counts students falling in each range
    plt.hist(student_grades, bins=intervals, edgecolor="black")
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    # understood from visual provided in task, rather explicit statement
    plt.xlim(0, 100)
    plt.ylim(0, 30)
    plt.show()
