try:
    number = float(input("Float son kiriting: " ))
    print(f"Yaxlitlangan son {round(number, 2)}")
except ValueError:
    print("Xatolik yuz berdi")