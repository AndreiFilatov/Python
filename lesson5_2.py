"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('lesson5_2.txt', 'r', encoding='utf-8') as file:
    print('Число слов')
    lines = 0
    line_str = file.readline()
    while line_str:
        lines += 1
        for spec_char in [',', '.', '!', '?', '/']:
            line_str = line_str.replace(spec_char, '')
        line_list = [x for x in line_str.split() if x.isalpha()]
        print(f'---> в {lines}-й строке: {len(line_list)}')
        line_str = file.readline()
    if lines == 1:
        print(f'В файле {lines} строка.')
    elif lines in [2, 3, 4]:
        print(f'В файле {lines} строки.')
    else:
        print(f'В файле {lines} строк.')