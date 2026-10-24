t = (1, 2, 2, 3, 1)
seen = set()
unique = tuple(x for x in t if not (x in seen or seen.add(x)))
print(unique)
