# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# каждому из чисел в диапазоне от 2 до 9.

# def begin():
#     arr_min = 2
#     arr_max = 99
#     div_min = 2
#     div_max = 9
#     for i in range(div_min, div_max + 1):
#         tenplist = []
#         print(f'Делимых на {i}: ', end = '')
#         for j in range (arr_min, arr_max):
#             if j % i == 0:
#                 tenplist.append(j)
#         print(len(tenplist))
#
#
# begin()

# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
# надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к.
# именно в этих позициях первого массива стоят четные числа.
# import random
#
#
# def begin():
#     arr_length = 10
#     arr_min = 1
#     arr_max = 100
#     lst = [random.randint(arr_min, arr_max) for _ in range(arr_length)]
#     # print(lst)
#     lst_even = [lst.index(x) for x in lst if x % 2 == 0]
#     print(lst_even)
#
#
# begin()

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# import random
#
#
# def begin():
#     arr_length = 10
#     arr_min = 1
#     arr_max = 100
#     lst = [random.randint(arr_min, arr_max) for _ in range(arr_length)]
#     print(lst)
#     lst_max = 0
#     lst_min = 100
#     for i in lst:
#         if lst_max < i:
#             lst_max = i
#     for i in lst:
#         if lst_min > i:
#             lst_min = i
#     print(lst_max, lst_min)
#     lst[lst.index(lst_min)], lst[lst.index(lst_max)] = lst[lst.index(lst_max)], lst[lst.index(lst_min)]
#     print(lst)
#
#
# begin()


# Определить, какое число в массиве встречается чаще всего.

# import random
#
#
# def begin():
#     arr_length = 100
#     arr_min = 1
#     arr_max = 10
#     lst = [random.randint(arr_min, arr_max) for _ in range(arr_length)]
#     a = []
#     lst_max = 0
#     for i in range(arr_min, arr_max + 1):
#         a.append(lst.count(i))
#     for i in a:
#         if lst_max <= i:
#             lst_max = i
#
#     print('Наиболее часто встречаются числа: ')
#     for i in range(arr_max):
#         if a[i] == lst_max:
#             print(f'{i + 1}:  {lst_max} раз')
#
#
# begin()


# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.

# import random
#
# # Как я понимаю, максимальный отрицательный элемент это число с минимальным модулем. По крайней мере,
# # в школе так рассказывали
#
# def begin():
#     arr_length = 10
#     arr_min = -50
#     arr_max = 50
#     lst = [random.randint(arr_min, arr_max) for _ in range(arr_length)]
#     print(lst)
#     a = [x for x in lst if x < 0]
#     neg_max = -50
#     for i in a:
#         if neg_max <= i:
#             neg_max = i
#
#     print(f'Максимальный отрицательный элемент равен {neg_max}')
#
#
# begin()



# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

# import random
#
#
# def summator(lst, a, b):
#     lst_crop = lst[lst.index(a ) + 1:lst.index(b)]
#     summa = 0
#     if lst_crop == []:
#         print(f'Между элементами {a} и {b} нет чисел')
#     else:
#         for i in lst_crop:
#             summa += i
#     print(f'Сумма чисел между элементами {a} и {b} равна {summa}')
#
#
#
# def begin():
#     arr_length = 10
#     arr_min = 1
#     arr_max = 100
#     lst = [random.randint(arr_min, arr_max) for _ in range(arr_length)]
#     print(lst)
#     lst_max = 0
#     lst_min = 100
#     for i in lst:
#         if lst_max < i:
#             lst_max = i
#     for i in lst:
#         if lst_min > i:
#             lst_min = i
#     if lst.index(lst_max) < lst.index(lst_min):
#         summator(lst, lst_max, lst_min)
#     else:
#         summator(lst, lst_min, lst_max)
#
#
# begin()

# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# import random
#
#
# def min_num(lst):
#     lst_min = 100
#     for i in lst:
#         if lst_min >= i:
#             lst_min = i
#     return lst_min
#
#
# def begin():
#     arr_length = 10
#     arr_min = 1
#     arr_max = 100
#     lst = [random.randint(arr_min, arr_max) for _ in range(arr_length)]
#     print(lst)
#     a = min_num(lst)
#     lst.remove(a)
#     b = min_num(lst)
#     print(a, b)
#
#
# begin()



# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
# import sys
#
#
# def m_input():
#     s = input('Введите 3 числа, разделенных пробелами: ')
#     s.strip()
#     a = s.strip().split(' ')
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
#
#
# def begin():
#     print('Заполним матрицу 5x4.')
#     matrix = []
#     for i in range(5):
#         matrix.append(m_input())
#     print(*matrix, sep = '\n')
#
#
# begin()


# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random



def begin():
    matrix = []
    for i in range(5):
        matrix.append([random.randint(1, 100) for i in range(5)])
    print(*matrix, sep='\n')
    mins = []
    for i in matrix:
        a = 100
        for j in i:
            if a >= j:
                a = j
        mins.append(a)
    print(mins)
    a = 0
    for i in mins:
        if a <= i:
            a = i
    print(f'Максимальное число из минимальных {a}')




begin()