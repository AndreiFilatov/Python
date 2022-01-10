def check(a):
    if a is None:
        return '?'
    elif len(a.replace(' ','')) == 0:
        return '?'
    else:
        return a

def func(name, surname, year, city, email, phone):
    print('Пользователь: ' + ' '.join(list(map(check, [name, surname, year, city, email, phone]))))

n = input('Введите имя: ')
s = input('Введите фамилию: ')
y = input('Введите год рождения: ')
c = input('Введите город проживания: ')
e = input('Введите email: ')
p = input('Введите телефон: ')

func(name=n, surname=s, year=y, city=c, email=e, phone=p)
