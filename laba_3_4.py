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
            x = int(input(f"Введите {i} элемент: "))
            a.append(x)
            break
        except ValueError:
            print("Ошибка: введите целое число. Буквы и другие символы не допускаются.")

print("Исходный массив:", a)
m = max(a)
print("Максимальный элемент:", m)
print("Массив в обратном порядке:", a[::-1])