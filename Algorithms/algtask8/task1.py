# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9
import hashlib

#print(hashlib.algorithms_available)

def hasher(str):
    str = bytearray(str.encode())
    hash_ = hashlib.sha1(bytearray(str))
    hhash = hash_.hexdigest()
    return hhash


def begin(str):
    st = set()
    lng = len(str)
    for i in range(lng):
        for j in range(lng+1):
            a = (str[i:j])
            if a == str:
                continue
            if len(a) > 0:
                st.add(hasher(a))
    print(f'Строка "{str}" содержит {len(st)} подстрок')


begin('papa')
