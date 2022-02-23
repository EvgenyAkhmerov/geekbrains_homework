# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def num_division(num_1, num_2):
    """
    This function provides division between two numbers : num_1 / num_2
    :param num_1: first number
    :param num_2: second number
    :return: their division
    """
    if num_2 == 0:
        print('division on zero is impossible, try again')
    else:
        return num_1 / num_2

num_1 = float(input('Enter first number'))
num_2 = float(input('Enter second number'))

print('Their division is equal ', num_division(num_1, num_2))
