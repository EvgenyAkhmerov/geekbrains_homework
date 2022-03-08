# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyException(Exception):

    def __init__(self, error):
        self.error = error


num_1 = int(input('Enter num: '))
if num_1 == 0:
    raise MyException('Division on zero is imposible')
else:
    print(1. / num_1)
