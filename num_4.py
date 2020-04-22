a = [1, 1, 2, 3, 4, 3, 4, 5, 7, 7, 5, 10]
b = [el for el in a if a.count(el) == 1]
print(b)
