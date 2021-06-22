s = []
t = []
sm = 0
cnt = 0
s1 = []
r1 = []
nnn = ''

with open('f5.txt', encoding='utf-8') as res:
    [s.append(i.split()) for i in res]
    [t.append(i[0]) for i in s]

    for i in range(1, 12):
        for j in s:
            if i == int(j[0]):
                cnt += 1
                sm += int(j[-1])
        s1.append(i)
        if sm == 0:
            r1.append('-')
        else:
            r1.append(sm / cnt)
        cnt, sm = 0, 0

    for k, v in zip(s1, r1):
        nnn += f'{k}\t{v}\n'


with open('file_one.txt', 'w+', encoding='utf-8') as ouf:
    ouf.write(nnn)