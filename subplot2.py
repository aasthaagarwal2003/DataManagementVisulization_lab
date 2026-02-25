import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Linear")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Quadratic")

plt.tight_layout()
plt.show()