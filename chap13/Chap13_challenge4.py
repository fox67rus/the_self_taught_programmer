class Horse:
    def __init__(self,
                 name,
                 rider):
        self.name = name
        self.rider = rider


class Rider:
    def __init__(self, name):
        self.name = name


guk = Rider("Гук")
spirit = Horse("Спирит", guk)
print(spirit.rider.name)
