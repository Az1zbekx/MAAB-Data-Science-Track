import numpy as np


def fun(F):
    return (F - 32) * 5 / 9


arr = np.array([32, 68, 100, 212, 77])

vfun = np.vectorize(fun)

print(vfun(arr))
