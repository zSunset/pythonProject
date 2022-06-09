"""3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл.
Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше
записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из
скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
© geekbrains.ru 16
горные лыжи"""
import json
from itertools import zip_longest

key = {}
with open("user.csv", encoding='utf-8') as user, \
        open("hobby.csv", encoding='utf-8') as hobby:
    num_lines_users = sum(1 for line in user)
    num_lines_hobby = sum(1 for lines in hobby)

    if num_lines_users > num_lines_hobby:
        exit(1)
    user.seek(0)
    hobby.seek(0)
    for line_user, line_user_hobby in zip_longest(user, hobby):
        key[line_user.strip()] = line_user_hobby.strip() if \
            line_user_hobby is not None else line_user_hobby

with open('all_hobby.json', 'w', encoding='utf=8') as file_f:
    json.dump(key, file_f, ensure_ascii=False)
print(key)
