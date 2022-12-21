class Orange:
    def __init__(self, w, c):
        """ вес в граммах """
        self.weight = w
        self.color = c
        self.mold = 0
        print("Создано!")

    def rot(self, days, temp):
        self.mold = days * temp


orange = Orange(60, "темный")
print(orange.mold)
orange.rot(10, 33)
print(orange.mold)
