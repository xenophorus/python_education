# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random


def summator(lst, a, b):
    lst_crop = lst[lst.index(a ) + 1:lst.index(b)]
    summa = 0
    if lst_crop == []:
        print(f'Между элементами {a} и {b} нет чисел')
    else:
        for i in lst_crop:
            summa += i
    print(f'Сумма чисел между элементами {a} и {b} равна {summa}')



def begin():
    arr_length = 10
    arr_min = 1
    arr_max = 100
    lst = [random.randint(arr_min, arr_max) for _ in range(arr_length)]
    print(lst)
    lst_max = 0
    lst_min = 100
    for i in lst:
        if lst_max < i:
            lst_max = i
    for i in lst:
        if lst_min > i:
            lst_min = i
    if lst.index(lst_max) < lst.index(lst_min):
        summator(lst, lst_max, lst_min)
    else:
        summator(lst, lst_min, lst_max)


begin()
