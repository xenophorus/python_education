print('Введите три числа')
a = int(input('\tВведите число a: '))
b = int(input('\tВведите число b: '))
c = int(input('\tВведите число c: '))

if a == b or a == c or b == a:
    print(f'среднего числа нет')

if max(a, b, c) == a:
    print(f'среднее число - {max(b, c)}')
if max(a, b, c) == b:
    print(f'среднее число - {max(a, c)}')
if max(a, b, c) == c:
    print(f'среднее число - {max(a, b)}')
