# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    """
    Function summarizes two biggest number from 3

    :param num_1:
    :param num_2:
    :param num_3:
    :return: sum
    """

    num_list = [num_1, num_2, num_3]

    if num_1 <= num_2 and num_1 <= num_3:
        sum = num_2 + num_3
    elif num_2 > num_3:
        sum = num_1 + num_2
    else:
        sum = num_1 + num_3

    return sum

print(my_func(1000, 1, 100))
