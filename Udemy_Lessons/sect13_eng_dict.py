import json

data = json.load(open('data/data.json'))


def translate(word):
    if word in data:
        return data[word]
    else:
        return "The word does not exist. Please check it"


word = input('Enter word: ').lower()

print(translate(word))
