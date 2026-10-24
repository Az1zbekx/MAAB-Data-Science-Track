try:
    a, b, c = map(int, input("Uchta butun son kiriting: ").split())
    print((bool(a != b and b != c and a != c)))
except ValueError:
    print("Xatolik yuz berdi")
    