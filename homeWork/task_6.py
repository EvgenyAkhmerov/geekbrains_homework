# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

#7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def reg_up(word):
    """
    translates word into upper register

    :param word:
    :return: word in upperregister
    """
    latter_list = list(word)
    latter_list[0] = latter_list[0].upper()

    word = ''
    for latter in latter_list:
        word += latter

    return word

def translator_str_into_list(str):
    """
    This function translates string into word list

    :param str:
    :return: word lost, which are included into string
    """
    word_list = ['']
    i = 0

    for latter in str:
        if latter != ' ':
            word_list[i] += latter
        else:
            i += 1
            word_list.append('')

    return word_list

my_str = input('Enter some words')

word_list = translator_str_into_list(my_str)
new_str = ''

for word in word_list:
    word = reg_up(word)
    new_str += word + ' '

print(new_str)
