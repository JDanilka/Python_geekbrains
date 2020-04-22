from functools import reduce

def my_func(x, y):
    return x * y


a = [el for el in range(100, 1001) if el & 1]
print(reduce(my_func, a))
