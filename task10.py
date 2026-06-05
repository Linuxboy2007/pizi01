# -*- coding: utf-8 -*-
import random

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

# Создаем матрицу
mat = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(-10, 10))
    mat.append(row)

# Выводим исходную
print("\nИсходная матрица:")
for row in mat:
    print(row)

# Заменяем минимумы на 0
for i in range(n):
    минимум = min(mat[i])  # находим минимум в строке
    for j in range(m):
        if mat[i][j] == минимум:
            mat[i][j] = 0  # заменяем на 0

# Выводим результат
print("\nРезультат (минимумы обнулены):")
for row in mat:
    print(row)