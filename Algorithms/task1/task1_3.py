print('Введите координаты точки A')
x1 = float(input('\tx1 = '))
y1 = float(input('\ty1 = '))

print('Введите координаты точки B')
x2 = float(input('\tx2 = '))
y2 = float(input('\ty2 = '))


k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print('Уравнение:')
print(f'y = {k}*x + {b}')
