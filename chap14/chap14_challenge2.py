class Square:
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

    def print_size(self):
        print("{} на {}".format(self.side, self.side))

    def __repr__(self, ):
        return "{} на {} на {} на {}".format(self.side,self.side,self.side,self.side)


sq1 = Square(10)
sq2 = Square(20)
sq3 = Square(100)

print(sq1)
print(sq2)
print(sq3)
