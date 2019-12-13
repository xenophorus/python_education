def begin():
    n = int(input('Введите число: '))
    b = len(str(n))
    count(n, b)


def count(n, b):
    a = 0
    while n != 0:
        if (n % 10) % 2 == 0:
            a += 1
        n = n // 10
    print(f'Четных цифр {a}, нечетных {b - a}.')


begin()
