class Stationery:
    title = "Канцелярские принадлежности"

    def draw(self):
        print('Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print('Карандашом рисуй в альбоме')


class Pen(Stationery):
    def draw(self):
        print('Ручкой пиши в тетради')


class Handle(Stationery):
    def draw(self):
        print('Для рисования маркером нужна специальная бумага')


stat = Stationery()
print(stat.title)
stat.draw()
pencil_1 = Pencil()
pencil_1.draw()
pen_1 = Pen()
pen_1.draw()
handle_1 = Handle()
handle_1.draw()
