translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
with open('test_3.txt', 'r', encoding='UTF-8') as file:
    a = file.read().split('\n')
    for i in a:
        i = i.split(' ', 1)
        my_list.append(translate[i[0]] + i[1])
    print(my_list)
with open('test_3.1.txt', 'w', encoding='UTF-8') as file1:
    for itm in my_list:
        print(itm + '\n')
