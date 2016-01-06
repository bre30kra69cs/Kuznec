# coding: utf-8

# Импорт пакетов и модулей
from R_actions import r_functions
from R_actions import l_action



# Инициализация классов и функций
# Функция R преобразования
def r_conversion(str_object):
    # Из S(a) в S(a15||…||a0)
    mas_input_16th = [str_object[::2][i]+str_object[1::2][i] for i in range(int(len(str_object)/2))]
    # Перевод строки из двух 16-ых обозначений в восем 2-ых
    mas_input_2th = [r_functions.s2_to_v8(i) for i in mas_input_16th]
    # V8 → D
    mas_input_10th = [r_functions.v8_to_d(i) for i in mas_input_2th]
    # ℓ: D16 → D
    result_output_10th = l_action.ℓ_conversion(mas_input_10th)
    # D → V8
    result_output_2th = r_functions.d_to_v8(result_output_10th)
    # Перевод строки из восми 2-ых обозначений в два 16-ых
    result_output_16th = r_functions.v8_to_s2(result_output_2th)
    # Организация и объеденение массива с результатом и строки
    mas_output_16th = [result_output_16th] + mas_input_16th[:15]
    return "".join(mas_output_16th)


# Функция обратная R преобразования
def rr_conversion(str_object):
    # Из S(a) в S(a15||…||a0)
    mas_input_16th = [str_object[::2][i]+str_object[1::2][i] for i in range(int(len(str_object)/2))]
    # Перевод строки из двух 16-ых обозначений в восем 2-ых
    mas_input_2th = [r_functions.s2_to_v8(i) for i in mas_input_16th]
    # V8 → D
    mas_input_10th = [r_functions.v8_to_d(i) for i in mas_input_2th]
    # ℓ: D16 → D
    result_output_10th = l_action.ℓ_conversion(mas_input_10th[1:] + [mas_input_10th[0]])
    # D → V8
    result_output_2th = r_functions.d_to_v8(result_output_10th)
    # Перевод строки из восми 2-ых обозначений в два 16-ых
    result_output_16th = r_functions.v8_to_s2(result_output_2th)
    # Организация и объеденение массива с результатом и строки
    mas_output_16th = mas_input_16th[1:] + [result_output_16th]
    return "".join(mas_output_16th)
