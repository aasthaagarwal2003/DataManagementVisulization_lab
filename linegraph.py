import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))
x = []
y = []

for i in range(n):
    x.append(int(input("Enter x value: ")))
    y.append(int(input("Enter y value: ")))

plt.plot(x, y)
plt.title("Line Graph (User Input)")
plt.show()