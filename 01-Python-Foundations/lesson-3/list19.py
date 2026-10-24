lst = [1, 2, 3, 2]
old = 2
new = 99
if old in lst:
    idx = lst.index(old)
    lst[idx] = new
print(lst)
