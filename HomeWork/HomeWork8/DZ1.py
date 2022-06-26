"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
    email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
    email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?

"""
import re
mail = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    found_info = mail.findall(email)
    if found_info:
        name, addr = found_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, addr)


email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')
#