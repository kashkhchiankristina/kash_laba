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


