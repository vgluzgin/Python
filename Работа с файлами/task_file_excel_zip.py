'''


Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой.
К счастью, у него сохранились расчётные листки всех сотрудников.
Помогите по этим расчётным листкам восстановить зарплатную ведомость.
Архив с расчётными листками доступен по ссылке
https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip
(вы можете скачать и распаковать его вручную или самостоятельно научиться делать это с помощью скрипта на Питоне).

Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел, его зарплата.
Сотрудники должны быть упорядочены по алфавиту.

'''

import io
import zipfile
import requests
import glob
import pandas as pd
import openpyxl


r = requests.get("https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip")
with r, zipfile.ZipFile(io.BytesIO(r.content)) as archive:
    archive.extractall('output')

    # на этом шаге сделали запрос, скачали и расспаковали zip архив в папку 'output'

files = [i for i in glob.glob(r'C:\Users\...\Project\output\*'.format('.xslx'))]

    # далее получили список всех путей к обрабатываемым файлам папки output

result = []

for file in files:
    excel_document = openpyxl.load_workbook(file) # открываем файл и загружаем данные

    sheet = excel_document.active                 # обращаемся к активному листу файла excel

    result.append(f'{sheet[2][1].value} {str(sheet[2][3].value)}') # в пустой список добавляем значения из нужных нам ячеек

result.sort()                                     # сортировка списка - сотрудники должны быть упорядочены по алфавиту

    # необходимые данные получены, можем вывести их на печать, используя цикл:

for j in result:
    print(j)


