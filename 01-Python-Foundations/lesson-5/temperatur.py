def convert_far_to_cel(F):
    C = (F - 32) * 5 / 9
    return C

def convert_cel_to_far(C):
    F = C * 9 / 5 + 32
    return F

try:
    F = float(input("Enter a temperature in degrees F: "))
    C = convert_far_to_cel(F)
    print(f"{F:.0f} degrees F = {C:.2f} degrees C")

    C = float(input("Enter a temperature in degrees C: "))
    F = convert_cel_to_far(C)
    print(f"{C:.0f} degrees C = {F:.2f} degrees F")
except ValueError:
    print("Error")