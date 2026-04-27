#Корунов, варианты 6, 20
n = int(input("n = "))
m = int(input("m = "))

A = []
for i in range(n):
    row = list(map(int, input(f"Введите значения строки {i + 1}, через пробел: ").split()))
    A.append(row)

b = 0

for i in range(n):
    maximum = max(A[i])
    b += maximum

print("Сумма:", b)