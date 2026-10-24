t = (1, 2, 3, 2)
element = 2
lst = list(t)
if element in lst:
    lst.remove(element)
new_t = tuple(lst)
print(new_t)
