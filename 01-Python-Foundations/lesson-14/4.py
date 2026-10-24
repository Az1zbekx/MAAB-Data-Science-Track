import numpy as np

A = np.array([10, -2, 3, -2, 8, -1, 3, -1, 6])
A = A.reshape(3, 3)
b = np.array([12, -5, 15])
b = b.reshape(3, 1)
res = np.linalg.solve(A, b)
print(res)
