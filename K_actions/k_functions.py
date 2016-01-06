# coding: utf-8

# Импорт пакетов и модулей
from F_actions import f_main



# Инициализация классов и функций
# Получение итерационного подключа
def get_ki(mas_c, k1, k2):
    result = [k1, k2]
    for i in mas_c:
        result = f_main.f_conversion(i, result[0], result[1])
    return result