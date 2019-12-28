#  Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#  заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge(l, r):

    res_lst = []
    while len(l) > 0 and len(r) > 0:
        if l[0] <= r[0]:
            res_lst.append(l[0])
            l = l[1:]
        else:
            res_lst.append(r[0])
            r = r[1:]
    while len(l) > 0:
        res_lst.append(l[0])
        l = l[1:]
    while len(r) > 0:
        res_lst.append(r[0])
        r = r[1:]

    return res_lst



def splitter(lst):

    if len(lst) <= 1:
        return lst

    center = len(lst) // 2
    leftp = lst[center:]
    rightp = lst[:center]
    #print(leftp, rightp)
    leftp = splitter(leftp)
    rightp = splitter(rightp)
    return merge(leftp, rightp)


def begin():
    lst = [random.randint(0, 150) for x in range(50)]
    print(lst)
    lst = splitter(lst)
    print(lst)



begin()

