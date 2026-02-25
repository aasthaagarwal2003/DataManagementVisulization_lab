import matplotlib.pyplot as plt

n = int(input("Enter number of categories: "))
labels = []
values = []

for i in range(n):
    labels.append(input("Enter label: "))
    values.append(int(input("Enter value: ")))

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart (User Input)")
plt.show()
