a = int(input('Введите год: '))
if a % 400 == 0:
    print(f'{a} год - високосный')
elif a % 100 == 0:
    print(f'{a} год - невисокосный')
elif a % 4 == 0:
    print(f'{a} год - високосный')
else:
    print(f'{a} год - невисокосный')
