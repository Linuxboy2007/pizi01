n = int(input("Введите размер матрицы n:"))
a = []
print('Введите элементы матрицы')

for i in range(n):
    b = []
    for j in range(n):
        b.append(float(input()))
    a.append(b)

print("\nИсходная матрица")
for i in range(n):
    for j in range(n):
        print(a[i][j], end = " ")

diag = []
for i in range(n):
    diag.append(a[i][i])

summa = 0
for i in range(n):
    summa += diag[i]

sred = summa / n

min_diag = diag[0]
for i in range(n):
    if diag[i] < min_diag:
        min_diag = diag[i]

print("\nЭлементы по диагонали:", diag)
print("Среднее = ", sred)
print("Минимум = ", min_diag)

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            a[i][j] = a[i][j] / sred
        else:
            a[i][j] = a[i][j] / min_diag

print("\nПреобразованная матрица:")
for i in range(n):
    for j in range(n):
        print(round(a[i][j], 3), end = " ")
    print()