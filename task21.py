# -*- coding: utf-8 -*-
import random

# Ввод размера матрицы
n = int(input("Введите размер матрицы n: "))

# Создаем две пустые матрицы
A = []
B = []

# Заполняем первую матрицу A
print("\nМатрица A:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(-10, 10))
    A.append(row)
    print(row)

# Заполняем вторую матрицу B
print("\nМатрица B:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(-10, 10))
    B.append(row)
    print(row)

# Создаем результирующую матрицу C
C = []

# Для каждой строки
for i in range(n):
    # Находим максимальное значение в i-й строке матрицы B
    max_v = B[i][0]  # берем первый элемент как максимум
    for j in range(n):
        if B[i][j] > max_v:
            max_v = B[i][j]

    print(f"\nМаксимум в строке {i + 1} матрицы B: {max_v}")

    # Создаем новую строку для матрицы C
    new_row = []
    for j in range(n):
        # Умножаем каждый элемент строки A на max_v
        new_row.append(A[i][j] * max_v)
    C.append(new_row)

    print(f"Строка {i + 1} матрицы A: {A[i]}")
    print(f"Результат умножения на {max_v}: {new_row}")

# Выводим результат
print("\n" + "=" * 50)
print("Результирующая матрица C:")
for row in C:
    print(row)