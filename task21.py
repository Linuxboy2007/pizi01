
import random


def replace_min_in_rows(matrix):
    for i in range(len(matrix)):
        if matrix[i]:  # если строка не пустая
            min_val = min(matrix[i])  # находим минимальное значение в строке
            for j in range(len(matrix[i])):
                if matrix[i][j] == min_val:
                    matrix[i][j] = 0.0  # заменяем на ноль
    return matrix


def generate_random_matrix(n, m, min_val=-10.0, max_val=10.0):
    return [[round(random.uniform(min_val, maxval), 2) for in range(m)] for in range(n)]


def print_matrix(matrix, name="Матрица"):
    print(f"\n{name}:")
    for row in matrix:
        print(' '.join(f'{x:7.2f}' for x in row))


if name == "main__":
    n = int(input("Введите количество строк n: "))
    m = int(input("Введите количество столбцов m: "))
    matrix = generate_random_matrix(n, m, -10, 10)

    print_matrix(matrix, "Исходная матрица")
    result = replace_min_in_rows(matrix)
    print_matrix(result, "Матрица после замены (минимальные элементы строк обнулены)")
# -*- coding: utf-8 -*-
#аны две действительные квадратные матрицы размером n*n. Получить новую
#матрицу умножением элементов каждой строки первой матрицы на наибольшее
#из значений элементов соответствующей строки второй матрицы.