#  Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
#  на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут

import random


# import timeit


# s = '''
# import random
# def bubble_sort(lst):
#     idx = len(lst) -1
#     c = 1
#     while c < len(lst):
#         for i in range(idx):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#         c += 1
# bubble_sort([random.randint(-10000, 10000) for _ in range(1000)])
# '''
#
# t = '''
# # Алгоритм, который чуть умнее. Нет нужды сравнивать числа с уже отсортированными
#
# import random
# def bubble_sort1(lst):
#     idx = len(lst) -1
#     c = 1
#     while c < len(lst):
#         for i in range(idx):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#         idx -= 1
#         c += 1
# bubble_sort1([random.randint(-10000, 10000) for _ in range(1000)])
# '''
# # Списки длиной в 1000 эл.:
# # 19.1023961
# # 12.1109057
# # Списки длиной в 10000 эл. (number=10):
# # 204.8971889
# # 130.6797027
#
# print(timeit.timeit(s, number=100))
# print(timeit.timeit(t, number=100))

def bubble_sort(lst):
    idx = len(lst) - 1
    c = 1
    while c < len(lst):
        for i in range(idx):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        c += 1


# Алгоритм, который чуть умнее. Нет нужды сравнивать числа с уже отсортированными
def bubble_sort1(lst):
    idx = len(lst) - 1
    c = 1
    while c < len(lst):
        for i in range(idx):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        idx -= 1
        c += 1


def begin():
    lst = [random.randint(-1000, 1000) for _ in range(100)]
    lst1 = [random.randint(-1000, 1000) for _ in range(100)]
    bubble_sort(lst)
    bubble_sort1(lst1)
    print(lst)
    print(lst1)


begin()
