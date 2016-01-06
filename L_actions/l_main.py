# coding: utf-8

# Импорт пакетов и модулей
from Main_code.Print_theard import print_class
from Logo_info import state_info
from R_actions import r_main



# Инициализация классов и функций
# Функция L преобразования
def l_conversion(string):
    result = string
    for i in range(16):
        result = r_main.r_conversion(result)
        state_info.block = "r"
        state_info.value = result
        print_class.sleepy()
    return result


# Функция обратная L преобразования
def rl_conversion(string):
    result = string
    for i in range(16):
        result = r_main.rr_conversion(result)
        state_info.block = "r"
        state_info.value = result
        print_class.sleepy()
    return result

