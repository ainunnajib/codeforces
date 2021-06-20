from sys import stdin, stdout
t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())

    lr = []
    dr = {}
    for i in range(n):
        row = stdin.readline()
        lr.append(row)

        r = list(map(int, row.split()))
        for x in r:
            dr[x] = i

    lc = []
    for i in range(m):
        c = list(map(int, stdin.readline().split()))
        lc.append(c)

    for i in range(n):
        c = lc[0][i]
        stdout.write(lr[dr[c]])
