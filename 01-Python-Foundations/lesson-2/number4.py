try:
    a, b = map(int, input("2 ta butun son kiriting: ").split())
    print(f"Butun sonni bo'lish natijasi {a / b}\nQoldiq natijasi {a % b}")
except ValueError:
    print("Xatoli yuz berdi")
    