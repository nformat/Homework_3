print("Выводим числа от 0 до 10:")
i = 0
while i <= 10:
    print(i)
    i += 1

print("Выводим числа от 20 до 1 в одну строку:")
i = 20
while i > 0:
    print(i, end=" ")
    i -= 1


a = input("\n\nТретья задачка\nВведите целое число:\n")
b = 0
while True:
    try:
        a = int(a)
    except ValueError:
        print("Введено не целое число!!!")
        break
    if a % 2 == 0:
        print("Сейчас мы делим:", a)
        a = a / 2
        b += 1
    else:
        print(a, " - Нечетное число, останавливаемся!\nИтераций деления:", b)
        break

