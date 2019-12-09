# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая
# 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


def printout(a, b):
    for i in range(a, b):
        print(f'{i} {chr(i)}'.rjust(6, " "), end='|')
    print()


def printcount(a, b, x):
    if x == 0:
        printout(a, b)
        return None
    else:
        printout(a, a + 10)
        begin(a + x, b, x)


def begin(a, b, x):
    if a + 10 < b:
        printcount(a, b, x)
    else:
        printcount(a, b, 0)


begin(32, 128, 10)
