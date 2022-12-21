import math


class Triangle:
    def __init__(self, a, b, c):
        self.side1 = a
        self.side2 = b
        self.side3 = c

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))


my_triangle = Triangle(3, 4, 5)
print(my_triangle.area())

my_triangle2 = Triangle(5, 6, 7)
print(my_triangle2.area())
