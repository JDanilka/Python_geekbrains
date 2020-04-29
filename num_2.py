class Road:
    __length = None
    __width = None
    weigth = None
    depth = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculation(self):
        self.weigth = 25
        self.depth = 4
        result = self.length * self.width * self.weigth * self.depth / 1000
        print(f'Для покрытия всего дорожного полотна необходимо {result} т. асфальта')


road_1 = Road(100, 5)
road_1.calculation()
