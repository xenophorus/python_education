# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

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


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, spoiler):
        self.got_spoiler = spoiler
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, lift):
        self.can_lift = lift
        super().__init__(speed, color, name, is_police)


class PoliceCar(SportCar):
    def __init__(self, speed, color, name, is_police, spoiler, migalkees):
        self.got_migalkees = migalkees
        super().__init__(speed, color, name, is_police, spoiler)

town_car = Car(50, 'red', 'Drandoolet', False)
sport_car = SportCar(100, 'blue', 'SportDrandoolet', False, True)
work_car = WorkCar(30, 'yellow', 'HeavyDrandoolet', False, 500)
police_car = PoliceCar(100, 'dark blue', 'PoliceDrandoolet', True, True, True)

print(town_car.name, town_car.speed, town_car.color, town_car.is_police)
print(sport_car.name, sport_car.speed, sport_car.color, sport_car.is_police, sport_car.got_spoiler)
print(work_car.name, work_car.is_police, work_car.color, work_car.speed, work_car.can_lift)
print(police_car.speed, police_car.color, police_car.name, police_car.is_police, police_car.got_spoiler,
      police_car.got_migalkees)

police_car.turn('right')
sport_car.turn('left')
work_car.turn(10)
