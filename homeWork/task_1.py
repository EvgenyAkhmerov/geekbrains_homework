# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open("task_1.txt", 'a') as file:
    while True:
        smth_data = input('Enter data: ')
        if smth_data != '':
            file.write(smth_data + '\n')
        else:
            break
