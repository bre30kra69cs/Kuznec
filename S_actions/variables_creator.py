# coding: utf-8

# Импорт пакетов и модулей
from S_actions import associative_table



# Инициация параетров и переменных
astv_dtos_16th = associative_table.astv_dtos_16th



# Инициализация классов и функций
# Класс создания пеерменной для S действия
class s_format:
    def __init__(self, str_object):
        self.str_object = str_object
    def get_16th_ilist(self):
        return [self.str_object[::2][i]+self.str_object[1::2][i] for i in range(int(len(self.str_object)/2))]
    def get_16th_dict(self):
        list = [self.str_object[::2][i]+self.str_object[1::2][i] for i in range(int(len(self.str_object)/2))]
        result = {}
        for i in range(len(list)):
            result[astv_dtos_16th[str(i)]] = list[i]
        return result