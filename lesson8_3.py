class MyError(Exception):

    def __init__(self, message):
        self.message = message


lst = []
step = 1
while True:
    try:
        el = input(f'{step}. Введите число: ')
        if not el.isdecimal():
            raise MyError('\tВведено не число !')
    except MyError as err:
        if el == 'stop':
            print('\tВвод завершен !')
            break
        else:
            print(err)
    else:
        print('\tВведено число.')
        lst.append(int(el))
    step += 1

print(f'Итоговый список: {lst}')