a = [1, 2, 15.0, 'a', "location", True]
b = (1, 2, 15.0, 'a', "location", True)
# print(a)
# print(type(a))
# print(a[-1])
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# print(a.count(15))
#
# print(a)
# print(dir(a))
# a[0] = 'string'
# print(b)
# print(type(a))
# print(type(b))

matrix = [[1, 0, 0, 0, 0],
          [2, 1, 0, 0, 0],
          [2, 2, 1, 0, 0],
          [2, 2, 2, 1, 0],
          [2, 2, 2, 2, 1]]

matrix_t = list(zip(*matrix))

# print(matrix)
for el in matrix:
    print(el)

print('_' * 15)

for item in matrix_t:
    print(list(item))




