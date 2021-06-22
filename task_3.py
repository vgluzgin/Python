s2 = []
res = []
n = int(input())
s = [input().lower() for i in range(n)]

vv = int(input())
s1 = [input().lower().split(' ') for j in range(vv)]

[res.append(i) for row in s1 for i in row if i not in s]


[print(i) for i in set(res)]
