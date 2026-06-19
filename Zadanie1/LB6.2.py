arr = [int(input(f"Введите {i + 1}-й элемент: ")) for i in range(10)]

s = 0

for x in arr:
    if x > 5:
        s += x

print("Массив:", arr)
print("Сумма чисел больше 5:", s)