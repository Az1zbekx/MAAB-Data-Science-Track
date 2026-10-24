try:
    a, b, c = map(int, input("3 ta butun son kiritng: ").split())
    print(f"Eng katta son {max(a, b, c)}\nEng kichik son {min(a, b, c)}")
except ValueError:
    print("Xatolik yuz berdi")