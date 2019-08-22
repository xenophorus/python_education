import random

words = ('знакомство', 'шаблон', 'контекст', 'пользователь',
         'товар', 'корзина')

secret_word = random.choice(words)

# print(secret_word)

gamer_word = ['*'] * len(secret_word)

error_count = 0

while True:
    letter = input("Введите одну букву: ").strip().lower()
    if len(letter) != 1 or not letter.isalpha():
        continue

    if letter in secret_word:
        for position, symbol in enumerate(secret_word):
            if symbol == letter:
                gamer_word[position] = symbol
        if '*' not in gamer_word:
            print('Вы выиграли!')
            break

    else:
        error_count += 1
        print('\tошибок допущено: ', error_count)
        if error_count == 8:
            print("Вы проиграли!")
            break

    print(''.join(gamer_word))

print("Bye!")


