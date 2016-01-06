# coding: utf-8

# Импорт пакетов и модулей
from S_actions import associative_table
from S_actions import variables_creator
from S_actions import s_functions



# Инициализация классов и функций
# Функция S преобразования
def s_conversion(string_16th):
    # Из строки в S(a)
    s_object = variables_creator.s_format(string_16th)
    # Из S(a) в S(a15||…||a0)
    s_input_16th_list = s_object.get_16th_ilist()
    # Перевод строк массива из двух 16-ых обозначений в восем 2-ых
    s_input_2th_list = [s_functions.s2_to_v8(i) for i in s_input_16th_list]
    # Int8: V8 → ℤ28
    s_input_d_list = [s_functions.v8_to_d(i) for i in s_input_2th_list]
    # π': ℤ28 → ℤ28.
    s_state_d_list = [associative_table.π_list[i] for i in s_input_d_list]
    # Vec8: ℤ28 → V8
    s_output_2th_list = [s_functions.d_to_v8(i) for i in s_state_d_list]
    # Перевод строк массива из восми 2-ых обозначений в два 16-ых
    s_output_16th_list = [s_functions.v8_to_s2(i) for i in s_output_2th_list]
    # Результат
    return "".join(s_output_16th_list)


# Функция обратная S преобразования
def rs_conversion(string_16th):
    # Из строки в S(a)
    s_object = variables_creator.s_format(string_16th)
    # Из S(a) в S(a15||…||a0)
    s_input_16th_list = s_object.get_16th_ilist()
    # Перевод строк массива из двух 16-ых обозначений в восем 2-ых
    s_input_2th_list = [s_functions.s2_to_v8(i) for i in s_input_16th_list]
    # Int8: V8 → ℤ28
    s_input_d_list = [s_functions.v8_to_d(i) for i in s_input_2th_list]
    # π': ℤ28 → ℤ28.
    s_state_d_list = [associative_table.rπ_list[i] for i in s_input_d_list]
    # Vec8: ℤ28 → V8
    s_output_2th_list = [s_functions.d_to_v8(i) for i in s_state_d_list]
    # Перевод строк массива из восми 2-ых обозначений в два 16-ых
    s_output_16th_list = [s_functions.v8_to_s2(i) for i in s_output_2th_list]
    # Результат
    return "".join(s_output_16th_list)
