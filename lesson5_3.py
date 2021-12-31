"""
Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников
имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('lesson5_3.txt', 'r', encoding='utf-8') as file:
    employee = []
    count = 0
    sum = 0
    line_str = file.readline()
    while line_str:
        line_list = line_str.split()
        # Проверка на то, что строка имеют структуру, похожую на "Фамилия" + пробел + "Сумма"
        if len(line_list) >= 2 and line_list[0].isalpha() and line_list[1].isdecimal():
            if float(line_list[1]) < 20000: employee.append(line_list[0])
            count += 1
            sum += float(line_list[1])
        line_str = file.readline()
    print(f'Средняя величина дохода сотрудников: {sum / count}')
    print(f'Сотрудники с окладом менее 20 тыс.:')
    for i in range(0, len(employee)):
        print(f'\t{i+1}. {employee[i]}')