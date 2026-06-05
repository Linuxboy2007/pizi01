import random

def form_triangles(matrix):
    n = len(matrix)  # размер квадратной матрицы
    upper = []
    lower = []

    for i in range(n):
        for j in range(n):
            if j >= i:   # верхний треугольник (диагональ и выше)
                upper.append(matrix[i][j])
            if j <= i:   # нижний треугольник (диiагональ и ниже)
                lower.append(matrix[i][j])

    return upper, lower


def generate_random_square_matrix(n, min_val=-10, max_val=10):
    return [[random.randint(min_val, maxval) for  in range(n)] for  in range(n)] #FFFFFFFFFFFFFFFFFFFFFFFFFFFFF


def print_matrix(matrix):
    print("Квадратная матрица:")
    for row in matrix:
        print(' '.join(f'{x:4}' for x in row))
    print()

def print_array(arr, name):
    print(f"{name}: {arr}")
    print(f"Количество элементов: {len(arr)}")
    print()


if name == "main__":
    n = int(input("Введите размер квадратной матрицы n: ")) 
    matrix = generate_random_square_matrix(n, -9, 9)
    print_matrix(matrix)
    upper, lower = form_triangles(matrix)
    print("Результат:")
    print_array(upper, "Верхний треугольник (включая главную диагональ)")
    print_array(lower, "Нижний треугольник (включая главную диагональ)")# -*- coding: utf-8 -*-
