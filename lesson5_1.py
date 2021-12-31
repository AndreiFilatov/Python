"""
Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует
пустая строка.
"""

with open('lesson5_1.txt', 'w', encoding='utf-8') as file:
    while True:
        user_str = input('Введите данные: ')
        if not user_str:
            print('Запись завершена !')
            break
        else:
            file.write(user_str + '\n')
