# 2023/11/16 00:00|Домашнее задание по теме "Файлы в операционной системе".
# Цель задания:
#
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и использование модуля time для корректного отображения времени.
#
# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.
#
# Комментарии к заданию:
#
# Ключевая идея – использование вложенного for
#
# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = ?
#     filetime = ?
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
#
#
#
# Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в папке проекта (directory = “.”)
# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория: .
#
# Пример решения:
#
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория: .
# Пример кода:
# https://onlinegdb.com/j1Euu7cvQ
#
#
# import os
# import time
#
# directory = '.' # Замените на путь к вашему каталогу
#
# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = os.path.join(root, file)
#     filetime = os.path.getmtime(filepath)
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = os.path.getsize(filepath)
#     parent_dir = os.path.dirname(filepath)
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

import os
import time

directory = 'F:\lessonsprojekt\pythonProject20\module7.py'
directory_norm = os.path.normpath(directory)
count = 0
for dirpath, dirmanes, filenames in os.walk(directory_norm):
    for file in filenames:
        full_filenames = os.path.join(dirpath, file)
        filetime = os.path.getmtime(full_filenames) # дата открытия (сек)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # дата  в норм. форме
        file_size = os.path.getsize(full_filenames) # размер
        parent_file = os.path.dirname(full_filenames) # родительская директория
        count += 1
        print(f'Обнаружен файл: {file}, Путь: {full_filenames}, Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_file}')

print(count)