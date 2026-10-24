import numpy as np


def fun(a, b):
    return a ** b


arr1 = np.array([2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4])

vfun = np.vectorize(fun)
print(vfun(arr1, arr2))
