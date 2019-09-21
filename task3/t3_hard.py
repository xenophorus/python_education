# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

import random

'''

Первоначальный вариант. Интересно было попробовать через рандом
def armattack(player, enemy):
    while player['health'] > 0 and enemy['health'] > 0:
        if random.randint(0, 1) == 1:
            player['health'] = player['health'] - reflect(enemy['damage'], player['armor'])
            print(f"{enemy['name']} нанес {enemy['damage']} урона! У {player['name']} осталось {player['health']} hp")
        else:
            enemy['health'] = enemy['health'] - reflect(player['damage'], enemy['armor'])
            print(f"{player['name']} нанес {player['damage']} урона! У {enemy['name']} осталось {enemy['health']} hp")
'''


def reflect(a, b):
    return a / b

def creation(name):
    chardata = ['name', 'health', 'damage', 'armor']
    # print(name)
    a = dict(zip(chardata, [name, random.randint(75, 115), random.randint(25, 35), 1.2]))
    with open(name + '.txt', 'w') as file:
        for key, value in a.items():
            file.write(f'{key} {value}\n')
    # return a

def reading(name):
    cont = {}
    with open(name + '.txt') as file:
        for i in file.read().splitlines():
            a, b = (i.split(' '))
            if b.isdigit():
                b = float(b)
            cont[a] = b
        return cont

def attack(pl1, pl2):
    for _ in range(10):
        pl1['health'] = pl1['health'] - round(reflect(pl2['damage'], float(pl1['armor'])), 2)
        # print(f'player {pl1["name"]}, health {pl1["health"]}, damaged {pl2["damage"]}')
        if (pl1['health']) <= 0:
            print(f'{pl2["name"]} победил с остатком здоровья {pl2["health"]}')
            break
        pl2['health'] = pl2['health'] - round(reflect(pl1['damage'], float(pl2['armor'])),2)
        # print(f'player {pl2["name"]}, health {pl2["health"]}, damaged {pl1["damage"]}')
        if (pl2['health']) <= 0:
            print(f'{pl1["name"]} победил с остатком здоровья {pl1["health"]}')
            break


pname = 'alex'  # input('Введите имя игрока: ')
ename = 'hank'
player = creation(pname)
enemy = creation(ename)

# print(reading(pname), reading(ename))
attack(reading(pname), reading(ename))

'''
Округление не всегда работает корректно, решение нашел, но реализовывать не стал. 
'''