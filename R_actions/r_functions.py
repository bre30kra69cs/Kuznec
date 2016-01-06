# coding: utf-8

# Импорт пакетов и модулей
from S_actions import associative_table



# Инициализация классов и функций
# Перевод строки из двух 16-ых обозначений в восем 2-ых
def s2_to_v8(z2):
    return associative_table.astv_stot_16th[z2[0]] + associative_table.astv_stot_16th[z2[1]]


# Перевод строки из восми 2-ых обозначений в два 16-ых
def v8_to_s2(v8):
    return associative_table.astv_ttos_16th[v8[:4]] + associative_table.astv_ttos_16th[v8[4:]]


# Перевод из 8 2-ых в десчтичное значение
def v8_to_d(v8):
    result = 0
    result = result + (2**0)*int(v8[7])
    result = result + (2**1)*int(v8[6])
    result = result + (2**2)*int(v8[5])
    result = result + (2**3)*int(v8[4])
    result = result + (2**4)*int(v8[3])
    result = result + (2**5)*int(v8[2])
    result = result + (2**6)*int(v8[1])
    result = result + (2**7)*int(v8[0])
    return result


# Перевод из десятичного в 8 2-ых значение
def d_to_v8(d):
    result = ""
    for i in range(8):
        adder = d%2
        result = str(adder) + result
        d = d//2
    return result


# Умножение двух V8 строк(чисел) в поле F
def mul_F(p1,p2):
    result = ["x" for i in range(8)]
    for i in range(8):
        if p1[i] == "1" and p2[i] == "1":
            result[i] = "1"
        else:
            result[i] = "0"
    return "".join(result)


# Сложение двух V8 строк(чисел) в поле F
def sum_F(p1,p2):
    result = ["x" for i in range(8)]
    for i in range(8):
        if p1[i] != p2[i]:
            result[i] = "1"
        else:
            result[i] = "0"
    return "".join(result)


