# coding: utf-8

# Импорт пакетов и модулей
from S_actions import associative_table
from S_actions import variables_creator
from S_actions import s_functions



mas = [0 for i in range(256)]
masi = associative_table.π_list
print(masi[165])
for i in range(256):
    r = masi[i]
    mas[r] = i

print(mas)