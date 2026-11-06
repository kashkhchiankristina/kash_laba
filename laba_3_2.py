print('Введите целые числа в столбик, оканчивающийся на 0:')
s = 0
n = 0
f = False

while not f:
    try:
        i = input()
        x = int(i)
        if x == 0:
            f = True
        else:
            s += x
            n += 1
    except ValueError:
        print('Ошибка: введите целое число. Буквы и другие символы не допускаются.')

print(f'Сумма чисел: {s}')
print(f'Количество чисел: {n}')
