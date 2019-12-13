def begin():
    n = int(input('Введите число: '))
    a = ''
    while n != 0:
        a = a + str(n % 10)
        n = n // 10
    print(int(a))


begin()
