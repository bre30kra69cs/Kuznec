# coding: utf-8

# Импорт пакетов и модулей
from L_actions import l_main
from S_actions import s_main
from X_actions import x_main
from K_actions import c_action



# Инициализация классов и функций
# Функция LSX преобразования
def lsx_conversion(k, a):
    x = x_main.x_conversion(c_action.s32_to_v128(k), c_action.s32_to_v128(a))
    s = s_main.s_conversion(c_action.v128_to_s32(x))
    return l_main.l_conversion(s)


# Функция братная LSX преобразования
def rlsx_conversion(k, a):
    x = x_main.x_conversion(c_action.s32_to_v128(k), c_action.s32_to_v128(a))
    l = l_main.rl_conversion(c_action.v128_to_s32(x))
    return s_main.rs_conversion(l)