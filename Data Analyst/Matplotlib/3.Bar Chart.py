# Bar Chart and Histogram
#---------------------------------------
from matplotlib import pyplot as plt

''' 
Histogram: A diagram consisting of rectangles whose area is proportional
to the frequency of a variable whose WIDTH IS EUAL TO CLASS INTERVAL 
-------------------------------------------------------------------------
Bar Chart: A bar chart or bar graph is a chart or graph that presents 
grouped data with rectangular bars with lengths proportional 
to the values that they represent. 
'''

# Bar Chart
x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

plt.bar(x, y, label='Bar1', color='violet')
plt.bar(x2, y2, label="Bar2", color='cyan')

plt.xlabel("Population")
plt.ylabel("Economy")
plt.title("Bangladesh")
plt.legend()

plt.show()

