try:
    number = int(input("Butun son kiriting: "))
    if number % 2 == 0 and number > 0:
        print("Bu son juft son")
    else:
        print("Bu son toq son")
except ValueError:
    print("Xatolik yuz bor")