# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

#Special symbol is *

def sum_num_in_str(str):
    """
    function summarizes number in str, where symbols divided by space

    :param str: input string of number
    :return: sum
    """
    num = ''
    sum = 0
    str += ' '

    for letter in str:
        if  letter == '*':
            break
        elif letter != ' ':
            num += letter
        else:
            sum += int(num)
            num = ''

    return sum

summary = 0

while True:
    my_num_str = input('Enter number divided by space')
    summary += sum_num_in_str(my_num_str)
    print(summary)

    if '*' in my_num_str:
        break
