# coding: utf-8

# Импорт пакетов и модулей
from Main_code.Print_theard import print_class
from Logo_info import state_info
from L_actions import l_main
from S_actions import s_main
from X_actions import x_main
from K_actions import c_action



# Инициализация классов и функций
# Функция F преобразования
def f_conversion(k, a1, a0):
    x = x_main.x_conversion(c_action.s32_to_v128(k), c_action.s32_to_v128(a1))
    state_info.block = "x"
    state_info.value = c_action.v128_to_s32(x)
    print_class.sleepy()
    s = s_main.s_conversion(c_action.v128_to_s32(x))
    state_info.block = "s"
    state_info.value = s
    print_class.sleepy()
    l = l_main.l_conversion(s)
    state_info.block = "l"
    state_info.value = l + " "
    print_class.sleepy()
    return [c_action.v128_to_s32(x_main.x_conversion(c_action.s32_to_v128(l), c_action.s32_to_v128(a0))), a1]


