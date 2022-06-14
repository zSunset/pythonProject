"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
«руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
templates, например:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
расположены в родительских папках (они играют роль пространств имён); предусмотреть
возможные исключительные ситуации; это реальная задача, которая решена, например, во
фреймворке django
"""
import os
import yaml

catalog = {'My_project': [{'settings': ['__init__.py', 'dev.py', 'prod.py']},
           {'mainapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{'mainapp': ['base.html', 'index.html'
                                                                                            ]}]}]},
                          {'templates': [{'authapp': ['base.html', 'index.html']}]}
]}
f = open('catalog.yaml', 'w')
f.write(yaml.dump(catalog))
f.close()

with open('catalog.yaml') as file:
    catalog =yaml.safe_load(file)

def my_catalog(catlog):
    for cat, log in catlog.items():
        if not os.path.exists(cat):
            os.mkdir(cat)
        os.chdir(cat)
        for loger in log:
            if isinstance(loger, dict):
                my_catalog(loger)
            else:
                if not os.path.exists(loger):
                    if '.' in loger:
                        with open(loger, 'w') as f:
                            f.write('')
    else: os.chdir('../')
my_catalog(catalog)