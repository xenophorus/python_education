# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random


def min_num(lst):
    lst_min = 100
    for i in lst:
        if lst_min >= i:
            lst_min = i
    return lst_min


def begin():
    arr_length = 10
    arr_min = 1
    arr_max = 100
    lst = [random.randint(arr_min, arr_max) for _ in range(arr_length)]
    print(lst)
    a = min_num(lst)
    lst.remove(a)
    b = min_num(lst)
    print(a, b)


begin()
