txt = input("Matn kiriting: ")
unli, undosh = 0, 0
arr = ['a', 'e' , 'u', 'i', 'o']
for i in txt:
    if i.isalpha() and i.lower() in arr:
        unli += 1
    elif i.isalpha() and i.lower() not in arr:
        undosh += 1
print(f"Unlilar soni {unli}\nUndoshlar soni {undosh}")
