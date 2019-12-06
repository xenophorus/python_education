print('Введите три числа')
a = float(input('\tВведите число a: '))
b = float(input('\tВведите число b: '))
c = float(input('\tВведите число c: '))

if a == 0 or b == 0 or c == 0:
    print('Треугольник не получится!')
elif a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('\tРавносторонний треугольник')
    elif a == b or b == c or a == c:
        print('\tРавнобедренный треугольник')
    else:
        print('\tРазносторонний треугольник')
else:
    print('Треугольник не получится!')
