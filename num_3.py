n = int(input('Введи любое число n= '))
a = int(str(n) + str(n))
b = int(str(n) + str(n)+ str(n))
result = n + a + b
ans_str = 'Вот, что получим {0} + {1} + {2} = {3}'.format(n,a,b,result)
print(ans_str)
