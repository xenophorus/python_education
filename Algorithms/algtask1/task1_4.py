import random

print('Задайте границы для генерации числа в натуральных числах, '
      'второе число больше первого иил равно ему.')
a = int(input('\tВведите первое число: '))
b = int(input('\tВведите второе число: '))

print('Сгенерировано число ', random.randint(a, b))

print('Задайте границы для генерации числа в действительных положительных числах,'
      'второе число больше первого иил равно ему.')
c = float(input('\tВведите первое число: '))
d = float(input('\tВведите второе число: '))

print('Сгенерировано число ', random.uniform(c, d))

print('Задайте границы для генерации буквы, '
      'вторая буква больше первой иил равна ей.')
a = input('\tВведите первую букву: ')
b = input('\tВведите вторую букву: ')

print('Сгенерирована буква ', chr(random.randint(ord(a), ord(b))))