# -*- coding: utf-8 -*-
n = int(input("Введите размер квадртной матрицы: "))

A = []
print("Матрица A:")
for i in range(n):
    row = list(map(float, input(f"Строка {i+1} матрицы A: ").split()))
    A.append(row)

B = []
print("Матрица B:")
for i in range(n):
    row = list(map(float, input(f"Строка {i+1} матрицы B: ").split()))
    B.append(row)

proizv = []
for i in range(n):
    p = 1.0
    for j in range(n):
        p *= B[i][j]
    proizv.append(p)

C = []
for i in range(n):
    new_row = []
    for j in range(n):
        new_row.append(A[i][j] + proizv[i])
    C.append(new_row)

print("Новая матрица:")
for i in C:
    print(i)
    
    #Даны две действительные квадратные матрицы размером n*n. Получить новую
#матрицу прибавлением к элементам каждого столбца первой матрицы
#произведения элементов соответствующих строк второй матрицы