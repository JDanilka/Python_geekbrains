def my_funk_1(x, y):
    return x ** y


print(f'{my_funk_1(1.1, -2):.3f}')


def my_funk_2(x, y):
    return round(pow(x,y), 3)


print(my_funk_2(2.2, -3))


def my_func_3(a, b):
    my_res = 1
    for i in range(abs(b)):
        my_res *= a
    if b >= 0:
        return my_res
    else:
        return 1 / my_res


print(f'{my_funk_1(1.1, -2):.3f}')
