class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6

    def area(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6


my_hexagon = Hexagon(3, 4, 5, 3, 4, 5)
print(my_hexagon.area())
