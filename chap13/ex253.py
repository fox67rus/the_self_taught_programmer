class Shape:
    def __init__(self, w, leng):
        self.width = w
        self.length = leng

    def print_size(self):
        print("{} на {}".format(self.width, self.length))


class Square(Shape):
    pass


my_square = Square(20, 25)
my_square.print_size()
