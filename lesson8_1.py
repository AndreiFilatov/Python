import datetime


class Date:

    def __init__(self, str_date=''):
        try:
            self.date = datetime.datetime.strptime(str_date, '%d-%m-%Y')
        except ValueError:
            self.date = None

    @classmethod
    def to_date(cls, str_date=''):
        d = str_date[:2]
        m = str_date[3:5]
        y = str_date[6:10]
        return cls(d + '-' + m + '-' + y) if cls.valid(d, m, y) else cls('')

    @staticmethod
    def valid(d, m, y):
        try:
            d, m, y = int(d), int(m), int(y)
            if 1000 <= y <= 9999:
                if m in [1, 3, 5, 7, 8, 10, 12] and 1 <= d <= 31:
                    return True
                elif m in [4, 6, 9, 11] and 1 <= d <= 30:
                    return True
                elif m == 2 and (y % 4 != 0 and d == 28 or y % 4 == 0 and d == 29):
                    return True
        except ValueError:
            return False


# Пример 1
d = Date('05-01-2021')
print(f'1) {d.date}')

# Пример 2
d = Date('aaaa')
print(f'2) {d.date}')

# Пример 3
d = Date('05-35-2021')
print(f'3) {d.date}')

# Пример 4
d = Date.to_date('05-01-2021')
print(f'4) {d.date}')

# Пример 5
d = Date.to_date('aaaa')
print(f'5) {d.date}')

# Пример 6
d = Date.to_date('05-35-2021')
print(f'6) {d.date}')

# Пример 7
d = d.to_date('29-02-2024') # с "Date" на "d" заменил специально
print(f'6) {d.date}')