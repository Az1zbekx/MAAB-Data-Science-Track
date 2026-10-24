x = np.linspace(-5, 5, 300)
x_positive = np.linspace(0, 5, 300)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, x**3, color='purple')
axs[0, 0].set_title("f(x) = x³")
axs[0, 0].set_xlabel("x")
axs[0, 0].set_ylabel("y")

axs[0, 1].plot(x, np.sin(x), color='green')
axs[0, 1].set_title("f(x) = sin(x)")
axs[0, 1].set_xlabel("x")
axs[0, 1].set_ylabel("y")

axs[1, 0].plot(x, np.exp(x), color='orange')
axs[1, 0].set_title("f(x) = exp(x)")
axs[1, 0].set_xlabel("x")
axs[1, 0].set_ylabel("y")

axs[1, 1].plot(x_positive, np.log(x_positive + 1), color='red')
axs[1, 1].set_title("f(x) = log(x + 1)")
axs[1, 1].set_xlabel("x")
axs[1, 1].set_ylabel("y")

plt.tight_layout()
plt.show()
