# coding: utf-8

# Импорт пакетов и модулей
from Logo_info import state_info
from Dec_Enc_algoritms import dec_enc_func
from Main_code.Print_theard import print_class
from Main_code import params



# Инициализация параметров и переменных
input = params.input
test_output = params.test_output
main_key = params.main_key



# Выполнение скрипта
Mr_Printer = print_class.Mr_Printer(state_info.value)
Mr_Printer.start()

output = dec_enc_func.encryption(input, main_key)
print("Шифрование.")
print("Открытый текст :", input)
print("Шифротекст:", output)

print("\n")
print("Дешифрование.")
print("Шифротекст:", output)
print("Открытый текст :", dec_enc_func.decryption(output, main_key))