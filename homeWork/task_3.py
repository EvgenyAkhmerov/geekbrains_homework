# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

with open("task_3.txt", 'r') as file:
    staff_list = file.readlines()
    avrg_salary = [0, 0]
    print('Over 20000 earn next employees:')
    n = 1
    for empl in staff_list:
        empl_list = empl.split(' ')
        if float(empl_list[1]) >= 20000:
            print(f'{n}) {empl_list[0]}')
            n += 1
        avrg_salary[0] += float(empl_list[1])
        avrg_salary[1] += 1

    print(f'Average salary all employees: {avrg_salary[0] / avrg_salary[1]:.2f}')
