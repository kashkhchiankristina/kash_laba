while True:
    try:
        n = int(input("Введите длину массива: "))
        if n <= 0:
            print("Ошибка: длина массива должна быть положительным числом.")
            continue
        break
    except ValueError:
        print("Ошибка: введите целое число. Буквы и другие символы не допускаются.")

a = []
for i in range(n):
    while True:
        try:
            x = float(input(f"Введите {i} элемент: "))
            a.append(x)
            break
        except ValueError:
            print("Ошибка: введите число. Буквы и другие символы не допускаются.")

print("Исходный массив:", a)
s = sum(a) / n
for i in range(n):
    if a[i] == 0:
        a[i] = s
print("Полученный массив:", a)