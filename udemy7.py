# file = open('fruits.txt')
# content = file.read()
# file.close()
#
# print(content)

# def lettercount(letter, file):
#     myfile = open(file)
#     cont = myfile.read()
#     return cont.count(letter)
#
# def lettercount(letter, file):
#     with open(file) as myfile:
#         cont = myfile.read()
#         return cont.count(letter)
#
# print(lettercount('c', 'textfiles/bear.txt'))

#
# with open('textfiles/vegetables.txt', 'w') as myfile:
#     myfile.write('Tomato\nPotato')

# with open('textfiles/bear1.txt') as myfile:
#      tbear = myfile.read()
#
# with open('textfiles/bear2.txt', 'a+') as bears:
#     bears.write(tbear)

with open('textfiles/data.txt', 'r') as f:
    cont = f.read()


with open('textfiles/data.txt', 'a+') as f:
    f.write(cont)
    f.write(cont)
