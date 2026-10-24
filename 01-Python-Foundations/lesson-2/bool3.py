try:
    number = int(input("Butun son kiriting: "))
    print(bool(number > 0 and number % 2 == 0))
except ValueError:
    print("Xatolik yuz berdi")