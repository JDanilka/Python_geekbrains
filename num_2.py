with open("text_2.txt", encoding='UTF-8') as file:
    lines = 1
    symbols = 0
    for i in file:
        lines += i.count("\n")
        symbols = len(i)-1
        print(f'В строке {symbols} симв.')
    print(f'Кол-во строк - {lines}')
