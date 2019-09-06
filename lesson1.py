def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


# stud_grades = {'Steve': 5.5, 'Lynn': 6.2, 'Ingrid': 7.1}
#
# print(mean(a))
# print(mean(stud_grades))

# for key, value in stud_grades.items():
#     print('{} has grade {}'.format(key, value))
#
# for i in stud_grades.keys():
#     print(i)

# user_input = input("Enter your name: ")
# message1 = "Hello, %s!" % user_input
# message2 = "Hello, {}!".format(user_input)
#
# print(message1)
# print(message2)

# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
#
# for i in phone_numbers.values():
#     print('00' + i[1:])
#
# def greatName(sName, sSurname):
#     tName = sName[0].upper() + sName[1:].lower()
#     tSurname = sSurname[0].upper() + sSurname[1:].lower()
#     return 'Hi %s %s' % (tName, tSurname)
#
# print(greatName('ann', 'johnson'))

# b = [i // 2 for i in a]
# c = [i / 2 for i in a if i % 2 != 1]
# print(b)
# print(c)
#
# b = [12, 32, 'er', 'asdf', 34, '3e5', 22, -7, 'no data']
#
#
# def isDigit(b):
#     c = [i if type(i) != str else 0 for i in b]
#     return(c)
#
#
# print(isDigit(b))
#
a = [5, 32, '5', 23, 76, 3, 12, 7, 4, 5]


# def summ(a):
#     soom = 0
#     for elm in a:
#         soom = soom + float(elm)
#     return soom
#
#
# print(summ(a))

def concat(d, e):
    return str(d) + str(e)


print(concat('coding ', 'Python'))
print(concat(4, 2))
