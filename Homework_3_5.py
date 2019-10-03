a = input("Введите первое значение:\n")
b = input("Введите второе значение:\n")

try:
    a, b = float(a), float(b)
except ValueError:
    pass
print("Сумма значений:\n", a + b)
