import numpy as np
r1 = int(input('ввести количество строк у первой матрицы'))
s1 = int(input('ввести количество столбцов у первой матрицы'))
r2 = int(input('ввести количество строк у второй матрицы'))
s2 = int(input('ввести количество столбцов у второй матрицы'))
a1 = []
b1 = []
for i in range(r1):
    f = []
    for j in range(s1):
        f1 = int(input())
        f.append(f1)
    a1.append(f)
for i in range(r2):
    k = []
    for j in range(s2):
        k1 = int(input())
        k.append(k1)
    b1.append(k)
a = np.array(a1, dtype=int)
b = np.array(b1, dtype=int)
if r1 != r2 or s1 != s2:
    print('нельзя складывать')
else:
    c = a + b
    print('сложение:', c)
if s1 == r2:
    d = np.dot(a, b)
    print('умножение:', d)
else:
    print('нельзя умножать')
