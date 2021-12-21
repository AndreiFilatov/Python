print('\nДобро пожаловать!'
      '\n----> Добавить новый товар: 1' + \
      '\n----> Собрать аналитику: 2'
      '\n----> Выйти из системы: 0')

products = []
while True:
    flag = input('\nВведите 1, 2 или 0: ')

    if flag not in ['0', '1', '2']:
        print('Сделайте выбор еще раз !')
    elif flag == '0':
        break
    elif flag == '1':
        name = input('\tНазвание: ')

        while True:
            try:
                price = int(input('\tЦена: '))
            except ValueError:
                print('Введите корректную цену товара !')
            else:
                break

        while True:
            try:
                count = int(input('\tКоличество: '))
            except ValueError:
                print('Введите корректное количество товара !')
            else:
                break

        unit = input('\tЕдиницы: ')

        dict = {'название' : name, 'цена' : price, 'количество' : count, 'ед.' : unit}
        tuple = (len(products)+1, dict)
        products.append(tuple)
        print('Товар добавлен !')
    else:
        name, price, count, unit = [], [], [], []
        for product in products:
            name.append(product[1].get('название'))
            price.append(product[1].get('цена'))
            count.append(product[1].get('количество'))
            unit.append(product[1].get('ед.'))
        dict = {'название' : name, 'цена' : price, 'количество' : count, 'ед.' : unit}
        for key, value in dict.items():
            print(f'\t{key} : {value}')