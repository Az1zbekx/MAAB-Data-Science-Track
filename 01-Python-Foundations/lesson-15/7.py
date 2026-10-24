products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['red', 'blue', 'green', 'purple', 'orange']

plt.figure()
plt.bar(products, sales, color=colors)
plt.title("Sales by Product")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()
