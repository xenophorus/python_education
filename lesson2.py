import os
import psutil
import sys
import platform
import shutil


print("Great Python Program!")
print("Hello, Programmer!")

name = input("Ваше имя: ")

print("Ghbdtn, ", name)
answer = ''
while answer != 'n':
    answer = input("Давай поработаем? (y/n) ")
    if answer == 'y':
        print("OK. You can choose:")
        print("1. File list")
        print("2. System info")
        print("3. List of processes")
        print("4. Дублировать файлы по текуцщему адресу")
        print("5. Удалить все дубликаты, что мы понасоздавали")
        print("6. Удалить файл выборочно")
        do = int(input("Enter a number: "))
        if do == 1:
            print(os.listdir(os.getcwd()))
        elif do == 2:
            print("Текущий путь:" + os.getcwd())
            print("Имя пользователя: " + os.getlogin())
            print("File system encoding: " + sys.getfilesystemencoding())
            print("CPU type: " + platform.processor())
            print("Количество ядер: " + str(psutil.cpu_count()))
            print("\tв том числе логических: " +
                  str(psutil.cpu_count() - psutil.cpu_count(logical=False)))
            print("Частота процессора: " + str(psutil.cpu_freq()))
            print("Тип ОС: " + platform.system())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            a = os.listdir(os.getcwd())
            counter = 0
            for i in a:
                if a[counter][0] != '.':
                    # print(a[counter] + '.dbl')
                    shutil.copy(a[counter], a[counter] + '.dbl')
                    print(a[counter] + " copied")
                counter += 1
        elif do == 5:
            a = os.listdir(os.getcwd())
            for i in a:
                if i.count('.dbl'):
                    print(i + ' removed')
                    os.remove(i)
        elif do == 6:
            a = os.listdir(os.getcwd())
            counter = 0
            print("Выберите файл для удаления:")
            for i in a:
                print(str(counter) + '. ' + a[counter])
                counter += 1
            b = int(input())
            if b > len(a):
                print("Неверный номер!")
            else:
                os.remove(a[b])
                print("Файл " + (a[b]) + " удален")
        else:
            print("Number is out of range!")

    # elif answer == 'n':
    #     pass
    # else:
    #     pass
