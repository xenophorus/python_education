# Начало
# вывод("Введите 2 числа")
# ввод(первое число)
# ввод(второе число)
# Если второе число != 0
#     вывод(частное)
# Иначе вывод ("Нет решений")
# Конец

# 57-00

x = 953
a = x // 100
b = (x - (a * 100)) // 10
c = (x - a * 100) - b * 10
print(a * b * c)
print(a + b + c)
