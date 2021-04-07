from matplotlib import pyplot as plt

# Data for x axis
dev_x = [x for x in range(25, 36)]
# Data for y axis
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# Simple plot
# ----------------------------

# plt.plot(dev_x, dev_y)
# plt.show()

# ----------------------------

# Simple plot
# ----------------------------

plt.plot(dev_x, dev_y)
plt.show()

# ----------------------------
# Plot with label and title

# plt.plot(dev_x, dev_y)
# plt.xlabel('Ages')
# plt.ylabel('Salary')
# plt.title('Median Salary (USD) by Age')
# plt.show()

# ----------------------------

plt.plot(dev_x, dev_y)
plt.xlabel('Ages')
plt.ylabel('Salary')
plt.title('Median Salary (USD) by Age')
plt.show()

# ----------------------------
