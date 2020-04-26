#Создать программно файл в текстовом формате, 
#записать в него построчно данные, вводимые пользователем. 
#Об окончании ввода данных свидетельствует пустая строка.
# my_text = input('Введите данные через пробел - ').split()
#
# with open('text_1.txt', 'w', encoding='UTF-8') as file:
#     for i in my_text:
#         file.write(i + '\n')
my_text = []
while True:
    line_1 = input('Введите данные - ')
    if line_1 == '':
        print(my_text)
        exit()
    else:
        line_2 = line_1
        my_text.append(line_2)
    with open('text_1.txt', 'w', encoding='UTF-8') as file:
        for i in my_text:
            file.write(i + '\n')
