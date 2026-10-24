lst = [1, 2, 2, 3, 1]
seen = set()
unique = [x for x in lst if not (x in seen or seen.add(x))]
print(unique)
