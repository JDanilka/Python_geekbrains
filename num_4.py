class Cars:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return ('Машина поехала.')

    def stop(self):
        return ('Машина остановилась.')

    def turn(self, direction):
        return ('Машина повернула на' + direction)

    def show_speed(self):
        return (f'Скорость авомобиля {self.speed} км/ч.')


class TownCar(Cars):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            return ('Скорость превышена.')
        else:
            return (f'Скорость авомобиля {self.speed} км/ч.')


class SportCar(Cars):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class WorkCar(Cars):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            return ('Скорость превышена.')
        else:
            return (f'Скорость авомобиля {self.speed} км/ч.')

class PoliceCar(Cars):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


my_car = TownCar('Opel', 'White', 60, False)
print(my_car.name, my_car.color, my_car.speed, my_car.is_police)
print(my_car.go(), my_car.show_speed(), my_car.turn('лево.'), my_car.stop())

my_sportcar = SportCar('Porshe', 'Red', 130, False)
print(my_sportcar.name, my_sportcar.color, my_sportcar.speed, my_sportcar.is_police)
print(my_sportcar.go(), my_sportcar.show_speed(), my_sportcar.turn('право.'), my_sportcar.stop())

my_workcar = WorkCar('Volkswagen', 'Black', 50, False)
print(my_workcar.name, my_workcar.color, my_workcar.speed, my_workcar.is_police)
print(my_workcar.go(), my_workcar.show_speed(), my_workcar.turn(' работу.'), my_workcar.stop())

my_police = PoliceCar('Jeep', 'Multicolor', 75)
print(my_police.name, my_police.color, my_police.speed)
print(my_police.go(), my_police.show_speed(), my_police.turn('лево.'), my_police.stop())
