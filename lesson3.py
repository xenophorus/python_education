import re


keys = 'qwerty'
values = range(1, 10)
print(dict(zip(keys, values)))

mydict = {key: value ** 2 for key, value in zip(keys, values)}

print(mydict)


pattern = '[a-z]+@[a-z]+\.(ru|org|com)'
email = 'alex@mail.ru'

print(re.match(pattern, email).group(2))
