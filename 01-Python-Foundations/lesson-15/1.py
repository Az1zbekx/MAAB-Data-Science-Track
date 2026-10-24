import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4

plt.figure()
plt.plot(x, y, color='blue')
plt.title("Plot of f(x) = x² - 4x + 4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
