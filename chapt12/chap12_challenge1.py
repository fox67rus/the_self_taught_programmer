class Apple():
    def __init__(self, c, w, t):
        self.color = c
        self.weight = w
        self.fresh = 0
        self.taste = t
        print("Создано!")


apple = Apple("зеленый", 150, "сладкое")
print(apple.color)