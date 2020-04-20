def my_sum():
    sum_res = 0
    el = False
    while el == False:
        num = input('Введите числа через пробел или #, чтобы закончить ввод - ').split()

        res = 0
        for i in range(len(num)):
            if num[i] == '#':
                el = True
                break
            else:
                res = res + int(num[i])
        sum_res = sum_res + res
        print(f'Сумма чисел - {sum_res}')
    print(f'Конечная сумма - {sum_res}')


my_sum()
