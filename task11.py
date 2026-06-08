import random

str = int(input("Введите количество строк: "))
stb = int(input("Введите количество столбцов: "))

matrix = []
for i in range(str):
    row = []
    for j in range(stb):
        row.append(random.randint(-10, 10))
    matrix.append(row)

print("\nСгенерированная матрица:")
for row in matrix:
    print(*row)

sums = [sum(row) for row in matrix]

min_row = sums.index(min(sums))
max_row = sums.index(max(sums))

print("\nСтрока с минимальной суммой:")
print(*matrix[min_row])
print("Сумма =", sums[min_row])

print("\nСтрока с максимальной суммой:")
print(*matrix[max_row])
print("Сумма =", sums[max_row])
