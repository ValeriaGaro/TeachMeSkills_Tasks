# создать класс
# сделать класс наследник
# переопределить метод родителя
# перегрузить метод init


class Telephone:
    def __init__(self, brand: str, model: str, colour: str):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.active = False
        self.lightning = 0

    def add_lightning(self, lightning):
        return lightning + 2


class Tablet(Telephone):
    def __init__(self, size: float, **kwargs):
        self.size = size
        self.FaceID = True
        super().__init__(**kwargs)

    def add_lightning(self, lightning):
        return lightning + 3


samsung = Tablet(
    brand="samsung",
    model="A324",
    colour="white",
    size=10.2
)


print(samsung.brand)
print(samsung.model)
print(samsung.colour)
print(samsung.size)








