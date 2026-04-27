n = int(input("Введите кол-во строк: "))
m = int(input("Введите кол-во столбцов: "))

a = []
for i in range(n):
    row = list(map(float, input().split()))
    a.append(row)

max_val = a[0][0]
max_i, max_j = 0, 0

for i in range(n):
    row_max = a[i][0]
    row_j = 0
    for j in range(m):
        if a[i][j] > row_max:
            row_max = a[i][j]
            row_j = j
    if row_max > max_val:
        max_val = row_max
        max_i = i
        max_j = row_j

print(max_i, max_j)