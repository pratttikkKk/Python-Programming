import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
values = [10, 24, 36, 8]

plt.figure()
plt.bar(labels, values)
plt.title("Bar chart")
plt.xlabel("Label")
plt.ylabel("Value")
plt.show()
