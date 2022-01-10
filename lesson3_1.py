def divide(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = 'деление на 0 !'
    return res

try:
    div = float(input('Ввеедите делимое: '))
except ValueError:
    print('Введите корректное делимое !')
else:
    try:
        sep = float(input('Ввеедите делитель: '))
    except ValueError:
        print('Введите корректный делитель !')
    else:
        print(f'Результат: {divide(div, sep)}')
