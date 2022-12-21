class Shape:
    def __init__(self, w, leng):
        self.width = w
        self.length = leng

    def print_size(self):
        print("{} на {}".format(self.width, self.length))


class Square(Shape):
    def area(self):
        return self.width * self.length


my_square = Square(20, 25)
print(my_square.area())
