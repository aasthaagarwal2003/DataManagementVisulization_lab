import matplotlib.pyplot as plt

subjects = ['Math', 'Physics', 'Chemistry', 'English']
marks = [85, 78, 92, 74]

plt.bar(subjects, marks)
plt.title("Bar Chart")
plt.show()