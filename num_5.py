with open('text_5.txt', 'w', encoding='UTF-8') as file:
    a = input('Введите набор чисел через пробел - ')
    file.writelines(a)
    b = a.split()
    print(f'Сумма чисел = {sum(map(int, b))}')
