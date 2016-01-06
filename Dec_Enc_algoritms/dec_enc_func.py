# coding: utf-8

# Импорт пакетов и модулей
from Main_code.Print_theard import print_class
from L_actions import l_main
from S_actions import s_main
from K_actions import k_main
from LSX_actions import lsx_main
from X_actions import x_main
from K_actions import c_action
from Logo_info import state_info



# Инициализация классов и функций
# Шифрование
def encryption(text, key):
    # Получаю раyндовые ключи
    keys = k_main.k_conversion(key)
    result = text
    state_info.raund = "start"
    state_info.block = "input"
    state_info.value = result
    print_class.sleepy()
    # Произвожу десять раундов
    for i in range(len(keys)-1):
        state_info.raund = i + 1
        x = x_main.x_conversion(c_action.s32_to_v128(keys[i]), c_action.s32_to_v128(result))
        state_info.block = "x"
        state_info.value = c_action.v128_to_s32(x)
        print_class.sleepy()
        s = s_main.s_conversion(c_action.v128_to_s32(x))
        state_info.block = "s"
        state_info.value = s
        print_class.sleepy()
        result = l_main.l_conversion(s)
        state_info.block = "l"
        state_info.value = result + " "
        print_class.sleepy()
    state_info.raund = state_info.raund + 1
    state_info.block = "x"
    main_result = c_action.v128_to_s32(x_main.x_conversion(c_action.s32_to_v128(result),
                                                    c_action.s32_to_v128(keys[len(keys)-1])))
    state_info.value = main_result
    print_class.sleepy()
    state_info.raund = "end"
    state_info.block = "output"
    state_info.value = main_result + " "
    print_class.sleepy()
    return main_result


# Дешифрование
def decryption(text, key):
    # Получаю раyндовые ключи
    keys = k_main.k_conversion(key)
    keys = keys[::-1]
    result = text
    state_info.raund = "start"
    state_info.block = "input"
    state_info.value = result
    print_class.sleepy()
    # Произвожу десять раундов
    for i in range(len(keys)-1):
        state_info.raund = i + 1
        x = x_main.x_conversion(c_action.s32_to_v128(keys[i]), c_action.s32_to_v128(result))
        state_info.block = "x"
        state_info.value = c_action.v128_to_s32(x)
        print_class.sleepy()
        l = l_main.rl_conversion(c_action.v128_to_s32(x))
        state_info.block = "l"
        state_info.value = l + " "
        print_class.sleepy()
        result = s_main.rs_conversion(l)
        state_info.block = "s"
        state_info.value = result
        print_class.sleepy()
    state_info.raund = state_info.raund + 1
    state_info.block = "x"
    main_result = c_action.v128_to_s32(x_main.x_conversion(c_action.s32_to_v128(result),
                                                    c_action.s32_to_v128(keys[len(keys)-1])))
    state_info.value = main_result
    print_class.sleepy()
    state_info.raund = "end"
    state_info.block = "output"
    state_info.value = main_result + " "
    print_class.sleepy()
    return main_result
