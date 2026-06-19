def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

nod = gcd(a, b)
nok = a * b // nod

print("НОД:", nod)
print("НОК:", nok)