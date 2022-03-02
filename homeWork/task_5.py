# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('task_5.txt', 'w') as file:
    file.write(' '.join([str(el) for el in range(1, 21)]))

with open('task_5.txt', 'r') as file:
    number_list = file.readline().split(' ')
    summ = 0
    for number in number_list:
        summ += int(number)
    print(f'Sum of numbers in task_5.txt: {summ}')
