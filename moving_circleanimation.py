import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
circle = plt.Circle((0, 0), 0.1)
ax.add_patch(circle)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def animate(i):
    circle.center = (i, 5)
    return circle,

ani = animation.FuncAnimation(fig, animate, frames=10, interval=200)
plt.show()