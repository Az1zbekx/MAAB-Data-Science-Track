try:
    number = int(input("Butun son kiriting: "))
    print(f"Shu sonning oxirgi raqami {number % 10}")
except ValueError:
    print("Xatolik yuz berdi")
    