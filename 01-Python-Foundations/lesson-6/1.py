def check(div):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return div(a, b)

    return wrapper


@check
def div(a, b):
    return a // b


try:
    a = int(input("a = "))
    b = int(input("b = "))
    print(div(a, b))
except ValueError as e:
    print(f"Error {e}")
