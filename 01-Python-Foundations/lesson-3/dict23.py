a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(not a.keys().isdisjoint(b.keys()))
