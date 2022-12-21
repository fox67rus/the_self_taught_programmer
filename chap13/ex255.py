class Shape:
    def __init__(self, w, leng):
        self.width = w
        self.length = leng

    def print_size(self):
        print("{} на {}".format(self.width, self.length))


class Square(Shape):
    def area(self):
        return self.width * self.length
    def print_size(self):
        print("Я {} на {}".format(self.width, self.length))


my_square = Square(20, 25)
my_square.print_size()
