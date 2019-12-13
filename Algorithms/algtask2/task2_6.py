import random


decr = lambda x: x - 1


def ncheck(x, a, n):
    if a == x:
        print(f'Вы выиграли! Загаданное число равно {x}')
    elif a > x:
        print(f'Загаданное число меньше {a}')
        begin(x, decr(n))
    elif a < x:
        print(f'Загаданное число больше {a}')
        begin(x, decr(n))


def begin(x, n):
    if n > 0:
        print(f'Угадайте число от 1 до 100\n\tУ вас {n} попыток.')
        a = int(input('Введите число: '))
        ncheck(x, a, n)
    else:
        print('Вы проиграли.')


begin(x=random.randint(1, 100), n=10)
