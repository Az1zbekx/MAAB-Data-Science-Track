"""
1. In Python, the difference between break and continue is that when a condition with break is met, the loop stops immediately. But when continue is used, it simply skips that iteration and continues with the next one.
a = 5
for i in range(0, 10):
    if a == 5:
        break

for i in range(0, 10):
    if a == 5:
        continue

2. A for loop has a clear starting and ending point — it runs up to a certain range or sequence. A while loop, on the other hand, doesn’t have a fixed end; it continues running as long as a condition remains true.

for i in range(0, 10):
    print(i)


i = 0
while i < 10:
    print(i)
    i += 1



3. A nested for loop can be used, for example, when you have a list inside another list and you want to check or process each element inside them.d forni aytaylik list ichida list bolsa ularni har birirni tekshirishda ishlatsak boladi
l = [[1,2],['a','b']]
for i in l:
    for j in i:
        print(j)

"""