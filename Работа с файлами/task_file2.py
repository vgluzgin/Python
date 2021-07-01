'''

    Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно
    смотреть, как, например, на наиболее часто используемые.
    Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое
    частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
    лексикографически первое (можно использовать оператор < для строк).

    В качестве ответа укажите вывод программы, а не саму программу.

    Слова, написанные в разных регистрах, считаются одинаковыми.

    Sample Input:

    abc a bCd bC AbC BC BCD bcd ABC

    Sample Output:

    abc 3
'''

s = []
s1 = []
val = []
cnt = []
fox = []

with open('f1.txt', encoding='utf-8') as res:
    s += res.read().split()

    for i in range(len(s)):
        s1.append(str(s[i]).lower())

    for j in s1:
        if j not in val:
            val.append(j)
            cnt.append(s1.count(j))
    mx = max(cnt)
    m = [i for i, j in enumerate(cnt) if j == mx] # список индексов максимальных значений списка cnt

    wo = [val[i] for i in m]

    fox.append(min(wo))
    fox.append(str(max(cnt)))

with open('f2.txt', 'w', encoding='utf-8') as ouf:
    ouf.write(' '.join(fox))