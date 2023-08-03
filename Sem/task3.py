# ✔ Добавьте к задачам 1 и 2 строки документации для классов.


import os
from time import time


class AuthoStr(str):
    """
    Данный класс является развитием класса str, который 
    сохраняет информацию кем и когда была создана строка
    """


    def __new__(cls, row):
        instance = super().__new__(cls, row)
        instance.user = os.getlogin()
        instance.created_time = time()
        return instance


my_str = AuthoStr('This is testing')
print(my_str)
print(my_str.user)
print(my_str.created_time)


print(AuthoStr.__doc__)


class Archive:
    """
    Данный класс архивирует строки и числа
    """


    list_str = []
    list_int = []


    def __init__(self, int1, str1):
        self.int1 = int1
        self.str1 = str1
        self.list_int.append(int1)
        self.list_str.append(str1)


    def get_int1(self):
        return self.int1


    def get_str1(self):
        return self.str1


    @classmethod
    def get_int_arch(cls):
        return cls.list_int


    @classmethod
    def get_str_arch(cls):
        return cls.list_str


a1 = Archive(42, 'Ответ на все вопросы вселенной')
print(a1.get_int_arch())
print(a1.get_str_arch())
a2 = Archive(43, 'А какой был вопрос?')
print(a2.get_int_arch())
print(a2.get_str_arch())
a3 = Archive(43, 'А какой был вопрос???')
print(a3.get_int_arch())
print(a3.get_str_arch())
print(a3.get_int1())
print(a3.get_str1())


print(Archive.__doc__)
