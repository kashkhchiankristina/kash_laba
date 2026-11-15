valid_length = False
while not valid_length:
    try:
        n = int(input("Введите длину массива: "))
        if n <= 0:
            print("Ошибка: длина массива должна быть положительным числом.")
        else:
            valid_length = True
    except ValueError:
        print("Ошибка: введите целое число. Буквы и другие символы не допускаются.")

a = []
for i in range(n):
    valid_element = False
    while not valid_element:
        try:
            x = float(input(f"Введите {i}-й элемент: "))
            a.append(x)
            valid_element = True
        except ValueError:
            print("Ошибка: введите число. Буквы и другие символы не допускаются.")

print("Исходный массив:", a)
s = sum(a) / n

for i in range(n):
    if a[i] == 0:
        a[i] = s

print("Полученный массив:", a)
