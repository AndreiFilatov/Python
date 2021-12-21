str = input('Введите число: ')
n = str[0]
i = 1
while i < len(str):
    if str[i] > n:
        n = str[i]
    i += 1
print(n)