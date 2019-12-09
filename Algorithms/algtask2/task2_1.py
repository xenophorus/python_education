import sys
import operator as o


def begin():
    oper = input('Введите сначала символ операции (+, -, *, /), \nлибо нуль для завершения: ')
    if oper == '0':
        print('Программа завершена!')
        sys.exit(0)
    elif oper in '+*-/':
        operation(oper)
    else:
        print('Вееден неверный символ! Попробуем еще раз.')


def operation(oper):
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    if oper == '*':
        print(o.mul(a, b))
    elif oper == '-':
        print(o.sub(a, b))
    elif oper == '+':
        print(o.add(a, b))
    else:
        print(o.truediv(a, b))
    begin()


begin()
