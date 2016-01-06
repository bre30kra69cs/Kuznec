# coding: utf-8

# Импорт пакетов и модулей
from Main_code.Print_theard import print_class
from Logo_info import state_info
from L_actions import l_main
from S_actions import associative_table



# Инициализация классов и функций
# Функция С регенерации
def c_conversion():
    result = []
    # D → V128
    mas_v128 = [d_to_v128(i + 1) for i in range(32)]
    # Перевод строки из 128 2-ых обозначений в 32 16-ый
    mas_s32 = [v128_to_s32(i) for i in mas_v128]
    for i in mas_s32:
        state_info.raund = "c#" + str(v128_to_d(s32_to_v128(i)))
        c = l_main.l_conversion(i)
        state_info.block = "result"
        state_info.value = c + " "
        print_class.sleepy()
        result.append(c)
    return result



# Перевод из десятичного в 128 2-ых значение
def d_to_v128(d):
    result = ""
    for i in range(128):
        adder = d%2
        result = str(adder) + result
        d = d//2
    return result


# Перевод из 128 2-ых значений в десятичное
def v128_to_d(v128):
    result = 0
    rv128 = v128[::-1]
    for i in range(len(rv128)):
        if rv128[i] == "1":
            result = result + (2**i)
    return result


# Перевод строки из 128 2-ых обозначений в 32 16-ый
def v128_to_s32(v128):
    mas_v4 = [v128[i * 4:i * 4 + 4] for i in range(32)]
    mas_s1 = [associative_table.astv_ttos_16th[i] for i in mas_v4]
    return "".join(mas_s1)


# Перевод строки из 32 16-ых обозначений в 128 2-ых
def s32_to_v128(s32):
    mas_v4 = [associative_table.astv_stot_16th[i] for i in s32]
    return "".join(mas_v4)