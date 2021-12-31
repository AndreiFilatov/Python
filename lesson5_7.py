"""
Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее
в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""

import json

with open('lesson5_7.txt', 'r', encoding='utf-8') as file:
    dict = {}
    line_str = file.readline()
    sum = 0
    count = 0
    while line_str:
        line_list = line_str.split()
        key = line_list[0]
        income = float('0' + ''.join(x for x in line_list[2] if x.isdecimal()))
        cost = float('0' + ''.join(x for x in line_list[3] if x.isdecimal()))
        profit = income - cost
        dict[key] = profit
        if profit >= 0:
            sum += profit
            count += 1
        line_str = file.readline()

lst = [dict, {'average_profit' : sum / count}]
print('Итоговый список:')
print('--->',lst)

with open('lesson5_7.json', 'w', encoding='utf-8') as file:
    json.dump(lst, file)