# -*- coding: utf-8 -*-
"""
Семизов С.А. ПИЗИ23о1
Даны две действительные квадратные матрицы размером n*n. Получить новую
матрицу прибавлением к элементам каждого столбца первой матрицы
произведения элементов соответствующих строк второй матрицы.

"""
import random

n = int(input("Введите n: "))
matrix1 = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
matrix2 = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

print("\nМатрица A:")
for i in range(n):
    for j in range(n):
        print(f"{matrix1[i][j]:4d}", end="")
    print()

print("\nМатрица B:")
for i in range(n):
    for j in range(n):
        print(f"{matrix2[i][j]:4d}", end="")
    print()

row_products = []
for i in range(n):
    product = 1
    for j in range(n):
        product *= matrix2[i][j]
    row_products.append(product)


result_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix1[i][j] + row_products[j])
    result_matrix.append(row)

print("\nНовая матрица C (A + произведение строк B):")
for i in range(n):
    for j in range(n):
        print(f"{result_matrix[i][j]:6d}", end="")
    print()