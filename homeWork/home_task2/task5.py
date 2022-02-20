# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]

add_elem = 1

while add_elem == True:
    my_list.append(int(input('Enter raiting ')))
    add_elem = int(input('Continue -- enter 1, if not -- 0 '))
    print(add_elem)


for j in range(len(my_list)):
    for i in range(len(my_list)-1 - j):
       if my_list[i+1] > my_list[i] :
           my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)
