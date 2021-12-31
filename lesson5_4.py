"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться
на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}

with open('lesson5_4_from.txt', 'r', encoding='utf-8') as file_from, \
        open('lesson5_4_to.txt', 'w', encoding='utf-8') as file_to:
    str_from = file_from.readline()
    while str_from:
        file_to.write(str_from.replace(
            str_from.split()[0], dict[str_from.split()[0]]
        ))
        str_from = file_from.readline()
