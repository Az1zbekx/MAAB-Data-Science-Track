d = {'a': 1, 'b': 2, 'c': 1}
val = 1
keys = [k for k, v in d.items() if v == val]
print(keys)
