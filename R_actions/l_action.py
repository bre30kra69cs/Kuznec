# coding: utf-8

# Импорт пакетов и модулей
from R_actions import associative_table
from R_actions import r_functions



# Инициализация классов и функций
# Функция ℓ замены
def ℓ_conversion(mas):
    result_sum = []
    for i in range(16):
        mul_mas = mul_format(ℓ_format(mas[i]), ℓ_format(associative_table.l_mas[i]))
        res_mas = equ_format(mul_mas, associative_table.modx)
        result_sum = result_sum + res_mas
    result = sum_format(result_sum)
    return rℓ_format(result)

# Переобразование десятичного значения в формат уравнения
def ℓ_format(dec):
    result = []
    two = r_functions.d_to_v8(dec)
    for i in range(8):
        if two[i] == "1":
            result.append(7-i)
    return result


# Переобразование из формата уравнения в десятичное значение
def rℓ_format(fmas):
    result = 0
    for i in fmas:
        result = result + (2**i)
    return result


# Нахождение многочлена от многочлена по модулю заданного многочлена
def equ_format(value, mod):
    while True:
        if len(value) != 0:
            if max(value) >= max(mod):
                state = []
                delta = max(value) - max(mod)
                for i in mod:
                    if i + delta in value:
                        pass
                    else:
                        state.append(i + delta)
                mod_delta = [delta + i for i in mod]
                for i in value:
                    if i in mod_delta:
                        pass
                    else:
                        state.append(i)
                value = state
            else:
                return value
        else:
            return []


# Перемножение многочленов
def mul_format(val1, val2):
    state = []
    for i in val2:
        for y in val1:
            state.append(i + y)
    result = []
    for i in state:
        if i in result:
            pass
        else:
            if state.count(i) % 2 != 0:
                result.append(i)
    return result


# Сумма многочленов
def sum_format(val):
    result = []
    for i in val:
        if i in result:
            pass
        else:
            if val.count(i) % 2 != 0:
                result.append(i)
    return result

