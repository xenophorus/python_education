def begin():
    n = int(input('Введите длину последовательности: '))
    print(counter(n, x=1.0))


def counter(n, x):
    if n == 0:
        return 0
    else:
        print(x)
        return x + counter(n - 1, x * (-0.5))


begin()
