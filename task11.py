# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:43:15 2026
import random

n = int(input("Введите n: "))
m = int(input("Введите m: "))
matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

maxx = -99999
minn = 1000000
for row in matrix:
    row_sum = sum(row)
    if row_sum > maxx:
        maxx = row_sum
    if row_sum < minn:
        minn = row_sum

print(matrix)
print(maxx)
print(minn)
@author: Urusor
"""

