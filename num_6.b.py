from itertools import cycle

a = [1, 10, 100, 1000, 'раз', 'два', 'три']
for el in cycle(a):
    print(el)
