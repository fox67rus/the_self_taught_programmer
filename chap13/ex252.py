class Shape:
    def __init__(self, w, leng):
        self.width = w
        self.length = leng

    def print_size(self):
        print("{} на {}".format(self.width, self.length))


my_shape = Shape(20, 25)
my_shape.print_size()
