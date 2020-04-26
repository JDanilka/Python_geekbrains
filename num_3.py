with open('text_3.txt', 'r', encoding='UTF-8') as file:
    a = []
    b = []
    list_1 = file.read().split('\n')
    for i in list_1:
        i = i.split()
        if int(i[1]) < 20000:
            a.append(i[0])
        b.append(i[1])
    print(f'Сотрудники с окладом менее 20 тыс. руб {a}')
    print(f'Средний оклад по компании = {sum(map(int, b))/len(b)}')
