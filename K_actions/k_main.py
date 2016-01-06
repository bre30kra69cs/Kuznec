# coding: utf-8

# Импорт пакетов и модулей
from Main_code.Print_theard import print_class
from K_actions import k_functions
from K_actions import c_action
from Logo_info import state_info



# Инициализация классов и функций
# Функция K регенерации
def k_conversion(keys):
    # Выроботка констант
    mas_c = c_action.c_conversion()
    # Состовляющие мастер ключа
    k1 = keys[:32]
    state_info.raund = "key#12"
    state_info.block = "result k1"
    state_info.value = k1
    print_class.sleepy()
    k2 = keys[32:]
    state_info.block = "result k2"
    state_info.value = k2
    print_class.sleepy()
    # Выроботка подкючей 3 и 4
    state_info.raund = "key#34"
    k34 = k_functions.get_ki(mas_c[:8], k1, k2)
    k3 = k34[0]
    state_info.block = "result k3"
    state_info.value = k3
    print_class.sleepy()
    k4 = k34[1]
    state_info.block = "result k4"
    state_info.value = k4
    print_class.sleepy()
    # Выроботка подкючей 5 и 6
    state_info.raund = "key#56"
    k56 = k_functions.get_ki(mas_c[8:16], k3, k4)
    k5 = k56[0]
    state_info.block = "result k5"
    state_info.value = k5
    print_class.sleepy()
    k6 = k56[1]
    state_info.block = "result k6"
    state_info.value = k6
    print_class.sleepy()
    # Выроботка подкючей 7 и 8
    state_info.raund = "key#78"
    k78 = k_functions.get_ki(mas_c[16:24], k5, k6)
    k7 = k78[0]
    state_info.block = "result k7"
    state_info.value = k7
    print_class.sleepy()
    k8 = k78[1]
    state_info.block = "result k8"
    state_info.value = k8
    print_class.sleepy()
    # Выроботка подкючей 9 и 10
    state_info.raund = "key#910"
    k910 = k_functions.get_ki(mas_c[24:], k7, k8)
    k9 = k910[0]
    state_info.block = "result 9"
    state_info.value = k9
    print_class.sleepy()
    k10 = k910[1]
    state_info.block = "result 10"
    state_info.value = k10
    print_class.sleepy()
    return [k1, k2, k3, k4, k5, k6, k7, k8, k9, k10]
