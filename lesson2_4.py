str = input('Введите строку: ')
list = str.split()
for i in range(0, len(list)):
    print(f'{i+1}. {list[i][0:10]}')