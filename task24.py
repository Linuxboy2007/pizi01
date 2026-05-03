n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_val, i_max, j_max = 0, 0, 0
for i in range(n):
    for j in range(m):
        if abs(matrix[i][j]) > max_val:
            max_val = abs(matrix[i][j])
            i_max, j_max = i, j

matrix[k-1], matrix[i_max] = matrix[i_max], matrix[k-1] 

for row in matrix:
    row[k-1], row[j_max] = row[j_max], row[k-1] #FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

for row in matrix:
    print(*row)# -*- coding: utf-8 -*-

