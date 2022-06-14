"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
|--settings
|--mainapp
|--adminapp
|--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
данные о вложенных папках и файлах (добавлять детали)?
"""
import os

Project = {'Project': ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']}
for Proj, my_proj in Project.items():
    if os.path.exists(Proj):
        print(Proj)
    else:
        for i in my_proj:
            strakted = os.path.join(Proj, i)
            os.makedirs(strakted)