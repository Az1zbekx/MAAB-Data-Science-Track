try:
    number = int(input("Butun son kiriting: "))
    print(bool(number % 3 == 0 and number % 5 == 0))
except ValueError:
    print("Xatolik yuz berdi")
    