# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def ncount(n):
    if n == 0:
        return 0
    else:
        b = n % 10
        n = n // 10
        return b + ncount(n)


def begin(x, y):
    a = input('Введите последовательность любых чисел, разделенных пробелами:\n')
    a = a.strip()
    for i in a.split(' '):
        b = (ncount(int(i)))
        if max(x, b) == b:
            x = b
            y = i
    print(y, x)


begin(x=0, y=0)
