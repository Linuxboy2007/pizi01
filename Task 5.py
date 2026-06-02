#Кострикин №5

n = int(input("n = "))
m = int(input("m = "))

A = []
for i in range(n):
    row = list(map(float, input(f"Введите значения строки {i + 1}, через пробел: ").split()))
    A.append(row)

max_val = max(max(row) for row in A)

for i in range(n):
    for j in range(m):
        if A[i][j] == max_val:
            A[i][j] = 0

for row in A:
    print(' '.join(map(str, row)))