# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# каждому из чисел в диапазоне от 2 до 9.

def begin():
    arr_min = 2
    arr_max = 99
    div_min = 2
    div_max = 9
    for i in range(div_min, div_max + 1):
        tenplist = []
        print(f'Делимых на {i}: ', end = '')
        for j in range (arr_min, arr_max):
            if j % i == 0:
                tenplist.append(j)
        print(len(tenplist))


begin()
