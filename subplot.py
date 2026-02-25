import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))
x = []
y1 = []
y2 = []

for i in range(n):
    x.append(int(input("Enter x value: ")))
    y1.append(int(input("Enter y1 value: ")))
    y2.append(int(input("Enter y2 value: ")))

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Plot 2")

plt.tight_layout()
plt.show()