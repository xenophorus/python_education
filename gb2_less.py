# a = 'Anastasiya'
# print(a[::-1])
# print(a[::2])
# print(a[::-3])
#
# email = 'welcome@mail.ru'
# index = email.find('@')
# print(email[:index])

# name = 'ИВаноВ петР паЛЫч'
# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(len(name))
# print(name.count('а'))
# print(name.split())

# email = 'welcome@mail.ru'
# user, host = email.split('@')
# print(user, host)

# a = ['milk', 'meat', 'egg', 'bread', 'sausage', 'weenie']
# b = range(1, 10)

# for i in enumerate(a, start=1):
#     print(i)
#
# print(max(a, key=len))

# for i in zip(b, a):
#     print(i)


# lst = [str(i) for i in b]

# a = ['milk', 'meat', 'egg', 'bread', 'sausage', 'weenie']
# b = range(1, 10)
#
# lst1 = [i for i in b if my_filter(i) == True]
# lst = list(filter(my_filter, b))
#
# print(lst, lst1)
#
# lst2 = list(map(lambda x: x ** 2, b))
# lst3 = list(filter(lambda x: x % 2 == 0, b))
#
# print(lst2, lst3)

# file = open('fruits.txt')
# for line in file:
#     print(line.strip())
#
# file.close()

# file = open('berries.txt', 'a+')
# file.write('grape\n')
# file.seek(0)
# print(file.readline())
#
# file.close()

file = open('berries.txt', 'r')

for line in file:
    print(line.strip())

with open('berries.txt', 'a+', encoding='utf-8') as file:
    file.write('grape\n')
    file.seek(0)
    print(file.readlines())
