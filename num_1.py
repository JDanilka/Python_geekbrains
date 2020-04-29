from time import sleep
from itertools import cycle


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for i in cycle(TrafficLight.__color):
            i = 0
            while i < 3:
                print(TrafficLight.__color[i])
                if i == 0:
                    sleep(7)
                elif i == 1:
                    sleep(2)
                elif i == 2:
                    sleep(7)
                i += 1


a = TrafficLight()
print(f'Цвета светофора {a._TrafficLight__color}')
a.running()
