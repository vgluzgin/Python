from collections import Counter
'''Как из списка преобразовать данные в словарь с парами {ключ: колличество вхождений в список}'''

# вариант списка
list = [3, 5 , 'sdfsdff', 3, 5, 7, 'sdfsdfsdfsd', 7, 7, 3, 3, 9, 234234, 2343, 1, 2, 3, 1, 2, 3, 2313]

Distribution_of_list_items = {}
Distribution_of_list_items = Counter(list)

print(Distribution_of_list_items)