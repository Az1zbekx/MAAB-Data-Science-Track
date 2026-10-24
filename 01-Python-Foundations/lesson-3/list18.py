from collections import deque

lst = [1, 2, 3, 4]
sub = [2, 3]

def contains_sublist(lst, sub):
    for i in range(len(lst) - len(sub) + 1):
        if lst[i:i+len(sub)] == sub:
            return True
    return False

print(contains_sublist(lst, sub))
