n = int(input("Введите размер квадратной матрицы: "))

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"Введите элемент [{i}][{j}]: ")))
    matrix.append(row)

print("Матрица:")
for row in matrix:
    print(row)

print("Максимальные элементы строк:")
for row in matrix:
    print(max(row))

print("Минимальные элементы столбцов:")
for j in range(n):
    column = []
    for i in range(n):
        column.append(matrix[i][j])
    print(min(column))