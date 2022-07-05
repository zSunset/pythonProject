"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна
возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами
использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента передали
код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре
был передан аргумент? В качестве примера выведите курсы доллара и евро.


# ● атрибут headers — словарь с заголовками ответа сервера;
# ● атрибут status_code — число, код ответа сервера;
# ● атрибут content — содержимое ответа;
# ● метод close() — освобождает (закрывает) соединение.
"""

import requests
from decimal import *
from datetime import datetime

getcontext().prec = 4

def currency_rates(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if val not in response:
        return None

    rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f"{Decimal(rub.replace(',', '.'))}, {datetime(day=day, month=month, year=year)}"


print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('eur'))
