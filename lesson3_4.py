def new_pow(x, y):
    res = 1 / x
    for i in range(2, abs(y)+1):
        res /= x
    return res

try:
    x = int(input('Введите x (x > 0): '))
    if x <= 0:
        print('Число x должно быть целым положительным !')
    else:
        y = int(input('Введите y (y < 0): '))
        if y >= 0: print('Число y должно быть целым отрицательным !')
except ValueError:
    print('Введено некорректное число !')
else:
    if x > 0 and y < 0:
        print(f'Результат: {new_pow(x, y)}')
        print(f'Проверка:  {x**y}')
