# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

variable1 = 35
variable2 = 4.44
variable3 = 'variable4'
variable4 = [variable1, variable2, variable3]

print(variable4)

variable5 = input('Введите что-нибудь: ')

print('Вы ввели: ' + variable5)

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

digit = input('Введите число: ')

print(int(digit) + 2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = input('Введите свой возраст: ')

if int(age) >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')

# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

while True:
    number = int(input('Введите число: '))
    if  number > 0 and number < 10:
        print(number ** 2)
        break
    else:
        continue

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.

x = int(input('Введите x: '))
y = int(input('Введите y: '))

x = x + y
y = x - y
x = x - y

print(x)
print(y)


# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
weight = float(input('Введите вес: '))
fullstr = (name[0].upper() + name[1:].lower() + ' ' +
           surname[0].upper() + surname[1:].lower() + ', ' +
           'возраст ' + str(age) + ', вес ' + str(weight))

if age <= 30 and weight > 50 and weight < 150:
    print(fullstr + ' - хорошее состояние')
elif age > 30 and weight > 50 and weight < 150:
    print(fullstr + ' - следует заняться собой')
else:
    print(fullstr + ' - следует обратится к врачу!')
