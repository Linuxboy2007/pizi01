#Чекрышов Задание 6
n = int(input("n = "))
m = int(input("m = "))

A = []
for i in range(n):
    row = list(map(int, input(f"Введите значения строки {i + 1}, через пробел: ").split()))
    A.append(row)

# Сумма максимумов строк
b = sum(max(row) for row in A)

print("Сумма наибольших значений элементов строк:", b)