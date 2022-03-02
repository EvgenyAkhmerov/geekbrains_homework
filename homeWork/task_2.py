# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт
# строк и слов в каждой строке.

with open("task_2.txt", 'r') as file:
    words_list = file.readlines()
    print(f'text file has {len(words_list)} strings')
    n = 1
    for string in words_list:
        print(f'{n}\'th string has {len(string.split(" "))} words')
        n += 1
