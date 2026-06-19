arr = [int(input(f"Введите {i + 1}-й элемент: ")) for i in range(10)]

max_el = max(arr)

less_count = 0
greater_count = 0

for x in arr:
    if x < max_el:
        less_count += 1
    elif x > max_el:
        greater_count += 1

print("Массив:", arr)
print("Максимальный элемент:", max_el)
print("Количество элементов меньше максимального:", less_count)
print("Количество элементов больше максимального:", greater_count)