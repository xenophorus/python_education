# Определить, какое число в массиве встречается чаще всего.

import random


def begin():
    arr_length = 100
    arr_min = 1
    arr_max = 10
    lst = [random.randint(arr_min, arr_max) for _ in range(arr_length)]
    a = []
    lst_max = 0
    for i in range(arr_min, arr_max + 1):
        a.append(lst.count(i))
    for i in a:
        if lst_max <= i:
            lst_max = i

    print('Наиболее часто встречаются числа: ')
    for i in range(arr_max):
        if a[i] == lst_max:
            print(f'{i + 1}:  {lst_max} раз')


begin()
