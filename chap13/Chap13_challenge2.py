class Rectangle:
    def __init__(self, w, leng):
        self.width = w
        self.length = leng

    def calculate_perimeter(self):
        return (self.width + self.length) * 2


class Square:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 4 * self.side

    def change_size(self, cs):
        return self.side + cs


my_rectangle = Rectangle(4, 5)
my_square = Square(5)

print(my_square.change_size(-1))
