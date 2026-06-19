import math


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
d = float(input("Введите сторону d: "))
diagonal = float(input("Введите диагональ: "))

s1 = triangle_area(a, b, diagonal)
s2 = triangle_area(c, d, diagonal)

area = s1 + s2

print("Площадь четырехугольника:", round(area, 2))