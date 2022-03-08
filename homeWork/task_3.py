# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.

class MyException(Exception):

    def __init__(self, error):
        self.error = error



pers_list = []
while True:
    pers_input = input('If you want continue: enter number, else input stop: ')
    if pers_input == 'stop':
        break
    try:
        if not pers_input.isdigit():
            raise MyException('Write a number!')
    except MyException as err:
        print(err)
        continue
    pers_list.append(int(pers_input))

print(pers_list)
