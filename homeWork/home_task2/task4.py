#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово длинное,
# выводить только первые 10 букв в слове.

my_str = input('Enter some words divided by space')
words_list = ['']
i = 0

for latter in my_str:
    if latter != ' ':
        words_list[i] += latter
    else:
        i += 1
        words_list.append('')

i = 1
for word in words_list:
    print(i, word[0:10])
    i += 1
