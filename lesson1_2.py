seconds = int(input('Введите время в секундах: '))
h = seconds // 3600
m = (seconds - 3600 * h) // 60
s = seconds - h * 3600 - m * 60
print("%02d:%02d:%02d" % (h, m, s))