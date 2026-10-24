d = {'a': 1, 'b': {'x': 10}}
print(any(isinstance(v, dict) for v in d.values()))
