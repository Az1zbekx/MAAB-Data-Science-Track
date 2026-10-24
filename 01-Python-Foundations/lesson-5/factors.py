try:
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Error")
    else:
        for i in range(1, n + 1):
            if n % i == 0:
                print(f"{i} is a factor for {n}")
except ValueError:
    print("Error")