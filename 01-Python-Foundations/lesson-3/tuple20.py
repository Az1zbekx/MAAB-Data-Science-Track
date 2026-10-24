t = (1, 2, 3, 4, 5, 6)
n = 2
nested = tuple(t[i:i+n] for i in range(0, len(t), n))
print(nested)
