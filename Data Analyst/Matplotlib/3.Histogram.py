# Histogram
''' 
Histogram: A diagram consisting of rectangles whose area is proportional
to the frequency of a variable whose WIDTH IS EUAL TO CLASS INTERVAL 
'''

from matplotlib import pyplot as plt

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 4, 9, 102, 110, 120, 122, 130, 11, 115, 112, 80, 75, 65, 54, 44, 43, 42, 48]
ids = [x for x in range(len(population_ages))]

print(ids)

bins = [0, 10, 20, 40, 50, 60, 70, 80, 90, 100, 120, 130]


plt.hist(population_ages, bins, histtype='bar', rwidth=0.8, label='Population')


plt.xlabel("x")
plt.ylabel("y")
plt.title("Population Ages")
plt.legend()
plt.show()