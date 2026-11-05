while True:
    try:
        p = float(input('Введите цену 1 кг конфет: '))
        if p < 0:
            print('Цена не может быть отрицательной. Попробуйте ещё раз.')
            continue
        break
    except ValueError:
        print('Ошибка: введите корректное число.')

for k in range(1, 11):
    c = k * p
    print(f'{k} кг = {c:.2f} руб')

print()

print('Введите целые числа в столбик, оканчивающийся на 0:')
s = 0
n = 0

while True:
    try:
        i = input()
        x = int(i)
        if x == 0:
            break
        s += x
        n += 1
    except ValueError:
        print('Ошибка: введите целое число. Буквы и другие символы не допускаются.')

print(f'Сумма чисел: {s}')
print(f'Количество чисел: {n}')
