# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

subject_dict = {}

with open('task_6.txt', 'r') as file:
    subject = file.readlines()

    for i in range(len(subject)):

        subject[i] = subject[i].replace('\n', '')
        subject[i] = subject[i].replace('(л)', '')
        subject[i] = subject[i].replace('(лаб)', '')
        subject[i] = subject[i].replace('(пр)', '')
        subject[i] = subject[i].replace('—', '')
        subject[i] = subject[i].replace(':', '')

        hours = 0

        for elem in subject[i].split():
            if elem.isdigit():
                hours += int(elem)

        subject_dict[subject[i].split()[0]] = hours

print(subject_dict)
