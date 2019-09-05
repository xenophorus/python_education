def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


a = [5, 32, 5, 23, 76, 3, 12, 7, 4, 5]
stud_grades = {'Steve': 5.5, 'Lynn': 6.2, 'Ingrid': 7.1}

print(mean(a))
print(mean(stud_grades))

# user_input = input("Enter your name: ")
# message1 = "Hello, %s!" % user_input
# message2 = "Hello, {}!".format(user_input)
#
# print(message1)
# print(message2)

def greatName(sName, sSurname):
    tName = sName[0].upper() + sName[1:].lower()
    tSurname = sSurname[0].upper() + sSurname[1:].lower()
    return 'Hi %s %s' % (tName, tSurname)

print(greatName('ann', 'johnson'))




