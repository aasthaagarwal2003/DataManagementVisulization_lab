import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))
x = []
y = []

for i in range(n):
    x.append(int(input("Enter x value: ")))
    y.append(int(input("Enter y value: ")))

plt.scatter(x, y)
plt.title("Scatter Plot (User Input)")
plt.show()