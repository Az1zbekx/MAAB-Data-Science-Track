t = (1, 2)
n = 3
repeated = tuple(x for x in t for _ in range(n))
print(repeated)
