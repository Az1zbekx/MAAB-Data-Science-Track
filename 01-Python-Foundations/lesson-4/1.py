try:
    l1 = list(map(str, input("l1 = ").split()))
    l2 = list(map(str, input("l2 = ").split()))
    l3 = []
    for i in l1:
        if i not in l2:
            l3.append(i)
    for i in l2:
        if i not in l1:
            l3.append(i)
    print(f"l3 = {l3}")
except ValueError:
    print("Error")