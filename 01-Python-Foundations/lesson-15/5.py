data = np.random.normal(0, 1, 1000)

plt.figure()
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
