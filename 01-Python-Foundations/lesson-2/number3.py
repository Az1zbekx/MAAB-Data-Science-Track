try:
    k = int(input("Kilometrni butun sonda kiriting: "))
    print(f"{k} kilometr\n{k * 1000} metr\n{k * 100000} santimetr")
except ValueError:
    print("Xatolik yuz berdi")