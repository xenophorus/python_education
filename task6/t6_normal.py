# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random
import sys

class Person:
    def __init__(self, health, damage, armor, name):
        self.health = health
        self.damage = damage
        self.armor = armor
        self.name = name

    def _dmgcount(self, dmg):
        self.health = self.health - (dmg / self.armor)
        return self.health


class Player(Person):

    def attack(self):
        Enemy._dmgcount(self, self.damage)


class Enemy(Person):

    def attack(self):
        Player._dmgcount(self, self.damage)


def create_pers(a, n):
    return a(random.randint(80, 120), random.randint(25, 35), (random.randint(10, 15) / 10), n)


def first_attack(player, enemy):
    if random.randint(1, 2) % 2 == 0:
        fight(player, enemy)
    else:
        fight(enemy, player)


def fight(player1, player2):
    print('Битва началась!')
    while True:
        damaging(player1, player2)
        damaging(player2, player1)


def damaging(player1, player2):
    hp = player1._dmgcount(player1.damage)
    print(f'{player1.name} наносит {player2.name} {player1.damage} урона! '
          f'У {player2.name} осталось {round(hp, 1)} здоровья!')
    if hp <= 0:
        print(f'\t{player2.name} повержен!')
        sys.exit()


def start():
    player = create_pers(Player, 'Психованный Мыш')
    enemy = create_pers(Enemy, 'Зловещий Слизень')

    print(f'{player.name}, {player.health} здороаья, урон - {player.damage}, сила брони - {player.armor}')
    print(f'{enemy.name}, {enemy.health} здороаья, урон - {enemy.damage}, сила брони - {enemy.armor}')

    first_attack(player, enemy)


start()