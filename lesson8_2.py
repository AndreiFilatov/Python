class MyError(Exception):

    def __init__(self, message):
        self.message = message


try:
    flag = 'num' # флаг нужен, чтобы при обработке ошибки ValueError понимать,
                 # на какой строчке сломалась программа
    numerator = float(input('Введите делимое: '))
    flag = 'div'
    divisor = float(input('Введите делитель: '))
    if divisor == 0:
        raise MyError('На нолик лучше не делить !')
except ValueError:
    if flag == 'num':
        print('Делимое не является числом !')
    else:
        print('Делитель не является числом !')
except MyError as err:
    print(err)
else:
    print(f'Ответ: {numerator} / {divisor} = {numerator/divisor}')