#Кострикин №19

n = int(input("n = "))

A = []
for i in range(n):
    row = list(map(float, input(f"Введите строку {i+1} первой матрицы: ").split()))
    A.append(row)

B = []
for i in range(n):
    row = list(map(float, input(f"Введите строку {i+1} второй матрицы: ").split()))
    B.append(row)

C = []
for i in range(n):
    min_val = min(B[i])
    new_row = [A[i][j] * min_val for j in range(n)]
    C.append(new_row)

for row in C:
    print(' '.join(map(str, row)))