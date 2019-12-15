# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

import sys


def m_input():
    s = input('Введите 3 числа, разделенных пробелами: ')
    s.strip()
    a = s.strip().split(' ')
    sum_ = 0
    for i in a.copy():
        if i.isdigit() == False:
            print('Некорректный ввод!')
            sys.exit()
        elif len(a) != 3:
            print('Неверное число цифр!')
            sys.exit()
        else:
            a.append(int(a.pop(0)))
            sum_ += int(i)
    a.append(sum_)
    return a


def begin():
    print('Заполним матрицу 5x4.')
    matrix = []
    for i in range(5):
        matrix.append(m_input())
    print(*matrix, sep = '\n')


begin()
