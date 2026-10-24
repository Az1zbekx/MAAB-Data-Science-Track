try:
    number = int(input("Butun son kiriting: "))
    print(bool(number >= 10 and number <= 20))
except ValueError:
    print("Xatoli yuz berdi")
    