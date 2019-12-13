# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
# надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к.
# именно в этих позициях первого массива стоят четные числа.
import random


def begin():
    arr_length = 10
    arr_min = 1
    arr_max = 100
    lst = [random.randint(arr_min, arr_max) for _ in range(arr_length)]
    lst_even = [lst.index(x) for x in lst if x % 2 == 0]
    print(lst_even)


begin()
