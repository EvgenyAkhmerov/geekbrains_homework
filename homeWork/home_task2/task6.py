#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),

analysis_dict = {
    'название' : [],
    'цена' : [],
    'количество' : [],
    'ед' : []
}

items_list = []
item_dict = {}
add = int(input('Хотите добавить товар? (Введите 1, если да, 0, если нет) '))
i = 1

while add == True:

     items_list.append((i, {
         'название': None,
         'цена': None,
         'количество': None,
         'ед': None
     }))

     items_list[i-1][1]['название'] = input('Введите название товара ')
     items_list[i-1][1]['цена'] = input('Введите цену товара ')
     items_list[i-1][1]['количество'] = input('Введите количество товара ')
     items_list[i-1][1]['ед'] = input('Введите в чем измеряется кол-во товара ')

     add = int(input('Хотите добавить товар? (Введите 1, если да, 0, если нет) '))
     i += 1

print(items_list)

for item in items_list:
    for key in item[1].keys():
        analysis_dict[key].append(item[1][key])

print(analysis_dict)
