import sys


def not_sieved(lst, divisor, z):
    newlst = []
    for i in lst:
        if lst[divisor] >= i:
            newlst.append(i)
    for i in lst:
        if i % lst[divisor] != 0 and lst[divisor] <= i:
            newlst.append(i)
    z -= 1
    divisor += 1
    if z == 0:
        print(newlst[divisor])
        sys.exit()
    not_sieved(newlst, divisor, z)


def sieve(lst, n, z):
    lst2 = [x for x in lst if x > n and x % n != 0]
    z -= 1
    if z == 0:
        print(lst2[0])
        sys.exit()
    sieve(lst2, lst2[0], z)


def main():
    z = int(input('Введите порядковый номер желаемого простого числа: '))
    if z == 1:
        print('2')
        sys, exit()
    lst = [x for x in range(2, 1000)]
    #sieve(lst, lst[0], z - 1)  # z - 1 потому, что первая проверка не требовала вычислений
    not_sieved(lst, 0, z - 1)


main()
