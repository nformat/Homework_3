print("Проверяем является ли введный символ числом. Возвращает число.")
def cdig():
    """
    Проверяет является ли введный символ числом. Возвращает число.
    """

    while True:
        a = input("Введите число:\n")
        try:
            a = float(a)
            return a
        except ValueError:
            pass


print(cdig())

def cstr():
    """
    Проеряет есть ли пробел внутри слова. Пробелы вначале и в конце игнорируются. Возвращает строку.
    """
    while True:
        a = input("Введите слово без пробелов в середине:\n")
        if " " not in a.strip() and a != "":
            return a


print("Строка:\n\"", cstr(), "\"")

print("Определяем высокосный ли год")
def is_year_leap(y):
    """
    Возвращающет True, если год високосный, и False иначе.

    """
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False


print(is_year_leap(2000))

print("\nОпределяем существует ли треугольник, стороны которго равны введеным числам.")
def tre(a,b,c):
    """
    Определяет существует ли треуголник с такими сторонами. Возвращает True или False
    """

    l = [a, b, c]
    l.sort()
    if l[2]<l[0]+l[1]:
        return True
    else:
        return False


a = int(input("Введите первое число:\n"))
b = int(input("Введите второе число:\n"))
c = int(input("Введите третье число:\n"))
print(tre(a, b, c))

print("\nОпределяем тип треугольника, стороны которго равны введеным числам.")
def tretype(a, b, c):
    """
    Определяет существует ли треуголник с такими сторонами. Возвращает True или False
    """

    l = [a, b, c]
    l.sort()
    if l[2] < l[0] + l[1]:
        if  l[2] == l[0] == l[1]:
            t = "равносторний"
        elif l[0] == l[1]:
            t = "равнобедренный"
        else:
            t = "разностороний"
    else:
        t = "несуществует"
    return t

a = int(input("Введите первое число:\n"))
b = int(input("Введите второе число:\n"))
c = int(input("Введите третье число:\n"))
print("Труголник", tretype(a, b, c))

def distance(x1, y1, x2, y2):
    """
    Вычисляющет расстояние между точками (x1y1) и (x2y2) и возвращает его
    """
    d = (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    return d


print("Расстояние между точками(x1, y1) и (x2, y2):\n", distance(0, 0, 1, 1))
