# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class TownCar:
    def __init__(self):
        self.speed = 50
        self.color = 'red'
        self.name = 'Drandoolet'
        self.is_police = False

    def go(self):
        print('moving forward')

    def stop(self):
        print('stopping')

    def turn(self, direction):
        if direction == 'right':
            print('Turning right')
        elif direction == 'left':
            print('Turning left')
        else:
            print('Turning somewhere')


class SportCar(TownCar):
    def __init__(self):
        super().__init__()
        self.speed = 100
        self.name = 'Speedy Drandoolet'
        self.color = 'green'


class WorkCar(TownCar):
    def __init__(self):
        super().__init__()
        self.speed = 30
        self.color = 'yellow'
        self.name = 'Work Drandoolet'


class PoliceCar(SportCar):
    def __init__(self):
        super().__init__()
        self.color = 'blue'
        self.name = 'Police Drandoolet'
        self.is_police = True


print(TownCar.is_police, TownCar.color, TownCar.name)



