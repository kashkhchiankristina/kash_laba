import math

print('Расчет скорости резания при токарной обработке.')

def num(text, mini, maxi):
    while True:
        try:
            x = float(input(text))
            if mini <= x <= maxi:
                return x
            print('ошибка: введите число от', mini, 'до', maxi)
        except ValueError:
            print('введите число')

def diam(d):
    if d < 10:
        return 'малый диаметр'
    elif d <= 100:
        return 'нормальный диаметр'
    else:
        return 'крупный диаметр'

print('1 - черновая (k = 1.0)')
print('2 - получерновая (k = 0.85)')
print('3 - чистовая (k = 0.7)')

obr = False
while not obr:
    c = input('выбери режим 1-3: ')
    match c:
        case '1': mode, k, obr = 'черновая', 1.0, True
        case '2': mode, k, obr = 'получерновая', 0.85, True
        case '3': mode, k, obr = 'чистовая', 0.7, True
        case _: print('введите число 1, 2 или 3')

D = num('введите диаметр от 1 до 500 мм: ', 1, 500)
n = num('введите частоту вращения от 50 до 3000 об/мин: ', 50, 3000)

v = math.pi * D * n / 1000
v_adj = v * k

print('режим:', mode)
print('скорость v:', round(v, 2), 'м/мин')
print('скорость v_adj:', round(v_adj, 2), 'м/мин')
print('класс диаметра:', diam(D))