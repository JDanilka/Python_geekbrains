class Material:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def sq_c(self):
        return f'{(self.V / 6.5 + 0.5):.2f}'

    def sq_s(self):
        return f'{(self.H * 2 + 0.3):.2f}'

    @property
    def sq_gen(self):
        return str(f'Всего нужно {((self.V / 6.5 + 0.5) + (self.H * 2 + 0.3)):.2f} м. ткани')


class Coat(Material):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.sq_coat = round(self.V / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани для пальто {self.sq_coat}м'


class Suit(Material):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.sq_suit = round(self.H * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани для костюма {self.sq_suit}м '


my_coat = Coat(2, 1.6)
my_suit = Suit(2, 1.6)
print(my_coat)
print(my_suit)
print(my_coat.sq_c())
print(my_suit.sq_s())
print(my_suit.sq_gen)
