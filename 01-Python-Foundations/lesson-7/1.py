import math


class Vector:
    def __init__(self, *arr):
        self.arr = arr

    def __str__(self):
        return f"Vector{self.arr}"

    def __add__(self, other):
        if len(self.arr) != len(other.arr):
            raise ValueError("Vector dimensions must be the same")
        return Vector(*(a + b for a, b in zip(self.arr, other.arr)))

    def __sub__(self, other):
        if len(self.arr) != len(other.arr):
            raise ValueError("Vector dimensions must be the same")
        return Vector(*(a - b for a, b in zip(self.arr, other.arr)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.arr) != len(other.arr):
                raise ValueError("Vector dimensions must be the same")
            return sum(a * b for a, b in zip(self.arr, other.arr))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.arr))
        else:
            raise ValueError("Error value")

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(a * a for a in self.arr))

    def normalize(self):
        mg = self.magnitude()
        if mg == 0:
            raise ValueError("It is impossible to have magnitude 0")
        return Vector(*(round((a / mg), 3) for a in self.arr))


v1 = Vector(1, 2, 3, 4)
v2 = Vector(5, 6, 7, 8)
print(v1)
print(v2)
v3 = v1 + v2
print(v3)
v3 = v1 - v2
print(v3)
v3 = v1 * v2
print(v3)
print(v1 * 3)
print(3 * v1)
print(v1.magnitude())
print(v1.normalize())
