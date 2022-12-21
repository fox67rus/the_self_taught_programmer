class Square:
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

    def print_size(self):
        print("{} на {}".format(self.side, self.side))


def compare_object(obj1, obj2):
    if obj1 is obj2:
        return True
    else:
        return False


sq1 = Square(5)
sq2 = sq1
sq3 = Square(10)

print(compare_object(sq1, sq2))
print(compare_object(sq1, sq3))
