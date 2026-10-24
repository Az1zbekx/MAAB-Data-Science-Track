import numpy as np
arr = np.random.rand(5, 5)
mean = arr.mean()
for i in range(5):
    for j in range(5):
        arr[i][j] = (arr[i][j] - arr.min()) / (arr.max() - arr.min())
print(arr)
