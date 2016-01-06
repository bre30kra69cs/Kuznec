# coding: utf-8

# Инициализация классов и функций
# Функция X преобразования
def x_conversion(k, a):
    result = ""
    if len(k) == len(a):
        for i in range(128):
            if k[i] == a[i]:
                result = result + "0"
            else:
                result = result + "1"
        return result
    else:
        return 0

