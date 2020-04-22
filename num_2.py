a = [2, 5, 1, 14, 3, 4, 9, 3]
b = [el for num, el in enumerate(a) if a[num - 1] < a[num]]
print(f'Исходный список {a}')
print(f'Новый список {b}')
