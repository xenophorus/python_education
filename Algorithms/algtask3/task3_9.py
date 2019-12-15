# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random


def begin():
    matrix = []
    for i in range(5):
        matrix.append([random.randint(1, 100) for i in range(5)])
    print(*matrix, sep='\n')
    mins = []
    a = []
    for i in range(5):
        lst = []
        a = 100
        for j in range(5):
            lst.append(matrix[j][i])
        for i in lst:
            if a >= i:
                a = i
        mins.append(a)
    for i in mins:
        if a <= i:
            a = i
    print(f'Максимальное число из минимальных: {a}')


begin()
