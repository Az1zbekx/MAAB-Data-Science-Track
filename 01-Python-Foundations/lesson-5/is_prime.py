def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

try:
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Error")
    else:
        print(is_prime(n))

except ValueError:
    print("Error")