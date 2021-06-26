'''

В файле https://stepik.org/media/attachments/lesson/209723/3.html
находится одна таблица.
Просуммируйте все числа в ней и введите в качестве ответа одно число - эту сумму.
Для доступа к ячейкам используйте возможности BeautifulSoup.

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

total = 0
html = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html').read().decode('utf-8')
s = str(html)

soup = BeautifulSoup(s, 'html.parser')
for i in soup.find_all('td'):
    total += int(i.text)
print(total)