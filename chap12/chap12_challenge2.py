import math


class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2


my_circle = Circle(10)
print(my_circle.area())
