import collections as c


# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их к
# ак [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


def tplplus(x):
    hlist = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
             '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f')
    return hlist[hlist.index(x[0]) + hlist.index(x[1])]


def pos1(x):
    if len(x) == 2:
        return x[0]
    else:
        return '0'

def pos0(x):
    if len(x) == 2:
        return x[1]
    else:
        return x


def reducer(dc):
    a = c.deque(map(pos1, dc))
    b = c.deque(map(pos0, dc))
    if a[0] != '0':
        a.append('0')
        addzeros(b, 1)
    else:
        a.popleft()
        a.append('0')
    hplus(c.deque(zip(a, b)))


def hplus(dc):
    dc = c.deque(map(tplplus, dc))
    if any(len(x) == 2 for x in dc):
        reducer(dc)
    else:
        print([x for x in dc])


def addzeros(lst, x):
    for i in range(x):
        lst.appendleft('0')
    return lst


def hmul(a, b):
    if len(b) > len(a):
        a, b = b, a
    for i in b:
        dc = [(x, i) for x in a]
        print(dc)

def main():
    a = c.deque('abc')
    b = c.deque('123')
    hmul(a, b)
    if len(a) > len(b):
        b = addzeros(b, (len(a) - len(b)))
    elif len(b) > len(a):
        a = addzeros(a, (len(b) - len(a)))
    hplus(c.deque(zip(a, b)))


    # print('Введите два шестнадцатеричных числа')
    # a = input('Введите первое число: ').lower()
    # b = input('Введите второе число: ').lower()



main()
