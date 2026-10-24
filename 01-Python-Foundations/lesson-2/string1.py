try:
    name = input("Salom ismingiz nima: ")
    year = int(input("Tug'ilgan yilingiz: "))
    if year > 0 and year < 2026:
        print(f"{name} sizning yoshingiz {2025 - year} da")
    else:
        print("Xatolik yuz berdi: ")
except ValueError:
    print("Xatolik yuz berdi")
