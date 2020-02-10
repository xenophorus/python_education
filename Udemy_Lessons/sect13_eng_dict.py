import json
from difflib import get_close_matches

data = json.load(open('data/data.json'))


def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return f'Did you mean {get_close_matches(word, data.keys())[0]} instead?'
    else:
        return "The word does not exist. Please check it"


word = input('Enter word: ').lower()

print(translate(word))
