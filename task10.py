# -*- coding: utf-8 -*-
import random

def generate_random_matrix(n, min_val=-10.0, max_val=10.0):
    return [[round(random.uniform(min_val, maxval), 2) for  in range(n)] for  in range(n)]


def multiply_rows_by_max_ofsecond(A, B):
    n = len(A)
    C = [[0.0] * n for  in range(n)]

    for i in range(n):
        max_in_row_B = max(B[i])  # наибольшее значение в i-й строке матрицы B
        for j in range(n):
            C[i][j] = round(A[i][j] * max_in_row_B, 2)

    return C


def print_matrix(matrix, name="Матрица"):
    print(f"\n{name}:")
    for row in matrix:
        print(' '.join(f'{x:8.2f}' for x in row))


if name == "main__":
    n = int(input("Введите размер квадратных матриц n: "))

    A = generate_random_matrix(n, -10, 10)
    B = generate_random_matrix(n, -5, 15)
    print_matrix(A, "Первая матрица A")
    print_matrix(B, "Вторая матрица B")

    C = multiply_rows_by_max_of_second(A, B)

    print_matrix(C, "Результат C (A[i][j] * max(B[i]))")

    print("\n" + "="*60)
    print("Пояснение (максимумы строк матрицы B):")
    for i in range(n):
        max_val = max(B[i])
        print(f"Строка {i+1}: max(B[{i}]) = {max_val:.2f}")
