t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    s = [sum([l[i][j] for i in range(n)]) for j in range(5)]
    c = []
    for i in range(5):
        if s[i] >= n//2:
            c.append(i)
    if len(c) < 2:
        print('NO')
    else:
        possible = False
        x = []
        for i in c:
            x.append([l[j][i] for j in range(n)])
        for i in range(len(x)-1):
            for j in range(i+1, len(x)):
                onei, onej, both = 0, 0, 0
                for k in range(n):
                    if x[i][k] + x[j][k] == 0:
                        break
                    if x[i][k] + x[j][k] == 2:
                        both += 1
                    elif x[i][k] == 1:
                        onei += 1
                    else:
                        onej += 1
                if onei + onej + both < n:
                    continue
                if onei + both >= n//2 and onej + both >= n//2:
                    possible = True
                    break
            if possible:
                break
        print('YES' if possible else 'NO')