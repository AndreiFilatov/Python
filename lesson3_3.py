def my_func(a1, a2, a3):
    return sum(sorted([a1, a2, a3], reverse=True)[0:2])

try:
    x1 = float(input('Введите 1-ое число: '))
    x2 = float(input('Введите 2-ое число: '))
    x3 = float(input('Введите 3-ье число: '))
except ValueError:
    print('Введено некорректное число !')
else:
    print(f'Результат: {my_func(x1, x2, x3)}')
