n = int(input("Введите нечетный размер квадратной матрицы: "))

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(float(input(f"Введите элемент [{i}][{j}]: ")))
    matrix.append(row)

center = n // 2

max_i = 0
max_j = 0
max_value = matrix[0][0]

for i in range(n):
    if matrix[i][i] > max_value:
        max_value = matrix[i][i]
        max_i = i
        max_j = i

    if matrix[i][n - 1 - i] > max_value:
        max_value = matrix[i][n - 1 - i]
        max_i = i
        max_j = n - 1 - i

matrix[center][center], matrix[max_i][max_j] = matrix[max_i][max_j], matrix[center][center]

print("Преобразованная матрица:")
for row in matrix:
    print(row)