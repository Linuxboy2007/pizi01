# -*- coding: utf-8 -*-
"""
5
Шапоренко А.М. ПИЗИ23о1
Дана действительная матрица размером n*m. Все элементы с наибольшим
значением заменить нулями (таких элементов может быть несколько)

"""
def replace_max_in_rows(matrix):
    for row in matrix:
        if not row:          
            continue
        max_val = max(row)   
        for i in range(len(row)):
            if row[i] == max_val:
                row[i] = 0.0
    return matrix

if "name" == "__main__":
    try:
        n = int(input("Введите количество строк (n): "))
        m = int(input("Введите количество столбцов (m): "))

        matrix = []
        print("Введите элементы матрицы построчно (через пробел):")
        for i in range(n):
            row = list(map(float, input(f"Строка {i+1}: ").split()))
            if len(row) != m:
                print(f"Ошибка. Попробуйте снова.")
                exit(1)
            matrix.append(row)

        print("Исходная матрица:")
        for row in matrix:
            print(" ".join(f"{x:.2f}" for x in row))

        replace_max_in_rows(matrix)

        print("Матрица конечная:")
        for row in matrix:
            print(" ".join(f"{x:.2f}" for x in row))

    except ValueError:
        print("Ошибка ввода: необходимо вводить числа.")
