x = int(input('Введите трехзначное число: '))
a = x // 100
b = (x - (a * 100)) // 10
c = (x - a * 100) - b * 10
print(a * b * c)
print(a + b + c)
