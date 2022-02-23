# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее. Подсказка: используйте функцию count() и cycle()
# модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором повторение
# элементов списка прекратится.

from itertools import count, cycle

start = int(input('Enter start number'))
end = int(input('Enter end number'))

for el in count(start):
    if el <= end:
        print(el)
    else:
        break

laps_amount= int(input('Enter amount of cycles'))
my_list = [1, 2, 3, 4, 5]

lap = 0
for el in cycle(my_list):
    if lap == laps_amount:
        break

    print(el)

    if el == my_list[len(my_list)-1]:
        lap += 1
        print('- ' * 30)
