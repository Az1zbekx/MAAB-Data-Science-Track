try:
    a, b = map(int, input("Ikkita butun son kiriting: ").split())
    print(bool(a == b))
except ValueError:
    print("Xatolik yuz berdi")
    