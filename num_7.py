from itertools import count
from math import factorial

def generator():
    for el in count(2, 2):
        yield factorial(el)


a = 0
for itm in generator():
    if a < 15:
        print(itm)
        a += 1
    else:
        break
