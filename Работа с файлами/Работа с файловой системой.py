'''
Для работы с файловой системой и файлами в python,
на помощь приходят библиотеки os и os.path они связаны с операционной системой и путями в операционной системе
компьютера
'''

import os
import os.path

print(os.listdir())
# напечатает все файлы и папки, в данном случае без аргументов, напечатает файлы и папки из текущей директории

print(os.listdir('относительный путь до директории'))
# напечатает все файлы и папки, из директории по указанному относительному пути

print(os.getcwd())
# напечатает путь к текущей папке

print(os.path.exists('file.txt'))
# напечатает True или False при наличии или отсутствии файла или папки указанной в аргументе

print(os.path.isfile('file.txt'))  # проверяет путь является файлом?
print(os.path.isfile('tests'))
# True
# False
print(os.path.exists('file.txt'))  # проверяет путь является папкой?
print(os.path.exists('tests'))
# False
# True

print(os.path.abspath('file.txt'))  # узнать абсолютный путь по относительному пути

os.shdir('.tests')  # перейти в другую директорию

for current_dir, dirs, files in os.walk('.'):  # '.' означает текущую директорию
    print(current_dir, dirs, files)
# особая !!! функция os.walk
# позволяет рекурсивно пройтись по всем директориям, включая папки подпапки и т.д.
# результат возврата - генератор
# при каждом обращении он возвращает tuple из 3 элементов
# 1) строковое представление текущей директории которую осматривает
# 2) список всех подпапок которые находятся в данной директории
# 3) список всех файлов которые находятся в данной директории

import shutil  # библиотека для копирования файлов

shutil.copy('tests/test1.txt', 'tests/test2.txt')  # откуда и куда копировать файл
shutil.copytree('tests', 'tests/testcopy')  # откуда и куда копировать папку



