list = [7, 5, 3, 3, 2]
while True:
    n = input('Введите число: ')
    if n == 'СТОП':
        break
    try:
        n = int(n)
    except ValueError:
        print('Введите целочисленное значение !')
    else:
        list.append(n)
        list.sort(reverse=True)
        print(list)