# Задание 3.8
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
import cProfile
import sys
import random
import timeit

# Я взял сам алгоритм составления строки матрицы и суммирования всех ее членов. Ввод чисел убрал, заменил большим
# списком. Также здесь я сознательно оставил преобразование массивов в строку и обратно.
# Преобразование в числа есть в оригинальной функции.


#Оригинальная функция.

# t = '''
# def m_input2():
#     c = [x for x in range(1000)]
#     s = [str(i) for i in c]
#     sum_ = 0
#     for i in s.copy():
#         s.append(int(s.pop(0)))
#         sum_ += int(i)
#     s.append(sum_)
#     return s
#
# m_input2()
# '''
#
# #range 100 - 0.011761000000000008
#        1    0.000    0.000    0.000    0.000 task3_8.py:119(m_input2)

# #range 1000 - 0.1570243
#        1    0.001    0.001    0.003    0.003 task3_8.py:121(m_input2)

# #range 10000 - 5.1623624
#        1    0.010    0.010    0.054    0.054 task3_8.py:123(m_input2)

# #range 100000 - 419.0402085
#        1    0.128    0.128    4.106    4.106 task3_8.py:125(m_input2)

#cProfile.run('m_input2()')
# a = timeit.timeit(t, number=100)
# print(a)


############################################################################################


# s = '''
# def m_input1():
#     c = [x for x in range(100000)]
#     s = [str(i) for i in c]
#     b = [int(i) for i in s]
#     b.append(sum(b))
#     return b
#
# m_input1()
# '''
# #
# #range 100 - 0.006234799999999999
#        1    0.000    0.000    0.000    0.000 task3_8.py:111(m_input1)

# #range 1000 - 0.052081800000000004
#        1    0.000    0.000    0.001    0.001 task3_8.py:111(m_input1)

# #range 10000 - 0.5939444
#        1    0.000    0.000    0.006    0.006 task3_8.py:111(m_input1)

# #range 100000 - 6.7729168
#        1    0.000    0.000    0.062    0.062 task3_8.py:111(m_input1)
#
# cProfile.run('m_input1()')
# a = timeit.timeit(s, number=100)
# print(a)

################################################################################################
# Этот вариант интересен как правильно решенный в рамках условий задачи.
# Если же вместо sum_ += int(i) b.append(sum_) написать b.append(sum(b)), то результаты
# приближаются к лучшим. Хотя немного не дотягивают.

#t = '''
# def m_input2():
#     c = [x for x in range(100)]
#     s = [str(i) for i in c]
#     b = []
#     sum_ = 0
#     for i in s:
#         b.append(int(i))
#         sum_ += int(i)
#     b.append(sum_)
#     return b
#
# m_input2()
#'''
#
# #range 100 - 0.007903899999999998
#        1    0.000    0.000    0.000    0.000 task3_8.py:82(m_input2)

# #range 1000 - 0.09008839999999999
#        1    0.001    0.001    0.001    0.001 task3_8.py:82(m_input2)

# #range 10000 - 0.9305231999999999
#        1    0.006    0.006    0.010    0.010 task3_8.py:82(m_input2)

# #range 100000 - 9.6429717
#        1    0.066    0.066    0.107    0.107 task3_8.py:82(m_input2)

#cProfile.run('m_input2()')
# b = timeit.timeit(t, number=100)
# print(b)


######################################################################################

# Оригинальная функция
# def m_input():
#     s = input('Введите 3 числа, разделенных пробелами: ')
#     s.strip()
#     a = s.strip().split()
#     sum_ = 0
#     for i in a.copy():
#         if i.isdigit() == False:
#             print('Некорректный ввод!')
#             sys.exit()
#         elif len(a) != 3:
#             print('Неверное число цифр!')
#             sys.exit()
#         else:
#             a.append(int(a.pop(0)))
#             sum_ += int(i)
#     a.append(sum_)
#     return a


#Улучшение предыдущей функции.
# def m_input():
#     s = input('Введите 3 числа, разделенных пробелами: ')
#     a = s.strip().split()
#     b = []
#     sum_ = 0
#     for i in a.copy():
#         if i.isdigit() == False:
#             print('Некорректный ввод!')
#             sys.exit()
#         elif len(a) != 3:
#             print('Неверное число цифр!')
#             sys.exit()
#         else:
#             b.append(int(i))
#             sum_ += int(i)
#     b.append(sum_)
#     return b

# Лучшее решение. Минимум вызовов. Линейный рост.
def m_input():
    s = input('Введите 3 числа, разделенных пробелами: ')
    a = s.strip().split()
    for i in a:
        if not i.isdigit():
            print('Некорректный ввод!')
            sys.exit()
        elif len(a) != 3:
            print('Неверное число цифр!')
            sys.exit()
    b = [int(i) for i in a]
    b.append(sum(b))
    return b


def begin():
    print('Заполним матрицу 5x4.')
    matrix = []
    for i in range(5):
        matrix.append(m_input())
    print(*matrix, sep='\n')


begin()
