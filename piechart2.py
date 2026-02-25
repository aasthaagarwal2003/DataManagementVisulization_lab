import matplotlib.pyplot as plt

activities = ['Study', 'Sleep', 'Exercise', 'Entertainment']
hours = [8, 7, 2, 7]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()