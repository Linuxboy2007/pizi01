# -*- coding: utf-8 -*-
"""
Задание 21.
Даны две действительные квадратные матрицы размером n*n.
Получить новую матрицу умножением элементов каждой строки первой матрицы
на наибольшее из значений элементов соответствующей строки второй  матрицы.
"""

n = int(input("Введите размер матрицы n: "))

print("\nВведите матрицу A построчно:")
A = []
for i in range(n):
    row = list(map(float, input().split()))
    if len(row) != n:
        raise ValueError(f"В строке {i + 1} матрицы A должно быть {n} элементов")
    A.append(row)

print("\nВведите матрицу B построчно:")
B = []
for i in range(n):
    row = list(map(float, input().split()))
    if len(row) != n:
        raise ValueError(f"В строке {i + 1} матрицы B должно быть {n} элементов")
    B.append(row)

C = []
for i in range(n):
    max_in_row_b = max(B[i])
    new_row = [A[i][j] * max_in_row_b for j in range(n)]
    C.append(new_row)

print("\nМатрица A:")
for row in A:
    print(row)

print("\nМатрица B:")
for row in B:
    print(row)

print("\nРезультирующая матрица C:")
for row in C:
    print(row)
