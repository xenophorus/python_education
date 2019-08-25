import os
import psutil
import sys
import platform

print("Great Python Program!")
print("Hello, Programmer!")

name = input("Ваше имя: ")

print("Ghbdtn, ", name)
answer = input("Давай поработаем? (y/n) ")

if answer == 'y':
    print("OK. YOu can choose:")
    print("1. File list")
    print("2. System info")
    print("3. List of processes")
    do = int(input("Enter a number: "))
    if do == 1:
        print(os.listdir())
    elif do == 2:
        print("Текущий путь:" + os.getcwd())
        print("Имя пользователя: " + os.getlogin())
        print("File system encoding: " + sys.getfilesystemencoding())
        print("CPU type: " + platform.processor())
        print("Количество ядер: " + str(psutil.cpu_count()))
        print("\tв том числе логических: " + str(psutil.cpu_count() - psutil.cpu_count(logical=False)))
        print("Частота процессора: " + str(psutil.cpu_freq()))
        print("Тип ОС: " + platform.system())
    elif do == 3:
        print(psutil.pids())
    else:
        print("Number is out of range!")

elif answer == 'n':
    pass
else:
    pass
