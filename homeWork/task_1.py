# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.

class Date:

    day_in_month = {
        'январь': 31,
        'февраль': 28,
        'март': 31,
        'апрель': 30,
        'май': 31,
        'июнь': 30,
        'июль': 31,
        'август': 30,
        'сентябрь': 31,
        'октябрь': 31,
        'ноябрь': 30,
        'декабрь': 31
    }

    def __init__(self, date):
        self.date = date

    @classmethod
    def return_num_date(cls, date):
        return [int(el) if el.isdigit() else el for el in date.split('-')]

    @staticmethod
    def valid_date(date):
        num_date = date.split('-')
        if num_date[1] == 'февраль' and int(num_date[2]) in list(range(2000, 2030, 4)) and int(num_date[0]) > 29:
            return 'Error. in this month there are only 29 days'
        elif num_date[1] != 'февраль' and int(num_date[0]) > Date.day_in_month[num_date[1]]:
            return f'Error. in this month there are only {Date.day_in_month[num_date[1]]} days'

        return 'All right'


date_1 = '9-январь-2001'
date_2 = '31-апрель-2020'
date_3 = '29-февраль-2000'

print(Date.valid_date(date_1))
print(Date.valid_date(date_2))
print(Date.valid_date(date_3))

print(Date.return_num_date(date_1))
