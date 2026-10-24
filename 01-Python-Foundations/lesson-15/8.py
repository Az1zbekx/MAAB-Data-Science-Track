labels = ['T1', 'T2', 'T3', 'T4']
cat_a = [10, 15, 20, 25]
cat_b = [5, 10, 15, 10]
cat_c = [2, 5, 10, 8]

x = np.arange(len(labels))

plt.figure()
plt.bar(x, cat_a, label='Category A', color='skyblue')
plt.bar(x, cat_b, bottom=cat_a, label='Category B', color='orange')
bottom_cat = np.array(cat_a) + np.array(cat_b)
plt.bar(x, cat_c, bottom=bottom_cat, label='Category C', color='green')

plt.xticks(x, labels)
plt.xlabel("Time Period")
plt.ylabel("Values")
plt.title("Stacked Bar Chart of Categories Over Time")
plt.legend()
plt.show()
