"""
Создать (программно) текстовый файл, записать в него программно
набор чисел, разделенных пробелами. Программа должна подсчитывать
сумму чисел в файле и выводить ее на экран.
"""

import random

# Генерация случайной последовательности чисел
n = random.randint(0,100)
seq = ' '.join(str(random.randint(0,n)) for i in range(n))

# Запись в файл случайной последовательности чисел
with open('lesson5_5.txt', 'w', encoding='utf-8') as file:
    file.write(seq)

with open('lesson5_5.txt', 'r', encoding='utf-8') as file:
    print(f'Сумма чисел в файле: {sum(float(x) for x in file.readline().split())}')
