t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    coord = {}
    d = {}
    for i in range(n):
        x = a[i]
        if x not in coord:
            coord[x] = i
        else:
            if x not in d:
                d[x] = i - coord[x]
            else:
                d[x] = min(d[x], i - coord[x])
            coord[x] = i
    if len(d) == 0:
        print(-1)
    else:
        print(n - min(d.values()))