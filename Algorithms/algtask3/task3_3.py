# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random


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
    print(lst_max, lst_min)
    lst[lst.index(lst_min)], lst[lst.index(lst_max)] = lst[lst.index(lst_max)], lst[lst.index(lst_min)]
    print(lst)


begin()
