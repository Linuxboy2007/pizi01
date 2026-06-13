# -*- coding: utf-8 -*-
"""
Агапчева Анастасия Алексеевна. Задана целочисленная квадратная матрица размером n*n. Написать программу,
преобразующую исходную матрицу по правилу: нечетные столбцы разделить на
среднее значение диагональных элементов матрицы, а четные оставить без
изменения.
"""
n = int(input("Введите размер матрицы: "))

matrix = []
print("Введите элементы матрицы построчно (через пробел):")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

sum_diagonal = 0
for i in range(n):
    sum_diagonal += matrix[i][i]  

mean_diagonal = sum_diagonal / n

for i in range(n):
    for j in range(n):
        if j % 2 == 1:  
            matrix[i][j] = matrix[i][j] / mean_diagonal

print("\nПреобразованная матрица:")
for i in range(n):
    for j in range(n):
        
        if matrix[i][j] == int(matrix[i][j]):
            print(f"{int(matrix[i][j])}", end=" ")
        else:
            print(f"{matrix[i][j]:.2f}", end=" ")
    print()

