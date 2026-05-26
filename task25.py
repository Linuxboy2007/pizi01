#Чекрышов Задание 25

n = int(input("n = "))


A = []
print("Введите матрицу построчно:")
for i in range(n):
    row = list(map(int, input(f"Строка {i + 1}: ").split()))
    A.append(row)

# Поиск минимального элемента на главной диагонали и его столбца
min_value = A[0][0]
min_col = 0

for i in range(n):
    if A[i][i] < min_value:
        min_value = A[i][i]
        min_col = i

print(f"\nМинимальный элемент главной диагонали: {min_value} в столбце {min_col + 1}")


B = []
for i in range(n):
    new_row = []
    for j in range(n):
        if j != min_col:  
            new_row.append(A[i][j])
    B.append(new_row)


print("\nИсходная матрица:")
for row in A:
    print(" ".join(f"{x:4d}" for x in row))

# Вывод результата
print(f"\nМатрица после удаления столбца {min_col + 1}:")
for row in B:
    print(" ".join(f"{x:4d}" for x in row))
print(f"Новый размер матрицы: {n} x {n-1}")