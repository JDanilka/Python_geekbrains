def func_3(my_list: list) -> int:
    min_1 = min(my_list)
    my_list.remove(min_1)
    return sum(my_list)


x = int(input('Ввведите 1 число - '))
y = int(input('Ввведите 2 число - '))
z = int(input('Ввведите 3 число - '))
my_list = [x, y, z]
print(func_3(my_list))
