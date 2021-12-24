def int_func(text):
    res = text[0].upper()
    for i in range(1, len(text)):
        res += text[i].lower()
    return res

print('Результат: ' + ' '.join(
    list(
        map(int_func, [x.strip() for x in input("Введите строку из слов, разделенных пробелом: ").split()])
        )
    )
)