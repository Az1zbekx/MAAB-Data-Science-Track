txt = input("Matn kiriting: ")
s = input("O'zgartirishni xoxlagan jumlangiz: ")
k = input("Qanday o'zgartirmoqchisiz: ")
if s in txt:
    txt = txt.replace(s, k)
    print(f"Matn talablarga binoan o'zgardi\n{txt}")
else:
    print("O'zgaruvchi satr matndan topilmadi")
