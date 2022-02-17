# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты,
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк. (Добавил еще дни)

person_time = input('Введите время в секундах')

seconds = int(person_time)
days = seconds // (3600 * 24)
hours = (seconds % (3600 * 24)) // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f' Время: {days}:{hours:02}:{minutes:02}:{seconds:02}, дд:чч:мм:сс')
