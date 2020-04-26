dict = {}
with open('text_6.txt', 'r', encoding="UTF-8") as file:
    for i in file:
        a, b, c, d = i.split()
        dict[a] = int(b) + int(c) + int(d)
print(f'Кол-во занятий по предметам {dict}')
