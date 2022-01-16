t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = []
    for i in range(n):
        for j in range(m):
            x = i + j
            x = max(x, n-1-i + m-1-j)
            x = max(x, i + m-1-j)
            x = max(x, n-1-i + j)
            l.append(x)
    l.sort()
    print(*l)