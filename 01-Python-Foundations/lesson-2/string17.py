txt = input("Matn kiriting: ")
arr = ['a', 'e', 'u', 'i', 'o']
for i in txt:
    if i.lower() in arr:
        txt = txt.replace(i, '*')
print(f"Unli harflar * ga o'zgardi {txt}")