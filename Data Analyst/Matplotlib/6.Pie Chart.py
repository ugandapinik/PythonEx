from matplotlib import pyplot as plt

# Pie Chart


days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

# x1=[68,74,69,68,72,66,71]
# y1=[145,157,158,182,204,144,198]
#
# x2=[61,63,65,67,69]
# y2=[107,118,122,144,132]

slices = [7, 2, 2, 13]
activities = ['Sleeping', 'Eating', 'Working', 'Playing']
colors = ['c', 'm', 'r', 'b']

plt.pie(slices, labels=activities,
        colors=colors,
        startangle=90,
        shadow=True,
        explode=(0, 0.05, 0, 0),
        autopct='%1.1f%%')


plt.xlabel("Days")
plt.ylabel("Daily Works")
plt.title("Stack Plots")
plt.show()