# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на
# склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве
# единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class MyException(Exception):

    def __init__(self, text):
        self.text = text


class Warehouse:

    def __init__(self, square):

        self.square = square           # How much warehouse can contain items
        self.items_in_warehouse = {
                                    'printer': {},
                                    'scanner': {},
                                    'copier': {}
        }

        self.space = {
                        'printer': self.square // 4,
                        'scanner': self.square // 3,
                        'copier': self.square // 3
        }

    def __str__(self):
        return f'\n' \
               f'Printers: \n' \
               f'{self.items_in_warehouse["printer"]} \n' \
               f'free space: {self.space["printer"]} \n' \
               f'{"-" * 30} \n' \
               f'Scanners: \n' \
               f'{self.items_in_warehouse["scanner"]} \n' \
               f'free space: {self.space["scanner"]} \n' \
               f'{"-" * 30} \n' \
               f'Copier: \n' \
               f'{self.items_in_warehouse["copier"]} \n' \
               f'free space: {self.space["copier"]} \n' \
               f'{"-" * 30} \n'


class OfficeEquipment:

    def __init__(self, type, amount, title, working=True):
        self.type = type
        self.amount = amount
        self.title = title
        self.working = working

    def __str__(self):
        return f'Title: {self.title}; quantity: {self.amount}; is working: {self.working}'

    def put_into_warehouse(self, warehouse, amount_of_items):
        """
        This function remote office equipment to warehouse

        :param warehouse:
        :param amount_of_items: how much do you want to remote?
        :return:
        """

        try:
            if type(amount_of_items) == type(''):
                raise MyException(f'Amount of printers must be integer! | {self.type} -- {self.title}')
        except MyException as err:
            print(err)
            return

        try:
            if amount_of_items > self.amount:
                raise MyException(f'You want to send more printers than you have got! | {self.type} -- {self.title}')
        except MyException as err:
            print(err)
            return

        if warehouse.space[self.type] >= amount_of_items:
            warehouse.items_in_warehouse[self.type][self.title] = amount_of_items
            warehouse.space[self.type] -= amount_of_items
            self.amount -= amount_of_items
        else:
            warehouse.items_in_warehouse[self.type][self.title] = warehouse.space[self.type]
            self.amount -= warehouse.space[self.type]
            warehouse.space[self.type] = 0


class Printer(OfficeEquipment):

    def __init__(self, amount_of_paper, amount_of_paint, *args):
        super().__init__(*args)
        self.amount_of_paper = amount_of_paper
        self.amount_of_paint = amount_of_paint


class Scanner(OfficeEquipment):

    def __init__(self, square_of_scan, *args):
        super().__init__(*args)
        self.square_of_scan = square_of_scan


class Copier(OfficeEquipment):

    def __init__(self, amount_of_paper, speed_of_copy, *args):
        super().__init__(*args)
        self.amount_of_paper = amount_of_paper
        self.speed_of_copy = speed_of_copy


printer_1 = Printer(100, 100, 'printer', 100, 'ecosys 2521')
printer_2 = Printer(100, 100, 'printer', 200, 'ecosys 5461')
scanner_1 = Scanner(100, 'scanner', 250, 'Xerox 2121')
scanner_2 = Scanner(120, 'scanner', 100, 'Xerox 3121')
copier_1 = Copier(100, 30, 'copier', 40, 'hp 2121')
copier_2 = Copier(100, 25, 'copier', 400, 'hp 2f21')


print(printer_1)
print(printer_2)
print(scanner_1)
print(scanner_2)
print(copier_1)
print(copier_2)

warehouse_1 = Warehouse(1000)  # Creation of warehouse

printer_1.put_into_warehouse(warehouse_1, '100')
printer_2.put_into_warehouse(warehouse_1, 150)
scanner_1.put_into_warehouse(warehouse_1, 240)
scanner_2.put_into_warehouse(warehouse_1, 200)
copier_1.put_into_warehouse(warehouse_1, 40)
copier_2.put_into_warehouse(warehouse_1, 400)

print(warehouse_1)

print(printer_1)
print(printer_2)
print(scanner_1)
print(scanner_2)
print(copier_1)
print(copier_2)
