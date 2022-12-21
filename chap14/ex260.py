class Rectangle:
    rect = []

    def __init__(self, w, leng):
        self.width = w
        self.length = leng
        self.rect.append((self.width, self.length))

    def print_size(self):
        print("{} на {}".format(self.width, self.length))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.rect)
