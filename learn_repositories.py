def table_results():
    n = int(input())
    s = [input().split(';') for _ in range(n)]
    command = []
    [command.append(j) for i in s for j in i if not j.isdigit() and j not in command]
    res = {com: [0, 0, 0, 0, 0] for com in command}

    for k1, g1, k2, g2 in s:
        res[k1][0] += 1
        res[k2][0] += 1
        if int(g1) > int(g2):
            res[k1][1] += 1
            res[k1][4] += 3
            res[k2][3] += 1
        elif int(g1) < int(g2):
            res[k2][1] += 1
            res[k2][4] += 3
            res[k1][3] += 1
        elif int(g1) == int(g2):
            res[k1][2] += 1
            res[k1][4] += 1
            res[k2][2] += 1
            res[k2][4] += 1
    for i in command:
        print('{}:{}'.format(i, ' '.join(map(str, res[i]))))


if __name__ == '__main__':
    table_results()
