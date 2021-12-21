a = float(input('Введите результат 1-го дня: '))
b = float(input('Введите обший результат: '))

day = 1
res = a
while True:
    day += 1
    res *= 1.1
    if res >= b:
        break

if b <= a:
    print(f'Номер дня: 1')
else:
    print(f'Номер дня: {day}')