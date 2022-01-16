t = int(input())
for _ in range(t):
    n, m, r, c = map(int, input().split())
    g = [[1*(x == 'B') for x in input()] for i in range(n)]
    sumrow = sum(g[r-1])
    sumcol = sum([g[i][c-1] for i in range(n)])
    if g[r-1][c-1] == 1:
        print(0)
    elif sumrow > 0 or sumcol > 0:
        print(1)
    elif sum([sum(g[x]) for x in range(n)]) > 0:
        print(2)
    else:
        print(-1)