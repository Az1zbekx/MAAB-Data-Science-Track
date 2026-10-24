import numpy as np

A = np.array([4, 5, 6, 3, -1, 1, 2, 1, -2])
A = A.reshape(3, 3)
b = np.array([7, 4, 5])
b = b.reshape(3, 1)
res = np.linalg.solve(A, b)
print(res)
