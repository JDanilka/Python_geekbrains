from sys import argv

name, time, salary = argv
try:
    time = int(time)
    salary = int(salary)
    result = time * salary * 1.2
    print(f'Количество отработанных часов - {time}')
    print(f'Оплата труда за 1 час - {salary}')
    print(f'Заработная плата сотрудника с учетом премии 20%  {result}')
except ValueError:
    print('Введите число')
