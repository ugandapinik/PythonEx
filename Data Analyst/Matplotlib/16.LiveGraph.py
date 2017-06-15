from matplotlib import pyplot as plt
from matplotlib import animation as animation
from matplotlib import style


# SELECT THE STYLE
style.use('fivethirtyeight')

figure = plt.figure()
ax1 = figure.add_subplot(1, 1, 1)


def animate(interval):
    graph_data = open('example.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []

    for line in lines:
        if  len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)

    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(figure, animate, interval=1000)
plt.show()

