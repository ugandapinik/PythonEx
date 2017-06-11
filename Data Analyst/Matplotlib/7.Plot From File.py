from matplotlib import pyplot as plt
import csv


x = []
y = []

'''
# Part: 1
# Using buidling package 'CSV'
with open('example.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label="Loaded From File!")
'''

import numpy as np
# Import the numpy and using 'Numpy'

x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x, y, label="By Numpy from Files")


plt.xlabel("Days")
plt.ylabel("Daily Works")
plt.title("Stack Plots")
plt.show()