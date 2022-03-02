# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

russian_number = [
    "один",
    "два",
    "три",
    "четыре"
]

initial_file = open('task_4_initial.txt', 'r')
new_file = open('task_4_new.txt', 'w')

number_list = initial_file.readlines()

new_number_list = [el.split(' ') for el in number_list]

for i in range(len(new_number_list)):
    new_number_list[i][0] = russian_number[i]
    new_number_list[i] = " ".join(new_number_list[i])

print(f'New number list:\n{"".join(new_number_list)}')

new_file.write(''.join(new_number_list))

initial_file.close()
new_file.close()
