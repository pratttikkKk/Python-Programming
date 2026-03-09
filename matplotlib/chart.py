import matplotlib.pyplot as plt

sizes = [40, 30, 20, 10]
labels = ["Red", "Blue", "Green", "Yellow"]

plt.figure()
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie chart")
plt.show()
