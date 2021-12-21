income = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))
profit = income - costs
if profit > 0:
    print(f'Финансовый результат: прибыль в размере {profit:.2f}')
    print(f'\t Рентабельность составляет: {profit / income:.1%}')
    n = int(input('\t Введите число сотрудников фирмы: '))
    print(f'\t Прибыль фирмы в расчете на одного сотрудника составляет {profit / n:.2f}')
else:
    print(f'Финансовый результат: убыток в размере {abs(profit):.2f}')
