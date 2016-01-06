# coding: utf-8

# Импорт пакетов и модулей
from Logo_info import state_info
from Main_code import params
import threading
import time



# Инициализация классов и функций
# Класс потока учёта изменения state
class Mr_Printer(threading.Thread):
    def __init__(self,value):
        threading.Thread.__init__(self)
        self.value = value
    def run(self):
        while True:
            new_value = state_info.value
            if self.value != new_value:
                if params.print_switch:
                    print(state_info.raund, state_info.block, state_info.value)
                self.value = new_value


# Функция засыпания
def sleepy():
    if params.time_switch:
        time.sleep(params.sleep_time)