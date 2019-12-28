# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
import random


def without_sorting(lst):
    for i in lst:
        nless = []
        nmore = []
        equal = []
        for j in range(len(lst)):
            if i > lst[j]:
                nless.append(lst[j])
            if i < lst[j]:
                nmore.append(lst[j])
            if i == lst[j]:
                equal.append(lst[j])
        if max(len(nmore), len(nless)) == min(len(nmore), len(nless)) + len(equal) - 1:
            # print(nmore, nless, equal)
            return i


def begin():
    lst = [random.randint(1, 100) for _ in range(55)]
    print(lst)
    med = without_sorting(lst)
    print(f'Медиана - {med}')


begin()
