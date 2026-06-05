# -*- coding: utf-8 -*-
"""
Задание 7.
Дана целочисленная квадратная матрица размером n*n.
Сформировать два одномерных массива:
- в первый переслать по строкам верхний треугольник, включая главную диагональ;
- во второй — нижний треугольник, включая главную диагональ.
"""

n = int(input("Введите размер квадратной матрицы n: "))

print("Введите матрицу построчно (элементы через пробел):")
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        raise ValueError(f"В строке {i + 1} должно быть {n} элементов")
    matrix.append(row)

upper = []
lower = []

for i in range(n):
    for j in range(n):
        if j >= i:
            upper.append(matrix[i][j])
        if j <= i:
            lower.append(matrix[i][j])

print("\nИсходная матрица:")
for row in matrix:
    print(" ".join(f"{x:4}" for x in row))

print("\nВерхний треугольник (включая главную диагональ):")
print(upper)

print("\nНижний треугольник (включая главную диагональ):")
print(lower)
