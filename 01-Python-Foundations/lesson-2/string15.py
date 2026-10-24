txt = input("Matn kiriting: ")
s = ""
arr = txt.split()
for i in arr:
    s += i[0]
print(f"Matndagi so'zlarning bosh harflaridan tuzilgan so'z {s}")