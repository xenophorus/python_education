import collections as c

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
    return hplus(c.deque(zip(a, b)))


def hplus(dc):
    dc = c.deque(map(tplplus, dc))
    if any(len(x) == 2 for x in dc):
        return reducer(dc)
    else:
        return dc


def addzeros(lst, x):
    for i in range(x):
        lst.appendleft('0')
    return lst


def addzerosr(lst, x):
    for i in range(x):
        lst.append('0')
    return lst


def multbl(x):
    hmullist = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
                '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f',
                '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f',
                '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f',
                '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f',
                '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f',
                '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f',
                '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f',
                '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f',
                '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f',
                'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af',
                'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf',
                'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf',
                'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df',
                'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef',
                'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff')
    return hmullist[hmullist.index(x[0]) * hmullist.index(x[1])]


def divider(x):
    for i in range(int(len(x) / 2)):
        x.popleft()


def summator(dc):
    a = c.deque()
    for i in range(len(dc)):
        a, dc[i] = checker(a, dc[i])
        a = hplus(c.deque(zip(a, dc[i])))
    return a


def hmul(a, b):
    dc = c.deque()
    if len(b) > len(a):
        a, b = b, a
    for i in b:
        dc.append([(x, i) for x in a])
    for i in range(len(dc)): # Вычисляем произведения отдельных элементов
        dc.append(c.deque(map(multbl, dc[i])))
    divider(dc)
    for i in range(len(dc)):
        dc.append(reducer(dc[i]))
    divider(dc)
    for i in range(len(dc)):
        addzerosr(dc[i], len(dc) - i - 1)
    return summator(dc)


def checker(a, b):
    if len(a) > len(b):
        b = addzeros(b, (len(a) - len(b)))
    elif len(b) > len(a):
        a = addzeros(a, (len(b) - len(a)))
    return a, b


def main():
    print('Введите два шестнадцатеричных числа')
    a = c.deque(input('Введите первое число: ').lower())
    b = c.deque(input('Введите второе число: ').lower())

    # a = c.deque('abcdef')
    # b = c.deque('df')

    a, b = checker(a, b)
    sum_ = hplus(c.deque(zip(a, b)))
    print(list(sum_))
    mul_ = hmul(a, b)
    print(list(mul_))

'''
Разбор не смотрел. Хотел выполнить задание сам, только после этого посмотреть, как можно было. 
Не стал делать проверку на правильность ввода числа, при умножении на нуль не стал редуцировать ответ до одного нуля,
сложного в этом нет, но боюсь не успеть до второго дедлайна  
'''

main()
