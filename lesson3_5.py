def new_sum(lst, stop):
    global summa
    for el in lst:
        if el == stop: return stop
        try:
            a = float(el)
        except:
            a = 0
        finally:
            summa += a

stop = input('Введите специальный символ: ')
summa = 0
while True:
    lst = [x.strip() for x in input('\tВведите числа через пробел: ').split()]
    res = new_sum(lst, stop)
    print(f'Сумма равна: {summa}')
    if res == stop:
        break
