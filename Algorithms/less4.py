# import timeit
# print(timeit.timeit("x = 2 + 2"))
# print(timeit.timeit("x = sum(range(1000))"))
# print(sum(range(10)))

import collections

counter = collections.Counter()
for word in 'crabalocker':
    counter[word] += 1
print(counter)
print(counter['counter'])
print(counter['collections'])

print(list(counter.elements()))