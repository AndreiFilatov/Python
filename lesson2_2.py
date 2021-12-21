list = input('Введите элементы списка через запятую: ').split(',')

for i in range(0, int(len(list) / 2)):
    temp = list[2 * i].strip()
    list[2 * i] = list[2 * i + 1].strip()
    list[2 * i + 1] = temp

print(list)