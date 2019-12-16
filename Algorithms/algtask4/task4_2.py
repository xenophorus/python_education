import sys
import timeit
import cProfile


sys.setrecursionlimit(5000)


# s = '''
# def not_sieved(lst, divisor, z):
#     z -= 1
#     if z == 0:
#         return lst[0] # при первой итерации мы уже имеем нужное число в начале списка. Его и выводим.
#     list2 = []
#     for i in lst:
#         if i % divisor != 0 and divisor < i:
#             list2.append(i)
#     return not_sieved(list2, list2[0], z)
#
# not_sieved(range(2,10000), 2, 100)
# '''
# # (range(2,100), 2, 10) 0.0038166999999999993
#         1    0.000    0.000    0.000    0.000 task4_2.py:103(main)
#         1    0.000    0.000    0.000    0.000 task4_2.py:108(<listcomp>)
#      10/1    0.000    0.000    0.000    0.000 task4_2.py:74(not_sieved)
#       217    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# # (range(2,1000), 2, 100) 0.1872025
#         1    0.000    0.000    0.003    0.003 task4_2.py:100(main)
#         1    0.000    0.000    0.000    0.000 task4_2.py:105(<listcomp>)
#     100/1    0.002    0.000    0.003    0.003 task4_2.py:71(not_sieved)
#     12443    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}

# # (range(2,10000), 2, 100) 1.8477659
#         1    0.000    0.000    0.039    0.039 task4_2.py:105(main)
#         1    0.000    0.000    0.000    0.000 task4_2.py:110(<listcomp>)
#     100/1    0.030    0.000    0.038    0.038 task4_2.py:76(not_sieved)
#    129976    0.009    0.000    0.009    0.000 {method 'append' of 'list' objects}

# # (range(2,10000), 2, 1000) 10.5892169
#         1    0.000    0.000    0.204    0.204 task4_2.py:109(main)
#         1    0.000    0.000    0.000    0.000 task4_2.py:114(<listcomp>)
#    1000/1    0.157    0.000    0.204    0.204 task4_2.py:80(not_sieved)
#    741526    0.047    0.000    0.047    0.000 {method 'append' of 'list' objects}

#############################################################################################################

# t = '''
# def sieve(lst, n, z):
#     lst2 = [x for x in lst if x % lst[n] != 0 or x <= lst[n]]
#     z -= 1
#     if z == 0:
#         return lst2[n]
#     else:
#         return sieve(lst2, n + 1, z)
#
# sieve(range(2,10000), 0, 100)
# '''
# # (range(2,100), 0, 10) 0.005606699999999999
#      10/1    0.000    0.000    0.000    0.000 task4_2.py:76(sieve)
#        10    0.000    0.000    0.000    0.000 task4_2.py:77(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task4_2.py:94(main)

# # (range(2,1000), 0, 100) 0.20480449999999997
#     100/1    0.000    0.000    0.002    0.002 task4_2.py:76(sieve)
#       100    0.002    0.000    0.002    0.000 task4_2.py:77(<listcomp>)
#         1    0.000    0.000    0.002    0.002 task4_2.py:94(main)

# # (range(2,10000), 0, 100) 1.4535263
#     100/1    0.001    0.000    0.016    0.016 task4_2.py:77(sieve)
#       100    0.015    0.000    0.015    0.000 task4_2.py:78(<listcomp>)
#         1    0.000    0.000    0.016    0.016 task4_2.py:95(main)

# # (range(2,10000), 0, 1000) 12.3910525
#    1000/1    0.012    0.000    0.156    0.156 task4_2.py:76(sieve)
#      1000    0.144    0.000    0.144    0.000 task4_2.py:77(<listcomp>)
#         1    0.000    0.000    0.157    0.157 task4_2.py:94(main)


# print(timeit.timeit(s, number=100))
# print(timeit.timeit(t, number=100))


def not_sieved(lst, divisor, z):
    z -= 1
    if z == 0:
        return lst[0] # при первой итерации мы уже имеем нужное число в начале списка. Его и выводим.
    list2 = []
    for i in lst:
        if i % divisor != 0 and divisor < i:
            list2.append(i)
    return not_sieved(list2, list2[0], z)


def sieve(lst, n, z):
    lst2 = [x for x in lst if x % lst[n] != 0 or x <= lst[n]]
    z -= 1
    if z == 0:
        return lst2[n]
    else:
        return sieve(lst2, n + 1, z)


def main():
    z = int(input('Введите порядковый номер желаемого простого числа: '))
    if z <= 0:
        print('Некорректный ввод!')
        return None
    lst = [x for x in range(2, 1000)]
    print(f'Sieved: {sieve(lst, 0, z)}')
    print(f'Not sieved: {not_sieved(lst, 2, z)}')

# def main():
#     z = 1000
#     if z <= 0:
#         print('Некорректный ввод!')
#         return None
#     lst = [x for x in range(2, 10000)]
#     #print(f'Sieved: {sieve(lst, 0, z)}')
#     print(f'Not sieved: {not_sieved(lst, 2, z)}')
#
# print(cProfile.run('main()'))

main()
