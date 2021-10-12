s, t, counter, ind = input(), input(), 0, 1
while ind != -1:
    ind = s.find(t)
    if ind >= 0:
        counter += 1
    s = s[ind+1:]
print(counter)
