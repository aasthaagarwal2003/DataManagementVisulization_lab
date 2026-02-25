import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
x, y = [], []
line, = ax.plot([], [])

ax.set_xlim(0, 10)
ax.set_ylim(0, 100)

def animate(i):
    x.append(i)
    y.append(i*i)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, frames=10, interval=500)
plt.show()