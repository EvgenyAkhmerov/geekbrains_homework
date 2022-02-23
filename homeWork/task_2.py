# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def person_description(name, sec_name, year_birth, city, email, tel_num):
    """
    Information about person
    return information in one line

    :param name: person's name
    :param sec_name: person's second name
    :param year_birth: person's year of birth
    :param city: person's city
    :param email: person's email
    :param tel_num: person's telephone number
    :return: information about person in one line
    """
    print(f'Name -- {name}; second name -- {sec_name}; year of birth -- {year_birth}; city -- {city}; email -- {email}; telephone number -- {tel_num}')

person_description(name='Evgeny', sec_name='Akhmerov', year_birth=2001, city='Dolgoprudny', tel_num='8-(800)-555-35-35', email='zhenya@mail.ru')
