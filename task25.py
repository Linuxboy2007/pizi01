n = int(input("Введите размер матрицы: "))

matrix = []
print("Введите элементы матрицы:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

min_elem = matrix[0][0]
col = 0

for i in range(1, n):
    if matrix[i][i] < min_elem:
        min_elem = matrix[i][i]
        col = i

print("\nМатрица после удаления столбца:")
for row in matrix:
    for j in range(n):
        if j != col:
            print(row[j], end=" ")
    print()
