lst = [1, 2, 3, 4, 5, 6]
n = 2
nested = [lst[i:i+n] for i in range(0, len(lst), n)]
print(nested)
