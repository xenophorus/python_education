import time
import os
import pandas


while True:
    if os.path.exists('../textfiles/vegetables.txt'):
        with open('../textfiles/vegetables.txt') as f:
            print(f.read())
    else:
        print('File does not exist')
    time.sleep(5)
