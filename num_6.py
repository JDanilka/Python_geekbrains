a = int(input('Введите число километров, которые Вам удалось пробежать в 1 день тренировок\n'))
b = int(input('А сколько километров Вам хотелось бы пробегать за одну тренировку?\n'))
d = 1
a_1 = a
while a_1 < b:
    d += 1
    a = a * 1.1
    a_1 = a
print(f"Вы сможете достигнуть желаемого результата на  %.d день" % d)
