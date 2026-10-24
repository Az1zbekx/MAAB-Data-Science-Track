lst = [1, 2, 3, 4]
n = len(lst)
if n % 2 == 1:
    print(lst[n // 2])
else:
    print(lst[n // 2 - 1], lst[n // 2])
